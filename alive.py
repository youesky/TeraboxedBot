from time import sleep
from requests import get as rget

from bot import logger
from config import WEBHOOK_URL, PORT


try:
    if len(WEBHOOK_URL) == 0: raise TypeError
    WEBHOOK_URL = WEBHOOK_URL.rstrip("/")
except TypeError: WEBHOOK_URL = None
if PORT is not None and WEBHOOK_URL is not None:
    while True:
        try:
            rget(WEBHOOK_URL).status_code
            sleep(600)
        except Exception as e:
            logger.error(f"alive.py: {e}")
            sleep(2)
            continue
