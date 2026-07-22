class PromptBuilder:

    @staticmethod
    def build(context, question):

        return f"""
You are an AI assistant

Answer ONLY using the context below. 

If the answer is not present in the context,

reply:

"I couldn't find that information in the uploaded documents." 

Context:

{context}

Question:

{question}

Answer:
"""