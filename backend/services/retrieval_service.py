import time
from backend.repositories.vector_repository import VectorRepository
from backend.config.settings import TOP_K_RESULTS


class RetrievalService:

    def __init__(self, repository):

        self.repository = repository

    def retrieve(self, question):

        start=time.perf_counter()

        docs = self.repository.similarity_search(question,TOP_K_RESULTS)

        elapsed = (time.perf_counter() - start) * 1000

        context = "\n\n".join(d.page_content for d in docs)

        sources = []

        for doc in docs:

            sources.append({"filename": doc.metadata["source"],
                            "page": doc.metadata["page"]+1})

        return context, sources, len(docs), elapsed