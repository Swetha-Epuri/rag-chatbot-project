# System Architecture

```mermaid
flowchart TD
    A[User] --> B[FastAPI]
    B --> C[Chat Service]
    C --> D[Conversation Memory]
    C --> E[Hybrid Retrieval]
    E --> F[FAISS Vetor Search]
    E --> G[BM25 Keyword Search]
    F --> H[Candidate Merge]
    G --> H[Candidate Merge]
    H --> I[Cross-Encoder Reranker]
    I --> J[Context Builder]
    J --> K[Prompt Builder]
    K --> L[Ollama LLM]
    L --> M[Answer + Sources]
    M --> B
