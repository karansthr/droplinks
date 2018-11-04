import asyncio
import os

import uvicorn
from starlette.applications import Starlette
from starlette.responses import FileResponse, JSONResponse, RedirectResponse
from starlette.staticfiles import StaticFiles

from core.settings import STATIC_ROOT
from utils import status_codes

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
        response, status = await Auth.SignUpUser.execute(data)
        if status == status_codes.OK:
            return RedirectResponse("/login")
        return JSONResponse(response, status)


@app.route("/login", methods=["POST", "GET"])
async def signin(request):
    if request.method == "GET":
        return home(request)
    if request.method == "POST":
        data = await request.json()
        message, status, session_id = await Auth.LoginUser.execute(data)
        response = JSONResponse(message, status)
        response.set_cookie('session_id', session_id)
        return response


@app.route("/contact", methods=["POST", "GET"])
async def contact(request):
    if request.method == "GET":
        return home(request)
    data = await request.json()
    message, status_code = await CreateContact.execute(data)
    return JSONResponse(message, status_code=status_code)


@app.route("/logout")
async def logout(request):
    pass


@app.route(".*", methods=["GET"])
async def catchall(request):
    return home(request)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    uvicorn.run(app, host="0.0.0.0", port=8000, loop=loop)
