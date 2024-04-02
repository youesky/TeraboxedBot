from os import getenv


# Required Variables
BOT_TOKEN = getenv("BOT_TOKEN", "7164272870:AAHbHvoWGurO1IS1L34Nv-tM8nurgNuwcsA")
ADMINS = []

# Optional Variables
API_ID = int(getenv("API_ID", "28542813"))
API_HASH = getenv("API_HASH", "02ce7c339f7776844ff4ab03da338ccd")
WEBHOOK = bool(getenv("WEBHOOK", False)) # for web support on/off
IMAGES = []

# ---------- DON'T TOUCH THIS ---------- #
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴘᴏ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"
DEFUALT_IMAGES = "https://te.legra.ph/file/9f100ca154c6e743b586f.jpg https://te.legra.ph/file/7ed7c6257b695386335e4.jpg https://te.legra.ph/file/91a0a949ce1e165e8e3a4.jpg"

for admin in getenv("ADMINS", "1034599258").split():
    ADMINS.append(int(admin))
for image in getenv("IMAGES", DEFUALT_IMAGES).split():
    IMAGES.append(str(image))
