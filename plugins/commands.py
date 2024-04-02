import time
from pyrogram import Client, filters
from pyrogram.filters import command, regex

from bot.helper.telegram_helper.message_utils import sendMessage, editMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.button_build import ButtonMaker
from bot.helper.themes import BotTheme
from bot.plugins.terabox import format_message

@Client.on_message(command("start"))
async def start(client, message):
    buttons = ButtonMaker()
    buttons.ubutton(BotTheme('ST_BN1_NAME'), BotTheme('ST_BN1_URL'))
    buttons.ubutton(BotTheme('ST_BN2_NAME'), BotTheme('ST_BN2_URL'))
    reply_markup = buttons.build_menu(2)
    await sendMessage(message, BotTheme('ST_MSG'))

@Client.on_message(regex(pattern=r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"))
async def link_handler(client, message):
    start_time = time.time()
    urls = extract_links(message.text or message.caption)
    if not urls: return sendMessage(message, "⚠️ No valid URLs found!")
    terabox_urls = [url for url in urls if await check_url_patterns_async(url)]
    if not terabox_urls: return sendMessage(message, "⚠️ Not a valid Terabox URL!")
    try:
        reply = await sendMessage(message, BotTheme('BYPASSING_URL'))
        link_message_help = "\n\n".join([await format_message(link) for link in terabox_urls])
        time_taken_help = get_readable_time(time.time() - start_time)
        await editMessage(reply, BotTheme('LINK_BYPASSED', link_message=link_message_help, time_taken=time_taken_help))
    except Exception as e:
        LOGGER.error(e)