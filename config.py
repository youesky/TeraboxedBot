from os import getenv


# Required Variables
BOT_TOKEN = getenv("BOT_TOKEN", "7164272870:AAHbHvoWGurO1IS1L34Nv-tM8nurgNuwcsA")
ADMINS = []

# Optional Variables
API_ID = int(getenv("API_ID", "28542813"))
API_HASH = getenv("API_HASH", "02ce7c339f7776844ff4ab03da338ccd")
SET_COMMANDS = bool(getenv("SET_COMMANDS", True)) # Set bot command automatically. Bool
WEBHOOK = bool(getenv("WEBHOOK", False))
IMAGES = []

# ---------- DON'T TOUCH THIS ---------- #
LOG_MSG = "{} Iꜱ Rᴇsᴛᴀʀᴛᴇᴅ....✨\n\n🗓️ Dᴀᴛᴇ : {}\n⏰ Tɪᴍᴇ : {}\n\n🖥️ Rᴇᴘᴏ: {}\n🉐 Vᴇʀsɪᴏɴ: {}\n🧾 Lɪᴄᴇɴꜱᴇ: {}\n©️ Cᴏᴩʏʀɪɢʜᴛ: {}"
DEFUALT_IMAGES = "https://te.legra.ph/file/fd38c3b6475dee45b3d0d.jpg https://te.legra.ph/file/dbc75abadc755300b1db7.jpg https://te.legra.ph/file/6452a9a983edc6b075947.jpg https://te.legra.ph/file/876dfbb376024367d75c5.jpg https://te.legra.ph/file/4ba2cf84d24b45e4c5fce.jpg https://te.legra.ph/file/7685ff7c159023a91cc64.jpg https://te.legra.ph/file/fb0a1dd462207aee52dee.jpg https://te.legra.ph/file/4f1ae4b2c4fdaef2c46d4.jpg https://te.legra.ph/file/8c60e09d8221bbbe9cb34.jpg https://te.legra.ph/file/d1d2dac213ee53e77b80e.jpg"

for admin in getenv("ADMINS", "1034599258").split():
    ADMINS.append(int(admin))
for image in getenv("IMAGES", DEFUALT_IMAGES).split():
    IMAGES.append(str(image))
