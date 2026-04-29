from pyrogram import Client, filters
from gates.pzy import pzyy
from functions.functions import GetCC, Symbol, get_bin_info, AntiSpam, ProxyRandom, proxy_x
from functions.database import Database
from functions.variables import PREFIXES
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
import asyncio
import json

# Definición del teclado inline
keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Buy", url="https://t.me/tocandotee"),
        InlineKeyboardButton("Channel", url="https://t.me/zyrexnews")
    ]
])

# Función principal para manejar mensajes
@Client.on_message(filters.command(['pay'], PREFIXES))
async def gate_te(client, message):

    symbol = await Symbol()
    with Database() as db:
        userid = message.from_user.id
        # Verificar si el usuario es premium
        if not db.is_premium(userid):
            return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No eres premium. Contacta a @tocandotee\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0")
        
        user_info = db.get_info_user(userid)
        is_free_user = user_info["MEMBERSHIP"].lower() == "free user"
        rol = user_info["RANK"].capitalize()
        credits = user_info.get("CREDITS", 0)
        if credits < 3:
            return await message.reply(
                f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No tienes créditos suficientes. Contacta a @tocandotee\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0",
                reply_markup=keyboard,
                quote=True,
            )
    # Verificar créditos del usuario y aplicar antispam
    antispam = await AntiSpam(userid, user_info["ANTISPAM"], is_free_user)
    if antispam:
        return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | ANTISPAM\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Wait: {antispam}s before checking another cc.\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0")

    # Procesamiento de la tarjeta
    card_details = await GetCC(message.text)
    if not card_details:
        return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Formato: <code>/pay cc|mm|yy|cvv</code>\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0")
    cc, mes, ano, cvv = card_details

    # Procesamiento de la información del BIN
    serie = cc[:6]  # Definir 'serie' como los primeros 6 dígitos de la tarjeta
    start_time2 = time.time()  
    resp = await get_bin_info(serie)
    if not resp:
        return await message.reply("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Bin Not Found ⚠️\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0")
    
    bin_data = resp.get("BIN", resp)
    brand = bin_data.get("brand", "N/A")
    level = bin_data.get("level", "N/A")
    type_v = bin_data.get("type", "N/A")
    bank = bin_data.get("issuer", {}).get("name", "N/A") if isinstance(bin_data.get("issuer"), dict) else bin_data.get("bank_name", "N/A")
    country = bin_data.get("country", {}).get("name", "N/A") if isinstance(bin_data.get("country"), dict) else bin_data.get("country_name", "N/A")
    flag = bin_data.get("country", {}).get("flag", "") if isinstance(bin_data.get("country"), dict) else bin_data.get("flag", "")


    if message.from_user.id not in [7882956639] and (bin_data.get("banned", False) or "prepaid" in level.lower() or "prepaid" in type_v.lower()):
        return await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Bin: <code>{serie}</code>\nBin banned, operation prohibited\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0")

    # Envío del mensaje inicial con indicador amarillo
    taken2 = round(time.time() - start_time2, 2)
    msgedit = await client.send_message(
        chat_id=message.chat.id, 
        text=f"""
♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Payeezy 35$ (/pay)
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Processing Please Wait... (🟡)
<a href="https://t.me/zyrexnews">ゕ</a>﹒Took: {taken2}
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0
    """, 
    reply_to_message_id=message.id
    )

    # Inicialización de variables antes del bucle de reintentos
    status = "Unknown"
    response = "Error desconocido"
    taken_total = 0  # Valor inicial por si el bucle falla y no se asigna

    # Contador de reintentos
    retries = 0
    max_retries = 3
    start_time_total = time.time()
    ip_info = proxy_x()
    # Intentos de procesamiento de la tarjeta
    while retries < max_retries:
        try:
            start_time = time.time()
            status, response = await pzyy(cc, mes, ano, cvv, await ProxyRandom())
            taken_retry = round(time.time() - start_time, 2)
            taken_total = round(time.time() - start_time_total, 2)
            break

        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries == 1:
            await msgedit.edit_text(
                text=f"""
♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Payeezy 35$ (/pay)
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>Checking...</b>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{cc[:6]}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{brand}</code> - <code>{level}</code> - <code>{type_v}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{bank}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{country}</code> - <code>{flag}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Time: <code>{taken_total}</code> 
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: <code>{ip_info}</code>
<a href="https://t.me/zyrexnews">ゕ</a>Time: <code>{taken_total}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{message.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0
                """
            )
        if retries >= max_retries:
            status = "Declined ❌"
            response = "Max retries exceeded"
            taken_total = round(time.time() - start_time_total, 2)  # El tiempo total después del último fallo
            break
        await asyncio.sleep(2)  # Espera antes de intentar nuevamente

    # Final results processing
    if "approved" in status.lower():
        with Database() as db:
            db.remove_credits(userid, 3)
        status_text = "Approved ✅"
    elif "declined" in status.lower():
        with Database() as db:
            db.remove_credits(userid, 1)
        status_text = "Declined ❌"
    else:
        status_text = status

    # Bin info safety handler
    bin_data = resp.get("BIN", resp)
    brand = bin_data.get("brand", "N/A")
    level = bin_data.get("level", "N/A")
    type_v = bin_data.get("type", "N/A")
    bank = bin_data.get("issuer", {}).get("name", "N/A") if isinstance(bin_data.get("issuer"), dict) else bin_data.get("bank_name", "N/A")
    country = bin_data.get("country", {}).get("name", "N/A") if isinstance(bin_data.get("country"), dict) else bin_data.get("country_name", "N/A")
    flag = bin_data.get("country", {}).get("flag", "") if isinstance(bin_data.get("country"), dict) else bin_data.get("flag", "")

    # Final Premium Response
    await msgedit.edit_text(
        text=f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Payeezy 35$ (/pay)
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>{status_text}</b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Response: <code>{response}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{serie}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{brand}</code> - <code>{level}</code> - <code>{type_v}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{bank}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{country}</code> - <code>{flag}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: <code>{ip_info}</code>
<a href="https://t.me/zyrexnews">ゕ</a>Time: <code>{taken_total}s</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{message.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0""",
        reply_markup=keyboard
    )
