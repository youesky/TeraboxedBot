#!/usr/bin/env python3
from random import choice as rchoice

from pyrogram.enums import ParseMode
from pyrogram.errors import ReplyMarkupInvalid, FloodWait, MessageNotModified, MessageEmpty

from bot import logger
from config import IMAGES

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
                LOGGER.error(format_exc())
        return await message.reply(text=text, quote=True, disable_web_page_preview=True, disable_notification=True,
                                    reply_markup=buttons, reply_to_message_id=rply.id if (rply := message.reply_to_message) and not rply.text and not rply.caption else None,
                                    **kwargs)
    except FloodWait as f:
        LOGGER.warning(str(f))
        await sleep(f.value * 1.2)
        return await sendMessage(message, text, buttons, photo)
    except ReplyMarkupInvalid:
        return await sendMessage(message, text, None, photo)
    except MessageEmpty:
        return await sendMessage(message, text, parse_mode=ParseMode.DISABLED)
    except Exception as e:
        LOGGER.error(format_exc())
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
        LOGGER.warning(str(f))
        await sleep(f.value * 1.2)
        return await editMessage(message, text, buttons, photo)
    except (MessageNotModified, MessageEmpty):
        pass
    except ReplyMarkupInvalid:
        return await editMessage(message, text, None, photo)
    except Exception as e:
        LOGGER.error(str(e))
        return str(e)


async def editReplyMarkup(message, reply_markup):
    try:
        return await message.edit_reply_markup(reply_markup=reply_markup)
    except MessageNotModified:
        pass
    except Exception as e:
        LOGGER.error(str(e))
        return str(e)
