from typing import Any

from pydantic import BaseModel

class PurifyDTO(BaseModel):
    messages_1: list[str]
    messages_2: list[str]

class SummaryDTO(BaseModel):
    summary: list[str]

class ResponseDTO(BaseModel):
    success: bool
    message: str
    data: PurifyDTO | SummaryDTO | None