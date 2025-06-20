import os
import sys
from pymongo import MongoClient
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__) + "/../")
sys.path.insert(0, base_dir)
load_dotenv(os.path.join(base_dir, ".env"))

MONGO_CONNECTION = os.getenv("MONGO_URI")

mongo_client = MongoClient(MONGO_CONNECTION).socket_chat