import requests
from openai import OpenAI

from app.core.config import settings


class LLMClient:
    def __init__(self):
        self.provider = settings.llm_provider

        if self.provider == "openai":
            if not settings.openai_api_key:
                raise RuntimeError("OPENAI_API_KEY is required when LLM_PROVIDER=openai")
            self.openai_client = OpenAI(api_key=settings.openai_api_key)
        else:
            self.openai_client = None

    def generate(self, prompt: str) -> str:
        if self.provider == "openai":
            return self._generate_openai(prompt)

        if self.provider == "ollama":
            return self._generate_ollama(prompt)

        return self._generate_fake(prompt)

    def _generate_openai(self, prompt: str) -> str:
        response = self.openai_client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {
                    "role": "system",
                    "content": "Tu es un assistant spécialisé en sensibilisation à la cybersécurité.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response.choices[0].message.content or ""

    def _generate_ollama(self, prompt: str) -> str:
        response = requests.post(
            f"{settings.ollama_base_url}/api/chat",
            json={
                "model": settings.ollama_model,
                "messages": [
                    {
                        "role": "system",
                        "content": "Tu es un assistant spécialisé en sensibilisation à la cybersécurité.",
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()
        data = response.json()

        return data["message"]["content"]

    def _generate_fake(self, prompt: str) -> str:
        return (
            "Réponse simulée du chatbot. "
            "Le backend fonctionne correctement."
        )