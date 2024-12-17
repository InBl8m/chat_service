from sqlalchemy.orm import Session
from .models import Chat


def create_chat(db: Session, user_1: str, user_2: str):
    new_chat = Chat(user_1=user_1, user_2=user_2, active=False)
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat


def get_chat_invites(db: Session, username: str):
    return db.query(Chat).filter(Chat.user_2 == username, Chat.active == False).all()


def accept_invitation(db: Session, chat_id: int, username: str):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if chat and chat.user_2 == username:
        chat.active = True
        db.commit()
        db.refresh(chat)
    return chat
