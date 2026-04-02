import glob
import PyPDF2

def load_docs(path):
    docs = []

    for f in glob.glob(f"{path}/*"):
        if f.endswith(".txt"):
            with open(f, "r", encoding="utf-8") as file:
                docs.append((f, file.read()))

        elif f.endswith(".pdf"):
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            docs.append((f, text))

    return docs