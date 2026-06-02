from openai import OpenAI

from app.core.config import settings


class LLMClient:
    def __init__(self):
        self.provider = settings.llm_provider

        if self.provider == "openai":
            if not settings.openai_api_key:
                raise RuntimeError("OPENAI_API_KEY is required when LLM_PROVIDER=openai")

            self.client = OpenAI(api_key=settings.openai_api_key)
        else:
            self.client = None

    def generate(self, prompt: str) -> str:
        if self.provider == "openai":
            return self._generate_openai(prompt)

        return self._generate_fake(prompt)

    def _generate_openai(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
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

    def _generate_fake(self, prompt: str) -> str:
        return (
            "Réponse simulée du chatbot. "
            "Le backend fonctionne correctement. "
            "Vous pouvez maintenant brancher un vrai modèle LLM."
        )