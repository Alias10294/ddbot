from app.agent.prompts    import SYSTEM_PROMPT
from app.db.conversations import ConversationRepository
from app.llm.client       import LLMClient


class Chatbot:
    def __init__(self):
        self.conversations = ConversationRepository()
        self.llm = LLMClient()

    def answer(self, conversation_id: str, message: str) -> str:
        history = self.conversations.get_history(conversation_id)

        self.conversations.add_message(
            conversation_id=conversation_id,
            role="user",
            content=message,
        )

        prompt = self._build_prompt(history, message)

        answer = self.llm.generate(prompt)

        self.conversations.add_message(
            conversation_id=conversation_id,
            role="assistant",
            content=answer,
        )

        return answer

    def _build_prompt(self, history: list[dict], message: str) -> str:
        formatted_history = "\n".join(
            f"{msg['role']}: {msg['content']}"
            for msg in history
        )

        return f"""
{SYSTEM_PROMPT}

Historique récent :
{formatted_history}

Message utilisateur :
{message}

Réponse :
"""