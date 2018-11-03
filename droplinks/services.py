from core import validators
from core.services import Service
from utils import status_codes
from utils.auth import (
    hash_password,
    user_exists,
    create_user,
    is_valid_user,
    create_session,
)
from .db import database


class CreateContact(Service):
    name = validators.String(max_length=120)
    email = validators.Email(max_length=120)
    subject = validators.String(max_length=120)
    message = validators.String(max_length=1200)

    async def process(self):
        collection = database.contacts
        await collection.insert_one(self.data)
        return {"message": "Request submitted successfully"}, 200


class Auth:
    user_collections = database.user

    class SignUpUser(Service):
        username = validators.String(max_length=120)
        password = validators.String(max_length=120)
        repassword = validators.String(max_length=120)
        email = validators.Email()

        async def process(self):
            if await user_exists(self.data["username"]):
                return ({"message": "User already exists"}, status_codes.CONFLICT)
            if self.data["password"] != self.data["repassword"]:
                return (
                    {"message": "Password does not match"},
                    status_codes.UNAUTHORIZED,
                )
            self.data["password"] = hash_password(self.data.pop("repassword"))
            try:
                await create_user(self.data)
                message = {"message": "User created successfully"}
                status_code = status_codes.OK
            except Exception:
                message = {"message": "Error creating user"}
                status_code = status_codes.BAD_REQUEST
                # log error
            return message, status_code

    class LoginUser(Service):
        username = validators.String(max_length=120)
        password = validators.String(max_length=120)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.data["password"] = hash_password(self.data["password"])

        async def process(self, *args, **kwargs):
            user = await is_valid_user(self.data["username"], self.data["password"])
            if user is None:
                message = {"message": "Invalid credential or user does not exits"}
                return message, status_codes.UNAUTHORIZED
            session_id = create_session(self.data["username"])
            return {"message": "Login successful"}, status_codes.OK, session_id
