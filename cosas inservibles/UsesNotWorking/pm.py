from pyrogram import Client, filters
from gates.paymentshub import checkout1
from functions.functions import GetCC, Symbol, get_bin_info, AntiSpam, ProxyRandomFromFile, proxy_x, get_text_from_pyrogram
from functions.database import Database
from functions.variables import PREFIXES
from functions.gate_manager import GateManager
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
import asyncio
import json

# Definición del teclado inline
keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Buy", url="https://t.me/tocandotee"),
        InlineKeyboardButton("Channel", url="https://t.me/ZyrexRefes")
    ]
])

# Función principal para manejar mensajes
@Client.on_message(filters.command(['pm'], PREFIXES))
async def gate_te(client, message):
    symbol = await Symbol()
    cmd = message.command[0]

    with Database() as db:
        user_id = message.from_user.id
        is_premium = db.is_premium(user_id)
        if not is_premium:
            return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No eres premium. Contacta a @tocandotee\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0", reply_markup=keyboard)
        
        user_info = db.get_info_user(user_id)
        is_free_user = user_info["MEMBERSHIP"].lower() == "free user"
        rol = user_info["RANK"].capitalize()
        credits = user_info.get("CREDITS", 0)

        if credits < 3:
            return await message.reply(
                f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No tienes créditos suficientes (3 Req).\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0",
                reply_markup=keyboard,
                quote=True,
            )

    antispam = await AntiSpam(user_id, user_info["ANTISPAM"], is_free_user)
    if antispam:
        return await message.reply(f"<b>[ANTISPAM] ESPERE {antispam}s PARA EL PROXIMO CHECKEO</b>")

    text = await get_text_from_pyrogram(message)
    ccs = await GetCC(text)

    if not ccs:
        return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Inserta una CC válida: <code>cc|mm|yy|cvv</code>\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0", quote=True)
    
    cc, mes, ano, cvv = ccs
    start_time2 = time.time()
    
    resp = await get_bin_info(cc[:6])
    if not resp:
        return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Bin incorrecto o inexistente 🔹\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0", quote=True)

    bin_data = resp.get("BIN", resp)
    serie = bin_data.get("bin", cc[0:6])
    brand = bin_data.get("brand", "N/A")
    level = bin_data.get("level", "N/A")
    type_v = bin_data.get("type", "N/A")
    bank = bin_data.get("issuer", {}).get("name", "N/A") if isinstance(bin_data.get("issuer"), dict) else bin_data.get("bank_name", "N/A")
    country = bin_data.get("country", {}).get("name", "N/A") if isinstance(bin_data.get("country"), dict) else bin_data.get("country_name", "N/A")
    flag = bin_data.get("country", {}).get("flag", "") if isinstance(bin_data.get("country"), dict) else bin_data.get("flag", "")

    if user_id not in [7882956639] and (bin_data.get("banned", False) or "prepaid" in level.lower() or "prepaid" in type_v.lower()):
        return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Bin: <code>{serie}</code>\nBin banned, operation prohibited\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0")

    taken2 = round(time.time() - start_time2, 2)
    msgedit = await client.send_message(
        chat_id=message.chat.id, 
        text=f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | UNK [CCN] (/pm)
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>Checking...</b>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{cc[:6]}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{brand}</code> - <code>{level}</code> - <code>{type_v}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{bank}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{country}</code> - <code>{flag}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: Live!✅
<a href="https://t.me/zyrexnews">ゕ</a>﹒Time: <code>{taken2}s</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{message.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0
""", 
        reply_to_message_id=message.id
    )

    status = "Unknown"
    response = "Error desconocido"
    retries = 0
    max_retries = 3
    start_time_total = time.time()
    
    while retries < max_retries:
        try:
            status, response = await checkout1(cc, mes, ano, cvv, await ProxyRandomFromFile())
            break
        except Exception:
            retries += 1
            await asyncio.sleep(2)

    taken_total = round(time.time() - start_time_total, 2)

    if "approved" in status.lower():
        with Database() as db:
            db.remove_credits(user_id, 3)
    elif "declined" in status.lower():
        with Database() as db:
            db.remove_credits(user_id, 1)

    await msgedit.edit_text(
        text=f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | UNK [CCN] (/pm)
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>{status}</b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Response: <code>{response}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{cc[:6]}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{brand}</code> - <code>{level}</code> - <code>{type_v}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{bank}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{country}</code> - <code>{flag}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: Live!✅
<a href="https://t.me/zyrexnews">ゕ</a>﹒Time: <code>{taken_total}s</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{message.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0""", 
        reply_markup=keyboard,
        disable_web_page_preview=True
    )
