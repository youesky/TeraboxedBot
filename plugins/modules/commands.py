import time, asyncio
from pyrogram import Client, filters
from pyrogram.filters import command, regex

from plugins.helper.ext_utils.bot_utils import get_readable_time, extract_links
from plugins.helper.telegram_helper.message_utils import sendMessage, editMessage
from plugins.helper.telegram_helper.button_build import ButtonMaker
from plugins.helper.themes import BotTheme
from plugins.terabox import format_message, check_url_patterns_async

@Client.on_message(command("start"))
async def start(client, message):
    buttons = ButtonMaker()
    buttons.ubutton(BotTheme('ST_BN1_NAME'), BotTheme('ST_BN1_URL'))
    buttons.ubutton(BotTheme('ST_BN2_NAME'), BotTheme('ST_BN2_URL'))
    reply_markup = buttons.build_menu(2)
    await sendMessage(message, BotTheme('ST_MSG'), reply_markup)

@Client.on_message(regex(pattern=r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"))
async def link_handler(client, message):
    start_time = time.time()
    print("1")
    urls = extract_links(message.text or message.caption)
    print("b")
    if not urls: return sendMessage(message, "⚠️ No valid URLs found!")
    print("c")
    terabox_urls = [url for url in urls if await check_url_patterns_async(url)]
    print("d")
    if not terabox_urls: return sendMessage(message, "⚠️ Not a valid Terabox URL!")
    print("e")
    try:
        reply = await sendMessage(message, BotTheme('BYPASSING_URL'))
        link_message_help = "\n\n".join([await format_message(link) for link in terabox_urls])
        time_taken_help = get_readable_time(time.time() - start_time)
        print("f")
        await editMessage(reply, BotTheme('LINK_BYPASSED', link_message=link_message_help, time_taken=time_taken_help))
        print("g")
    except Exception as e:
        LOGGER.error(e)