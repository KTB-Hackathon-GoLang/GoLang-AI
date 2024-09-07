from pydantic import BaseModel

class UserRequest(BaseModel):
    username: str
    relation: str
    chatroom_uuid: str
    chat_message: str
    chat_type: str

class ChatRoomRequest(BaseModel):
    usernames: list[str]
    chatroom_uuid: str
    relation: str
