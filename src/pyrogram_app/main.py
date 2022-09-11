import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait
from workclient import WorkClient

async def main():
    async with Client("Pyrogram App") as app:
        try:
            folder_list = await WorkClient.get_folder_list(app)            
            peer_list = WorkClient.get_peer_list(folder_list)
            await WorkClient.mute_peers(app, peer_list)
        except FloodWait as e:
           await asyncio.sleep(e.value)

asyncio.run(main())
