import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

load_dotenv()
# 1. Настройка подключения к PostgreSQL в Docker
# Формат: postgresql://user:password@host:port/database
DB_URL = os.getenv("DB_URL", "postgres://postgres:postgres@127.0.0.1:5432/dev_db")

# 2. Настройка подключения к PostgreSQL
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 3. Описание модели таблицы (Using SQLAlchemy ORM)
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

# Автоматически создаем таблицу в БД при запуске 
Base.metadata.create_all(bind=engine)

class ItemCreate(BaseModel):
    title:str

class ItemResponse(BaseModel):
    id:int
    title:str

    class Config:
        from_attributes = True

# 4. Инициализация приложения FastAPI
app=FastAPI(title="My first Backend API")

# Вспомогательная функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 4. API Эндпоинты (Марщруты)
@app.get("/")
def read_root():
    return {"message":"Бэкэнд успешно работает и подключен к PostgreSQL!"}

@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(title = item.title)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    """Получение всех записей из базы данных"""
    items = db.query(Item).all()
    return items