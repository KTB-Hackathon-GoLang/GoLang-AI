from pydantic import BaseModel

class UserMessage(BaseModel):
    user: str
    target: str
    message: str