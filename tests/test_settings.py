from backend.config.settings import MODEL_NAME
from backend.config.settings import TOP_K_RESULTS

def test_model_name():

    assert MODEL_NAME == "llama3.2:3b"

def test_top_k():

    assert TOP_K_RESULTS == 3