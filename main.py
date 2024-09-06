import json

from fastapi import FastAPI

from models.response import ResponseDTO
from models.message import UserMessage
from services.purify_service import purify
from services.summary_service import summary

app = FastAPI()

@app.post('/ai/purify')
async def purify_router(user_message: UserMessage):
    res = {
        "success": True,
        "message": "응답이 성공적으로 생성되었습니다.",
        "data": json.loads(purify(user_message.user_name, user_message.relation, user_message.message))
    }

    return ResponseDTO(**res)

@app.post('/ai/summary')
async def summary_router(user_message: UserMessage):
    res = {
        "success": True,
        "message": "응답이 성공적으로 생성되었습니다.",
        "data": json.loads(summary(user_message.user_name, user_message.relation, user_message.message))
    }

    return ResponseDTO(**res)
