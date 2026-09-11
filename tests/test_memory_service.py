from backend.services.memory_service import MemoryService


def test_message_storage():

    memory = MemoryService()

    memory.add_message("test-1","user","Hello")

    history = memory.get_history("test-1")

    assert len(history)==1

    assert history[0]["content"] == "Hello"

def test_conversation_isolation():

    memory = MemoryService()
    
    memory.add_message("conversation-1","user","Hello")

    memory.add_message("conversation-2","user","Goodbye")

    assert len(memory.get_history("conversation-1"))==1

    assert len(memory.get_history("conversation-2"))==1

def test_clear_conversation():

    memory = MemoryService()
        
    memory.add_message("test-1","user","Hello")

    memory.clear("test-1")

    assert memory.get_history("test-1")==[]

def test_memory_limit():

    memory = MemoryService(max_messages=3)

    for i in range(5):
        memory.add_message("test-1","user",f"Message {i}")

    history = memory.get_history("test-1")

    assert len(history) == 3

    assert history[0]["content"] == "Message 2"

    assert history[1]["content"] == "Message 3"

    assert history[2]["content"] == "Message 4"