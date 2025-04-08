from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client.novaforge

async def save_version(app_name: str, code: str):
    latest = await db.apps.find_one({"app_name": app_name}, sort=[("version", -1)])
    version = latest["version"] + 1 if latest else 1

    await db.apps.insert_one({
        "app_name": app_name,
        "version": version,
        "code": code,
        "timestamp": datetime.utcnow()
    })

async def get_versions(app_name: str):
    return await db.apps.find({"app_name": app_name}).to_list(None)

async def get_latest_version(app_name: str):
    return await db.apps.find_one({"app_name": app_name}, sort=[("version", -1)])