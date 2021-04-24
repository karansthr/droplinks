import hashlib
import uuid
from datetime import datetime, timedelta

from droplinks.db import database

user_collection = database.user
session_collection = database.session


def hash_password(password):
    return hashlib.sha224(password.encode("utf-8")).hexdigest()


async def user_exists(username=None, email=None):

    if username is email is None:
        return False
    if username and await database.user_collection.find_one({"username": username}):
        return True
    if email and await database.user_collection.find_one({"email": email}):
        return True
    return False


async def is_valid_user(username, password):
    if await database.user_collection.find_one(
        {"username": username, "password": password}
    ):
        print(
            await database.user_collection.find_one(
                {"username": username, "password": password}
            )
        )
        return True
    return False


async def create_user(userdata):
    result = await user_collection.insert_one(userdata)
    return result


async def create_session(username):
    session_id = uuid.uuid1()
    await session_collection.insert_one(
        {"username": username, "expires_on": datetime.now() + timedelta(days=15)}
    )
    return session_id
