import os
import time, datetime, pytz
import logging, asyncio
import logging.config

from aiohttp import web
from pyrogram import Client, enums

from plugins import web_server
from config import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL, LOG_MSG, WEBHOOK
from utils import temp, __repo__, __license__, __copyright__, __version__


logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("cinemagoer").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="TeraboxedBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=1000,
            plugins={"root": "plugins"},
            sleep_threshold=10
        )

    async def start(self):
        logging.info("Creating client from BOT_TOKEN")
        await super().start()
        me = await self.get_me()
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.id = me.id
        self.name = me.first_name
        self.mention = me.mention
        self.username = me.username
        self.log_channel = LOG_CHANNEL
        self.uptime = time.time()
        curr = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
        date = curr.strftime('%d %B, %Y')
        tame = curr.strftime('%I:%M:%S %p')
        logging.info(LOG_MSG.format(me.first_name, date, tame, __repo__, __version__, __license__, __copyright__))
        try: await self.send_message(LOG_CHANNEL, LOG_MSG.format(me.first_name, date, tame, __repo__, __version__, __license__, __copyright__), disable_web_page_preview=True)   
        except Exception as e: logging.warning(f"Bot Isn't Able To Send Message To LOG_CHANNEL \n{e}")
        if WEBHOOK is True:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", 8080).start()
            logging.info("Web Response Is Running......🕸️")
        logging.info(f"Teraboxed Bot [@{me.username}] Started!")

    async def stop(self, *args):
        await super().stop()
        me = await self.get_me()
        logger.info(f"{me.first_name} is_...  ♻️Restarting...")

Bot().run()