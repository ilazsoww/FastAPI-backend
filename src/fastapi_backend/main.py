from fastapi import FastAPI
from app.core.config import settings
from app.core.database import Base, engine
from app.api.v1.endpoints import items

# Заменит Alembic
# Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_TITLE)

app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/")
def read_root():
    return {"message":"Backend works & connected to PostgreSQL"}