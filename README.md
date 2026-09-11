# RAG Platform

A production-oriented Retrieval-Augmented Generation platform for question answering over user provided PDF documents.
The system combines semantic retrieval, lexical retrieval, hybrid ranking, cross-encoder reranking, conversational memory, asynchronous FastAPI endpoints, streaming responses and automated RAG evaluation.

## Features
- PDF document ingestion
- Text cleaning and recursive chunking
- Hugging Face sentence-transformer embeddings
- FAISS vector search
- BM25 lexical search
- Hybrid retrieval
- Cross-encoder reranking
- Context-grounded answer generation
- Local Ollama LLM integration
- Conversational memory
- Rest API
- Streaming chat responses
- Retrieval evaluation
- LLM-based answer evaluation
- Unit tests
- Modular service and repository architecture

## Architecture
```text
Client
    |
    V
FastAPI
    |
    V
Chat Service
    |
    ---> Conservation Memory
    |
    ---> Hybrid Retrieval
            |
            ---> FAISS
            |
            ---> BM25
            |
            V   
        Cross-Encoder Reranker
            |
            V
        Context Builder
            |
            V
        Prompt Builder
            |
            V
        Ollama LLM
            |
            V
        Answer + Sources     
```

