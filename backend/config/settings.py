from pathlib import Path

PROJECT_ROOT =Path(__file__).resolve().parent.parent.parent

DATA_DIR = PROJECT_ROOT / "data"
PDF_DIR = DATA_DIR / "pdfs"
VECTORISE_DIR = PROJECT_ROOT / "vectorstore"

TOP_K_RESULTS=3

MODEL_NAME = "llama3.2:3b"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

