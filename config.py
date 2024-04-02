from os import getenv

API_ID = int(getenv("API_ID", "28542813"))
API_HASH = getenv("API_HASH", "02ce7c339f7776844ff4ab03da338ccd")
BOT_TOKEN = getenv("BOT_TOKEN", "7164272870:AAHbHvoWGurO1IS1L34Nv-tM8nurgNuwcsA")
OWNER_ID = int(getenv("OWNER_ID", "1034599258")) 

LOG_CHANNEL = getenv("LOG_CHANNEL", "1034599258")
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴘᴏ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"
WEBHOOK = bool(environ.get("WEBHOOK", True)) # for web support on/off