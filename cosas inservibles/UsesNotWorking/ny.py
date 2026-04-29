from pyrogram import Client, filters
from gates.ny import unk
from functions.functions import GetCC, Symbol, get_bin_info, AntiSpam, ProxyRandom
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
        InlineKeyboardButton("Channel", url="https://t.me/ZyrexRefes")
    ]
])

# Función principal para manejar mensajes
@Client.on_message(filters.command(['ny'], PREFIXES))
async def gate_ki(client, message):

    symbol = await Symbol()
    with Database() as db:
        userid = message.from_user.id
        # Verificar si el usuario es premium
        if not db.is_premium(userid):
            return await message.reply(f"{symbol} No eres premium. Contacta a @tocandotee")
        
        user_info = db.get_info_user(userid)
        is_free_user = user_info["MEMBERSHIP"].lower() == "free user"
        rol = user_info["RANK"]
        # Verificar créditos del usuario
        credits = user_info.get("CREDITS", 0)
        if credits < 4:
            return await message.reply(
                "<b>Se necesitan más de 2 créditos para poder usar este comando. Si deseas comprar, envía el comando /price para conocer los precios y con quién realizar la compra.</b>",
                reply_markup=keyboard,
                quote=True,
            )

    antispam = await AntiSpam(userid, user_info["ANTISPAM"], is_free_user)
    if antispam:
        return await message.reply(f"<b>[ANTISPAM] ESPERE {antispam}s PARA EL PROXIMO CHECKEO</b>")
    
    # Procesamiento de la tarjeta
    card_details = await GetCC(message.text)
    if not card_details:
        return await message.reply(f"{symbol} <b>Please Enter A Valid Card! ⚠️</b>", quote=True)
    cc, mes, ano, cvv = card_details

    # Deducción de crédito inmediata antes de procesar la información del BIN
    with Database() as db:
        db.remove_credits(userid, 1)  # Deduce 1 crédito inmediatamente después de verificar la tarjeta

    # Procesamiento de la información del BIN
    serie = cc[:6]  # Definir 'serie' como los primeros 6 dígitos de la tarjeta
    resp = await get_bin_info(serie)
    if resp is None:
        return await message.reply("<b>Bin Not Found ⚠️</b>", quote=True)
    
    if message.from_user.id not in [6712112939,5007724193,5740101179,5947286310] and (resp["banned"] or "prepaid" in resp["level"].lower() or "prepaid" in resp["type"].lower()):
        return await message.reply(f"<b>Bin: <code>{resp['bin']}</code>\nBin banned, operation prohibited</b>")
    
    # Envío del mensaje inicial sin incluir el tiempo aún
    msgedit = await client.send_message(
        chat_id=message.chat.id, 
        text=f"""
<b>{symbol} Gateway: Unknown 1$ </b> (/ny) 
<b>{symbol} Card: <code>{cc}|{mes}|{ano}|{cvv}</code></b>
<b>{symbol} Processing Please Wait...</b>.
        """, 
        reply_to_message_id=message.id
    )

    start_time = time.time()  
    response, status = await unk(cc, mes, ano, cvv, await ProxyRandom())
    taken = round(time.time() - start_time, 2)  # Ahora taken tiene un valor definido

    # Actualización del mensaje con la respuesta del gateway y el tiempo de procesamiento
    await msgedit.edit_text(
        text=f"""
<b>
{symbol} Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
{symbol} Status: <code>{response}</code>
{symbol} Response: <code>{status}</code>
{symbol} Gateway: TSYS <code>[CCN / CHARGED]</code>
↯ » Info Killua Database « ↯
{symbol} Bin: <code>{cc[:6]}</code>
{symbol} Type: <code>{resp['brand']}</code> - <code>{resp['level']}</code> - <code>{resp['type']}</code>
{symbol} Bank: <code>{resp['bank_name']}</code>
{symbol} Country: <code>{resp['country_name']}</code> - <code>{resp['flag']}</code>
{symbol} Time: <code>{taken}</code>
{symbol} Proxy: Live!✅
{symbol} Req: @{message.from_user.username} [{rol}]
       </b> """, 
        reply_markup=keyboard
    )
