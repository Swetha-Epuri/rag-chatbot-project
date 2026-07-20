from loaders.pdf_loader import PDFLoader
from preprocess.cleaner import TextCleaner
from chunking.chunker import DocumentChunker
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
    
    
    for i, chunk in enumerate(chunks[:5], start=1):
        print(f"\nChunk {i}\n")

        print("Source :", chunk.metadata["source"])

        print(" Page :", chunk.metadata["page"])

        print()

        print(chunk.page_content[:400])

    print("\nChunk Statistics\n")

    for chunk in chunks[:5]:

        print(len(chunk.page_content))

    print(chunks[0].metadata)
if __name__=='__main__':
    main()