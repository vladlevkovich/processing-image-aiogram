from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = 'postgresql+asyncpg://test:root@localhost/image_bot'


settings = Settings()
