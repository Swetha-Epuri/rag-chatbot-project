from langchain_core.documents import Document
from backend.chunking.chunker import DocumentChunker

def test_chunk_creation():

    document = Document(page_content="Artificial Intelligence " * 500)

    chunker = DocumentChunker()

    chunks = chunker.split_documents([document])

    assert len(chunks) > 1