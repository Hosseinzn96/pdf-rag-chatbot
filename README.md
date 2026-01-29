
# 🤖 PDF ChatBot with LangChain, Chroma & Gradio

A **local Retrieval-Augmented Generation (RAG) application** that allows you to **upload a PDF** and ask **natural-language questions** about its content.  
The system uses **semantic search + an open-source LLM** to generate **accurate, context-aware answers**.

---

## ✨ Key Features

- 📄 **Upload any PDF** and query its content  
- 🔍 **Semantic retrieval** using **ChromaDB**  
- 🧠 **Local open-source LLM** (Flan-T5)  
- 💬 **Multi-turn conversation memory**  
- 🎛️ **Adjustable chunk size** for better retrieval quality  
- 🖥️ **Simple web UI** built with **Gradio**  
- 🔐 **No external APIs** – runs fully **offline**

---

## 🏗️ Architecture Overview

**Pipeline flow:**

1. **PDF upload**
2. Text extraction with **pdfplumber**
3. Chunking via **RecursiveCharacterTextSplitter**
4. Embedding with **Sentence-Transformers (MiniLM)**
5. Vector storage in **Chroma**
6. **Retrieval-Augmented Generation** using **LangChain RetrievalQA**
7. Answer generation with **Flan-T5**

---

## 🧠 How It Works (High Level)

- The PDF is converted into **overlapping text chunks**
- Each chunk is transformed into a **dense vector embedding**
- Chunks are stored in **Chroma** (in-memory vector database)
- User queries are embedded and **matched semantically**
- Retrieved context is **injected into the LLM prompt**
- The model generates a **grounded, context-aware answer**

---

## 🚀 Possible Improvements

- ✅ Persistent **Chroma** storage  
- ✅ **Session-based state** (multi-user)  
- ✅ **FastAPI backend**  
- ✅ **Docker & Cloud Run** deployment  
- ✅ **Agent-based RAG**  
- ✅ **Streaming responses**

---

## 📌 Tech Stack

- **Python 3.9+**
- **LangChain**
- **ChromaDB**
- **Transformers**
- **Sentence-Transformers**
- **Gradio**
- **pdfplumber**

---

## 🧑‍💻 Author

Built as a **hands-on RAG learning project** to understand:  
**document ingestion, semantic search, and LLM-based QA pipelines**.

