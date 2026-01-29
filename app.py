# app.py
import gradio as gr
from pdf_chatbot import setup_qa, ask_question

with gr.Blocks() as demo:
    gr.Markdown("# 🤖 PDF ChatBot with LangChain + Chroma")
    
    with gr.Row():
        pdf_file = gr.File(label="Upload PDF")
        upload_button = gr.Button("Process PDF")
        chunk_size_input = gr.Slider(minimum=200, maximum=2000, step=100, value=500, label="Chunk size")
    
    status = gr.Textbox(label="Status")
    
    with gr.Row():
        question = gr.Textbox(label="Ask a Question")
        answer = gr.Textbox(label="Answer")
        ask_button = gr.Button("Ask")
    
    # Connect buttons
    upload_button.click(fn=setup_qa, inputs=[pdf_file, chunk_size_input], outputs=status)
    ask_button.click(fn=ask_question, inputs=question, outputs=answer, queue=False)

demo.launch()


