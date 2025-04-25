from pymongo import MongoClient
from config import config

class Collection:
    """A class to interact with a MongoDB collection.
    It provides methods to insert, find, update, and delete documents."""
    
    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        self.collection = MongoClient[config.DB_STRING][config.DB_NAME][collection_name]

    def insert_document(self, document):
        """Insert a single document into the collection."""
        return self.collection.insert_one(document)

    def find_document(self, query):
        """Find a single document based on a query."""
        return self.collection.find_one(query)

    def find_documents(self, query):
        """Find multiple documents based on a query."""
        return list(self.collection.find(query))

    def update_document(self, query, update_values):
        """Update a single document based on a query."""
        return self.collection.update_one(query, {"$set": update_values})

    def delete_document(self, query):
        """Delete a single document based on a query."""
        return self.collection.delete_one(query)

    def delete_documents(self, query):
        """Delete multiple documents based on a query."""
        return self.collection.delete_many(query)
    
    