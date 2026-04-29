from pyrogram import Client, filters
from gates.bradescarde import bradescard
from functions.functions import GetCC, Symbol, get_bin_info, AntiSpam, ProxyRandomFromFile, proxy_x, Symbol2
from functions.database import Database
from functions.variables import PREFIXES
from functions.gate_manager import GateManager
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from httpx import AsyncClient

from functions.gate_manager import GateManager

import time
import asyncio
import json
import re
from datetime import datetime


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Buy", url="https://t.me/tocandotee"),
        InlineKeyboardButton("Channel", url="https://t.me/ZyrexRefes")
    ]
])


@staticmethod
def get_cc(text: str):
    try:
        input_msg = text.strip()
        input_numbers = re.findall(r'\d+', input_msg)

        current_year = datetime.now().year

        if not input_numbers: 
            return False
            
        cc = input_numbers[0]

        if len(input_numbers) >= 4:
            mes = input_numbers[1]
            ano = input_numbers[2]
            cvv = input_numbers[3]

            if (cc.isdigit() and 14 <= len(cc) <= 16 and
                mes.isdigit() and 1 <= int(mes) <= 12 and
                ano.isdigit() and (current_year <= int(ano) <= 2099 or (21 <= int(ano) <= 99 and len(ano) == 2)) and
                cvv.isdigit() and len(cvv) <= 4):
                if len(ano) == 2:
                    ano = "20" + ano
                return cc, mes, ano, cvv
            else:
                return False
        else:
            return False
        
    except:
        return False


@Client.on_message(filters.command(['bra'], PREFIXES))
async def gate_te(client, message):
    symbol = await Symbol()

    # Extraer los datos de la tarjeta usando get_cc
    cc_data = get_cc(message.text)
    if not cc_data:
        return await message.reply(f"{symbol} <b>Por favor ingresa un número de tarjeta válido! ⚠️</b>", quote=True)

    cc, mes, ano, cvv = cc_data

    # Obtener los primeros 6 dígitos para el BIN
    serie = cc[:6]


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
        return await message.reply(f"<b>Please Wait [<code>{antispam}s</code>] After Checking ⚠️</b>")


    with Database() as db:
        db.remove_credits(userid, 5)  


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
<b>{symbol} Gateway: BradesCard </b> (/bradescard) 
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
    card_data = None

    while retries < max_retries:
        try:
            start_time = time.time()
            try:
                card_data = await bradescard(cc, await ProxyRandomFromFile())
                status = "Approved ✅"
            except Exception as e:
                if "CC No Valida" in str(e):
                    status = "Declined ⚠️ "
                    response = "Card Was Not Accepted"
                else:
                    raise e
            
            taken_retry = round(time.time() - start_time, 2)
            taken_total = round(time.time() - start_time_total, 2)
            break

        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries == 1:
            await msgedit.edit_text(
                text=f"""
<b>{symbol} Gateway: BradesCard </b> (/bradescard) 
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
        try:
            (FechaLimitePago, PagoMinimo, PagoTotal, FechaCorte, DisponibleCompras,
            SaldoTotal, LimiteCredito, CardBalance, limitesMxn, accountnumber,
            fecha_mov, cargo_mov, sitio_mov) = card_data
            
            await msgedit.edit_text(
                text=f"""
<b>
{symbol} Card: <code>{cc}</code>
{symbol} Status: <code>Approved ✅</code>
{symbol} Gateway: Bradescard <code>[INFO]</code>
━━━━━━{symbol}━━━━━━
{symbol} Número De Cuenta: <code>{accountnumber}</code>
━━━━━━{symbol}━━━━━━
{symbol} Fecha Límite: <code>{FechaLimitePago}</code>
{symbol} Pago Mínimo: <code>${PagoMinimo}</code>
{symbol} Pago Total: <code>${PagoTotal}</code>
{symbol} Fecha Corte: <code>{FechaCorte}</code>
{symbol} Disponible: <code>${DisponibleCompras}</code>
{symbol} Saldo Total: <code>${SaldoTotal}</code>
{symbol} Límite Crédito: <code>${LimiteCredito}</code>
{symbol} Balance: <code>${CardBalance}</code>
{symbol} Límite MXN: <code>${limitesMxn}</code>
━━━━━━{symbol}━━━━━━
{symbol} Movimientos:
Fecha: <code>[{fecha_mov}]</code>
Cargo: <code>[${cargo_mov} MXN]</code>
Sitio / Comercio: <code>[{sitio_mov}]</code>
━━━━━━{symbol}━━━━━━
{symbol} Time: <code>{taken_total}</code>
{symbol} Proxy: <code>{ip_info}</code>
{symbol} Retries: <code>{retries}</code>
{symbol} Req: @{message.from_user.username} [{rol}]
</b>""",
                reply_markup=keyboard
            )
        except Exception as e:
            await msgedit.edit_text(
                text=f"""
<b>
{symbol} Card: <code>{cc}</code>
{symbol} Status: <code>Error ⚠️</code>
{symbol} Response: <code>Error processing response</code>
{symbol} Gateway: Bradescard <code>[INFO]</code>

{symbol} Time: <code>{taken_total}</code>
{symbol} Proxy: <code>{ip_info}</code>
{symbol} Retries: <code>{retries}</code>
{symbol} Req: @{message.from_user.username} [{rol}]
</b>""",
                reply_markup=keyboard
            )
    elif "declined" in status.lower():
        await msgedit.edit_text(
            text=f"""
<b>
{symbol} Card: <code>{cc}</code>
{symbol} Status: <code>Error ⚠️</code>
{symbol} Response: <code>Card Was Not Accepted Please Use BradesCard Bin</code>
{symbol} Gateway: Bradescard <code>[INFO]</code>

{symbol} Bin: <code>{cc[:6]}</code>
{symbol} Bank: <code>{resp['bank_name']}</code>
{symbol} Time: <code>{taken_total}</code>
{symbol} Proxy: <code>{ip_info}</code>
{symbol} Retries: <code>{retries}</code>
{symbol} Req: @{message.from_user.username} [{rol}]
</b>""",
            reply_markup=keyboard
        )
        await asyncio.sleep(0.5)


@Client.on_message(filters.command("bra", PREFIXES))
async def mass(client: Client, m: Message):
    # Registrar el gate

    # Verificar estado del gate
    gate_info = GateManager.get_gate_info("/bra")
    symbol = await Symbol()
    if gate_info["estado"] == "OFF":
        return await m.reply_text(f"""<b>Gateway: /bra
{symbol} Status: Apagado
{symbol} Razón: {gate_info['razon'] or 'N/A'}
{symbol} Última Revisión: {gate_info['ultima_revision']}</b>""", reply_to_message_id=m.id)

    # Resto del código original...
