import re

class TextCleaner:

    @staticmethod
    def clean_text(text:str) -> str:

        text = re.sub(r"\s+"," ", text)

        return text.strip()
    
    @staticmethod
    def remove_empty_documents(documents):
        
        cleaned = []

        for doc in documents:

            if doc.page_content.strip():

                cleaned.append(doc)

        return cleaned