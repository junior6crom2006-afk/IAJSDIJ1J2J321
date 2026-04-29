from functions.functions import ProxyRandom
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.recurly3 import recurly3
from pyrogram.client import Client
from pyrogram import filters
import asyncio

# Función principal para manejar mensajes
@Client.on_message(filters.command(['rap'], PREFIXES))  # type: ignore
@check_gate(command="/rap", gateway_name="Recurly CCN", required_credits=3)
async def gate_rap(client, message):
    cc, mes, ano, cvv = message.cc, message.mes, message.ano, message.cvv
    
    retries = 0
    max_retries = 3
    while retries < max_retries:
        try:
            status, response = await recurly3(cc, mes, ano, cvv, await ProxyRandom())
            break
        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries >= max_retries:
            status = "Declined ❌"
            response = "Max retries exceeded"
            break
        await asyncio.sleep(2)

    return status, response
