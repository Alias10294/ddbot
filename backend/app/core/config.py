from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Agent de Sécurité UPHF"
    app_env: str = "dev"

    frontend_origin: str = "http://localhost:5173"

    llm_provider: str = "fake"

    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"

    ollama_base_url: str = "http://ollama:11434"
    ollama_model: str = "llama3.2"

    class Config:
        env_file = ".env"


settings = Settings()