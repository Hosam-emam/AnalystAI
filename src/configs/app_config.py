from dotenv import load_dotenv
load_dotenv()
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # App Configuration
    APP_NAME: str = "AnalystAI"
    APP_VERSION: str = "0.0.1"
    
    # OpenRouter Configuration
    OPENROUTER_API_KEY: str

    # Logging Confguration
    LOG_DIR: str = "src/logs"
    LOG_MAX_BYTES: int = 10485760
    LOG_BACKUP_COUNT: int = 3

@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()