import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait
from pyrogram_app.workclient import WorkClient
from pyrogram_app.shifts import Employees
from pyrogram_app.logger import logger


async def main():
    async with Client("Pyrogram App") as app:
        try:
            is_on_work = Employees().is_on_work('Сергеев Семен')
            print(is_on_work)
            if not is_on_work[0]:
                print(is_on_work[1]['date'])
                folder_list = await WorkClient.get_folder_list(app)            
                peer_list = WorkClient.get_peer_list(folder_list)
                await WorkClient.mute_peers(
                       app=app, 
                       peer_list=peer_list,
                       mute_until=is_on_work[1]['date']
                )
            else:
                folder_list = await WorkClient.get_folder_list(app)            
                peer_list = WorkClient.get_peer_list(folder_list)
                await WorkClient.unmute_peers(
                       app=app, 
                       peer_list=peer_list,
                )

        except FloodWait as e:
            logger.error(e)
            await asyncio.sleep(e.value)

asyncio.run(main())
