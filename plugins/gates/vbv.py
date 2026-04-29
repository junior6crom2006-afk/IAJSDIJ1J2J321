from functions.functions import ProxyRandom, get_text_from_pyrogram
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.b3vbv import b3vbv
from pyrogram import Client, filters
import asyncio
import re

# Función principal para manejar mensajes
@Client.on_message(filters.command(['vbv'], PREFIXES))
@check_gate(command="/vbv", gateway_name="Braintree VBV", required_credits=0)
async def gate_vbv(client, message):
    try:
        text = await get_text_from_pyrogram(message, no_command=True)
        parts = re.findall(r'\d+', text)
        if len(parts) < 4:
            return await message.reply("❌ Formato: CC|MES|ANO|CVV", reply_to_message_id=message.id)
        cc, mes, ano, cvv = parts[0], parts[1], parts[2], parts[3]
    except Exception as e:
        return await message.reply(f"❌ Error: {str(e)}", reply_to_message_id=message.id)
    
    retries = 0
    max_retries = 3
    while retries < max_retries:
        try:
            status, response = b3vbv(cc, mes, ano, cvv, await ProxyRandom())
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
