from pymongo import MongoClient
import os 
from dotenv import load_dotenv

load_dotenv("../.env")

MONGO_CONNECTION = os.getenv("MONGO_URI")

mongo_client = MongoClient(MONGO_CONNECTION).socket_chat