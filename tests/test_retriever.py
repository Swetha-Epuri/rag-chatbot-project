from unittest.mock import MagicMock
from backend.retrieval.retriever import Retriever

def test_search_calls_vector_store():

    retriever = Retriever.__new__(Retriever)

    retriever.db = MagicMock()

    retriever.db.similarity_search.return_value = []

    retriever.search("AI")

    retriever.db.similarity_search.assert_called_once()