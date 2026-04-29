from functions.functions import ProxyRandom, get_text_from_pyrogram
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.pe import payflow22
from pyrogram.client import Client
from pyrogram import filters
import asyncio
import re

# Función principal para manejar mensajes
@Client.on_message(filters.command(['pe'], PREFIXES)) # type: ignore
@check_gate(command="/pe", gateway_name="Payflow AVS [CHARGED]", required_credits=3)
async def gate_pe(client, message):
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
    avsdata, procvv = "N/A", "N/A"
    
    while retries < max_retries:
        try:
            response, status, procvv, avsdata = await payflow22(cc, mes, ano, cvv, await ProxyRandom())
            break
        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries >= max_retries:
            response = "Declined ❌"
            status = "Max retries exceeded"
            break
        await asyncio.sleep(2)

    formatted_response = f"{status}\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒AVS: <code>{avsdata}</code> - CVV: <code>{procvv}</code>"
    return response, formatted_response
