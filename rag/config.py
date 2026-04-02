# rag/config.py

MODEL = "qwen2.5:3b"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

DOCS_PATH = "./docs/"
STORE_PATH = "./vectorstore/"

INDEX_FILE = f"{STORE_PATH}/faiss.index"
CHUNKS_FILE = f"{STORE_PATH}/chunks.pkl"

EMBED_MODEL = "BAAI/bge-base-en-v1.5"
RERANK_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"