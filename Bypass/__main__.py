from asyncio import create_subprocess_exec
from sys import executable
from os import path as ospath, execl
from signal import signal, SIGINT

from re import findall
from pyrogram import Client, idle
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.filters import command, private, regex, user

from Bypass import bot, LOGGER, OWNER_ID
from .helper import text

async def start(client, message):
    await bot.send_message(message.chat.id, f"__👋 Hi **{message.from_user.mention}**, i am Terabox Link Bypasser Bot, just send me any supported links and i will you get you results.\nCheckout /help to Read More__",
    reply_markup=InlineKeyboardMarkup([
        [ InlineKeyboardButton("🌐 Source Code", url="https://github.com/youesky/TeraboxedBot")],
        [ InlineKeyboardButton("Updates", url="https://t.me/Teraboxed") ]]), 
        reply_to_message_id=message.id)

async def help(client, message):
    msg = text.HELP_TEXT
    await bot.send_message(message.chat.id, text=msg, reply_to_message_id=message.id, disable_web_page_preview=True)

async def restart_command(client, message):
    restart_message = await message.reply('<i>Restarting...</i>')
    await (await create_subprocess_exec('python3', 'update.py')).wait()
    with open(".restartmsg", "w") as f:
        f.write(f"{restart_message.chat.id}\n{restart_message.id}\n")
    execl(executable, executable, "-m", "Bypass")

async def restart():
    if ospath.isfile(".restartmsg"):
        with open(".restartmsg") as f:
            chat_id, msg_id = map(int, f)
        try:
            await bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text="<i>Restarted !</i>")
        except Exception as e:
            LOGGER.error(e)

bot.add_handler(MessageHandler(
    help, filters=command(BotCommands.HelpCommand)))
bot.add_handler(MessageHandler(
    start, filters=command(BotCommands.StartCommand)))
bot.add_handler(MessageHandler(
    restart_command, filters=command(BotCommands.RestartCommand) & user(OWNER_ID)))

bot.loop.run_until_complete(restart())
bot.loop.run_forever()
