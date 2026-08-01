from backend.preprocess.cleaner import TextCleaner
from langchain_core.documents import Document

def test_clean_text_removes_extra_spaces():

    text = "Hello      All"

    cleaned = TextCleaner.clean_text(text)

    assert cleaned == "Hello All"


def test_clean_text_removes_newlines():

    text = "Hello\n\nAll"

    cleaned = TextCleaner.clean_text(text)

    assert cleaned == "Hello All"

def test_remove_empty_documents():

    docs = [Document(page_content="AI"),Document(page_content=""),Document(page_content="Machine Learning")]

    result = TextCleaner.remove_empty_documents(docs)

    assert len(result) == 2
    