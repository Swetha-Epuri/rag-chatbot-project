from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader



class PDFLoader:
    def __init__(self, pdf_directory: str):
        self.pdf_directory = Path(pdf_directory)

    def load_documents(self):
        
        documents = []

        pdf_files = self.pdf_directory.glob("*.pdf")

        for pdf in pdf_files:

            try:
            
                print(f"Loading {pdf.name}")
            
                loader = PyPDFLoader(str(pdf))
            
                pages = loader.load()
            
                documents.extend(pages)
            
            except Exception as e:

                print(f"Could not load {pdf.name}")

                print(e)
                
        
        return documents

