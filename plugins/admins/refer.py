from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.functions import Symbol
from functions.variables import PREFIXES
from datetime import datetime
import uuid
import sqlite3
import os

# Crear la base de datos si no existe
def init_db():
    if not os.path.exists("referencias.db"):
        conn = sqlite3.connect("referencias.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS referencias
                    (refer_id TEXT PRIMARY KEY, message_id INTEGER, 
                     user_id INTEGER, admin TEXT)''')
        conn.commit()
        conn.close()

init_db()

# Configura estos IDs
ADMIN_IDS = [7882956639,7160744560,8507555830] 
CANAL_PRIVADO = -1003713039756  # ID sin el -100
CANAL_PUBLICO = "@ZyrexRefes"  
# Añade aquí tu ID de usuario para recibir mensajes
MY_USER_ID = 7882956639  # Reemplaza con tu ID de usuario

@Client.on_message(filters.command(["refer", "delrefer"], PREFIXES))
async def refer_commands(client, message):
    try:
        symbol = await Symbol()
        command = message.command[0].lower()

        if command == "delrefer":
            if message.from_user.id not in ADMIN_IDS:
                await message.reply_text(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒No tienes permiso para usar este comando</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""")
                return

            if len(message.command) != 2:
                await message.reply_text(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Usage: .delrefer [UUID]</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""")
                return

            uuid_to_delete = message.command[1]
            
            # Buscar en la base de datos
            conn = sqlite3.connect("referencias.db")
            c = conn.cursor()
            c.execute("SELECT message_id FROM referencias WHERE refer_id = ?", (uuid_to_delete,))
            result = c.fetchone()
            
            if result:
                msg_id = result[0]
                try:
                    # Intentar eliminar del canal público
                    await client.delete_messages(CANAL_PUBLICO, msg_id)
                except Exception:
                    pass
                
                # Eliminar de la base de datos
                c.execute("DELETE FROM referencias WHERE refer_id = ?", (uuid_to_delete,))
                conn.commit()
                await message.reply_text(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Reference deleted successfully</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""")
            else:
                await message.reply_text(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Reference not found</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""")
            
            conn.close()
            return

        # Lógica de detección de imagen (incluyendo reply)
        photo = None
        if message.photo:
            photo = message.photo.file_id
        elif message.reply_to_message and message.reply_to_message.photo:
            photo = message.reply_to_message.photo.file_id

        if not photo:
            await message.reply_text(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒You must send an image with the command or reply to one.</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""")
            return
            
        # Verificar si hay mensaje
        if len(message.command) < 2:
            await message.reply_text(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Usage: .refer [message]</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""")
            return
            
        # Generar UUID único para la referencia
        refer_id = str(uuid.uuid4())[:8]
        
        # Obtener el mensaje y la imagen
        refer_text = " ".join(message.command[1:])
        
        # Obtener información del usuario
        user_id = message.from_user.id
        if message.from_user.username:
            user_mention = f"@{message.from_user.username}"
        else:
            user_mention = f"<a href='tg://user?id={user_id}'>{message.from_user.first_name}</a>"
        
        # Enviar directamente al canal público
        sent_msg = await client.send_photo(
            chat_id=CANAL_PUBLICO,
            photo=photo,
            caption=f"""
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Nueva Referencia</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒{refer_text}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒De: {user_mention}</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒ID: <code>{refer_id}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Fecha: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>"""
        )
        
        # Guardar en la base de datos
        conn = sqlite3.connect("referencias.db")
        c = conn.cursor()
        c.execute("INSERT INTO referencias (refer_id, message_id, user_id) VALUES (?, ?, ?)", 
                  (refer_id, sent_msg.id, user_id))
        conn.commit()
        conn.close()

        # Notificar a admins (sin botones)
        for admin_id in ADMIN_IDS:
            try:
                await client.send_message(
                    chat_id=admin_id,
                    text=f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Nueva Referencia</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Mensaje: {refer_text}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒De: {user_mention}</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒ID: <code>{refer_id}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Fecha: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>"""
                )
            except:
                pass
            
        await message.reply_text(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Tu referencia [<code>{refer_id}</code>] ha sido publicada exitosamente en {CANAL_PUBLICO}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""")
        
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")