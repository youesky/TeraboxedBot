import time, asyncio
from pyrogram import Client, filters
from pyrogram.filters import command, regex

from plugins.helper.telegram_helper.message_utils import sendMessage, editMessage
from plugins.helper.telegram_helper.button_build import ButtonMaker
from plugins.helper.themes import BotTheme
from plugins.terabox import format_message, extract_links

@Client.on_message(command("start"))
async def start(client, message):
    buttons = ButtonMaker()
    buttons.ubutton(BotTheme('ST_BN1_NAME'), BotTheme('ST_BN1_URL'))
    buttons.ubutton(BotTheme('ST_BN2_NAME'), BotTheme('ST_BN2_URL'))
    reply_markup = buttons.build_menu(2)
    await sendMessage(message, BotTheme('ST_MSG'), reply_markup)
