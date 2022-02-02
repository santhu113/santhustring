from asyncio.exceptions import TimeoutError
from Data import Data
from pyrogram import Client, filters
from telethon import TelegramClient
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

ERROR_MESSAGE = "Oops! An exception occurred! \n\n**Error** : {} " \
            "\n\nTolong any report bugs join @santhuvc jika eror " \
            "sensitive information and you if want to report this as " \
            "this error message is not being logged by us!"


@Client.on_message(filters.private & ~filters.forwarded & filters.command('generate'))
async def main(_, msg):
    await msg.reply(
        "𝐄𝐊𝐀𝐃𝐀 𝐌𝐄𝐊𝐔 𝐄𝐌𝐈 𝐊𝐀𝐕𝐀𝐋𝐎 𝐒𝐄𝐋𝐄𝐂𝐓 𝐂𝐇𝐄𝐒𝐔𝐊𝐎𝐍𝐃𝐈.",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("𝐏𝐘𝐑𝐎𝐆𝐑𝐀𝐌", callback_data="pyrogram"),
            InlineKeyboardButton("𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍", callback_data="telethon")
        ]])
    )


async def generate_session(bot, msg, telethon=False):
    await msg.reply(" {} Session Generation...".format("𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍" if telethon else "𝐏𝐘𝐑𝐎𝐆𝐑𝐀𝐌"))
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, '𝐚𝐫𝐞𝐲 𝐧𝐢𝐛𝐛𝐚 `API_ID 𝐊𝐎𝐓𝐔`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        await api_id_msg.reply('𝐚𝐫𝐞𝐲 𝐧𝐢𝐛𝐛𝐚 𝐀𝐏𝐈_𝐈𝐃 𝐊𝐎𝐓𝐔 (which must be an integer). Please start generating session again.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = await bot.ask(user_id, '𝐀𝐫𝐞𝐲 𝐧𝐢𝐛𝐛𝐚 `API_HASH 𝐤𝐨𝐭𝐮 𝐫𝐚`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    api_hash = api_hash_msg.text
    phone_number_msg = await bot.ask(user_id, '𝐧𝐢𝐛𝐛𝐚 `PHONE_NUMBER` 𝐤𝐨𝐭𝐮. \nExample : `+9163xxxxxxx`', filters=filters.text)
    if await cancelled(api_id_msg):
        return
    phone_number = phone_number_msg.text
    await msg.reply("Sending OTP...😝")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    else:
        client = Client(":memory:", api_id, api_hash)
    await client.connect()
    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply('`API_ID` and `API_HASH` combination is invalid😏. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply('`PHONE_NUMBER` is invalid😒. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = await bot.ask(user_id, "arey nibba telegram check chesuko otp send chesa. Adhe ekkada send cheyi, OTP ni e format lo send cheyi nibba ga. \nIf OTP is `12345`, **send chey** `12345`.", filters=filters.text, timeout=900)
        if await cancelled(api_id_msg):
            return
    except TimeoutError:
        await msg.reply('Time limit reached of 10 minutes. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    phone_code = phone_code_msg.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, phone_code, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, phone_code)
    except (PhoneCodeInvalid, PhoneCodeInvalidError):
        await msg.reply('OTP is invalid🤨. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError):
        await msg.reply('OTP is expired😔. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        try:
            two_step_msg = await bot.ask(user_id, 'Your account has enabled two-step verification. Please provide the password.', filters=filters.text, timeout=300)
        except TimeoutError:
            await msg.reply('Time limit reached of 5 minutes. Please start generating session again.', reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        try:
            password = two_step_msg.text
            if telethon:
                await client.sign_in(password=password)
            else:
                await client.check_password(password=password)
            if await cancelled(api_id_msg):
                return
        except (PasswordHashInvalid, PasswordHashInvalidError):
            await two_step_msg.reply('Invalid Password Provided. Please start generating session again.', quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = "**{} STRING SESSION** \n\n`{}` \n\nSupport Groups @santhuvc".format("TELETHON" if telethon else "PYROGRAM", string_session)
    await client.send_message("me", text)
    await client.disconnect()
    await phone_code_msg.reply("𝚊𝚛𝚎𝚢 𝚗𝚒𝚋𝚋𝚊 𝚐𝚊 𝚜𝚊𝚟𝚎𝚍 𝚖𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝚕𝚘 𝚌𝚑𝚞𝚍𝚞{} string session. \n\n𝙲𝚑𝚞𝚍𝚞 po😅! \n\nBy @santhuvc".format("telethon" if telethon else "pyrogram"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("Membatalkan Process!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("Memulai Ulang Bot!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("Membatalkan generation process!", quote=True)
        return True
    else:
        return False


# @Client.on_message(filters.private & ~filters.forwarded & filters.command(['cancel', 'restart']))
# async def formalities(_, msg):
#     if "/cancel" in msg.text:
#         await msg.reply("Membatalkan Semua Processes!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
#         return True
#     elif "/restart" in msg.text:
#         await msg.reply("Memulai Ulang Bot!", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
#         return True
#     else:
#         return False
