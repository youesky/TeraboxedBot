import asyncio

from plugins.helper.ext_utils.bot_utils import get_readable_file_size
from plugins.helper.mirror_utils.download_utils.direct_link_generator import terabox


async def format_message(link_data):
    download_link, title, total_size = terabox(link_data)
    file_name = f"<a href={link_data}>{title}</a>"
    file_size = get_readable_file_size(total_size)
    return f"┎ <b>Title</b>: {file_name}\n┠ <b>Size</b>: <code>{file_size}</code>\n┖ <b>Link</b>: <a href={download_link}>Link</a>"
