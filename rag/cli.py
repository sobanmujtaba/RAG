# rag/cli.py
# =============================
from rag.retrieval import load_index, retrieve
from rag.generation import generate


def run():
    index, chunks = load_index()

    while True:
        q = input("Ask (or exit): ")
        if q.lower() == "exit":
            break

        results = retrieve(q, index, chunks)
        context = "\n\n".join([r["text"] for r in results])

        print("\nContext:\n", context[:500])
        print("\nAnswer:")
        generate(context, q)