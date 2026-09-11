from rank_bm25 import BM25Okapi


class BM25Repository:

    def __init__(self, documents):

        self.documents = documents

        tokenized_documents = [self._tokenize(document.page_content) for document in documents]

        self.bm25 = BM25Okapi(tokenized_documents)

    def search(self, query, k):

        tokenized_query = self._tokenize(query)

        scores = self.bm25.get_scores(tokenized_query)

        ranked_indexes = sorted(range(len(scores)),
                                key=lambda i: scores[i],
                                reverse=True)

        return [self.documents[i] for i in ranked_indexes[:k]]


    @staticmethod
    def _tokenize(text):

        return text.lower().split()
    