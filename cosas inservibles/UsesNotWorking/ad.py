from pyrogram import Client, filters
from gates.ad import pf
from functions.functions import ProxyRandom, GetCC, Symbol, AntiSpam
from functions.database import Database
from functions.variables import PREFIXES
import time

@Client.on_message(filters.command('ad', PREFIXES,))
async def gate_kv(client, message):
    with Database() as db:
         userid = message.from_user.id
         kk = db.is_premium(userid)
         if False == kk:
             return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No eres premium. Contacta a @tocandotee\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0")
         else:
            user_info = db.get_info_user(userid)
            is_free_user = user_info["MEMBERSHIP"]
            is_free_user = is_free_user.lower() == "free user"
            rol = user_info["RANK"]
    antispam = await AntiSpam(userid, user_info["ANTISPAM"], is_free_user)
    if antispam != False: 
        return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | ANTISPAM\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Wait: {antispam}s before checking another cc.\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0")
    start_time = time.time()
    symbol = await Symbol()
    kk = await GetCC(message.text)
    if not kk:
        await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>Use: <code>/ad cc|mm|yy|cvv</code>\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0")
        return
    cc = kk[0]
    mes = kk[1]
    ano = kk[2]
    cvv = kk[3]

    card = f"{cc}|{mes}|{ano}|{cvv}"
    serie = cc[0:6]

    # Send initial message
    symbol = await Symbol()
    msgedit = await client.send_message(chat_id=message.chat.id, text=f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Payflow AVS CCN (/ad)
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>OFFLINE</b>
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0
""")