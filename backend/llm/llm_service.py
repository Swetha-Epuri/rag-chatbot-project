from langchain_ollama import ChatOllama

class LLMService:

    def __init__(self):
        self.llm = ChatOllama(model="llama3.2:3b", temperature=0)

    def generate(self,prompt):
        
        response = self.llm.invoke(prompt)

        return response.content