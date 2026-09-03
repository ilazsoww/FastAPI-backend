from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# 1. Настройка подключения к PostgreSQL в Docker
# Формат: postgresql://user:password@host:port/database
DB_URL = "postgresql://postgres:postgres@127.0.0.1:5432/dev_db"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. Описание модели таблицы (Using SQLAlchemy ORM)
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

# Автоматически создаем таблицу в БД при запуске 
Base.metadata.create_all(bind=engine)

# 3. Инициализация приложения FastAPI
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

@app.post("/items/")
def create_item(title:str, db: Session = Depends(get_db)):
    """ Создание новой записи в базе данных через POST запрос """
    db_item = Item(title=title)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"status":"success", "item":{"id": db_item.id, "title":db_item.title}}

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    """Получение всех записей из базы данных"""
    items = db.query(Item).all()
    return items