from fastapi import FastAPI
from app.routers import chat
from app.database import create_tables


create_tables()

app = FastAPI()

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
