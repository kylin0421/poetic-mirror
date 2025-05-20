# 🪞 Poetic Mirror ｜现代句 → 古诗语义匹配系统
*A Semantic Bridge from Modern Chinese to Classical Poetry*
(For English version, please scroll down)

<details open>
<summary>🇨🇳 中文简介（点击折叠）</summary>

以现代中文为引，探寻古典诗意的回响。  
输入一句现代语言，系统将检索出最契合其语义的古诗句作为回应，构建“古今对话”的诗意桥梁。

---

## 🔗 在线体验（Hugging Face Space）

👉 [点击体验 Poetic Mirror ⬈](https://huggingface.co/spaces/slxhere/Poetic_Mirror)

<p align="center">
  <img src="https://github.com/kylin0421/poetic-mirror/blob/main/template.png?raw=true" width="1000"/>
</p>

> 如果界面打不开，可能是 Space 还在唤醒中，请稍等片刻

---

## ✨ 项目亮点

- 🧠 利用语义匹配模型实现“以文找诗”，不是关键词搜索
- 🎯 Recall@1 提升至 0.19+，远超 baseline（0.02）
- ⚙️ 支持 embedding 缓存 + rerank 模块优化结果
- 🌐 已部署为 Hugging Face Space，可交互使用

---

## 💡 背景与动机

现代语言表达更趋理性、直接，而古典诗词则凝结着情绪、意象与象征。  
本项目尝试构建一种「语义桥梁」，让现代中文语句能够在古诗中找到情感与意境上的共鸣，从而激发新的创意表达方式。

---

## 🏗 技术架构

| 模块 | 说明 |
|------|------|
| 数据构建 | 利用大模型生成现代句-古诗对，构建 triplet 训练集 |
| 编码模型 | 双塔结构 + 微调 `sentence-transformers` 模型 |
| 检索系统 | `FAISS` 实时向量检索 |
| rerank 模块 | 使用大模型 `deepseek-chat` 二次排序提升精度 |
| 部署平台 | Hugging Face Space（无服务端运维） |

---



</details> <details> <summary>🌍 English Summary (click to expand)</summary>
Poetic Mirror is a semantic retrieval system that maps modern Chinese sentences to the most thematically resonant lines from classical Chinese poetry.
By leveraging sentence embeddings, vector search, and reranking, it enables modern expressions to be reflected in ancient verse — forming a poetic dialogue across time.

---

🔗 Online Demo

👉 [Try Poetic Mirror on Hugging Face Space ⬈](https://huggingface.co/spaces/slxhere/Poetic_Mirror)

---

✨ Highlights



🧠 Semantic retrieval instead of keyword matching

🎯 Recall@1 improved to 0.19+, far above baseline (0.02)

⚙️ Supports embedding caching + LLM-based reranking

🚀 Fully deployed via Hugging Face Space, no backend needed

---

💡 Motivation

Modern Chinese tends to be rational and direct, while classical poetry is rich in metaphor and emotion.
This project aims to bridge the two by retrieving poetic responses that reflect the semantics and sentiment of contemporary language.


---

🏗 Architecture

| Module	| Description |
|------|------|
| Data	| GPT-based generation of modern-poem triplets |
| Encoders	| Dual-tower sentence transformer, finetuned |
| Retrieval	| FAISS-based dense search |
| Rerank	| LLM-based reranking via DeepSeek-Chat |
| Deployment	| Hugging Face Space (no backend required) |



</details> 
