import pickle
import faiss
from sentence_transformers import SentenceTransformer, CrossEncoder
from rag.config import *

embedder = SentenceTransformer(EMBED_MODEL, device="cpu")
reranker = CrossEncoder(RERANK_MODEL, device="cpu")

def load_index():
    index = faiss.read_index(INDEX_FILE)
    with open(CHUNKS_FILE, "rb") as f:
        chunks = pickle.load(f)
    return index, chunks

def retrieve(query, index, chunks, k=10, final_k=3):
    q = embedder.encode([query]).astype("float32")
    faiss.normalize_L2(q)

    _, indices = index.search(q, k)
    candidates = [chunks[i] for i in indices[0]]

    pairs = [[query, c["text"]] for c in candidates]
    scores = reranker.predict(pairs)

    ranked = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)

    return [c for c, _ in ranked[:final_k]]