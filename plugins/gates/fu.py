from functions.functions import ProxyRandom
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.fullsteam import fullsteampay
from pyrogram import Client, filters
import asyncio

# Función principal para manejar mensajes
@Client.on_message(filters.command(['fu'], PREFIXES))
@check_gate(command="/fu", gateway_name="Fullsteam [AUTH]", required_credits=3)
async def gate_fu(client, message):
    cc, mes, ano, cvv = message.cc, message.mes, message.ano, message.cvv
    
    retries = 0
    max_retries = 3
    avs, cvv_r = "N/A", "N/A"
    
    while retries < max_retries:
        try:
            status, response, avs, cvv_r = await fullsteampay(cc, mes, ano, cvv, await ProxyRandom())
            break
        except Exception as e:
            retries += 1
            print(f"Retry {retries}/{max_retries} failed: {str(e)}")
            
        if retries >= max_retries:
            status = "Declined ❌"
            response = "Max retries exceeded"
            break
        await asyncio.sleep(2)

    # Inyectamos AVS y CVV dentro de 'response' para que el manager global pueda imprimirlo intacto
    formatted_response = f"{response}\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒AVS: <code>{avs}</code> - CVV: <code>{cvv_r}</code>"
    return status, formatted_response
