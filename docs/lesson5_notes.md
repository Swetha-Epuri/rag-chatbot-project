1. What is an embedding?
Answer:An embedding is a dense numerical vector (a list of floating-point numbers) that represents the semantic meaning of data—such as text, images, or audio—in a high-dimensional continuous space.Instead of viewing text as raw characters, an embedding model maps semantic concepts into coordinates. Words or chunks of text with similar concepts end up closer together in this mathematical space.
Key Takeaway to Mention: It translates human concepts into a format that computers can compare using vector geometry (like cosine similarity).

2. Why are embeddings better than keyword search?
Answer:Keyword search relies on lexical matching—looking for exact character overlaps. Embeddings perform semantic search—capturing the underlying intent and contextual meaning regardless of word choice.Embeddings solve three major limitations of keyword search:
Synonyms: 'How to fix a flat tire' matches 'Replacing a punctured wheel.
Polysemy & Context: It understands the difference between 'bank' as a financial institution versus a 'river bank.'
Typo & Phrasing Resistance: It focuses on the overall idea rather than strict syntax.

3. Why do we need a vector database?
Answer:Traditional relational or document databases are optimized for exact filtering, indexing, and key-value lookups. They struggle with high-dimensional vector similarity searches at scale.A vector database is purpose-built to index, store, and query millions of high-dimensional vectors efficiently. It uses specialized Approximate Nearest Neighbor (ANN) algorithms—like HNSW or IVF—to find the top-$K$ most similar vectors in milliseconds, rather than scanning every record sequentially ($O(N)$ brute-force calculation).

4. Why use FAISS?
Answer:FAISS (Facebook AI Similarity Search) is an open-source library optimized for fast, scalable vector similarity search. I chose FAISS for this project because:
Zero External Infrastructure: It runs directly in-memory within Python/C++, eliminating the overhead of setting up and managing a full cloud cluster (like Pinecone or Qdrant).
Hardware Acceleration: It leverages native C++ optimization with optional GPU acceleration for extreme lookup speeds.
Algorithmic Versatility: It supports multiple indexing techniques (from simple flat L2 search to compressed IVF-PQ) depending on speed vs. accuracy tradeoffs.

5. What are vector dimensions?
Answer:A vector dimension represents the number of numerical features output by an embedding model to describe a piece of text. For instance, a 384-dimensional vector is simply a array containing 384 floating-point values.You can think of each dimension as a direction in a mathematical space capturing subtle linguistic nuances (e.g., tone, subject matter, tense).Higher dimensions (e.g., 1536 in OpenAI's text-embedding-3-small) capture richer semantic detail but consume more memory and compute.Lower dimensions (e.g., 384 in MiniLM) are significantly faster and lighter while retaining solid semantic representation for retrieval.

6. Why did we choose all-MiniLM-L6-v2?
Answer:We chose all-MiniLM-L6-v2 because it hits the sweet spot between speed, memory efficiency, and retrieval performance for local RAG applications:
Ultra-Lightweight & Fast: It produces 384-dimensional embeddings (compared to 1536+ for cloud models), making vector calculations and FAISS lookups fast on standard CPUs without requiring a GPU.
Completely Local & Private: Runs entirely on-device via sentence-transformers, meaning zero API latency, zero costs per token, and no sending sensitive document data over the wire.
Strong Benchmark Performance: Despite its small size (~80MB download), it performs exceptionally well on standard sentence representation benchmarks (MTEB) for general QA and semantic search.