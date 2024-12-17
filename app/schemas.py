from pydantic import BaseModel


class ChatCreate(BaseModel):
    user_1: str
    user_2: str


class ChatResponse(BaseModel):
    id: int
    user_1: str
    user_2: str
    active: bool

    class Config:
        from_attributes = True


class ChatCreateRequest(BaseModel):
    user_1: str
    user_2: str
    user_1_secret: str


class AcceptInvitationRequest(BaseModel):
    user_2_secret: str
