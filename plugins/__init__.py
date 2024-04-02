import time, asyncio
from aiohttp import web
from pyrogram import Client, filters
from pyrogram.filters import command, regex

from plugins.helper.telegram_helper.message_utils import sendMessage
from plugins.helper.themes import BotTheme
from plugins.terabox import format_message, extract_links


routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response(text="t.me/ebiza™")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

@Client.on_message(regex(pattern=r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"))
async def link_handler(client, message):
    start_time = time.time()
    print("heyy")
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