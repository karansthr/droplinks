from core.services import Service
from core import validators
from .utils import hash_password
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
        email = validators.Email()

        async def process(self):
            pass

    class Login(Service):
        username = validators.String(max_length=120)
        password = validators.String(max_length=120)

        async def process(self):
            pass

    @classmethod
    async def login(cls, username, password):
        instance = cls.Login({"username": username, "password": password})
        if instance.is_valid():
            user = await cls.is_valid_user(username, password)
            if user is None:
                message = {"message": "Invalid credential or user does not exits"}
                status_code = 401
                return message, status_code
            return {"message": "Login successful"}, 200
        return {"error": instance.errors}, 403

    @classmethod
    async def signup(cls, **kwargs):
        userdata = {
            "username": kwargs.get("username"),
            "password": cls.hash_password(kwargs.get("password")),
            "email": kwargs.get("email"),
        }
        if await cls.user_exists(userdata["username"], userdata["email"]):
            message = {"message": "Password does not match"}
            status_code = 403
            return message, status_code
        repassword = hash_password(kwargs.get("repassword"))
        if userdata["password"] != repassword:
            message = {"message": "Password does not match"}
            status_code = 403
            return message, status_code
        cls.Register(userdata)
        try:
            await cls.create_user(**userdata)
            message = {"message": "User created successfully"}
            status_code = 200
        except Exception as e:
            message = {"message": "Error creating user", "error": str(e)}
            status_code = 403
        return message, status_code

    @classmethod
    async def create_user(cls, **userdata):
        result = await cls.user_collections.insert_one(userdata)
        return result

    @classmethod
    async def user_exists(cls, username=None, email=None):
        if username is email is None:
            return False
        result = False
        if username and await cls.user_collections.find({"username": username}):
            result = True
        if email and await cls.user_collections.find({"email": email}):
            result = True
        return result

    @classmethod
    async def is_valid_user(cls, username, password):
        password = hash_password(password)
        if await cls.user_collections.get({"username": username, "password": password}):
            return True
        return False
