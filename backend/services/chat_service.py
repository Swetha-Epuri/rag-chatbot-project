from backend.retrieval.retriever import Retriever
from backend.prompts.promt_builder import PromptBuilder
from backend.llm.llm_service import LLMService
from backend.embeddings.embedding_service import EmbeddingService


class ChatService:

    def __init__(self):
        
        embedding_service = EmbeddingService()

        embeddings = embedding_service.get_embeddings()

        self.retriever = Retriever(embeddings)

        self.llm = LLMService()

    def ask(self,question):
        
        results = self.retriever.search(question)

        context = "\n\n".join(doc.page_content for doc in results)

        prompt = PromptBuilder.build(context,question)

        response = self.llm.generate(prompt)

        sources = []

        for doc in results:

            sources.append(f"{doc.metadata["source"]}" f"(Page {doc.metadata["page"]+1})")

        return response,sources

