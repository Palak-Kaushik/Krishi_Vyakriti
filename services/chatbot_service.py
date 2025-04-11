import os
import pickle
import numpy as np
import faiss
import torch
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
import gradio as gr

# === Configuration ===
INDEX_PATH = "/home/sanjyot/Desktop/Vyakriti2.0-SIH-2024-1563/Krishi_Vyakriti/services/faiss_index.index"
CHUNKS_PATH = "/home/sanjyot/Desktop/Vyakriti2.0-SIH-2024-1563/Krishi_Vyakriti/services/text_chunks.pkl"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 3
GENAI_API_KEY = "AIzaSyCHBfm_5boUJvTh7n4VdkYMzTA4dMveLRo"  #gemini api key
# === Load Gemini
genai.configure(api_key=GENAI_API_KEY)

# === Load embedding model (just once)
device = "cuda" if torch.cuda.is_available() else "cpu"
embedding_model = SentenceTransformer(MODEL_NAME, device=device)
gen_model = genai.GenerativeModel("gemini-1.5-pro")


# === Load FAISS vector DB
def load_vector_database():
    if os.path.exists(INDEX_PATH) and os.path.exists(CHUNKS_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(CHUNKS_PATH, "rb") as f:
            chunks = pickle.load(f)
        return index, chunks
    else:
        raise FileNotFoundError("Vector DB files not found. Please generate them before running the chatbot.")


# === Retrieve Relevant Chunks
def retrieve_chunks(query, index, chunks, top_k=TOP_K):
    query_embedding = embedding_model.encode(query, normalize_embeddings=True).reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    return [chunks[i] for i in indices[0]]


# === Generate response using Gemini
def generate_response_with_gemini(query, context):
    prompt = (
        "You are an expert in precision agriculture. Use the context below to answer the query.\n"
        "Be concise, helpful, and only use the given information.\n\n"
        f"---\n{context}\n---\n"
        f"Query: {query}\n"
        "Answer:"
    )
    response = gen_model.generate_content(prompt)
    return response.text.strip()


# === Full Query Handler
def generate_response(query):
    index, chunks = load_vector_database()
    relevant_chunks = retrieve_chunks(query, index, chunks)
    context = "\n---\n".join(relevant_chunks)
    return generate_response_with_gemini(query, context)


# === Suggested Questions
def get_suggested_questions():
    return [
        "What is precision agriculture?",
        "How to improve soil fertility in sandy soil?",
        "What are NDVI-based insights?",
        "Is drip irrigation better than sprinkler?",
        "What sensors are used in smart farming?"
    ]


# === Gradio Chat UI
def run_chatbot():
    with gr.Blocks(title="Precision Agriculture Chatbot") as demo:
        gr.Markdown("# 🌱 Precision Agriculture Gemini Chatbot")
        gr.Markdown("Ask about farming practices, soil health, irrigation,and more!")

        chatbot = gr.Chatbot()
        msg = gr.Textbox(placeholder="Type your question here...")
        clear = gr.Button("Clear Chat")

        chat_history = []

        def respond(user_input):
            nonlocal chat_history
            response = generate_response(user_input)
            chat_history.append((user_input, response))
            return "", chat_history

        msg.submit(respond, inputs=[msg], outputs=[msg, chatbot])
        clear.click(lambda: [], None, chatbot, queue=False)

    demo.launch(share=True, debug=True)


# === Run the chatbot when the script is executed
if __name__ == "__main__":
    run_chatbot()
