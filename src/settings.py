from typing import Literal

from pydantic import SecretStr, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    environment: Literal['dev', 'production'] = 'dev'

    api_id: int
    api_hash: str

    app_version: str
    session_filename: str
    commands_access: list[str]

    @computed_field
    @property
    def debug(self) -> bool:
        return self.environment == 'dev'

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
