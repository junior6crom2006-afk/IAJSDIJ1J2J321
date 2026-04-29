from pyrogram import Client, filters
from functions.gate_manager import GateManager
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
import asyncio
import re
from gates.au import payflowccn1
from functions.functions import ProxyRandom, proxy_x, get_text_from_pyrogram, Symbol
from functions.database import Database
from functions.variables import PREFIXES
from functions.global_manager import check_gate, keyboard

# Función principal para manejar mensajes
@Client.on_message(filters.command(['au'], PREFIXES))
@check_gate(command="/au", gateway_name="Payflow CCN", required_credits=0)
async def gate_te(client, message):
    # Registrar el gate
    GateManager.register_gate(
        comando=f"/{message.command[0]}",
        nombre="Gateway Name",
        tipo="CCN",  # Opciones: CCN, AUTH, CHARGED
        premium=True
    )
    try:
        text = await get_text_from_pyrogram(message, no_command=True)
        parts = re.findall(r'\d+', text)
        
        if len(parts) < 4:
            return await message.reply("❌ Formato: CC|MES|ANO|CVV", reply_to_message_id=message.id)
        
        cc, mes, ano, cvv = parts[0], parts[1], parts[2], parts[3]
        
        if not all([cc.isdigit() and len(cc) in [14,15,16], mes.isdigit() and 1 <= int(mes) <= 12, 
                    ano.isdigit() and len(ano) in [2,4], cvv.isdigit() and len(cvv) <= 4]):
            return await message.reply("❌ Datos inválidos", reply_to_message_id=message.id)
            
    except Exception as e:
        return await message.reply(f"❌ Error: {str(e)}", reply_to_message_id=message.id)

    # Contador de reintentos
    retries = 0
    max_retries = 3
    # Intentos de procesamiento de la tarjeta
    while retries < max_retries:
        try:
            status, response = await payflowccn1(cc, mes, ano, cvv, await ProxyRandom())
            break
        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries >= max_retries:
            status = "Declined ❌"
            response = "Max retries exceeded"
            break
        await asyncio.sleep(2)

    # Retornamos status y response (El Global Manager hace todo el trabajo visual restante)
    return status, response
