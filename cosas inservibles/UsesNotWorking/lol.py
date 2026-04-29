from pyrogram import Client, filters
from functions.gate_manager import GateManager
from gates.tapgateway import pene
from functions.functions import GetCC, Symbol, get_bin_info, AntiSpam, ProxyRandom, proxy_x
from functions.database import Database
from functions.variables import PREFIXES
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
import asyncio
import json

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Buy", url="https://t.me/tocandotee"),
        InlineKeyboardButton("Channel", url="https://t.me/ZyrexRefes")
    ]
])

@Client.on_message(filters.command(['lol'], PREFIXES))
async def gate_lol(client, message):

    
    symbol = await Symbol()
    gate_info = GateManager.get_gate_info("/lol")
    if gate_info["estado"] == "OFF":
        return await message.reply_text(f"""<b>
{symbol} Gateway: /lol
{symbol} Status: Apagado
{symbol} Razón: {gate_info['razon'] or 'N/A'}
{symbol} Última Revisión: {gate_info['ultima_revision']}</b>""", reply_to_message_id=message.id)

    with Database() as db:
        userid = message.from_user.id
        if not db.is_premium(userid):
            return await message.reply(f"{symbol} No eres premium. Contacta a @tocandotee")
        
        user_info = db.get_info_user(userid)
        is_free_user = user_info["MEMBERSHIP"].lower() == "free user"
        rol = user_info["RANK"]
        credits = user_info.get("CREDITS", 0)
        if credits < 3:
            return await message.reply(
                f"<b>{symbol} Insufficient credits ⚠️\nNecesitas al menos 3 créditos.</b>",
                reply_markup=keyboard,
                quote=True,
            )

    antispam = await AntiSpam(userid, user_info["ANTISPAM"], is_free_user)
    if antispam:
        return await message.reply(f"<b>Hey Carnal !! Vas Muy Rapido, Porfavor Espera {antispam} Segundos Para Hacer El Proximo Checkeo</b>")

    if message.reply_to_message and message.reply_to_message.text:
        card_details = await GetCC(message.reply_to_message.text)
    else:
        card_details = await GetCC(message.text)
    
    if not card_details:
        return await message.reply(f"{symbol} <b>Please Enter A Valid Card! ⚠️</b>", quote=True)
    cc, mes, ano, cvv = card_details

    serie = cc[:6]
    start_time2 = time.time()  
    resp = await get_bin_info(serie)
    if resp is None:
        return await message.reply("<b>Bin Not Found ⚠️</b>", quote=True)
    
    if message.from_user.id not in [] and (resp["banned"] or "prepaid" in resp["level"].lower() or "prepaid" in resp["type"].lower()):
        return await message.reply(f"<b>Bin: <code>{resp['bin']}</code>\nBin banned, operation prohibited</b>")

    # Envío del mensaje inicial con indicador amarillo
    taken2 = round(time.time() - start_time2, 2)
    msgedit = await client.send_message(
        chat_id=message.chat.id, 
        text=f"""
<b>{symbol} Gateway: TapGateway CCN </b> (/lol) 
<b>{symbol} Card: <code>{cc}|{mes}|{ano}|{cvv}</code></b>
<b>{symbol} Processing Please Wait... (🟡)</b>
<b>{symbol} Took: {taken2}</b>
    """, 
    reply_to_message_id=message.id
    )

    status = "Unknown"
    response = "Error desconocido"
    taken_total = 0  

    # Contador de reintentos
    retries = 0
    max_retries = 3
    start_time_total = time.time()
    ip_info = proxy_x()

    while retries < max_retries:
        try:
            start_time = time.time()
            status, response = await pene(cc, mes, ano, cvv, await ProxyRandom())
            taken_retry = round(time.time() - start_time, 2)
            taken_total = round(time.time() - start_time_total, 2)
            break

        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries == 1:
            await msgedit.edit_text(
                text=f"""
<b>{symbol} Gateway: TapGateway CCN </b> (/lol) 
<b>{symbol} Card: <code>{cc}|{mes}|{ano}|{cvv}</code></b>
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
        with Database() as db:
            db.remove_credits(userid, 3)
        await msgedit.edit_text(
            text=f"""
<b>{symbol} Gateway: TapGateway CCN </b> (/lol) 
<b>{symbol} Card: <code>{cc}|{mes}|{ano}|{cvv}</code></b>
<b>{symbol} Processing Please Wait... (🟢)</b>
<b>{symbol} Took: {taken2}</b>
            """
        )
        await asyncio.sleep(1)
    elif "declined" in status.lower():
        with Database() as db:
            db.remove_credits(userid, 1)
        await msgedit.edit_text(
            text=f"""
<b>{symbol} Gateway: TapGateway CCN </b> (/lol) 
<b>{symbol} Card: <code>{cc}|{mes}|{ano}|{cvv}</code></b>
<b>{symbol} Processing Please Wait... (🔴)</b>
<b>{symbol} Took: {taken2}</b>
            """
        )
        await asyncio.sleep(1)

    await msgedit.edit_text(
        text=f"""
<b>
{symbol} Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
{symbol} Status: <code>{status}</code>
{symbol} Response: <code>{response}</code>
{symbol} Gateway: TapGateway <code>[CCN]</code>
↯ » Info Killua Database « ↯
{symbol} Bin: <code>{cc[:6]}</code>
{symbol} Type: <code>{resp['brand']}</code> - <code>{resp['level']}</code> - <code>{resp['type']}</code>
{symbol} Bank: <code>{resp['bank_name']}</code>
{symbol} Country: <code>{resp['country_name']}</code> - <code>{resp['flag']}</code>
{symbol} Time: <code>{taken_total}</code> 
{symbol} Proxy: <code>{ip_info}</code>
{symbol} Retries: <code>{retries}</code>
{symbol} Req: @{message.from_user.username} [{rol}]
</b> """, 
        reply_markup=keyboard
    )
