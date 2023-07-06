from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✦𝐏ᴇʀsᴏɴᴀL✦",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="✦𝐆ʟᴏʙᴀL✦", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ 𝐂ʟᴏsE ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✦𝐓ᴏP 10 𝐋ɪsT✦", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="✦𝐎ᴡ𝐍✦", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="✦𝐆ʟᴏʙᴀL✦", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="✦𝐆ʀᴏᴜP✦", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="☆ 𝐁ᴀᴄK ☆", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="☆ 𝐂ʟᴏsE ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✦𝐀ᴜᴅɪO✦", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="✦𝐕ɪᴅᴇO✦", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="☆ 𝐁ᴀᴄK ☆", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="☆ 𝐂ʟᴏsE ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✦𝐓ᴏ𝐏 10 𝐋ɪs𝐓✦", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="✦𝐏ᴇʀsᴏɴᴀ𝐋✦", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="✦𝐆ʟᴏʙᴀL✦", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="✦𝐆ʀᴏᴜP✦", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="☆ 𝐁ᴀᴄK ☆", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="☆ 𝐂ʟᴏsE ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ 𝐁ᴀᴄK ☆",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="☆ 𝐂ʟᴏsE ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✦𝐃ᴇʟᴇᴛE✦",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="☆ 𝐁ᴀᴄK ☆",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="☆ 𝐂ʟᴏsE ☆",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="☆ 𝐂ʟᴏsE ☆",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
