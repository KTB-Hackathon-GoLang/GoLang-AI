from pydantic import BaseModel

class Messages(BaseModel):
    messages: list[str]

class ResponseDTO(BaseModel):
    success: bool
    message: str
    data: Messages | str | None
