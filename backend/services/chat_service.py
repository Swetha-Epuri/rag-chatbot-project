from backend.prompts.promt_builder import PromptBuilder
from backend.exceptions.custom_exceptions import LLMServiceError
from backend.logging.logger import logger
import time
from backend.dto.chat_dto import(ChatResultDTO,SourceDTO)

class ChatService:

    def __init__(self,retrieval_service,llm,memory_service):

        self.retrieval_service = retrieval_service

        self.llm = llm

        self.memory_service = memory_service

    async def ask(self,question,conversation_id):

        history = self.memory_service.get_history(conversation_id)

        history_text = "\n".join(f"{message['role']}:"f"{message['content']}" for message in history)

        context, sources, chunk_count, retrieval_time = self.retrieval_service.retrieve(question)

        prompt = PromptBuilder.build(context,question,history_text)

        self.memory_service.add_message(conversation_id,"user",question)

        llm_start = time.perf_counter()
            
        answer = await self.llm.generate(prompt)

        self.memory_service.add_message(conversation_id,"assistant",answer)

        llm_time = (time.perf_counter() - llm_start) * 1000

        source_dtos = [SourceDTO(filename=source["filename"],page=source["page"],score=source["score"])for source in sources]

        return ChatResultDTO(answer=answer,sources=source_dtos,retrieved_chunks=chunk_count,retrieval_time_ms=retrieval_time,llm_time_ms=llm_time)

    async def stream(self,question):

        (context, sources, chunk_count, retrieval_time) = self.retrieval_service.retrieve(question)
        
        prompt = PromptBuilder.build(context,question)

        return self.llm.stream_answer(prompt)

       