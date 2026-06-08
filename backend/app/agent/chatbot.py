from app.db.conversations import InMemoryConversationStore
from app.llm.client       import LangflowClient
from app.rag.classerRag   import selectionner_chunk


class Chatbot:
    def __init__(self):
        self.conversations = InMemoryConversationStore()
        self.llm           = LangflowClient()


    def answer(self, conversation_id: str, message: str) -> str:
        print("=== CHAT REQUEST ===")
        print("MESSAGE:", message)

        chunks = selectionner_chunk(message)

        print("=== RAG OK ===")
        print("CHUNKS:", len(chunks))

        augmented_message = self._build_augmented_message(
            message = message,
            chunks  = chunks)

        print("=== AUGMENTED MESSAGE OK ===")
        print("LENGTH:", len(augmented_message))
        print("PREVIEW:", augmented_message[:1000])

        answer = self.llm.generate(
            message    = augmented_message,
            session_id = conversation_id)

        print("=== LLM OK ===")

        self.conversations.add_message(
            conversation_id = conversation_id,
            role            = "user",
            content         = message)

        self.conversations.add_message(
            conversation_id = conversation_id,
            role            = "assistant",
            content         = answer)

        return answer


    def _build_augmented_message(self, message: str, chunks: list[dict]) -> str:
        contexte = "\n\n".join(
            f"Source : {chunk.get('url', 'source inconnue')}\n{chunk.get('content', '')}"
            for chunk in chunks
        )

        if not contexte:
            return message

        return f"""
Contexte :
{contexte}

Question :
{message}
""".strip()