#!/usr/bin/env python3
import asyncio
from time import time
from datetime import datetime

from pyrogram import Client
from pyrogram.types import BotCommand

from bot import logger
from config import SET_COMMANDS


SIZE_UNITS   = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']

def get_readable_file_size(size_in_bytes):
    if size_in_bytes is None:
        return '0B'
    index = 0
    while size_in_bytes >= 1024 and index < len(SIZE_UNITS) - 1:
        size_in_bytes /= 1024
        index += 1
    return f'{size_in_bytes:.2f}{SIZE_UNITS[index]}' if index > 0 else f'{size_in_bytes}B'

def get_readable_time(seconds):
    periods = [('d', 86400), ('h', 3600), ('m', 60), ('s', 1)]
    result = ''
    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(seconds, period_seconds)
            result += f'{int(period_value)}{period_name}'
    return result

async def set_commands(client):
    if not SET_COMMANDS: return
    try:
        bot_cmds = [
            BotCommand("start", "Alive!?"),
            BotCommand("restart", "[Admins Only]")
        ]
        await client.set_bot_commands(bot_cmds)
        logger.info('Bot Commands have been Set & Updated')
    except Exception as e:
        logger.error(e)
