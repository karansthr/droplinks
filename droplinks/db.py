import asyncio

import uvloop
import motor.motor_asyncio

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
client = motor.motor_asyncio.AsyncIOMotorClient()
database = client.droplinks
