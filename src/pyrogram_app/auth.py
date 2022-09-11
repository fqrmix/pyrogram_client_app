from pyrogram import Client
from config import API_HASH, API_ID

auth_app = Client("Pyrogram App", api_hash=API_HASH, api_id=API_ID)

auth_app.run()

