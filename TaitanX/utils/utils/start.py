from typing import Union
import re
import os
from os import getenv

from dotenv import load_dotenv

from pyrogram import filters


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
load_dotenv()
YOUR_GROUP = getenv("YOUR_GROUP", "https://t.me/timepassgroup01")
YOUR_CHANNEL = getenv("YOUR_CHANNEL", "https://t.me/dangerous_fighter_clan_0")
OWNER_USERNAME = getenv("OWNER_USERNAME", "https://t.me/taitangamerz")
OWNER_USERNAME = getenv("OWNERR_USERNAME", "https://t.me/taitangamer")

def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋 ғᴇᴀᴛᴜʀᴇ 🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️ sᴇᴛᴛɪɴɢ ⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ 𝐀ᴅᴅ 𝐌ᴇ 𝐓ᴏ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ 𝐌ᴀɴᴛᴀɪɴᴇʀ ✨", url=f"https://t.me/{OWNER_USERNAME}",
            ),
            InlineKeyboardButton(
                text="🔎 𝐇ᴇʟᴘ 🔎", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💫 𝐒ᴜᴘᴘᴏʀᴛ 💫", url=f"https://t.me/{YOUR_GROUP}",
            ),
            InlineKeyboardButton(
                text="🍁 𝐆ʀᴏᴜᴘ 🍁", url=f"https://t.me/{YOUR_CHANNEL}",
            )
        ],
        [
            InlineKeyboardButton(
                text="❄️ 𝐎ᴡɴᴇʀ ❄️",
                url=f"https://t.me/{OWNERR_USERNAME}",
            )
        ],
     ]
    return buttons
