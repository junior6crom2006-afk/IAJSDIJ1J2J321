from pyrogram import Client, filters
from functions.variables import PREFIXES
from functions.gate_manager import GateManager
from functions.functions import Symbol
import os
import re
import json

@Client.on_message(filters.command(['addmanager'], PREFIXES))
async def add_manager(client, message):
    try:
        if len(message.command) != 2:
            return await message.reply("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Uso: /addmanager nombre_archivo.py")
        
        filename = message.command[1]
        if not filename.endswith('.py'):
            filename += '.py'
            
        filepath = f"plugins/gates/{filename}"
        
        if not os.path.exists(filepath):
            return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒El archivo {filename} no existe en plugins/gates/")
        
        # Guardar información de la modificación
        temp_data = {
            "chat_id": message.chat.id,
            "message_id": message.id,
            "filename": filename,
            "action": "pending"
        }
        
        with open("database/temp_manager.json", "w") as f:
            json.dump(temp_data, f)
            
        await message.reply("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Procesando...")
        
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Añadir import si no existe
        if 'from functions.gate_manager import GateManager' not in content:
            imports = 'from functions.gate_manager import GateManager\n'
            if 'from pyrogram import Client' in content:
                content = content.replace('from pyrogram import Client', 'from pyrogram import Client\n' + imports)
            else:
                content = imports + content
        
        function_start = content.find('@Client.on_message')
        function_def = content.find('async def', function_start)
        insert_point = content.find(':', function_def) + 1
        
        # Nuevo código del GateManager
        manager_code = """
    # Registrar el gate
    GateManager.register_gate(
        comando=f"/{message.command[0]}",
        nombre="Gateway Name",
        tipo="CCN",  # Opciones: CCN, AUTH, CHARGED
        premium=True
    )
    symbol = await Symbol()
    # Verificar estado del gate
    gate_info = GateManager.get_gate_info(f"/{message.command[0]}")
    if gate_info["estado"] == "OFF":
        return await message.reply(f\"\"\"<b>
{symbol} Gateway: /{message.command[0]}
{symbol} Status: Apagado
{symbol} Razón: {gate_info['razon'] or 'N/A'}
{symbol} Última Revisión: <code>{gate_info['ultima_revision']}</code></b>\"\"\", reply_to_message_id=message.id)"""

        # Si ya existe un GateManager, reemplazarlo
        if 'GateManager.register_gate' in content:
            pattern = r"(?s)# Registrar el gate.*?message\.id\)"
            new_content = re.sub(pattern, manager_code.strip(), content)
            action = "actualizado"
        else:
            new_content = content[:insert_point] + manager_code + content[insert_point:]
            action = "añadido"
        
        # Guardar el archivo
        with open(filepath, 'w') as file:
            file.write(new_content)
            
    except Exception as e:
        await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Error: {str(e)}")
        if os.path.exists("database/temp_manager.json"):
            os.remove("database/temp_manager.json")

@Client.on_message(filters.command("start"))
async def check_pending_manager(client, message):
    try:
        if os.path.exists("database/temp_manager.json"):
            with open("database/temp_manager.json", "r") as f:
                data = json.load(f)
            
            if data["action"] == "pending":
                await client.send_message(
                    data["chat_id"],
                    f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒GateManager actualizado exitosamente en {data['filename']}
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Recuerda configurar en el registro:
<a href="https://t.me/zyrexnews">ゕ</a>﹒Nombre
<a href="https://t.me/zyrexnews">ゕ</a>﹒Tipo (CCN/AUTH/CHARGED)
<a href="https://t.me/zyrexnews">ゕ</a>﹒Premium (True/False)
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Verificación de estado
<a href="https://t.me/zyrexnews">ゕ</a>﹒Formato con símbolos
<a href="https://t.me/zyrexnews">ゕ</a>﹒Etiquetas <b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Formato monoespacio para fechas""",

                    reply_to_message_id=data["message_id"]
                )
            
            os.remove("database/temp_manager.json")
    except Exception as e:
        print(f"Error checking pending manager: {str(e)}")
