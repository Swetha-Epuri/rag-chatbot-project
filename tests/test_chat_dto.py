from backend.dto.chat_dto import ChatResultDTO, SourceDTO


def test_chat_result_creation():

    result = ChatResultDTO(answer="AI",sources=[SourceDTO("AI.pdf",1,0.95)],retrieved_chunks=1,retrieval_time_ms=10.00,llm_time_ms=100.0)

    assert result.answer == "AI"
    assert len(result.sources) == 1
    assert result.sources[0].filename.endswith("AI.pdf")
    assert result.sources[0].page == 1
    assert result.sources[0].score == 0.95