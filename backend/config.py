from pathlib import Path

PROJECT_ROOT =Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

PDF_DIR = DATA_DIR / "pdfs"

VECTORISE_DIR = PROJECT_ROOT / "vectorstore"