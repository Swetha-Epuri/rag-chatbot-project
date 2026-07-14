from loaders.pdf_loader import PDFLoader
from preprocess.cleaner import TextCleaner
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
    
    for doc in cleaned_documents[:2]:

        print("\nSource :", doc.metadata["source"])

        print("Page :", doc.metadata["page"])

        print()

        print(doc.page_content[:300])

if __name__=='__main__':
    main()