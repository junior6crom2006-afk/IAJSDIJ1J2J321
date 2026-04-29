from pyrogram import Client, filters
from pyrogram.types import Message
from re import findall
from functions.database import Database
from functions.variables import PREFIXES
from functions.functions import Symbol
FORMAT_CMD = f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Uso: /crd id/Credit</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Uso: /dcrd id/Credit</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
"""


@Client.on_message(filters.command(["crd", "dcrd"], PREFIXES))
async def creditos(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_owner(user_id):
            return await m.reply("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Comando disponible solo para administradores.", quote=True)
        info_user = db.get_info_user(user_id)
        symbol = await Symbol()
        text = m.text[len(m.command[0]) + 2 :].strip()
        data_nums = findall(r"\d+", text)
        if len(data_nums) != 2:
            return await m.reply(FORMAT_CMD, quote=True)
        id = data_nums[0]
        creditos = int(data_nums[1])
        
        if m.command[0] == "crd":
            result = db.add_credits(id, creditos)
            await m.reply(
                f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Créditos añadidos a la cuenta</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒UserID: <code>{id}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Créditos Nuevos: <code>{creditos}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Admin: @{m.from_user.username}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                quote=True,
            )
        elif m.command[0] == "dcrd":
            result = db.remove_credits(id, creditos)
            await m.reply(
                f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Créditos removidos de la cuenta</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒UserID: <code>{id}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Créditos Removidos: <code>{creditos}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Admin: @{m.from_user.username}</b>
━━━━━━━{symbol}━━━━━━━</b>""",
                quote=True,
            )