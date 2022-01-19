from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    db_name: str
    db_pass: str
    db_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
