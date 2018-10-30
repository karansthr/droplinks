import asyncio
import hashlib
import sys

import uvloop
import motor.motor_asyncio

sys.path.append("..")
from core.services import Service
from core import validators

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
client = motor.motor_asyncio.AsyncIOMotorClient()
database = client.droplinks


class CreateContact(Service):
    name = validators.String(max_length=120)
    email = validators.Email()
    subject = validators.String(max_length=120)
    message = validators.String(max_length=1200)

    async def process(self):
        collection = database.contacts
        await collection.insert_one(self.data)
        return {'message': 'Request submitted successfully'}, 200


class Auth:
    user_collections  = client.user

    class Login(Service):
        username = validators.String(max_length=120)
        password = validators.String(max_length=120)
        
    class Register(Service):
        username = validators.String(max_length=120)
        password = validators.String(max_length=120)
        email = validators.Email()
    
    @staticmethod
    def hash_password(password):
        return hashlib.sha224(bytes(password)).hexdigest()
    
    @classmethod
    async def login(cls, username, password):
        cls.Login({'username': username, 'password':password})
        user = await cls.is_valid_user(username, password)
        if user is None:
            message = {'message': 'Invalid credential or user does not exits'}
            status_code = 401
            return message, status_code

    @classmethod
    async def signup(cls, **kwargs):
        userdata = {
            'username': kwargs.get('username'),
            'password': cls.hash_password(kwargs.get('password')),
            'email': kwargs.get('email')
        }
        if await cls.user_exists(userdata['username'], userdata['email']):
            message = {'message': 'Password does not match'}
            status_code = 403
            return message, status_code
        repassword = cls.hash_password(kwargs.get('repassword'))
        if userdata['password'] != repassword:
            message = {'message': 'Password does not match'}
            status_code = 403
            return message, status_code
        cls.Register(userdata)
        try:
            await cls.create_user(**userdata)
            message = {'message': 'User created successfully'}
            status_code = 200
        except Exception as e:
            message = {'message': 'Error creating user', 'error': str(e)}
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
        if username and await cls.user_collections.find({'username': username}):
            result = True
        if email and await cls.user_collections.find({'email': email}):
            result = True
        return result

    @classmethod
    async def is_valid_user(cls, username, password):
        password = cls.hash_password(password)
        if await cls.user_collections.get({'username': username, 'password': password}):
            return True
        return False
