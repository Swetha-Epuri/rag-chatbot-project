from langchain_ollama import ChatOllama
from backend.config.settings import MODEL_NAME


class LLMService:

    def __init__(self):
        self.llm = ChatOllama(model=MODEL_NAME, temperature=0)

    async def generate(self,prompt):
        
        response = await self.llm.ainvoke(prompt)

        return response.content
    
    async def stream_answer(self,prompt):

        async for chunk in self.llm.astream(prompt):

           if chunk.content:
               yield chunk.content