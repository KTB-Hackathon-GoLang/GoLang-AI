import json

from fastapi import FastAPI

from models.response import ResponseDTO
from models.message import UserMessage
from services.purify_service import purify
from services.summary_service import summary

with open('prompts/purify_prompt', 'r') as file:
    purify_prompt = file.read()

with open('prompts/summary_prompt', 'r') as file:
    summary_prompt = file.read()

app = FastAPI()

@app.post('/ai/purify')
async def purify_router(user_message: UserMessage):
    res = {
        "success": True,
        "message": "응답이 성공적으로 생성되었습니다.",
        "data": json.loads(purify(purify_prompt, user_message.message))
    }
    return ResponseDTO(**res)

@app.post('/ai/summary')
async def summary_router(user_message: UserMessage):
    res = {
        "success": True,
        "message": "응답이 성공적으로 생성되었습니다.",
        "data": json.loads(summary(summary_prompt, user_message.message))
    }
    return ResponseDTO(**res)
