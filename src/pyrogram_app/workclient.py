from pyrogram.client import Client
from pyrogram.raw.types import (DialogFilterDefault, DialogFilter,
                                InputPeerNotifySettings, InputNotifyPeer,
                                NotificationSoundDefault)
from pyrogram.raw.functions.account import UpdateNotifySettings
from pyrogram.raw.functions.messages import GetDialogFilters
from pyrogram.errors import FloodWait
from pyrogram_app.logger import logger
import datetime

class WorkClient:
    def get_folder_list(app: Client):
        return app.invoke(
                GetDialogFilters()
            )

    def get_peer_list(folder_list: list):
        result = []
        for current_folder in folder_list:
            if type(current_folder) is DialogFilterDefault:
                pass
            elif type(current_folder) is DialogFilter:
                if current_folder.title == 'Work/Chn' or \
                        current_folder.title == "Work/54fz":
                    for current_peer in current_folder.include_peers:
                        result.append(current_peer)
        return result

    async def mute_peers(app: Client, peer_list: list, mute_until: datetime.datetime):
        logger.info(f"Peer count: {len(peer_list)}")
        i = 1
        for peer in peer_list:
            peer = InputNotifyPeer(peer=peer)
            mute_until_timestamp = round(mute_until.timestamp())
            await app.invoke(
                UpdateNotifySettings(
                    peer=peer,
                    settings=InputPeerNotifySettings(
                        show_previews=False,
                        mute_until=int(mute_until_timestamp),
                        sound=NotificationSoundDefault()
                    )
                )
            )
            logger.info(f"{peer} was muted! [{i}/{len(peer_list)}]")
            i += 1
        pass

    async def unmute_peers(app: Client, peer_list: list):
        logger.info(f"Peer count: {len(peer_list)}")
        i = 1
        for peer in peer_list:
            peer = InputNotifyPeer(peer=peer)
            await app.invoke(
                UpdateNotifySettings(
                    peer=peer,
                    settings=InputPeerNotifySettings(
                        show_previews=True,
                        mute_until=None,
                        sound=NotificationSoundDefault()
                    )
                )
            )
            logger.info(f"{peer} was unmuted! [{i}/{len(peer_list)}]")
            i += 1
        pass
