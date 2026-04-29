from functions.functions import ProxyRandom
from functions.global_manager import check_gate
from functions.variables import PREFIXES
from gates.stripe_auth import stripeauth
from pyrogram import Client, filters
import asyncio

# Función principal para manejar mensajes
@Client.on_message(filters.command(['ly'], PREFIXES))
@check_gate(command="/ly", gateway_name="Stripe Auth", required_credits=3)
async def gate_ly(client, message):
    cc, mes, ano, cvv = message.cc, message.mes, message.ano, message.cvv
    
    retries = 0
    max_retries = 3
    while retries < max_retries:
        try:
            status, response = await stripeauth(cc, mes, ano, cvv, await ProxyRandom())
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
