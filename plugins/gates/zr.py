from functions.functions import ProxyRandom
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.CYBERCHASE_CCN import cyberchaseccn
from pyrogram.client import Client
from pyrogram import filters
import asyncio

# Función principal para manejar mensajes
@Client.on_message(filters.command(['zr'], PREFIXES))  # type: ignore
@check_gate(command="/zr", gateway_name="Cybersource + Chase CCN", required_credits=0)
async def gate_zr(client, message):
    cc, mes, ano, cvv = message.cc, message.mes, message.ano, message.cvv
    
    retries = 0
    max_retries = 3
    while retries < max_retries:
        try:
            status, response = await cyberchaseccn(cc, mes, ano, cvv, await ProxyRandom())
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
