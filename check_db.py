from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Chat  # Импорт модели Chat из вашего проекта
from app.database import Base, get_db
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Получаем данные подключения из .env
POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

# Строка подключения к базе данных PostgreSQL
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Создаем движок SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Получаем сессию и делаем запрос
def check_chats():
    db = SessionLocal()
    try:
        # Запрос всех записей из таблицы Chat
        chats = db.query(Chat).all()

        # Выводим все записи
        for chat in chats:
            print(f"Chat ID: {chat.id}, User 1: {chat.user_1}, User 2: {chat.user_2}, Active: {chat.active}")
    finally:
        db.close()

if __name__ == "__main__":
    check_chats()
