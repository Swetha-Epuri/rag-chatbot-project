from backend.retrieval.retriever import Retriever
from backend.llm.llm_service import LLMService
from backend.embeddings.embedding_service import EmbeddingService
from backend.repositories.vector_repository import VectorRepository
from backend.services.retrieval_service import RetrievalService 
from backend.services.memory_service import MemoryService
from backend.config.settings import DOCUMENT_STORE_PATH
from backend.vectorstore.document_store import DocumentStore
from backend.repositories.bm25_repository import BM25Repository
from backend.services.hybrid_retrieval_service import (HybridRetrievalService)
from backend.config.settings import (DOCUMENT_STORE_PATH)
from backend.services.reranker_service import RerankerService


class Container:

    def __init__(self):
        
        embeddings = EmbeddingService().get_embeddings()

        vector_repository = VectorRepository(embeddings)

        document_store = DocumentStore(DOCUMENT_STORE_PATH)

        documents = document_store.load()

        bm25_repository = BM25Repository(documents)

        reranker = RerankerService()

        self.retrieval_service = HybridRetrievalService(vector_repository,bm25_repository,reranker)

        self.llm = LLMService()

        self.memory_service = MemoryService(max_messages=10)

        