import json
from functions.database import Database
from pyrogram import Client, filters

bot_status = {}

@Client.on_message(filters.command("man"))
async def handle_cmdgate(client, message):
    user_id = message.from_user.id
    with Database() as db:
        if not db.is_owner(user_id):
            return
    parts = message.text.split()
    if len(parts) < 3:
        return await message.reply("""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Uso: /mantenimiento [on/off] [razón]</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""")
    _, state, *reason = parts
    reason = " ".join(reason) if reason else "No reason provided"
    if state not in ["on", "off"]:
        return await message.reply("El estado debe ser 'on' o 'off'")

    bot_status = {"state": state == "on", "reason": reason}
    verificar_mantenimiento(bot_status)
    await message.reply(
        f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒El bot se encuentra {'En Mantenimiento' if state == 'on' else 'Fuera De Mantenimiento'}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Razon: {reason}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
"""
    )

def verificar_mantenimiento(states):
    with open("functions/botstatus.json", "w") as file:
        json.dump(states, file)