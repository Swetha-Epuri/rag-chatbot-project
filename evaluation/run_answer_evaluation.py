import asyncio
import json
from backend.core.container import Container
from evaluation.answer_evaluator import (AnswerEvaluator)
from backend.services.chat_service import ChatService

def load_dataset():

    with open("data/evaluation/evaluation_dataset.json","r",encoding="utf-8") as file:
        return json.load(file)

async def main():

    print("\nStarting Answer Evaluation...\n")

    dataset = load_dataset()

    container = Container()

    chat_service = ChatService(container.retrieval_service,container.llm,container.memory_service)

    evaluator = AnswerEvaluator()

    results = []

    for item in dataset:

        question = item["question"]

        print(f"Evaluating: {question}")

        (context,sources,chunk_count,retrieval_time) = container.retrieval_service.retrieve(question)

        chat_result = await chat_service.ask(question,"test-001")

        answer = chat_result.answer

        evaluation = await evaluator.evaluate(question=question,context=context,answer=answer)

        results.append({"question": question,"answer": answer,"evaluation": evaluation})

        avg_answer_relevance = sum(items["evaluation"]["answer_relevance"]["score"] for items in results) / len(results)

        avg_faithfulness = sum(items["evaluation"]["faithfulness"]["score"] for items in results) / len(results)

        avg_context_relevance = sum(items["evaluation"]["context_relevance"]["score"] for items in results) / len(results)

        print("\n\nAnswer Evaluation RESULTS\n\n")

        for result in results:

            print(f"\nQuestion: {result['question']}")

            print(f"Answer Relevance: {result['evaluation']['answer_relevance']['score']}")

            print(f"Faithfulness: {result['evaluation']['faithfulness']['score']}")

            print(f"Context Relevance: {result['evaluation']['context_relevance']['score']}")


        print("\nAveraged Scores")

        print(f"Answer Relevance: {avg_answer_relevance:.3f}")

        print(f"Faithfulness: {avg_faithfulness:.3f}")

        print(f"Context Relevance: {avg_context_relevance:.3f}")


if __name__ == "__main__":

    asyncio.run(main())

