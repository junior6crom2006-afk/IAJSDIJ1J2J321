from pyrogram import Client, filters
from functions.variables import PREFIXES
from functions.database import Database
from functions.gate_manager import GateManager
import os

@Client.on_message(filters.command(['gatenew'], PREFIXES))
async def create_new_gate(client, message):
    try:
        # Verificar formato
        args = message.text.split()
        if len(args) != 2:
            return await message.reply_text("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Uso: /gatenew comando|import|tipo|gateway\nEjemplo: /gatenew te|stripeccn1|ccn|Stripe Auth", reply_to_message_id=message.id)
        
        # Parsear argumentos
        comando, import_name, gate_type, gateway_name = args[1].split("|")
        if not all([comando, import_name, gate_type, gateway_name]):
            return await message.reply_text("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Todos los campos son requeridos", reply_to_message_id=message.id)
        
        if gate_type.lower() not in ['ccn', 'auth', 'charged']:
            return await message.reply_text("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Tipo de gate inválido. Usar: ccn, auth o charged", reply_to_message_id=message.id)

        # Crear el nuevo archivo del gate con el formato correcto
        template = f"""Gateway: {gateway_name} [{gate_type.upper()}]"""
        
        # Crear el nuevo archivo del gate
        template_path = "plugins/gates/kl.py"  # Tu archivo plantilla
        new_gate_path = f"plugins/gates/{comando}.py"
        
        if os.path.exists(new_gate_path):
            return await message.reply_text(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Ya existe un gate con el comando {comando}", reply_to_message_id=message.id)

        # Leer la plantilla
        with open(template_path, 'r') as file:
            template = file.read()

        # Reemplazar valores
        new_content = template.replace(
            'from gates.stripeccn1 import stripeccn1',
            f'from gates.{import_name} import {import_name}'
        ).replace(
            "@Client.on_message(filters.command(['kl'], PREFIXES))",
            f"@Client.on_message(filters.command(['{comando}'], PREFIXES))"
        ).replace(
            'async def gate_te',
            f'async def gate_{comando}'
        ).replace(
            'Gateway: Stripe CCN_AUTH',
            f'Gateway: {import_name.capitalize()}'
        ).replace(
            '[CCN_AUTH]',
            f'[{gate_type.upper()}]'
        )

        # Guardar el nuevo archivo
        with open(new_gate_path, 'w') as file:
            file.write(new_content)

        # Registrar el gate en la base de datos
        GateManager.register_gate(
            comando=f"/{comando}",
            nombre=f"{import_name.capitalize()}",
            tipo=gate_type.upper(),
            premium=True
        )

        await message.reply_text(f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Gate creado exitosamente</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Comando: /{comando}</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Import: {import_name}</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Tipo: {gate_type.upper()}</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Archivo: plugins/gates/{comando}.py</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""", reply_to_message_id=message.id)

    except Exception as e:
        await message.reply_text(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Error al crear el gate: {str(e)}", reply_to_message_id=message.id) 