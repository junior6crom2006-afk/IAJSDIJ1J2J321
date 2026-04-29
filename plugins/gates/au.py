from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
import asyncio
from gates.au import payflowccn1
from functions.functions import ProxyRandom, proxy_x
from functions.database import Database
from functions.variables import PREFIXES
from functions.global_manager import check_gate, keyboard

# Función principal para manejar mensajes
@Client.on_message(filters.command(['au'], PREFIXES))
@check_gate(command="/au", gateway_name="Payflow CCN", required_credits=0)
async def gate_te(client, message):
    cc, mes, ano, cvv = message.cc, message.mes, message.ano, message.cvv

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
