import time, asyncio
from pyrogram import Client, filters
from pyrogram.filters import command, regex

from bot import logger

from plugins.helper.ext_utils.bot_utils import get_readable_time
from plugins.helper.ext_utils.bulk_links import extract_links, check_url_patterns_async
from plugins.helper.ext_utils.task_manager import format_message
from plugins.helper.telegram_helper.message_utils import sendMessage, editMessage
from plugins.helper.telegram_helper.button_build import ButtonMaker
from plugins.helper.themes import BotTheme


@Client.on_message(command("start"))
async def start(client, message):
    buttons = ButtonMaker()
    buttons.ubutton(BotTheme('ST_BN1_NAME'), BotTheme('ST_BN1_URL'))
    buttons.ubutton(BotTheme('ST_BN2_NAME'), BotTheme('ST_BN2_URL'))
    reply_markup = buttons.build_menu(2)
    await sendMessage(message, BotTheme('ST_MSG'), reply_markup, photo='IMAGES')

@Client.on_message(regex(pattern=r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"))
async def link_handler(client, message):
    start_time = time.time()
    urls = extract_links(message.text or message.caption)
    terabox_urls = [url for url in urls if await check_url_patterns_async(url)]
    if not terabox_urls: return await sendMessage(message, BotTheme('NON_VALID_URL'))
    reply = await sendMessage(message, BotTheme('BYPASSING_URL'), photo='IMAGES')
    link_message_help = "\n\n".join([await format_message(link) for link in terabox_urls])
    time_taken_help = get_readable_time(time.time() - start_time)
    try: await editMessage(reply, BotTheme('LINK_BYPASSED', link_message=link_message_help, time_taken=time_taken_help), photo='IMAGES')
    except Exception as e: logger.error(e)
