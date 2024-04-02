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
DEFUALT_IMAGES = "https://te.legra.ph/file/50948ffe9bae7ae144fdc.jpg https://te.legra.ph/file/6fff8b3db750d6ca79eaf.jpg https://te.legra.ph/file/c9a03c5fa076aa6f5d6ed.jpg https://te.legra.ph/file/cbb22ce0a7e7d22d5fabe.jpg https://te.legra.ph/file/e1956382d55e05ed7840c.jpg https://te.legra.ph/file/5f55c2f2f12f71deb3476.jpg https://te.legra.ph/file/acc3af2d3ada7a9d7c0ac.jpg https://te.legra.ph/file/3d941e162755166cc6f16.jpg https://te.legra.ph/file/2782b15b446801060949c.jpg"

for admin in getenv("ADMINS", "1034599258").split():
    ADMINS.append(int(admin))
for image in getenv("IMAGES", DEFUALT_IMAGES).split():
    IMAGES.append(str(image))
