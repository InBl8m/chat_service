from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Chat(Base):
    __tablename__ = 'chats'

    id = Column(Integer, primary_key=True, index=True)
    user_1 = Column(String, index=True)
    user_2 = Column(String, index=True)
    user_1_secret = Column(String, nullable=True)
    user_2_secret = Column(String, nullable=True)
    active = Column(Boolean, default=False)
