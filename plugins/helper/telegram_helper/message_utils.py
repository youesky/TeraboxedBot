#!/usr/bin/env python3
import asyncio
from random import choice as rchoice

from pyrogram.enums import ParseMode
from pyrogram.types import InputMediaPhoto
from pyrogram.errors import ReplyMarkupInvalid, FloodWait, MessageNotModified, MessageEmpty

from main import logger


IMAGES = "https://te.legra.ph/file/fd38c3b6475dee45b3d0d.jpg https://te.legra.ph/file/dbc75abadc755300b1db7.jpg https://te.legra.ph/file/6452a9a983edc6b075947.jpg https://te.legra.ph/file/876dfbb376024367d75c5.jpg https://te.legra.ph/file/4ba2cf84d24b45e4c5fce.jpg https://te.legra.ph/file/7685ff7c159023a91cc64.jpg https://te.legra.ph/file/fb0a1dd462207aee52dee.jpg https://te.legra.ph/file/4f1ae4b2c4fdaef2c46d4.jpg https://te.legra.ph/file/8c60e09d8221bbbe9cb34.jpg https://te.legra.ph/file/d1d2dac213ee53e77b80e.jpg"

async def sendMessage(message, text, buttons=None, photo=None, **kwargs):
    try:
        if photo:
            try:
                if photo == 'IMAGES':
                    photo = rchoice(IMAGES)
                return await message.reply_photo(photo=photo, reply_to_message_id=message.id,
                                                 caption=text, reply_markup=buttons, disable_notification=True, **kwargs)
            except IndexError:
                pass
            except (PhotoInvalidDimensions, WebpageCurlFailed, MediaEmpty):
                des_dir = await download_image_url(photo)
                await sendMessage(message, text, buttons, des_dir)
                await aioremove(des_dir)
                return
            except Exception as e:
                logger.error(format_exc())
        return await message.reply(text=text, quote=True, disable_web_page_preview=True, disable_notification=True,
                                    reply_markup=buttons, reply_to_message_id=rply.id if (rply := message.reply_to_message) and not rply.text and not rply.caption else None,
                                    **kwargs)
    except FloodWait as f:
        logger.warning(str(f))
        await sleep(f.value * 1.2)
        return await sendMessage(message, text, buttons, photo)
    except ReplyMarkupInvalid:
        return await sendMessage(message, text, None, photo)
    except MessageEmpty:
        return await sendMessage(message, text, parse_mode=ParseMode.DISABLED)
    except Exception as e:
        logger.error(format_exc())
        return str(e)


async def editMessage(message, text, buttons=None, photo=None):
    try:
        if message.media:
            if photo:
                photo = rchoice(IMAGES) if photo == 'IMAGES' else photo
                return await message.edit_media(InputMediaPhoto(photo, text), reply_markup=buttons)
            return await message.edit_caption(caption=text, reply_markup=buttons)
        await message.edit(text=text, disable_web_page_preview=True, reply_markup=buttons)
    except FloodWait as f:
        logger.warning(str(f))
        await sleep(f.value * 1.2)
        return await editMessage(message, text, buttons, photo)
    except (MessageNotModified, MessageEmpty):
        pass
    except ReplyMarkupInvalid:
        return await editMessage(message, text, None, photo)
    except Exception as e:
        logger.error(str(e))
        return str(e)


async def editReplyMarkup(message, reply_markup):
    try:
        return await message.edit_reply_markup(reply_markup=reply_markup)
    except MessageNotModified:
        pass
    except Exception as e:
        logger.error(str(e))
        return str(e)
