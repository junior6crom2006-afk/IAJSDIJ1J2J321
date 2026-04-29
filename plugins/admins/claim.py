from pyrogram import Client, filters
from pyrogram.types import Message  # Importa Message
from functions.database import Database
from functions.variables import PREFIXES
from functions.functions import Symbol
import re
import logging
import json
@Client.on_message(filters.command("claim", PREFIXES))
async def claim(client: Client, message: Message):
    ## INFO
    USER_INFO = message.from_user
    CHAT_INFO = message.chat

    USER_ID = USER_INFO.id
    CHAT_ID = CHAT_INFO.id
    with open("functions/botstatus.json", "r") as file:
        bot_state = json.load(file)
    
    if bot_state["state"]:
        return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒El bot Se Encuentra En Mantenimiento\nRazón: {bot_state['reason']}")

    ## VERIFICATION IN THE DATABASE
    with Database() as db:
        pass

    ## COMMAND
    COMMAND = message.command[0]

    ## GET KEY
    key = re.findall(r'ZYREX-\w+', message.text)
    if not key:
        return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Formato: <code>/{COMMAND} KEY-KilluaCheckerxxxx</code>", quote=True)
    key = key[0]

    logging.debug(f"Clave extraída: {key}")  # Agrega logging para ver la clave extraída

    with Database() as db:
        logging.debug(f"Verificando si el usuario {USER_ID} es vendedor")  # Agrega más logging
        if db.is_seller(USER_ID):
            return await message.reply(
                "♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Los sellers no pueden reclamar keys",
                quote=True,
            )
        logging.debug(f"Intentando reclamar la clave: {key}")  # Agrega más logging
        result = db.claim_key(key, USER_ID)
        logging.debug(f"Resultado de la reclamación: {result}")  # Agrega más logging

    if result is None:
        return await message.reply(     
            f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No existe esa key bro hahah",
            quote=True,
        )
    
    expiration = result["expiration"]
    plan_name = result["plan"]
    symbol = Symbol()
    await message.reply(
        f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Key claimed</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Usuario: @{USER_INFO.username}</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒UserID: <code>{USER_ID}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <code>{plan_name}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Expiration Time: <code>{expiration}</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
        quote=True,
    )