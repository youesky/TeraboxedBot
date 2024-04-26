from logging import getLogger, ERROR,Formatter, FileHandler, StreamHandler, INFO, basicConfig, error as log_error, info as log_info, warning as log_warning
from os import environ, remove
from pyrogram import Client as tgClient, enums
from uvloop import install

install()
basicConfig(format="[%(asctime)s] [%(levelname)s] - %(message)s", #  [%(filename)s:%(lineno)d]
            datefmt="%d-%b-%y %I:%M:%S %p",
            handlers=[FileHandler('log.txt'), StreamHandler()],
            level=INFO)

getLogger("pyrogram").setLevel(ERROR)
LOGGER = getLogger(__name__)

with open('config.json', 'r') as f: DATA = load(f)
def getenv(var): return environ.get(var) or DATA.get(var, None)

BOT_TOKEN = getenv("TOKEN")
API_HASH = getenv("HASH") 
API_ID = getenv("ID")


log_info("Creating client from BOT_TOKEN")
bot = tgClient('bot', API_ID, API_HASH, bot_token=BOT_TOKEN, workers=1000,
               parse_mode=enums.ParseMode.HTML).start()

bot_loop = bot.loop
