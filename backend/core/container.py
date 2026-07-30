from backend.retrieval.retriever import Retriever
from backend.llm.llm_service import LLMService
from backend.embeddings.embedding_service import EmbeddingService


class Container:

    def __init__(self):
        
        embeddings = EmbeddingService().get_embeddings()

        self.retriever = Retriever(embeddings)

        self.llm = LLMService()