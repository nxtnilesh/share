from pymongo import MongoClient
import logging

def connect_to_mongo(uri, db_name):
    try:
        client = MongoClient(uri)
        return client[db_name]
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {e}")
        raise
