from collections import defaultdict

class MemoryService:

    def __init__(self, max_messages=10):

        self.max_messages = max_messages

        self.conversations = defaultdict(list)

    def add_message(self,conversation_id,role,content):

        self.conversations[conversation_id].append({"role":role,"content":content})

        self._trim(conversation_id)

    def get_history(self,conversation_id):

        return self.conversations.get(conversation_id,[])

    def clear(self,conversation_id):
        self.conversations.pop(conversation_id,None)

    def _trim(self,conversation_id):

        history = self.conversations[conversation_id]

        if len(history) > self.max_messages:

            self.conversations[conversation_id] = history[-self.max_messages:]