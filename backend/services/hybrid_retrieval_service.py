import time


class HybridRetrievalService:

    def __init__(self, vector_repository, bm25_repository, reranker):

        self.vector_repository = (vector_repository)

        self.bm25_repository = (bm25_repository)

        self.reranker = reranker

    def retrieve(self, question, k=20):

        start = time.perf_counter()

        vector_docs = (self.vector_repository.similarity_search(question, k))

        bm25_docs = (self.bm25_repository.search(question, k ))

        combined = []

        seen = set()

        for doc in vector_docs + bm25_docs:

            key = (doc.metadata.get("source"),
                   doc.metadata.get("page"),
                   doc.page_content)

            if key not in seen:

                seen.add(key)

                combined.append(doc)

        reranked = self.reranker.rerank(question,combined,top_k=5)

        documents = [document for document,score in reranked]


        context = "\n\n".join(document.page_content for document in documents)

        reranked_sources = [{ "filename": document.metadata.get("source", "unkown"),
                    "page": document.metadata.get("page", 0)+1,
                    "score": float(score)} 
                    for document,score in reranked]

        elapsed = (time.perf_counter()-start)*1000

        return(context,reranked_sources,len(documents),elapsed)