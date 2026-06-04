from collections import defaultdict
from typing      import Literal, TypedDict


Role = Literal["user", "assistant", "system"]


class Message(TypedDict):
    role   : Role
    content: str


class InMemoryConversationStore:
    def __init__(self):
        self._messages: dict[str, list[Message]] = defaultdict(list)


    def get_history(self, conversation_id: str, limit: int = 10) -> list[Message]:
        return self._messages[conversation_id][-limit:]

    def add_message(self, conversation_id: str, role: Role, content: str) -> None:
        self._messages[conversation_id].append(
            {
                "role": role,
                "content": content,
            })