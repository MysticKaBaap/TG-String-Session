import os

from heroku3 import from_key
from pyrogram import Client
from pyromod import listen

API_ID = 2239456
API_HASH = "43839c63dcf38c8cd512f102ede7f618"
BOT_TOKEN = "1790125508:AAHvrGtAVX-Dk6xNzpBG95RlqhBVOW9Iu_s"
APP_NAME = os.environ.get("APP_NAME", None)
API_KEY = os.environ.get("API_KEY", None)
HU_APP = from_key(API_KEY).apps()[APP_NAME]

bot = Client(":memory:",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN)
