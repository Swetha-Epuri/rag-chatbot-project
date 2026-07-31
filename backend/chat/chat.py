from backend.services.chat_service import ChatService
from backend.core.container import Container
from backend.logging.logger import logger

def main():

    container = Container()

    chat = ChatService(container.retriever,container.llm)

    while True:
        
        question = input("\nAsk a question (type exit to quit): ")

        if question.lower() == "exit":
            break
        try:

            answer, sources = chat.ask(question)
    
            print("\nAnswer\n")
            print(answer)

            logger.info("Response generated succesfully.")
        
        except Exception as e:

            print(f"\nError: {e}") 

        for source in sources:

            print(source)

if __name__=='__main__':
    main()