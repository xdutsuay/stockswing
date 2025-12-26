import motor.motor_asyncio
from fastapi import Depends
from app.config import AppConfig

config = AppConfig()

client = motor.motor_asyncio.AsyncIOMotorClient(config.mongo_uri)
db = client["stockprod"]
