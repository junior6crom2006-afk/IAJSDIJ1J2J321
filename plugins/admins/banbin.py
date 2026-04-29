import pyrogram, os
from pyrogram import Client, filters
from pyrogram.types import Message
from functions.functions import *
from os import getenv
from functions.database import Database
from functions.variables import PREFIXES
import json


BANNED_BINS_FILE = "json/banned_bins.json"

@Client.on_message(filters.command(["banbin", "unbanbin"], PREFIXES))
async def ban_unban(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_owner(user_id):
            return
        if len(m.command) != 2:
            return await m.reply("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Invalid Bin ⚠️", quote=True)
        command, bin_number = m.command
        if len(bin_number) < 6 or not bin_number[:6].isdigit():
            return await m.reply("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Invalid Bin ⚠️", quote=True)
        bin_id = bin_number[:6]  
        ban_bin = True if command == "banbin" else False
        with open(BANNED_BINS_FILE, "r+") as file:
            banned_bins = json.load(file)
            if ban_bin:
                if bin_id not in banned_bins:
                    banned_bins.append(bin_id)
                text = "♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Bin <code>{}</code> baneado con éxito ✅"
            else:
                if bin_id not in banned_bins:
                    return await m.reply("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Bin no encontrado ⚠️", quote=True)
                banned_bins.remove(bin_id)
                text = "♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Bin (<code>{}</code>) desbaneado con éxito ✅"
            file.seek(0)
            json.dump(banned_bins, file, indent=4)
            file.truncate()
        await m.reply(text.format(bin_id), quote=True)
