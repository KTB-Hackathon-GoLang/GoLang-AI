from pydantic import BaseModel

class UserMessage(BaseModel):
    user_name: str
    relation: str
    message: str