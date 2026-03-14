from pydantic import BaseSettings


class Settings(BaseSettings):
    app_env: str = "development"

    model_name: str = "demo-linear-model"

    class Config:
        env_file = ".env"


settings = Settings()