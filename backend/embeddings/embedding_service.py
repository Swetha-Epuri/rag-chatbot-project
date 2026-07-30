from langchain_huggingface import HuggingFaceEmbeddings
from backend.config.settings import EMBEDDING_MODEL

class EmbeddingService:

    def __init__(self):
        self.model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)  

    def get_embeddings(self):

        return self.model