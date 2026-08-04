from fastapi import APIRouter
from backend.schemas.request_models import ChatRequest
from backend.schemas.response_models import ChatResponse
from backend.core.container import Container
from backend.services.chat_service import ChatService
from backend.indexing.build_index import build_index
from backend.logging.logger import logger


router = APIRouter(prefix="/api/v1")

container = Container()


chat_service = ChatService(container.retriever,container.llm)



@router.get("/health")
def health():
    return {
        "status": "healthy", "service": "RAG Chatbot"
    }



@router.post(
    "/chat", response_model=ChatResponse
)
def chat(request: ChatRequest):

    logger.info(f"Received Question: {request.question}")
    
    answer,sources = chat_service.ask(request.question)

    logger.info("Answer generated.")

    return ChatResponse(answer=answer,sources=sources)



@router.post("/index")
def rebuild():

    build_index()

    return{"status": "success"}