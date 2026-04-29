from pyrogram import Client, filters
from gates.b3ccn import b3ccn
from functions.functions import GetCC, Symbol, get_bin_info, AntiSpam, ProxyRandom
from functions.database import Database
from functions.variables import PREFIXES
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
import asyncio
import json
import random

def countrys():
    countries = [
        ("US", "🇺🇸"),
        ("AU", "🇦🇺"),
        ("UK", "🇬🇧"), 
        ("ES", "🇪🇸"),
        ("DE", "🇩🇪"),
        ("CA", "🇨🇦"),
        ("FR", "🇫🇷"),
        ("IT", "🇮🇹"),
        ("JP", "🇯🇵"),
        ("BR", "🇧🇷")
    ]
    country, flag = random.choice(countries)
    return f"{country} {flag}"

# Definición del teclado inline
keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Buy", url="https://t.me/tocandotee"),
        InlineKeyboardButton("Channel", url="https://t.me/ZyrexRefes")
    ]
])

# Función principal para manejar mensajes
@Client.on_message(filters.command(['nl'], PREFIXES))
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

    antispam = await AntiSpam(userid, user_info["ANTISPAM"], is_free_user)
    if antispam:
        return await message.reply(f"<b>Hey Carnal !! Vas Muy Rapido, Porfavor Espera {antispam} Segundos Para Hacer El Proximo Checkeo</b>")
    
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
<b>{symbol} Gateway: Braintree 5$ </b> (/nl) 
<b>{symbol} Card: <code>{cc}|{mes}|{ano}|{cvv}</code></b>
<b>{symbol} Processing Please Wait...</b>.
        """, 
        reply_to_message_id=message.id
    )

    # Inicialización de variables antes del bucle de reintentos
    status = "Unknown"
    response = "Error desconocido"
    taken = 0  # Valor inicial por si el bucle falla
    
    # Contador de reintentos
    retries = 0
    max_retries = 3  # Máximo número de reintentos
    start_time_total = time.time()  # Comienza a medir todo el tiempo total

    # Intentos de procesamiento de la tarjeta
    while retries < max_retries:
        try:
            start_time = time.time()  # Reiniciar el cronómetro para cada intento
            status, response = await b3ccn(cc, mes, ano, cvv, await ProxyRandom())
            taken = round(time.time() - start_time_total, 2)  # Tiempo total incluyendo reintentos
            break  # Si el intento fue exitoso, salimos del bucle

        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries == 1:
            await msgedit.edit_text(
                text=f"""
<b>{symbol} Gateway: Braintree 5$ </b> (/nl) 
<b>{symbol} Card: <code>{cc}|{mes}|{ano}|{cvv}</code></b>
<b>{symbol} Processing Please Wait...</b>.
<b>{symbol} Retries: {retries}</b>  [Please Wait..]
                """
            )
        if retries >= max_retries:
            status = "Declined ❌"
            response = "Max retries exceeded"
            taken = round(time.time() - start_time_total, 2)
            break
        await asyncio.sleep(2)  # Espera antes de intentar nuevamente

    # Actualización del mensaje con la respuesta
    await msgedit.edit_text(
        text=f"""
<b>
{symbol} Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
{symbol} Status: <code>{status}</code>
{symbol} Response: <code>{response}</code>
{symbol} Gateway: Braintree <code>[CCN]</code>
↯ » Info Killua Database « ↯
{symbol} Bin: <code>{cc[:6]}</code>
{symbol} Type: <code>{resp['brand']}</code> - <code>{resp['level']}</code> - <code>{resp['type']}</code>
{symbol} Bank: <code>{resp['bank_name']}</code>
{symbol} Country: <code>{resp['country_name']}</code> - <code>{resp['flag']}</code>
{symbol} Time: <code>{taken}</code>
{symbol} Proxy: <code>{random.randint(100, 255)}.x{random.randint(0, 99)}.{random.randint(0, 9)}xx.{random.randint(0, 99)} ✅ </code> <code>[{countrys()}]</code>
{symbol} Retries: <code>{retries}</code>
{symbol} Req: @{message.from_user.username} [{rol}]
       </b> """, 
        reply_markup=keyboard
    )
