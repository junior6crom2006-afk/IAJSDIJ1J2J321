from functions.functions import RandomPene3, get_text_from_pyrogram
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.ve import zuora_adyen
from pyrogram.client import Client
from pyrogram import filters
import asyncio
import re

# Función principal para manejar mensajes
@Client.on_message(filters.command(['ve', 'ny'], PREFIXES))  # type: ignore
@check_gate(command="/ve", gateway_name="Zuora + Adyen [AUTH]", required_credits=0)
async def gate_ve(client, message) -> tuple[str, str]:
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
    errorMessage: str = "Timeout"
    
    while retries < max_retries:
        try:
            errorMessage = str(await zuora_adyen(cc, mes, ano, cvv, await RandomPene3()))
            break
        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries >= max_retries:
            errorMessage = "Max retries exceeded"
            break
        await asyncio.sleep(2)
    
    status = "Declined ❌" if ("fail" in errorMessage.lower() or "error" in errorMessage.lower()) else "Checking Result ⚠️!"

    return status, errorMessage
