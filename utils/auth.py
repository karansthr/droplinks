import hashlib
import uuid
from datetime import datetime, timedelta

from droplinks.db import database


def hash_password(password):
    return hashlib.sha224(bytes(password)).hexdigest()


async def user_exists(username=None, email=None):
    if username is email is None:
        return False
    result = False
    if username and await database.user_collections.find({"username": username}):
        result = True
    if email and await database.user_collections.find({"email": email}):
        result = True
    return result


async def is_valid_user(username, password):
    if await database.user_collections.get(
        {"username": username, "password": password}
    ):
        return True
    return False


async def create_user(userdata):
    result = await database.user_collections.insert_one(userdata)
    return result


async def create_session(username):
    session_id = uuid.uuid1()
    user = await database.user_collections.get({"username": username})
    await database.session.insert_one(
        {"username": user.username, "expires_on": datetime.now() + timedelta(days=15)}
    )
    return session_id
