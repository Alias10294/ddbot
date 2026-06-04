from app.db.conversations import InMemoryConversationStore
from app.llm.client       import LangflowClient


class Chatbot:
    def __init__(self):
        self.conversations = InMemoryConversationStore()
        self.llm           = LangflowClient()


    def answer(self, conversation_id: str, message: str) -> str:
        answer = self.llm.generate(
            message    = message,
            session_id = conversation_id)

        self.conversations.add_message(
            conversation_id = conversation_id,
            role            = "user",
            content         = message)

        self.conversations.add_message(
            conversation_id = conversation_id,
            role            = "assistant",
            content         = answer)

        return answer