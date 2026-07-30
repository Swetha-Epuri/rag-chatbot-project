from backend.loaders.pdf_loader import PDFLoader
from backend.preprocess.cleaner import TextCleaner
from backend.chunking.chunker import DocumentChunker
from backend.embeddings.embedding_service import EmbeddingService
from backend.vectorstore.faiss_store import FAISSstore
from backend.config.settings import PDF_DIR


def build_index():

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



    chunker = DocumentChunker()

    chunks =chunker.split_documents(cleaned_documents)    
    
    print(f"\nCreated {len(chunks)} chunks\n")



    embedding_service = EmbeddingService()

    embedding_model = embedding_service.get_embeddings()

    vector_store = FAISSstore(embedding_model)

    vector_store.create(chunks)

    print("\nFAISS Index Created Successfully!")



if __name__=='__main__':
    build_index()