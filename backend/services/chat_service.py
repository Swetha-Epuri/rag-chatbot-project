from backend.prompts.promt_builder import PromptBuilder



class ChatService:

    def __init__(self,retriever,llm):

        self.retriever = retriever

        self.llm = llm

    def ask(self,question):
        
        results = self.retriever.search(question)

        context = "\n\n".join(doc.page_content for doc in results)

        prompt = PromptBuilder.build(context,question)

        response = self.llm.generate(prompt)

        sources = []

        for doc in results:

            sources.append(f"{doc.metadata["source"]}" f"(Page {doc.metadata["page"]+1})")

        return response,sources

