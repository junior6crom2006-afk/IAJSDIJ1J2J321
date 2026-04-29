from functions.functions import ProxyRandom
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.ka import payflow44
from pyrogram import Client, filters
import asyncio

# Función principal para manejar mensajes
@Client.on_message(filters.command(['ka'], PREFIXES))
@check_gate(command="/ka", gateway_name="Payflow AVS [CHARGED]", required_credits=3)
async def gate_ka(client, message):
    cc, mes, ano, cvv = message.cc, message.mes, message.ano, message.cvv
    
    retries = 0
    max_retries = 3
    avsdata, procvv = "N/A", "N/A"
    
    while retries < max_retries:
        try:
            response, status, procvv, avsdata = await payflow44(cc, mes, ano, cvv, await ProxyRandom())
            break
        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries >= max_retries:
            response = "Declined ❌"
            status = "Max retries exceeded"
            break
        await asyncio.sleep(2)

    # Nota: payflow44 devuelve `response` como el status y `status` como el mensaje (inverso al estandar).
    # Se formatea apropiadamente para el Global Manager (que espera `status, response`).
    formatted_response = f"{status} | AVS: <code>{avsdata}</code> | CVV: <code>{procvv}</code>"
    return response, formatted_response
