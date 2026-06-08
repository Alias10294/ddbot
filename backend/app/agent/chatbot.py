from urllib.parse import quote, unquote, urlsplit, urlunsplit, parse_qsl, urlencode

from app.db.conversations import InMemoryConversationStore
from app.llm.client       import LangflowClient
from app.rag.classerRag   import selectionner_chunk


class Chatbot:
    def __init__(self):
        self.conversations = InMemoryConversationStore()
        self.llm           = LangflowClient()


    def answer(self, conversation_id: str, message: str) -> str:
        chunks = selectionner_chunk(message)

        augmented_message = self._build_augmented_message(
            message = message,
            chunks  = chunks)

        answer = self.llm.generate(
            message    = augmented_message,
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


    def _encode_url_for_prompt(self, url: str | None) -> str:
        if not url:
            return "source inconnue"

        parts = urlsplit(url)

        if not parts.scheme or not parts.netloc:
            return url

        encoded_path = quote(unquote(parts.path), safe="/")
        encoded_query = urlencode(parse_qsl(parts.query), doseq=True)

        return urlunsplit((
            parts.scheme,
            parts.netloc,
            encoded_path,
            encoded_query,
            parts.fragment,
        ))


    def _build_augmented_message(self, message: str, chunks: list[dict]) -> str:
        contexte = "\n\n".join(
            f"Source : {self._encode_url_for_prompt(chunk.get('url'))}\n"
            f"{chunk.get('content', '')}"
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