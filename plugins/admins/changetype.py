from pyrogram import Client, filters
from functions.gate_manager import GateManager
from functions.functions import Symbol
from functions.variables import PREFIXES

@Client.on_message(filters.command(['changetype'], PREFIXES))
async def change_gate_type(client, message):
    try:
        args = message.text.split()
        if len(args) < 3:
            return await message.reply_text("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Uso: /changetype comando nuevo_tipo\nTipos: CCN, AUTH, CHARGED", reply_to_message_id=message.id)
        
        symbol = await Symbol()
        comando = args[1]
        if not comando.startswith('/'):
            comando = f'/{comando}'
            
        nuevo_tipo = args[2].upper()
        
        # Verificar que el tipo sea válido
        if nuevo_tipo not in ["CCN", "AUTH", "CHARGED"]:
            return await message.reply_text("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Tipo inválido. Usar: CCN, AUTH o CHARGED", reply_to_message_id=message.id)
        
        # Obtener info actual del gate
        gate_info = GateManager.get_gate_info(comando)
        if not gate_info:
            return await message.reply_text("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Gate no encontrado", reply_to_message_id=message.id)
            
        # Actualizar el tipo
        GateManager.update_gate_type(comando, nuevo_tipo)
        
        await message.reply_text(f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Gateway: {comando}</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Tipo Anterior: {gate_info['tipo']}</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Nuevo Tipo: {nuevo_tipo}</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Última Revisión: {gate_info['ultima_revision']}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""", reply_to_message_id=message.id)
            
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}", reply_to_message_id=message.id)
