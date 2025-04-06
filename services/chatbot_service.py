import os
import numpy as np
import pickle
import faiss
import torch
import google.generativeai as genai
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # gemini api key

INDEX_PATH = r"C:\Palak\git\precision_agriculture\the_code\Krishi_Vyakriti\services\faiss_index(1) (1).index"
CHUNKS_PATH = r"C:\Palak\git\precision_agriculture\the_code\Krishi_Vyakriti\services\text_chunks.pkl"
DOC_PATH = "Agrotech.docx"

# Load embedding model once
device = "cuda" if torch.cuda.is_available() else "cpu"
embedding_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-mpnet-base-v2", device=device)

#load precomputed FAISS index and chunks
def load_vector_database():
    if os.path.exists(INDEX_PATH) and os.path.exists(CHUNKS_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(CHUNKS_PATH, "rb") as f:
            chunks = pickle.load(f)
        return index, chunks
    else:
        raise FileNotFoundError("FAISS index or text chunks not found. Please initialize the DB first.") #functuion call and chunks

def retrieve_chunks(query, index, chunks, top_k=3):
    query_embedding = np.array(embedding_model.get_text_embedding(query)).reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    return [chunks[i] for i in indices[0]] #chunk retrieval 

def generate_response_with_gemini(query, context):
    prompt = (
        "You are an expert in precision agriculture. Use the context below to answer the query.\n"
        "Be concise and relevant.\n\n"
        f"---\n{context}\n---\n"
        f"Query: {query}\n"
        "Answer:"
    )
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_response(query: str):
    index, chunks = load_vector_database()
    relevant_chunks = retrieve_chunks(query, index, chunks)
    context = "\n---\n".join(relevant_chunks)
    return generate_response_with_gemini(query, context)

def get_suggested_questions():
    """Get a list of suggested questions for the chatbot"""
    return [
        "What crops are suitable for clay soil?",
        "How to identify nutrient deficiency in wheat?",
        "Best practices for drip irrigation",
        "How to interpret my NDVI results?",
        "When should I harvest my maize crop?"
    ]

