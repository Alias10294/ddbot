from app.db.conversations import InMemoryConversationStore, Message
from app.llm.client       import OllamaClient
from app.agent.prompts    import SYSTEM_PROMPT


class Chatbot:
    def __init__(self):
        self.conversations = InMemoryConversationStore()
        self.llm           = OllamaClient()


    def answer(self, conversation_id: str, message: str) -> str:
        history = self.conversations.get_history(conversation_id)

        messages: list[Message] = [
            {
                "role"   : "system",
                "content": SYSTEM_PROMPT,
            },
            *history,
            {
                "role"   : "user",
                "content": message,
            }
        ]
        answer = self.llm.generate(messages)


        self.conversations.add_message(
            conversation_id = conversation_id,
            role            = "user",
            content         = message)
        self.conversations.add_message(
            conversation_id = conversation_id,
            role            = "assistant",
            content         = answer)
        
        return answer