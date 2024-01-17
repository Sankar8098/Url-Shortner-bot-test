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

   async def start(client, message):
    btn = [[
        InlineKeyboardButton('Updates Channel', url=UPDATES_CHANNEL),
        InlineKeyboardButton('Support Group', url=SUPPORT_GROUP)
    ],[
        InlineKeyboardButton('Deploy', url='https://github.com/pandaznetwork/Adlinkflyshortnerbot')
    ]]
    text = """**Just send me link and get short link, You can also send multiple links seperated by a space or enter."""
    await message.reply(f"👋 Hello {message.from_user.mention},\n\nI'm {WEB_NAME} Shortner bot. {text}", reply_markup=InlineKeyboardMarkup(btn))    

