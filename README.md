# First FastAPI backend app
> This is my first experience building backend application using Python with Docker, FastAPI, DBeaver!

I want to become a backend developer sooner, because that's a vast sphere to develop in. 

### Future perspectives of this base project:
- Validation and schemes (Pydantic): Вынести входящие и исходящие данные в Pydantic-схемы (DTO/Schemas), чтобы четко разделять модели базы данных и то, что отправляется клиенту.
- Migrations (Alembic): Настроить инструмент миграций Alembic, чтобы при изменении структуры таблиц в Python-коде база данных обновлялась автоматически без потери данных.
- CRUD Operations and tables connection: Добавить новые эндпоинты (изменение PUT/PATCH, удаление DELETE) и связать несколько таблиц между собой (например, Users -> Items).
- Machine Learning / Data Pipeline: Подключить библиотеки Pandas / NumPy и сделать эндпоинт, который принимает входящие параметры, прогоняет их через ML-модель и отдает предсказание.

Preferably CRUD, Machine Learning ways.