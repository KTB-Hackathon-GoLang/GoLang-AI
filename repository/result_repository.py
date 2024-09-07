from pymongo import MongoClient

class ResultRepository:
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test']
    collection = db['chatResult']

    def save(self, result):
        self.collection.insert_one(result)
