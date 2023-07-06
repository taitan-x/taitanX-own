import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from TaitanX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < TaitanX <= 10:
        bar = "⬤─────────"
    elif 10 < TaitanX < 20:
        bar = "━⬤────────"
    elif 20 <= TaitanX < 30:
        bar = "━━⬤───────"
    elif 30 <= TaitanX < 40:
        bar = "━━━⬤──────"
    elif 40 <= TaitanX < 50:
        bar = "━━━━⬤─────"
    elif 50 <= TaitanX < 60:
        bar = "━━━━━⬤────"
    elif 60 <= TaitanX < 70:
        bar = "━━━━━━⬤───"
    elif 70 <= TaitanX < 80:
        bar = "━━━━━━━⬤──"
    elif 80 <= TaitanX < 95:
        bar = "━━━━━━━━⬤─"
    else:
        bar = "━━━━━━━━━⬤"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 ᴜᴘᴅᴀᴛᴇ 💥", url=f"https://t.me/taitanoffice"
            ),
            InlineKeyboardButton(
                text="🥀 sᴜᴩᴩᴏʀᴛ 💥", url=f"https://t.me/DXDREAMBIG"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
            )
        ],
    ]
    return buttons



def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < TaitanX <= 10:
        bar = "𝐓ᴀɪᴛᴀɴ 𝐈s 𝐒ᴛᴀʀᴛᴇᴅ"
    elif 10 < TaitanX < 20:
        bar = "𝐓ᴀɪᴛᴀɴ Gᴀᴍᴇʀ Bᴏᴛ"
    elif 20 <= TaitanX < 30:
        bar = "Bᴏᴛ Oᴡɴᴇʀ Tᴀɪᴛᴀɴ"
    elif 30 <= TaitanX < 40:
        bar = "Tᴀɪᴛᴀɴ ʙɪɢ Dᴀᴛᴀʙᴀsᴇ"
    elif 40 <= TaitanX < 50:
        bar = "Tᴀɪᴛᴀɴ Is sᴛᴀʀᴛᴇᴅ"
    elif 50 <= TaitanX < 60:
        bar = "Mᴀᴅᴇ Bʏ Tᴀɪᴛᴀɴ"
    elif 60 <= TaitanX < 70:
        bar = "Tᴀɪᴛᴀɴ Gᴀᴍᴇʀ Bᴏᴛ"
    elif 70 <= TaitanX < 80:
        bar = "Tᴀɪᴛᴀɴ Sᴇʀᴠᴇʀ Bᴏᴛ"
    elif 80 <= TaitanX < 95:
        bar = "Tᴀɪᴛᴀɴ ᴅᴀᴛᴀʙᴀsᴇ"
    else:
        bar = "Bʏᴇ Bʏᴇ Fɪɴɪsʜᴇᴅ"


    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="✢", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            )
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 ᴜᴘᴅᴀᴛᴇ 💥", url=f"https://t.me/taitanoffice"
            ),
            InlineKeyboardButton(
                text="🥀 sᴜᴩᴩᴏʀᴛ 💥", url=f"https://t.me/world_music_masti"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
            )
        ],
    ]
    return buttons

def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☩", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="✢", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
           )
        ],
        [
            InlineKeyboardButton(
                text="🥀 ᴜᴘᴅᴀᴛᴇ 💥", url=f"https://t.me/taitanoffice"
            ),
            InlineKeyboardButton(
                text="🥀 sᴜᴩᴩᴏʀᴛ 💥", url=f"https://t.me/world_music_masti"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
            )
        ],
    ]
    return buttons