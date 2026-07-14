from loaders.pdf_loader import PDFLoader



def main():

    loader = PDFLoader("data/pdfs")

    documents = loader.load_documents()

    print(f"Loaded {len(documents)} pages")

    print()

    for doc in documents:

        print(doc.metadata)

        print()

        print(doc.page_content[:300])

        print()

if __name__=='__main__':
    main()