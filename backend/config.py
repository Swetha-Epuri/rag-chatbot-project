from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ROOT =Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
PDF_DIR = DATA_DIR / "pdfs"
VECTORISE_DIR = PROJECT_ROOT / "vectorstore"

TOP_K_RESULTS=3

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

