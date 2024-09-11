import json

from fastapi import FastAPI

from models.request import UserRequest, ChatRoomRequest
from models.response import ResponseDTO
from repository.chat_file_repository import ChatFileRepository
from repository.chat_repository import ChatDetailRepository, ChatRepository
from repository.result_repository import ResultRepository
from services.ai_chating_service import ai_chating
from services.ending_result_service import ending_result_chat_title, ending_result_chat_summary
from services.purify_service import purify
from services.sentiment_service import analyze_sentiment
from services.summary_service import summary
from services.tokenizer import get_most_tokens

app = FastAPI()

chat_repository = ChatRepository()
chat_detail_repository = ChatDetailRepository()
chat_file_repository = ChatFileRepository()
result_repository = ResultRepository()

@app.post('/ai/purify')
async def purify_router(user: UserRequest):
    res = {
        "success": True,
        "message": "응답이 성공적으로 생성되었습니다.",
        "data": json.loads(purify(
            username=user.username,
            chatroom_id=user.chatroom_uuid,
            relation=user.relation,
            explain_situation=chat_detail_repository.find_detail(user.chatroom_uuid),
            chat_message=user.chat_message,
            file_path=chat_file_repository.find_by_chatroom_id(user.chatroom_uuid)
        ))
    }

    return ResponseDTO(**res)

@app.post('/ai/summarize')
async def summary_router(user: UserRequest):
    res = {
        "success": True,
        "message": "응답이 성공적으로 생성되었습니다.",
        "data": json.loads(summary(
            username=user.username,
            chatroom_id=user.chatroom_uuid,
            relation=user.relation,
            explain_situation=chat_detail_repository.find_detail(user.chatroom_uuid),
            chat_message=user.chat_message,
            file_path=chat_file_repository.find_by_chatroom_id(user.chatroom_uuid)
        ))
    }

    return ResponseDTO(**res)

@app.post('/ai/chat')
async def chatbot_router(user: UserRequest):
    res = {
        "success": True,
        "message": "응답이 성공적으로 생성되었습니다.",
        "data": ai_chating(
            username=user.username,
            chatroom_id=user.chatroom_uuid,
            relation=user.relation,
            explain_situation=chat_detail_repository.find_detail(user.chatroom_uuid),
            chat_message=user.chat_message,
            file_path=chat_file_repository.find_by_chatroom_id(user.chatroom_uuid)
        )
    }

    return ResponseDTO(**res)
    

@app.post('/ai/end-chat')
async def end_chat_router(chat_room: ChatRoomRequest):
    username1, username2 = chat_room.usernames
    chatroom_uuid = chat_room.chatroom_uuid

    summary = {
        "title": ending_result_chat_title(
            relation=chat_room.relation,
            explain_situation=chat_detail_repository.find_detail(chatroom_uuid),
        ),
        "content": ending_result_chat_summary(
            relation=chat_room.relation,
            explain_situation=chat_detail_repository.find_detail(chatroom_uuid),
            whole_message=chat_repository.find_chat_by_chat_room(chatroom_uuid)
        )
    }
    result1 = {
        "username": username1,
        "chatroom_uuid": chatroom_uuid,
        "summary": summary,
        "most_words": get_most_tokens(chatroom_uuid),
        "sentiment": analyze_sentiment(username1, chatroom_uuid),
    }

    result2 = {
        "username": username2,
        "chatroom_uuid": chatroom_uuid,
        "summary": summary,
        "most_words": get_most_tokens(chatroom_uuid),
        "sentiment": analyze_sentiment(username2, chatroom_uuid),
    }

    result_repository.save(result1)
    result_repository.save(result2)

    response = {
        "success": True,
        "message": "요청이 성공하였습니다.",
        "data": None
    }

    return ResponseDTO(**response)
