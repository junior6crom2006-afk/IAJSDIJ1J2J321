import aiohttp
import json
import time
import re
import asyncio
from pyrogram.client import Client
from pyrogram import filters
from functions.database import Database
from functions.variables import PREFIXES

# Definir encabezados básicos
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive"
}

async def verificar_indicios(session, url):
    resultados = {
        "server": None,
        "protection": set(),
        "captcha": "None detected in URL",
        "security_headers": [],
        "http_status": None
    }

    # Realizar una única solicitud para detectar diferentes mecanismos de seguridad
    try:
        async with session.get(url, headers=HEADERS) as response:  # Agregar encabezados a la solicitud
            headers = response.headers
            content = await response.text()

            # Guardar el primer resultado
            resultados["server"] = headers.get('Server', 'Unknown')
            resultados["http_status"] = response.status

            # Verificaciones de protección
            if 'cf-ray' in headers:
                resultados["protection"].add("Cloudflare")
            if 'Akamai-Gateway' in headers:
                resultados["protection"].add("Akamai")
            if 'X-Akamai-Request-ID' in headers:
                resultados["protection"].add("Akamai Request ID")
            if 'X-Amzn-Trace-Id' in headers:
                resultados["protection"].add("AWS WAF")
            if 'X-Cache' in headers and 'Miss from cloudfront' in headers['X-Cache']:
                resultados["protection"].add("CloudFront")
            if 'X-Sucuri-ID' in headers:
                resultados["protection"].add("Sucuri")
            if 'sucuri-js cookie' in headers:
                resultados["protection"].add("Sucuri")

            # Verificaciones de encabezados de seguridad
            if 'X-Content-Type-Options' in headers:
                resultados["security_headers"].append("X-Content-Type-Options")
            if 'X-Frame-Options' in headers:
                resultados["security_headers"].append("X-Frame-Options")
            if 'X-XSS-Protection' in headers:
                resultados["security_headers"].append("X-XSS-Protection")
            if 'Content-Security-Policy' in headers:
                resultados["security_headers"].append("Content-Security-Policy")
            if 'Strict-Transport-Security' in headers:
                resultados["security_headers"].append("Strict-Transport-Security")
            if 'Referrer-Policy' in headers:
                resultados["security_headers"].append("Referrer-Policy")
            if 'Permissions-Policy' in headers:
                resultados["security_headers"].append("Permissions-Policy")

            # Verificaciones de CAPTCHA
            if 'geocaptcha' in content.lower():
                resultados["protection"].add("Geocaptcha")
            if 'grecaptcha-badge' in content.lower():
                resultados["protection"].add("Google ReCaptcha")
            if 'https://hcaptcha.com/1/api.js' in content:
                resultados["protection"].add("hCaptcha")

            # Detección de Turnstile de Cloudflare
            if 'Turnstile' in content:
                resultados["protection"].add("Cloudflare Turnstile detected")

            # Detección de "Just a Moment"
            if 'Just a moment' in content:
                resultados["protection"].add("Cloudflare Just a Moment detected")

            # Verificación de protección contra bots
            if re.search(r'(?i)bot|scraper|crawler', content):
                resultados["security_headers"].append("Indication of bot protection detected in content.")

    except Exception as e:
        print(f"Error en la solicitud: {e}")

    return resultados

async def revisar_seguridad(url):
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        try:
            resultados = await asyncio.wait_for(verificar_indicios(session, url), timeout=5)
        except asyncio.TimeoutError:
            execution_time = time.time() - start_time
            return {
                "status": "error",
                "error_message": f"Request timed out after {round(execution_time, 3)} seconds.",
                "time": round(execution_time, 3)
            }

    execution_time = time.time() - start_time

    response_json = {
        "status": "success",
        "details": {
            "url": url,
            "protection": ", ".join(resultados["protection"]) if resultados["protection"] else "None found",
            "server_name": resultados["server"],
            "http_code": resultados["http_status"],
        },
        "time": round(execution_time, 3),
        "author": "@tocandotee"
    }

    return response_json

@Client.on_message(filters.command(['site'], PREFIXES)) #type: ignore
async def site_command(client, message):
    if len(message.command) < 2:
        return await message.reply("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Formato: <code>/site {url}</code>")

    url = message.command[1]

    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    with Database() as db:
        userid = message.from_user.id
        # Verificar si el usuario es premium
        if not db.is_premium(userid):
            return await message.reply("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No eres premium. Contacta a @tocandotee")

    # Llamar a la función de revisión de seguridad
    response = await revisar_seguridad(url)

    if response.get("status") == "error":
        await message.edit(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒{response['error_message']}")
    else:
        # Enviar la respuesta como JSON formateado
        json_response = json.dumps(response, indent=4, ensure_ascii=False)
        await message.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒{json_response}", reply_to_message_id=message.id)
