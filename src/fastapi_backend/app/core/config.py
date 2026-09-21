import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_TITLE: str = "Backend API"
    DB_URL: str = os.getenv("DB_URL", "postgresql://postgres:postgres@127.0.0.1:5432/dev-db")

settings = Settings()