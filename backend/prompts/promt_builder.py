class PromptBuilder:

    @staticmethod
    def build(context, question, history=""):

        return f"""
You are an AI assistant

Answer the user's question using the provided document context and conversation history. 

Rules:

1. Use the document context as the primary source of factual information.

2. Use conversation history to understand references such as "it", "they", or "that".

3. Do not invent information.

4. If the answer cannot be found in the document, say:
"I couldn't find that information in the uploaded documents." 

Conversation History:

{history}

Documnet Context:

{context}

Current Question:

{question}

Answer:
"""