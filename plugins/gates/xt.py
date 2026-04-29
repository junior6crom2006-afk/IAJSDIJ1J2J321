from functions.functions import ProxyRandom, get_text_from_pyrogram
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.b3avs import b3avscvv
from pyrogram.client import Client
from pyrogram import filters
import asyncio
import re

# Función principal para manejar mensajes
@Client.on_message(filters.command(['xt'], PREFIXES))  # type: ignore
@check_gate(command="/xt", gateway_name="Braintree AVS [AUTH]", required_credits=0)
async def gate_xt(client, message):
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
    processor_code, processor_text, cvv_code, avs_postal, network_code = "N/A", "N/A", "N/A", "N/A", "N/A"
    
    while retries < max_retries:
        try:
            status, processor_code, processor_text, cvv_code, avs_postal, avs_street, network_code, network_text = await b3avscvv(cc, mes, ano, cvv, bright_data_proxy(for_aiohttp=True))
            break
        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries >= max_retries:
            status = "Declined ❌"
            processor_text = "Max retries exceeded"
            break
        await asyncio.sleep(2)

    formatted_response = f"{processor_code} {processor_text} ({network_code})\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒AVS: <code>[{avs_postal}]</code> - CVV: <code>[{cvv_code}]</code>"
    return status, formatted_response
