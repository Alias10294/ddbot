from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Agent de Sécurité UPHF"
    app_env : str = "dev"

    frontend_origin: str = "http://localhost:5173"

    langflow_base_url: str = "http://langflow:7860"
    langflow_flow_id : str = ""
    langflow_api_key : str = ""

    class Config:
        env_file = ".env"


settings = Settings()