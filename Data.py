from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = ""
"https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg"

Hello {} Nenu string session genrate bot ni {}
┏━━━━━━━━━━━━━━━━━┓
┣» 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐘𝐎𝐔𝐑 𝐒𝐓𝐑𝐈𝐍𝐆 𝐒𝐄𝐒𝐒𝐈𝐎𝐍 𝐁𝐘 𝐔𝐒𝐈𝐍𝐆. 
┣» 𝐏𝐘𝐑𝐎𝐆𝐑𝐀𝐌.
┣» 𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍.
┣» 𝐄𝐍𝐉𝐎𝐘 𝐘𝐎𝐔𝐑 𝐒𝐓𝐑𝐈𝐍𝐆 𝐒𝐄𝐒𝐒𝐈𝐎𝐍. 
┣» [𝐃𝐄𝐏𝐋𝐎𝐘 𝐁𝐘 ❤️](https://t.me/santhu_music_bot)
┗━━━━━━━━━━━━━━━━━┛
[𝐎𝐖𝐍𝐄𝐑 ❤️](https://t.me/santhu_music_bot)
𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐄 [𝐎𝐖𝐍𝐄𝐑 ❤️](https://t.me/santhu_music_bot)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ​", callback_data="generate")],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ​", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("𝐍𝐞𝐭𝐰𝐨𝐫𝐤​", url="https://t.me/santhuvc")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ​​", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ​", callback_data="about")
        ],
            [InlineKeyboardButton("𝐉𝐎𝐈𝐍 𝐆𝐑𝐎𝐔𝐏​", url="https://t.me/santhuvc")],
        ]
        [InlineKeyboardButton("text="𝐀𝐃𝐃 𝐂𝐇𝐄𝐒𝐔𝐊𝐎𝐍𝐃𝐈", url=f"https://t.me/Santhustringbot?startgroup=true")
    ],    

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - about bot
/help - This Message
/start - start Bot
/pyrogram - "callback_data="pyrogram"),
/cancel -  process
/telethon - "callback_data="telethon"),
"""

    # About Message
    ABOUT = """
**About This Bot** 
https://te.legra.ph/file/e719f19bbeeb7f55e6202.jpg
Generate your string using pyrogram and telethon string session by @Santhustringbot

Group Support : [NETWORK](https://t.me/santhuvc)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @santhu_music_bot
    """
