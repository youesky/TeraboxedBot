import os
import time, datetime, pytz
import logging, asyncio
import logging.config

from aiohttp import web
from pyrogram import Client

from plugins import web_server 
from config import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL, LOG_MSG, WEBHOOK
from utils import temp, __repo__, __license__, __copyright__, __version__


logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("cinemagoer").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

loop = asyncio.get_event_loop_policy().get_event_loop()


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="TeraboxedBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=1000,
            plugins={"root": "plugins"}
        )

    async def start(self):
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
        logger.info(LOG_MSG.format(me.first_name, date, tame, __repo__, __version__, __license__, __copyright__))
        try: await self.send_message(LOG_CHANNEL, text=LOG_MSG.format(me.first_name, date, tame, __repo__, __version__, __license__, __copyright__), disable_web_page_preview=True)   
        except Exception as e: logger.warning(f"Bot Isn't Able To Send Message To LOG_CHANNEL \n{e}")
        if WEBHOOK is True:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", 8080).start()
            logger.info("Web Response Is Running......🕸️")
   
    async def stop(self, *args):
        await super().stop()
        me = await self.get_me()
        logger.info(f"{me.first_name} is_...  ♻️Restarting...")
        
if __name__ == "__main__":
    #loop.run_until_complete(Bot())
    bot = Bot()
    if not bot.is_initialized:
        bot.run()
        logger.info(f"if not")
