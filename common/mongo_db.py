from dotenv import dotenv_values
from pymongo import MongoClient
from bson import ObjectId

config = dotenv_values(".env")


class MongoDb():
    def __init__(self):
        self.mongodb_client = MongoClient(config["ATLAS_URI"])
        self.database = self.mongodb_client[config["DB_NAME"]]

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

        if (data is not None):
            self.database[collection].update_one(
                {"_id": ObjectId(id)}, {"$set": new_data})
            return self.database[collection].find_one({"_id": ObjectId(id)}), 201
        else:
            return {}, 404
