class DocumentRepository:

    def __init__(self):

        self.documents = []

    def add_documents(self, documents):

        self.documents = documents

    def get_documents(self):

        return self.documents