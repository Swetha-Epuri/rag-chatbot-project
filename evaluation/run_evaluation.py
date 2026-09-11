import json
from backend.core.container import Container
from evaluation.evaluator import RetrievalEvaluator


def load_dataset():

    with open("data/evaluation/evaluation_dataset.json","r",encoding = "utf-8") as file:
        return json.load(file)

def main():

    print("\nStarting RAG Evaluation ...\n")

    dataset = load_dataset()

    container = Container()

    evaluator = RetrievalEvaluator(retrieval_service=container.retrieval_service,k=5)

    results = evaluator.evaluate_dataset(dataset)

    print(f"Hit@5:{results['hit_at_k']:.3f}")

    print(f"Recall@5:{results['recall_at_k']:.3f}")

    print(f"MRR: {results['mrr']:.3f}")

    print(f"Average Latency: {results['avg_latency_ms']:.2f} ms")

    print("\n\n\nPer Query Results:\n")

    for result in results["query_results"]:

        print(f"Question: {result['question']}")

        print(f"Hit@5: {result['hit_at_k']}")

        print(f"Recall@5: {result['recall_at_k']:.3f}")

        print(f"Reciprocal Rank: {result['reciprocal_rank']:.3f}")

        print(f"Latency: {result['latency_ms']:.2f} ms")

if __name__=="__main__":
    main()