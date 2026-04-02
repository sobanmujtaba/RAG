import os
import pickle
import numpy as np
import faiss
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from rag.loader import load_docs
from rag.chunking import chunk_text
from rag.config import *

embedder = SentenceTransformer(EMBED_MODEL, device="cpu")

def build_index():
    docs = load_docs(DOCS_PATH)
    all_chunks = []

    for filename, doc in docs:
        chunks = chunk_text(doc)
        for chunk in chunks:
            all_chunks.append({
                "text": chunk,
                "source": os.path.basename(filename)
            })

    texts = [c["text"] for c in all_chunks]

    embeddings = [embedder.encode(t) for t in tqdm(texts)]
    embeddings = np.array(embeddings).astype("float32")

    faiss.normalize_L2(embeddings)

    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)

    os.makedirs(STORE_PATH, exist_ok=True)
    faiss.write_index(index, INDEX_FILE)

    with open(CHUNKS_FILE, "wb") as f:
        pickle.dump(all_chunks, f)