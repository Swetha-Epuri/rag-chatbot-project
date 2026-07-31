class RAGChatbotError(Exception):
    pass

class PDFLoadError(RAGChatbotError):
    pass

class EmptyDocumentError(RAGChatbotError):
    pass

class VectorStoreError(RAGChatbotError):
    pass

class LLMServiceError(RAGChatbotError):
    pass