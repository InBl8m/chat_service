from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.routers import chat
from app.database import create_tables
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение секретного ключа из переменных окружения
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not defined in the environment variables.")

# Создание таблиц в базе данных
create_tables()

# Инициализация приложения FastAPI
app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://192.168.1.196:3000"],
    allow_credentials=True,                  # Если вы используете cookies
    allow_methods=["*"],                     # Разрешить все HTTP-методы
    allow_headers=["*"],                     # Разрешить все заголовки
)
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# Подключение маршрутов
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
