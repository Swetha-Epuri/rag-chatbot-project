import time
from evaluation.metrics import (hit_at_k,recall_at_k,reciprocal_rank)


class RetrievalEvaluator:

    def __init__(self,retrieval_service,k=5):

        self.retrieval_service = (retrieval_service)

        self.k = k

    def evaluate_query(self,question,relevant_sources):

        start_time = time.perf_counter()

        result = self.retrieval_service.retrieve(question)

        elapsed_ms = (time.perf_counter()-start_time) * 1000

        context,sources,chunk_count, _ =result

        return {
            "question": question,
            "hit_at_k": hit_at_k(sources,relevant_sources,self.k),
            "recall_at_k": recall_at_k(sources,relevant_sources,self.k),
            "reciprocal_rank": reciprocal_rank(sources,relevant_sources),
            "latency_ms": elapsed_ms,
            "retrievaed_chunks": chunk_count
        }

    def evaluate_dataset(self,dataset):

        results = []

        for item in dataset:

            result = self.evaluate_query(question=item["question"],relevant_sources=item["relevant_sources"])

            results.append(result)

        if not results:

            return{
                "hit_at_k": 0.0,
                "recall_at_k": 0.0,
                "mrr": 0.0,
                "avg_latency_ms": 0.0
            }

        return{
                "hit_at_k": sum(result["hit_at_k"] for result in results)/len(results),
                        "recall_at_k": sum(result["recall_at_k"] for result in results)/len(results),
                        "mrr": sum(result["reciprocal_rank"] for result in results)/len(results),
                        "avg_latency_ms": sum(result["latency_ms"] for result in results)/len(results),
                        "query_results": results
                    }