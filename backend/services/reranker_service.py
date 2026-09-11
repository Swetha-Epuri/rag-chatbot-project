from sentence_transformers import CrossEncoder


class RerankerService:

    def __init__(self):

        self.model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def rerank(self,question,documents,top_k=5):

        if not documents:
            return []

        pairs = [[question,document.page_content]
                 for document in documents]

        scores = self.model.predict(pairs)

        ranked = sorted(zip(documents,scores),
                        key = lambda x: x[1],
                        reverse=True)

        return [(document, float(score)) for document, score in ranked[:top_k]]