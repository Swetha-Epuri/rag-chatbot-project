from pydantic import BaseModel


class SourceResponse(BaseModel):

    filename: str

    page: int

    score: float


class ChatResponse(BaseModel):
    answer: str

    sources: list[SourceResponse]

    retrieved_chunks: int

    retrieval_time_ms: float

    llm_time_ms: float