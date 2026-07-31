import logging
from pathlib import Path

from backend.config.settings import PROJECT_ROOT

LOG_DIR =PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE =LOG_DIR / "rag_chatbot.log"

logger = logging.getLogger("rag_chatbot")

logger.setLevel(logging.INFO)

if not logger.handlers:

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    file_handler = logging.FileHandler(LOG_FILE)

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)
    