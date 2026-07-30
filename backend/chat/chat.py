from backend.services.chat_service import ChatService
from backend.core.container import Container


def main():

    container = Container()

    chat = ChatService(container.retriever,container.llm)

    while True:
        
        question = input("\nAsk a question (type exit to quit): ")

        if question.lower() == "exit":
            break
        
        answer, sources = chat.ask(question)

        print("\nAnswer\n")
    
        print(answer)
        
        for source in sources:

            print(source)

if __name__=='__main__':
    main()