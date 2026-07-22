from langchain_ollama import ChatOllama

class LLMService:

    def __init__(self):
        self.llm = ChatOllama(model="llama3.2:3b", temperature=0)

    def get_llm(self):

        return self.llm