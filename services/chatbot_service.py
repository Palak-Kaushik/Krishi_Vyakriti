
import os
import numpy as np
import pickle
import faiss
import torch
import google.generativeai as genai
from langchain.embeddings import HuggingFaceEmbeddings
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])  # gemini api key

INDEX_PATH = r"C:\Palak\git\precision_agriculture\the_code\Krishi_Vyakriti\services\faiss_index(1) (1).index"
CHUNKS_PATH = r"C:\Palak\git\precision_agriculture\the_code\Krishi_Vyakriti\services\text_chunks.pkl"

# Load embedding model once
device = "cuda" if torch.cuda.is_available() else "cpu"

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="./local_models/all-mpnet-base-v2",
    model_kwargs={"device": device},
    cache_folder="./local_models/"  # Explicitly set cache folder
)

# Load precomputed FAISS index and chunks
def load_vector_database():
    if os.path.exists(INDEX_PATH) and os.path.exists(CHUNKS_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(CHUNKS_PATH, "rb") as f:
            chunks = pickle.load(f)
        return index, chunks
    else:
        raise FileNotFoundError("FAISS index or text chunks not found. Please initialize the DB first.")

def retrieve_chunks(query, index, chunks, top_k=3):
    query_embedding = np.array(embedding_model.embed_query(query)).reshape(1, -1)
    distances, indices = index.search(query_embedding, top_k)
    return [chunks[i] for i in indices[0]]

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