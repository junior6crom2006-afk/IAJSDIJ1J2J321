import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from functions.variables import PREFIXES
from functions.functions import Symbol
import sqlite3
def get_db_connection():
    conn = sqlite3.connect('db/api_data.db')
    return conn

def load_api_data(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS api_data (user_id TEXT, url TEXT)")
    cursor.execute("SELECT url FROM api_data WHERE user_id = ?", (user_id,))
    urls = cursor.fetchall()
    conn.close()
    return [url[0] for url in urls] 

def delete_api_data(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM api_data WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

@Client.on_message(filters.command(["mx"], PREFIXES))
async def apidelet_command(client: Client, m: Message):
    with open("functions/botstatus.json", "r") as file:
        bot_state = json.load(file)
    
    if bot_state["state"]:
        return await m.reply(f"El bot Se Encuentra En Mantenimiento\nRazón: {bot_state['reason']}")
    symbol = await Symbol()  
    user_id = m.from_user.id
    user_api_data = load_api_data(user_id)

    if user_api_data:
        delete_api_data(user_id)
        return await m.reply(
            f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | MX Tool
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Status</b>: <code>API(s) eliminada(s) exitosamente.</code>
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0""",
            quote=True,
        )
    else:
        return await m.reply(
            f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | MX Tool
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Status</b>: <code>No tienes un sitio guardado para eliminar.</code>
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0""",
            quote=True,
        )