from aiohttp import web
from subprocess import Popen

from config import PORT
from bot import Bot
from plugins.helper.ext_utils.bot_utils import set_commands


routes = web.RouteTableDef()
@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response(text="t.me/ebiza™")

Popen(f"gunicorn web.wserver:app --bind 0.0.0.0:{PORT} --worker-class gevent", shell=True)
alive = Popen(["python3", "alive.py"])
set_commands(Bot)
