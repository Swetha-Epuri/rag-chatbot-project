from backend.embeddings.embedding_service import EmbeddingService

def test_embedding_service_creation():

    service = EmbeddingService()

    embeddings = service.get_embeddings()

    assert embeddings is not None