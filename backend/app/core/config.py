from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Agent de Sécurité UPHF"
    app_env: str = "dev"

    frontend_origin: str = "http://localhost:5173"

    llm_provider: str = "fake"
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"

    class Config:
        env_file = ".env"


settings = Settings()