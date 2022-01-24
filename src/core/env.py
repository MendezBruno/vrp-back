from pydantic import BaseSettings, Field
from functools import lru_cache


class Settings(BaseSettings):
    db_name: str = Field(None, env="DB_NAME")
    db_pass: str = Field(None, env="DB_PASS")
    db_url: str = Field(None, env="DB_URL")
    orsm_base_url: str = Field(None, env="ORSM_BASE_URL")

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=128)
def get_settings() -> Settings:
    return Settings(_env_file='../.env', _env_file_encoding='utf-8')


settings = get_settings()
