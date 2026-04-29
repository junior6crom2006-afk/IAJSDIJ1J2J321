from pyrogram import Client, filters
from functions.gate_manager import GateManager
from functions.variables import PREFIXES
from functions.database import Database

@Client.on_message(filters.command("reload", PREFIXES))
async def reload_gates(client, message):
    user_id = message.from_user.id
    
    with Database() as db:
        if not db.is_owner(user_id):
            return

    GateManager.reload_cache()
    
    await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Reload Cache</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Cache de gateways recargado con éxito.</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""", quote=True)
