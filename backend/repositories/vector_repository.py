from langchain_community.vectorstores import FAISS
from backend.config.settings import VECTORISE_DIR


class VectorRepository:

    def __init__(self,embeddings):

        self.db = FAISS.load_local(str(VECTORISE_DIR),embeddings,allow_dangerous_deserialization=True)

    def similarity_search(self,query,k):

        return self.db.similarity_search(query,k=k)
    