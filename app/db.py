import os
from pymongo import MongoClient

DB = os.getenv('DATABASE')

client = MongoClient()
db = client[DB]
