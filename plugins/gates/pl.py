from functions.functions import bright_data_proxy
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.b3gateavs import b3gateavs
from pyrogram.client import Client
from pyrogram import filters
import asyncio

# Función principal para manejar mensajes
@Client.on_message(filters.command(['pl'], PREFIXES)) # type: ignore
@check_gate(command="/pl", gateway_name="Gateway", required_credits=0)
async def gate_pl(client, message):
    cc, mes, ano, cvv = message.cc, message.mes, message.ano, message.cvv
    
    retries = 0
    max_retries = 3
    while retries < max_retries:
        try:
            status, response = await b3gateavs(cc, mes, ano, cvv, bright_data_proxy(for_aiohttp=True))
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
