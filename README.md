# 🪞 Poetic Mirror ｜现代句 → 古诗语义匹配系统

以现代中文为引，探寻古典诗意的回响。  
输入一句现代语言，系统将检索出最契合其语义的古诗句作为回应，构建“古今对话”的诗意桥梁。

---

## 🔗 在线体验（Hugging Face Space）

👉 [点击体验 Poetic Mirror ⬈](https://huggingface.co/spaces/slxhere/Poetic_Mirror)

<p align="center">
  <img src="https://huggingface.co/spaces/slxhere/Poetic_Mirror/resolve/main/preview.png" width="600"/>
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

## 🚀 快速开始（本地运行）

```bash
git clone https://github.com/kylin0421/poetic-mirror.git
cd poetic-mirror
pip install -r requirements.txt
python app.py
