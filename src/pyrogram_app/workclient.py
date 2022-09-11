from pyrogram.client import Client
from pyrogram.raw.types import (DialogFilterDefault, DialogFilter,
                                InputPeerNotifySettings, InputNotifyPeer,
                                NotificationSoundDefault)
from pyrogram.raw.functions.account import UpdateNotifySettings
from pyrogram.raw.functions.messages import GetDialogFilters
from pyrogram.errors import FloodWait
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
                        print(type(current_peer))
                        result.append(current_peer)
        return result

    async def mute_peers(app: Client, peer_list: list):
        print(f"Peer count: {len(peer_list)}")
        i = 1
        for peer in peer_list:
            peer = InputNotifyPeer(peer=peer)
            await app.invoke(
                UpdateNotifySettings(
                    peer=peer,
                    settings=InputPeerNotifySettings(
                        show_previews=False,
                        mute_until=int(round(datetime.datetime(2022, 9, 12).timestamp())),
                        sound=NotificationSoundDefault()
                    )
                )
            )
            print(f"{peer} was muted! [{i}/{len(peer_list)}]")
            i += 1
        pass

    async def unmute_peers(app: Client, peer_list: list):
        print(f"Peer count: {len(peer_list)}")
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
            print(f"{peer} was unmuted! [{i}/{len(peer_list)}]")
            i += 1
        pass
