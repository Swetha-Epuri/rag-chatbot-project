from dataclasses import dataclass
from typing import List

@dataclass
class SourceDTO:
    filename: str
    page: int
    score: float = 0.0

@dataclass
class ChatResultDTO:
    answer: str
    sources: List[SourceDTO]
    retrieved_chunks: int
    retrieval_time_ms: float
    llm_time_ms: float