import json
from backend.llm.llm_service import LLMService
from evaluation.evaluation_prompts import (ANSWER_RELEVANCE_PROMPT,FAITHFULNESS_PROMPT,CONTEXT_RELEVANCE_PROMPT)

class AnswerEvaluator:

    def __init__(self):
        self.llm = LLMService()

    async def evaluate_answer_relevance(self,question,answer):

        prompt = ANSWER_RELEVANCE_PROMPT.format(question=question,answer=answer)

        response = await self.llm.generate(prompt)

        return self._parse_response(response)

    async def evaluate_faithfulness(self,context,answer):

        prompt = FAITHFULNESS_PROMPT.format(self,context=context,answer=answer)

        response = await self.llm.generate(prompt)

        return self._parse_response(response)

    async def evaluate_context_relevance(self,question,context):

        prompt = CONTEXT_RELEVANCE_PROMPT.format(self,question=question,context=context)

        response = await self.llm.generate(prompt)

        return self._parse_response(response)

    async def evaluate(self,question,context,answer):

        answer_relevance = await (self.evaluate_answer_relevance(question,answer))

        faithfulness = await ( self.evaluate_faithfulness(context,answer))

        context_relevance = await ( self.evaluate_context_relevance(question,context))

        return {"answer_relevance":answer_relevance,"faithfulness":faithfulness,"context_relevance":context_relevance}
        

    def _parse_response(self,response):
        try:

            return json.loads(response)

        except json.JSONDecodeError:

            try:

                start = response.find("{")

                end = response.rfind("}") + 1

                json_content = response[start:end]

                return json.loads(json_content)

            except Exception:

                return {
                "score": 0.0,
                "reason": ("could not parse"
                           "evaluation response")
            }

    