from backend.prompts.promt_builder import PromptBuilder
from backend.exceptions.custom_exceptions import LLMServiceError
from backend.logging.logger import logger


class ChatService:

    def __init__(self,retriever,llm):

        self.retriever = retriever

        self.llm = llm

    def ask(self,question):
        
        results = self.retriever.search(question)

        context = "\n\n".join(doc.page_content for doc in results)

        prompt = PromptBuilder.build(context,question)

        try:
            
            response = self.llm.generate(prompt)

        except Exception as e:
            
            logger.exception("LLM generation failed.")

            raise LLMServiceError(str(e))
        
        sources = []

        for doc in results:

            sources.append(f"{doc.metadata["source"]}" f"(Page {doc.metadata["page"]+1})")

        return response,sources

