# Fixed imports for runtime
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory




# ------------------------------
# PDF loading
# ------------------------------
def load_pdf(pdf_file):
    raw_text = ""
    with pdfplumber.open(pdf_file.name) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                raw_text += text + "\n"
    if not raw_text.strip():
        return None
    return raw_text

# ------------------------------
# Retriever builder (adjustable chunk size)
# ------------------------------
def build_retriever_from_text(raw_text, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_text(raw_text)
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_texts(chunks, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 5})

# ------------------------------
# LLM loader (lazy)
# ------------------------------
llm = None

def load_llm_if_needed():
    global llm
    if not llm:
        model_name = "google/flan-t5-base"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_length=512)
        llm = HuggingFacePipeline(pipeline=pipe)
    return llm

# ------------------------------
# Global objects
# ------------------------------
retriever = None
qa_chain = None

# ------------------------------
# Setup QA (called when PDF is uploaded)
# ------------------------------
def setup_qa(pdf_file, chunk_size=500):
    global retriever, qa_chain
    
    text = load_pdf(pdf_file)
    if not text:
        return "❗ PDF is empty or unreadable."
    
    retriever = build_retriever_from_text(text, chunk_size=chunk_size)
    
    # Optional multi-turn memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=load_llm_if_needed(),
        retriever=retriever,
        chain_type_kwargs={"memory": memory}
    )
    return f"✅ PDF uploaded and processed. You can now ask questions about {pdf_file.name}."

# ------------------------------
# Ask question function
# ------------------------------
def ask_question(query):
    if not qa_chain:
        return "❗ Please upload a PDF first."
    result = qa_chain.invoke({"query": query})
    return result["result"]
