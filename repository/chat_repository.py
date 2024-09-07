from pymongo import MongoClient

from repository.database import request_connect_db


class ChatRepository:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test']
    collection = db['chatMessage']

    def find_chat_by_username(self, username: str, chatroom_uuid: str) -> list[str]:
        query = { 'chatroomUUID': chatroom_uuid, 'username': username }
        projection = { '_id': 0, 'username': 1, 'message': 1 }

        cursor = self.collection.find(query, projection).sort('send_at', 1)

        results = [ ]
        for cur in cursor:
            results.append(cur)

        return results

    def find_chat_by_chat_room(self, chatroom_uuid: str) -> list[dict]:
        query = { 'chatroomUUID': chatroom_uuid }
        projection = {'_id': 0, 'username': 1, 'message': 1}

        cursor = self.collection.find(query, projection).sort('send_at', 1)

        results = []
        for cur in cursor:
            results.append(cur)

        return results

class ChatDetailRepository:
    db = request_connect_db('test')['DB']

    def find_detail(self, chatroom_id) -> str:
        response = self.db.execute(f'SELECT detail FROM chat_detail WHERE chatroom_id = {chatroom_id}')

        return response[0]['detail']
