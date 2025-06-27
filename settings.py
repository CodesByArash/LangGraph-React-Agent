from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    OPEN_WEATHER_API_KEY:str
    TAVILY_API_KEY:str
    OPENAI_API_KEY:str
    MAX_SEARCH_RESULTS:int
    class Config:
        env_file = ".env"


settings = Settings()
