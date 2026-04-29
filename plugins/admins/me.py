from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from functions.variables import PREFIXES
from functions.database import Database
from functions.functions import get_text_from_pyrogram, Symbol
import json
@Client.on_message(filters.command(["me"], PREFIXES))
async def plan(client: Client, m: Message):
    with open("functions/botstatus.json", "r") as file:
        bot_state = json.load(file)
    
    if bot_state["state"]:
        return await m.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒El bot Se Encuentra En Mantenimiento</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""")

    text = m.text[len(m.command[0]) + 2 :].strip()
    getting_info = False

    try:
        if text.isdigit():
            user_id = int(text)
            user = await client.get_users(user_id)
            getting_info = True
        elif text.startswith("@"):
            user = await client.get_users(text)
            getting_info = True
        else:
            user_id = m.from_user.id
            user = m.from_user
    except Exception:
        return await m.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Usuario o ID no encontrado o inválido.</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""")

    if getting_info:
        first_name = user.first_name
        user_name = user.username
        user_id = user.id
    else:
        first_name = m.from_user.first_name.replace("<", "").replace(">", "")
        user_name = m.from_user.username

    name = f"<a href='tg://user?id={user_id}'>{first_name}</a>"

    with Database() as db:
        info_user = db.get_info_user(user_id)

    membership = info_user["MEMBERSHIP"].capitalize()
    registered = info_user["REGISTERED"]
    registered = datetime.strptime(registered, "%Y-%m-%d %H:%M:%S")
    registered = registered.strftime("%y/%m/%d - %I:%M%p")
    antispam = info_user["ANTISPAM"]
    credits = info_user["CREDITS"]
    rol = info_user["RANK"] if Database.ID_OWNER != user_id else "Owner"
    rol = rol.capitalize()
    rol_display = f"[{rol}]" if rol.lower() != "user" else ""
    nick = info_user["NICK"]
    expiration_premium = info_user["EXPIRATION"] if info_user["EXPIRATION"] else ""

    if membership.lower() == "free":
        expiration_premium = "No membership"
    elif expiration_premium:
        now = datetime.strptime(expiration_premium, "%Y-%m-%d %H:%M:%S")
        diff = now - datetime.now()
        days = diff.days
        total_seconds = diff.seconds
        hours, total_seconds = divmod(total_seconds, 3600)
        minutes, seconds = divmod(total_seconds, 60)
        
        tiempo = []
        if days > 0:
            tiempo.append(f"<code>{days}</code> dias")
        if hours > 0:
            tiempo.append(f"<code>{hours}</code> horas")
        if minutes > 0:
            tiempo.append(f"<code>{minutes}</code> minutos")
        if seconds > 0:
            tiempo.append(f"<code>{seconds}</code> segundos")
            
        expiration_premium = ' '.join(tiempo)
    else:
        expiration_premium = "No membership"

    antispam = str(antispam)
    symbol = await Symbol()
    if not membership:
        membership = "No definido" 

    text = f"""
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒User: @{user_name} (<code>{user_id}</code>)</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Plan: <code>{membership}</code> | <code>{rol_display}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Creditos: <code>{credits}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Expiration: <code>{expiration_premium}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒AntiSpam: <code>{antispam}</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
"""
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Buy Checker", url="https://t.me/tocandotee"),
            InlineKeyboardButton("Refes", url="https://t.me/ZyrexRefes")
        ]
    ])

    await m.reply(text, 
                 quote=True, 
                 disable_web_page_preview=True,
                 reply_markup=buttons)
