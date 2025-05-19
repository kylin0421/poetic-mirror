import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
import time
import csv
from data.to_poem_list import to_poem_list
import os
import gradio as gr
from huggingface_hub import hf_hub_download,login


hf_token = os.environ.get("HF_TOKEN")
login(token=hf_token)
#====Settings====
model_path = "slxhere/modern_ancientpoem_encoder"
poem_csv_path = hf_hub_download(
    repo_id="slxhere/tang_poems",
    repo_type="dataset",
    filename="tang_poem.csv"
)
api_key = os.environ.get("DEEPSEEK_API_KEY")
base_url = "https://api.deepseek.com"
top_k = 5
embedding_cache_path = hf_hub_download(
    repo_id="slxhere/poetic-mirror-cache-tang-embedding",
    repo_type="dataset",
    filename="cached_tang_embedding.npy"
)


print("Loading model and data...")
model = SentenceTransformer(model_path)
client = OpenAI(api_key=api_key, base_url=base_url)
poem_sentences = to_poem_list(poem_csv_path)

#========

if os.path.exists(embedding_cache_path):
    poem_embeddings = np.load(embedding_cache_path)
else:
    print("Cached embeddings not found! Encoding... This might take some time...")
    poem_embeddings = model.encode(
        poem_sentences, batch_size=64, show_progress_bar=True, normalize_embeddings=True
    )
    np.save(embedding_cache_path, poem_embeddings)
    print(f"Embedding saved to {embedding_cache_path}")


def rerank_with_llm(modern, candidates):
    prompt = f"""
我说了一句话：“{modern}”，你觉得下面哪一句古诗最能表达这句话的情绪与意境？

"""
    for i, c in enumerate(candidates):
        prompt += f"{i+1}. {c}\n"
    prompt += "\n请直接回复最匹配的一句编号（如 2），不要解释。"

    try:
        resp = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是古诗匹配专家。"},
                {"role": "user", "content": prompt}
            ]
        )
        reply = resp.choices[0].message.content.strip()
        for line in reply.splitlines():
            if line.strip().isdigit():
                idx = int(line.strip()) - 1
                if 0 <= idx < len(candidates):
                    return idx
    except Exception as e:
        print("LLM error: ", e)
    return 0  


def retrieve_and_rerank(modern_sentence):
    start_time = time.time()
    emb = model.encode([modern_sentence], normalize_embeddings=True)
    sims = cosine_similarity(emb, poem_embeddings)[0]

    top_k_idx = sims.argsort()[-top_k:][::-1]
    top_k_sims = sims[top_k_idx]
    top_k_poems = [poem_sentences[i] for i in top_k_idx]

    rerank_idx = rerank_with_llm(modern_sentence, top_k_poems)

    scores = np.exp(top_k_sims - np.max(top_k_sims))
    probs = scores / scores.sum()

    results = [{
        "poem": top_k_poems[i],
        "score": round(float(probs[i]), 4),
        "(LLM selected)": i == rerank_idx
    } for i in range(top_k)]

    print(f"Reaction time: {time.time() - start_time:.2f}s")
    return results


def poetry_matcher(input_text):
    results = retrieve_and_rerank(input_text)
    return "\n".join(
        [f"{'✅' if r['(LLM selected)'] else '  '} [{r['score']}] {r['poem']}" for r in results]
    )

iface = gr.Interface(
    fn=poetry_matcher,
    inputs=gr.Textbox(lines=2, placeholder="Enter your sentence..."),
    outputs="text",
    title="🔭 Poetic Mirror 🖌",
    description="穿越千年诗意，为你精准匹配最契合的古诗名句——输入你的句子，邂逅古人共鸣。\nTravel through a thousand years of poetry—enter your sentence, and we'll find the most matching Tang dynasty verse for you."
)

iface.launch()

