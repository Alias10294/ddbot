from collections import defaultdict


class ConversationRepository:
    def __init__(self):
        self._messages: dict[str, list[dict]] = defaultdict(list)

    def get_history(self, conversation_id: str, limit: int = 10) -> list[dict]:
        return self._messages[conversation_id][-limit:]

    def add_message(self, conversation_id: str, role: str, content: str) -> None:
        self._messages[conversation_id].append(
            {
                "role": role,
                "content": content,
            }
        )