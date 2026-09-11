from langchain_core.documents import Document
from backend.repositories.bm25_repository import (BM25Repository)

def test_bm25_exact_keyword():

    documents = [Document(page_content="Python programming language"),
                 Document(page_content="Hava programming language"),
                 Document(page_content="XJ-4927 authentication error")]

    repository = BM25Repository(documents)

    results = repository.search("XJ-4927", 1)

    assert len(results) == 1

    assert "XJ-4927" in (results[0].page_content)