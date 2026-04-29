from pyrogram import Client, filters
from functions.gate_manager import GateManager
from functions.variables import PREFIXES
from functions.functions import Symbol


@Client.on_message(filters.command(['offgate', 'ongate'], PREFIXES))
async def toggle_gate_command(client, message):
    try:
        args = message.text.split()
        if len(args) < 2:
            return await message.reply_text("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Uso: /offgate comando razón", reply_to_message_id=message.id)
        symbol = await Symbol()
        comando = args[1]
        razon = ' '.join(args[2:]) if len(args) > 2 else None
        estado = message.command[0] == "ongate"
        
        gate_info = GateManager.toggle_gate(comando, estado, razon)
        if gate_info:
            await message.reply_text(f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Gateway: {comando}</b>
<b><a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Status: {'Encendido' if estado else 'Apagado'}</b>
<b><a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Razón: {razon or 'N/A'}</b>
<b><a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Última Revisión: {gate_info['ultima_revision']}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""", reply_to_message_id=message.id)
        else:
            await message.reply_text("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Gate no encontrado", reply_to_message_id=message.id)
            
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}", reply_to_message_id=message.id)
