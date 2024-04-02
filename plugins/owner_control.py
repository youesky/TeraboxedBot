import os, sys, asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID


@Client.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def restart_bot(bot, msg):
    sts = await msg.reply("Restarting........")
    await asyncio.sleep(2)
    await sts.delete()
    await msg.reply("Done........")
    os.execl(sys.executable, sys.executable, *sys.argv)
