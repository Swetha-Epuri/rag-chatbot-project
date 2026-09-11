from unittest.mock import MagicMock
from langchain_core.documents import Document
from backend.services.hybrid_retrieval_service import (HybridRetrievalService)


def test_hybrid_retrieval():

    vector_repo = MagicMock()

    bm25_repo = MagicMock()

    reranker = MagicMock()

    document_a = Document(page_content="Document A")

    document_b = Document(page_content="Document B")

    vector_repo.similarity_search.return_value = [document_a]

    bm25_repo.search.return_value = [document_b]

    reranker.rerank.return_value = [(document_b, 0.95), (document_a, 0.80)]

    service = HybridRetrievalService(vector_repo,bm25_repo,reranker)

    context, sources, count, elapsed = (service.retrieve("test"))

    assert count ==2

    assert "Document A" in context

    assert "Document B" in context

    assert len(sources) == 2

    assert sources[0]["score"] == 0.95

    reranker.rerank.assert_called_once()

    