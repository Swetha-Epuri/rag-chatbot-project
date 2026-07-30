from langchain_ollama import ChatOllama
from backend.config.settings import MODEL_NAME


class LLMService:

    def __init__(self):
        self.llm = ChatOllama(model=MODEL_NAME, temperature=0)

    def generate(self,prompt):
        
        response = self.llm.invoke(prompt)

        return response.content