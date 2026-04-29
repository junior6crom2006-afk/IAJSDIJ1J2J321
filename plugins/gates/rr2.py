from functions.functions import ProxyRandom, get_text_from_pyrogram
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.recurly5 import recurlyccn5
from pyrogram.client import Client
from pyrogram import filters
import asyncio
import re

# Función principal para manejar mensajes
@Client.on_message(filters.command(['rr'], PREFIXES)) # type: ignore
@check_gate(command="/rr", gateway_name="Recurly $11 CCN", required_credits=0)
async def gate_rr(client, message):
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
            proxy = await ProxyRandom()
            status, response = await asyncio.to_thread(recurlyccn5, cc, mes, ano, cvv, proxy)
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
