from dotenv import load_dotenv
import os
from pymongo import MongoClient
from bson import ObjectId

load_dotenv()


class MongoDb():
    def __init__(self):
        self.mongodb_client = MongoClient(os.getenv("ATLAS_URI"))
        self.database = self.mongodb_client[os.getenv("DB_NAME")]

    def get_all(self, collection):
        books = list(self.database[collection].find(limit=100))
        return books, 200

    def get(self, collection, id):
        data = self.database[collection].find_one({"_id": ObjectId(id)})
        if (data) is not None:
            return data, 200
        else:
            return {}, 404

    def insert(self, collection, data):
        insert_data = self.database[collection].insert_one(data)
        created_data = self.database[collection].find_one(
            {"_id": insert_data.inserted_id})
        return created_data, 201

    def delete(self, collection, id):
        delete_result = self.database[collection].delete_one(
            {"_id": ObjectId(id)})
        if delete_result.deleted_count == 1:
            return {}, 204
        else:
            return {}, 404

    def patch(self, collection, id, new_data):
        data = self.database[collection].find_one({"_id": ObjectId(id)})

        if ("_id" in new_data):
            del new_data["_id"]
        if (type(id) == ObjectId):
            id = str(id)

        if (data is not None):
            self.database[collection].update_one(
                {"_id": ObjectId(id)}, {"$set": new_data})
            return self.database[collection].find_one({"_id": ObjectId(id)}), 200
        else:
            return {}, 404

    def db_find(self, collection, multiple, query):
        if (multiple):
            data = list(self.database[collection].find(query))
        else:
            data = self.database[collection].find_one(query)
        if (data) is not None:
            return data, 200
        else:
            return {}, 404
