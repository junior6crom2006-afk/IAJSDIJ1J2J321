from pyrogram import *
import asyncio
import json
from functions.database import Database

@Client.on_message(filters.command('start', prefixes=['/', ',', '.', '!', '$', '-', '}', '{', ']','[', '(', ')', '#', '%' ], case_sensitive=False) & filters.text)
async def start(client, message):
    with Database() as db:
        userid = message.from_user.id
        username = message.from_user.username
        db.register_user(userid, username)
    
    m1 = await client.send_message(chat_id=message.chat.id, text=f"""<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Panel Principal</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Welcome @{message.from_user.username} to 𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒You are being registered in the database, please wait a moment.</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>  
        """, reply_to_message_id=message.id)
    await asyncio.sleep(1.5)
    await m1.edit(text=f"""<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Panel Principal</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Welcome @{message.from_user.username} to 𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒You've been added to the *DB*.</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒You can use /cmds to see the commands</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>  
        """)