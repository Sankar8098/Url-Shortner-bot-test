import asyncio
import datetime
import logging
import logging.config
import sys

from pyrogram import Client
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate

from config import *
from database import db
from database.users import filter_users
from helpers import temp
from pyshorteners import *

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)

    class Bot(Client):

    def __init__(self):
        super().__init__(
            "shortener",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins")
        )

    async def start(self):
        # your existing start method code

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")

if __name__ == "__main__":
    bot = Bot()
    bot.run()


