from langchain_community.vectorstores import FAISS
from config import VECTORISE_DIR,TOP_K_RESULTS

class Retriever:

    def __init__(self, embedding_model):
        self.db=FAISS.load_local(str(VECTORISE_DIR),embedding_model,allow_dangerous_deserialization=True)

    def search(self,query):

        results = self.db.similarity_search(query,k=TOP_K_RESULTS)

        return results