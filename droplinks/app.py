import asyncio
import os

import uvicorn
from starlette.applications import Starlette
from starlette.responses import FileResponse, JSONResponse
from starlette.staticfiles import StaticFiles

from core.settings import STATIC_ROOT

from .services import Auth, CreateContact

app = Starlette()
app.mount("/static", StaticFiles(directory=os.path.join(STATIC_ROOT, "static")))


@app.route("/", methods=["GET"])
def home(request):
    return FileResponse(os.path.join(STATIC_ROOT, "index.html"))


@app.route("/signup", methods=["POST", "GET"])
async def signup(request):
    if request.method == "GET":
        return home(request)
    if request.method == "POST":
        data = await request.json()
        response, status = await Auth.signup(data)
        return JSONResponse(response, status)


@app.route("/login", methods=["POST", "GET"])
async def signin(request):
    if request.method == "GET":
        return home(request)
    if request.method == "POST":
        data = await request.json()
        response, status = await Auth.login(data)
        return JSONResponse(response, status)


@app.route("/contact", methods=["POST", "GET"])
async def contact(request):
    if request.method == "GET":
        return home(request)
    data = await request.json()
    response, status_code = await CreateContact.execute(data)
    return JSONResponse(response, status_code=status_code)


@app.route(".*", methods=["GET"])
async def catchall(request):
    return home(request)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    uvicorn.run(app, host="0.0.0.0", port=8000, loop=loop)
