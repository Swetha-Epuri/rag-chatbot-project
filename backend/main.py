from loaders.pdf_loader import PDFLoader
from preprocess.cleaner import TextCleaner
from chunking.chunker import DocumentChunker
from embeddings.embedding_service import EmbeddingService
from vectorstore.faiss_store import FAISSstore
from retrieval.retriever import Retriever
from prompts.promt_builder import PromptBuilder
from llm.llm_service import LLMService
from config import PDF_DIR


def main():

    loader = PDFLoader(PDF_DIR)

    documents = loader.load_documents()

    print(f"\nLoaded {len(documents)} pages\n")

    cleaned_documents = []

    for doc in documents:

        cleaned_text = TextCleaner.clean_text(
            doc.page_content
        )

        doc.page_content = cleaned_text

        cleaned_documents.append(doc)

    cleaned_documents = TextCleaner.remove_empty_documents(cleaned_documents)

    chunker = DocumentChunker(chunk_size=500,chunk_overlap=100)

    chunks =chunker.split_documents(cleaned_documents)

    print(f"\nCreated {len(chunks)} chunks\n")
    
    


    embedding_service = EmbeddingService()

    embedding_model = embedding_service.get_embeddings()

    vector_store = FAISSstore(embedding_model)

    db = vector_store.create(chunks)

    print("\nFAISS Index Created Successfully!")



    retriever = Retriever(embedding_model)

    query = input("\nAsk a question: ")

    results = retriever.search(query)


    context = "\n\n".join([doc.page_content for doc in results])

    prompt = PromptBuilder.build(context,query)

    llm = LLMService().get_llm()

    response = llm.invoke(prompt)

    print("\nAnswer\n")

    print(response.content)

    print("\nSources\n")

    for doc in results:

        print( f"{doc.metadata["source"]}" f"(Page {doc.metadata["page"]+1})")

if __name__=='__main__':
    main()