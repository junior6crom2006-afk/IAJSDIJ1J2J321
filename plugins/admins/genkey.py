from pyrogram import Client, filters
from pyrogram.types import Message
from functions.database import Database
from functions.variables import PREFIXES
from re import findall
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functions.functions import Symbol
symbol = Symbol()



@Client.on_message(filters.command("key", PREFIXES))
async def gkey(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_owner(user_id):
            return
        
        # Parsing: /key [days] [plan] [quantity]
        args = m.command[1:]
        days = 1
        plan = "Premium"
        quantity = 1

        if len(args) >= 1:
            try: days = int(args[0])
            except: pass
        
        if len(args) >= 2:
            if args[1].upper() in ["PREMIUM", "VIP"]:
                plan = args[1].capitalize()
            else:
                try: quantity = int(args[1])
                except: pass
        
        if len(args) >= 3:
            try: quantity = int(args[2])
            except: pass

        keys_list = []
        for i in range(int(quantity)):
            key, expire_day = db.gen_key(int(days), plan)
            keys_list.append(f"<code>{key}</code>")

        keys_text = "\n".join(keys_list)

    await m.reply(
        f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Key generated</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Plan: <code>{plan}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Keys:</b>
{keys_text}
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Days: <code>{days}</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
        quote=True,
    )