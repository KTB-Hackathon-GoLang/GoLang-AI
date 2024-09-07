import ast

import requests

import secret
from repository.chat_repository import ChatRepository

headers = {
    'Content-Type': 'application/json',
    'X-NCP-APIGW-API-KEY-ID': secret.NAVER_CLOUD_ACCESS_KEY,
    'X-NCP-APIGW-API-KEY': secret.NAVER_CLOUD_SECRET_KEY
}

chat_repository = ChatRepository()

def analyze_sentiment(user_id, chatroom_id):
    chats = chat_repository.find_chat_by_username(user_id, chatroom_id)
    content = '\n'.join([chat['message'] for chat in chats])

    res = requests.post(
        'https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze',
        headers=headers,
        json={
            'content': content
        })

    return ast.literal_eval(res.content.decode())['document']['confidence']
