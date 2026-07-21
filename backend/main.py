from loaders.pdf_loader import PDFLoader
from preprocess.cleaner import TextCleaner
from chunking.chunker import DocumentChunker
from embeddings.embedding_service import EmbeddingService
from vectorstore.faiss_store import FAISSstore
from retrieval.retriever import Retriever
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




    print("\nTop Retrieved Chunks:\n")

    for i,doc in enumerate(results, start=1):

        print(f"\n\nResult {i}\n")

        print("Source :", doc.metadata["source"])

        print("Page :",doc.metadata["page"])

        print()

        print(doc.page_content[:400])
        
if __name__=='__main__':
    main()