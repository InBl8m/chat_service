from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Chat
from app.schemas import ChatCreateRequest

router = APIRouter()


@router.post("/create_chat")
def create_chat(chat_data: ChatCreateRequest, db: Session = Depends(get_db)):
    # Создание нового чата
    chat = Chat(
        user_1=chat_data.user_1,
        user_2=chat_data.user_2,
        offer=chat_data.offer,
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return chat


@router.get("/invited/{user_2}")
def get_pending_invitations(user_2: str, db: Session = Depends(get_db)):
    # Ищем непринятые приглашения для user_2
    invitations = db.query(Chat).filter(Chat.user_2 == user_2, Chat.active == False).all()

    if not invitations:
        raise HTTPException(status_code=404, detail="No pending invitations found.")

    return invitations


@router.post("/accept_invitation/{chat_id}")
def accept_invitation(chat_id: int, db: Session = Depends(get_db)):
    # Найти чат по ID
    chat = db.query(Chat).filter(Chat.id == chat_id).first()

    # Если чат не найден
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found.")

    # Если чат уже активен
    if chat.active:
        raise HTTPException(status_code=400, detail="Chat is already active.")

    chat.active = True

    # Сохранить изменения
    db.commit()
    db.refresh(chat)

    return {"message": "Invitation accepted.", "chat": chat}
