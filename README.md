# 🤖 PDF ChatBot with LangChain, Chroma & Gradio

A **local Retrieval-Augmented Generation (RAG) application** built with **LangChain** that allows users to **upload PDF documents** and ask **natural-language questions** about their content.

The system combines **semantic retrieval** with an **open-source LLM** to produce **grounded, context-aware answers**, while exposing **retrieval and chunking parameters** to understand and tune RAG behavior.

---

## 🖥️ Application Screenshot

![PDF ChatBot UI](./assets/app_screenshot.png)

---

## ✨ Key Features

- 📄 **PDF ingestion & querying** via LangChain document pipelines  
- 🔍 **Semantic retrieval** using **ChromaDB** as a vector store  
- 🧠 **Local open-source LLM** (**Flan-T5**) — no external APIs  
- 💬 **Multi-turn conversation memory** with LangChain memory modules  
- 🎛️ **Adjustable chunk size (runtime)** to study retrieval trade-offs  
- 🧩 **Modular LangChain architecture** (splitter → retriever → QA chain)  
- 🖥️ **Lightweight web UI** built with **Gradio**  
- 🔐 **Fully offline execution**

---

## 🏗️ Architecture Overview (LangChain-Centric)

**End-to-end RAG pipeline:**

1. **PDF upload** (Gradio UI)
2. **Text extraction** using `pdfplumber`
3. **Chunking** via `RecursiveCharacterTextSplitter`
4. **Embedding** with `HuggingFaceEmbeddings (MiniLM)`
5. **Vector storage** in `Chroma`
6. **Semantic retrieval** using LangChain retrievers
7. **Retrieval-Augmented Generation** via `RetrievalQA`
8. **Answer generation** with **Flan-T5**

This design mirrors **real-world production RAG systems**, with a clean separation between:
- document ingestion
- retrieval
- reasoning
- generation

---

## 🎛️ Adjustable Chunking (Why It Matters)

Chunking is a **core design decision in RAG systems**, and this project exposes it as a **runtime control**.

### Trade-offs:

- **Smaller chunks**
  - higher retrieval precision
  - lower noise
  - more retrieval steps

- **Larger chunks**
  - more context per chunk
  - fewer retrieval calls
  - higher risk of token overflow

By adjusting chunk size from the UI, you can directly observe:
- retrieval quality changes
- context-window limitations
- answer grounding behavior

This makes the project ideal for **learning LangChain internals and RAG optimization**.

---

## 🧠 How It Works (High Level)

- The PDF is split into **overlapping semantic chunks**
- Each chunk is converted into a **dense vector embedding**
- All embeddings are stored in **Chroma**
- A user query is embedded and **matched by semantic similarity**
- The top-k chunks are **injected into the LLM prompt**
- The LLM generates a **context-grounded answer**

> The model never answers from scratch — it reasons strictly over retrieved document context.

---

## 📁 Project Structure

```text
RAG Project/
│
├── app.py                # Gradio UI and user interaction
├── pdf_chatbot.py        # Core LangChain RAG pipeline
├── assets/
│   └── app_screenshot.png
└── README.md
