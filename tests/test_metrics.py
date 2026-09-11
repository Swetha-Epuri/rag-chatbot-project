from evaluation.metrics import (hit_at_k,recall_at_k,reciprocal_rank)

retrieved = [
    {
        "filename": "AI.pdf",
        "page": 1
    },
    {
        "filename": "AI.pdf",
        "page": 2
    },
    {
        "filename": "AI.pdf",
        "page": 2
    }
]

relevant = [
    {
        "filename": "AI.pdf",
        "page": 2
    }
]

def test_hit_at_k():

    result = hit_at_k(retrieved,relevant,k=2)

    assert result == 1

def test_hit_at_k_not_found():

    result = hit_at_k(retrieved,relevant,k=1)

    assert result == 0

def test_recall_at_k():

    result = recall_at_k(retrieved,relevant,k=2)

    assert result == 1.0

def test_recall_at_k_not_found():

    retrieved_sources = [
        {
            "filename": "AI.pdf",
            "page": 1
        },
        {
            "filename": "AI.pdf",
            "page": 2
        },
        {
            "filename": "AI.pdf",
            "page": 3
        }
    ]

    relevant_sources = [
        {
            "filename": "AI.pdf",
            "page": 3
        }
    ]

    result = recall_at_k(retrieved,relevant,k=1)

    assert result == 0.0

def test_reciprocal_rank():

    result = reciprocal_rank(retrieved,relevant)

    assert result == 0.5