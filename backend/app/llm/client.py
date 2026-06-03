import requests

from app.config           import settings
from app.db.conversations import Message


class OllamaClient:
    def generate(self, messages: list[Message]) -> str:
        response = requests.post(
            f"{settings.ollama_base_url}/api/chat",
            json={
                "model": settings.ollama_model,
                "messages": messages,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"]