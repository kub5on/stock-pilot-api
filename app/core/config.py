from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
    from typing import Literal
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR/".env.example",
        env_ignore_empty=True,
        env_file_encoding="utf-8",
        extra="ignore"
    )
    app_name: str = "stock-API"
    database_url: str = "DATABASE_URL"
    secret_key: str = "secret_key"
    algorithm: str = "HS256"
    debug: bool = True
    Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    finnhub_api_key: str = "finnhub-key"
    finnhub_base_url: str = "https://finnhub.io/api/v1"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    api_v1_str: str = "/api/v1"
    cors_origins: list[str] = [
        "http://localhost:3000", # frontend
        #"https://app.com"       # deployment
    ]

settings = Settings()
