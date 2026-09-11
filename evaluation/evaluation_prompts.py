ANSWER_RELEVANCE_PROMPT = """
You are an expert evaluator.
Evaluate how welll the answer adresses the user's question.

Qustion:
{question}

Answer:
{answer}

Give a score from 0 to 1.

Scoring guides:
1.0 = Completely anwers the question
0.8 = Mostly answers the question
0.5 = Partiallt answers the question
0.2 = Barely relevant
0.0 = Completeltl irrelevant

Return ONLY valid JSON.

Format:
{{
    "score": 0.0,
    "reason": "brief explaination"
}}
"""

FAITHFULNESS_PROMPT = """
You are an expert evaluator.
Determine whether the answer is supported by the provided context.

Context:
{context}

Answer:
{answer}

Give a score from 0 to 1.

Scoring guide:
1.0 = Fully supported by context
0.8 = Mostly supported
0.5 = Partiallly supported
0.2 = Mostly unsupported
0.0 = Completely unsupported or hallucinated

Return ONLY valid JSON.

Format:
{{
    "score": 0.0,
    "reason": "brief explaination"
}}
"""

CONTEXT_RELEVANCE_PROMPT = """
You are an expert evaluator.
Determine whether the answer is useful for answer the user's question.

Question:
{question}

Context:
{context}


Give a score from 0 to 1.

Scoring guide:
1.0 = Highly relevant 
0.8 = Mostly relevant
0.5 = Partiallly relevant
0.2 = Barely relevant
0.0 = Completely irrelevant

Return ONLY valid JSON.

Format:
{{
    "score": 0.0,
    "reason": "brief explaination"
}}
"""