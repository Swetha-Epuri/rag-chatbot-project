import asyncio
from evaluation.answer_evaluator import (AnswerEvaluator)

async def main():

    evaluator = AnswerEvaluator()

    result = await (evaluator.evaluate_answer_relevance(question=("What is machine learning?"),
                                                        answer = (
                                                            "Machine learning is a branch " 
                                                            "of artificial. intelligence that "
                                                            "learns patterns from data,"
                                                        )))
    print(result)

if __name__ == "__main__":
    asyncio.run(main())