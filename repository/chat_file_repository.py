from repository.database import request_connect_db

class ChatFileRepository:
    db = request_connect_db('test')['DB']

    def find_by_chatroom_id(self, chatroom_id: str):
        response = self.db.execute(f"SELECT filename FROM chat_file WHERE chatroom_id = {chatroom_id}")

        if type(response) == list:
            return response[0]['filename']
        else:
            return None
