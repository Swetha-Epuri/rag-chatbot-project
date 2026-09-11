from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from backend.schemas.request_models import ChatRequest
from backend.schemas.response_models import (SourceResponse,ChatResponse)
from backend.core.container import Container
from backend.services.chat_service import ChatService
from backend.indexing.build_index import build_index
from backend.logging.logger import logger
from backend.api.streaming import stream_response



router = APIRouter(prefix="/api/v1")

container = Container()


chat_service = ChatService(container.retrieval_service,container.llm,container.memory_service)



@router.get("/health")
def health():
    return {
        "status": "healthy", "service": "RAG Chatbot"
    }



@router.post(
    "/chat", response_model=ChatResponse
)
async def chat(request: ChatRequest):

    logger.info(f"Received Question: {request.question}")
    
    result = await chat_service.ask(request.question,request.conversation_id)

    logger.info("Answer generated.")

    return ChatResponse(
        answer=result.answer,
        sources=[SourceResponse(filename=source.filename,
                                page=source.page,
                                score=round(source.score,4))
                for source in result.sources],
                retrieved_chunks=result.retrieved_chunks, 
                retrieval_time_ms=round(result.retrieval_time_ms,2),
                llm_time_ms=round(result.llm_time_ms,2))



@router.post("/index")
def rebuild():

    build_index()

    return{"status": "success"}


@router.post("/chat/stream")
async def stream_chat(request: ChatRequest):

    stream = await chat_service.stream(request.question)

    return StreamingResponse(stream, media_type="text/plain")


@router.delete("/conversations/{conversation_id}")
async def clear_conversation(converstion_id: str):

    chat_service.memory_service.clear(converstion_id)

    return {"status":"cleared", "conversation_id":converstion_id}
