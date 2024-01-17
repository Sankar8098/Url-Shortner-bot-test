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
    await super().start()
    me = await self.get_me()
    self.owner = await self.get_users(int(OWNER_ID))
    self.username = f'@{me.username}'
    temp.BOT_USERNAME = me.username
    temp.FIRST_NAME = me.first_name
    if not await db.get_bot_stats():
        await db.create_stats()
    banned_users = await filter_users({"banned": True})
    async for user in banned_users:
        temp.BANNED_USERS.append(user["user_id"])
    logging.info(LOG_STR)
    await broadcast_admins(self, '** Bot started successfully **\n\nBot By @GreyMatter_Bots')
    logging.info('Bot started\n\nBot By @DKBOTZ')

