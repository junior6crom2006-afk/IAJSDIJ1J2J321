import re
from random import randint
import time
import string 
import random
import aiohttp
import asyncio


def clean_text(text):
    text_cleaned = " ".join(re.sub(r"<.*?>|\n", " ", text).split())
    return text_cleaned

def random_email() -> str:
    return (
        "".join(random.choice(string.ascii_letters) for x in range(15))
    ) + "@gmail.com"

def find_between(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None  

from datetime import datetime
import urllib.parse

def generar_fecha_hora():
    fecha_hora_actual = datetime.now()
    fecha_hora_formateada = fecha_hora_actual.strftime('%Y-%m-%d+%H:%M:%S')
    fecha_hora_codificada = urllib.parse.quote(fecha_hora_formateada)
    return fecha_hora_codificada

fecha_hora_generada = generar_fecha_hora()
mail = random_email()

cc = "4271783845979744"
mes = "01"
ano_modificado = "26"
cvv = "251"
    
async def main():
    async with aiohttp.ClientSession() as session:
        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'dwac_0f076b3f9ccac72360fae64879=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo%3D|dw-only|||CAD|false|Etc%2FGMT%2D5|true; cqcid=bcrOZsCaSfXzkCY91XLI2o5tVk; cquid=||; sid=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo; dwanonymous_b5bceefea2182acea02b5269de6a14d9=bcrOZsCaSfXzkCY91XLI2o5tVk; __cq_dnt=0; dw_dnt=0; dwsid=ywFykM0IIM-p7m6qYPGzmX-kqhtBF0uPQ7u4PQ1vXgSUDNYfK31bqC7Quve8G9ef-JNWhL1IWijSzpdfGQr7-Q==; _gcl_au=1.1.1957434750.1722700261; _ga=GA1.1.898551656.1722700261; _fbp=fb.1.1722700261759.241625233546480700; _hjSession_3849731=eyJpZCI6IjcyOTdhMDlhLTgzMDctNDUyYS05YWFlLWI0NTc0NDA2ZjA2ZCIsImMiOjE3MjI3MDAyNjE5NDIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __cq_uuid=bcrOZsCaSfXzkCY91XLI2o5tVk; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __kla_id=eyJjaWQiOiJaVEpqTm1GaE0yRXRZbUV5T1MwME9EUTBMVGc0WWpJdFpqTmpNamM0TXpKbU9HWTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjI3MDAyNjEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1vZGVjaG9jLmNhLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyMjcwMDM2MCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cubW9kZWNob2MuY2EvIn19; _ga_4G9RQHE7QG=GS1.1.1722700261.1.1.1722700359.59.0.0; _hjSessionUser_3849731=eyJpZCI6IjJlZGJhY2ZiLTYwMDQtNWNlMC1hMjNjLWFmYTQyYzNmYTM1NCIsImNyZWF0ZWQiOjE3MjI3MDAyNjE5NDEsImV4aXN0aW5nIjp0cnVlfQ==; __cq_bc=%7B%22bjvk-mode_choc_ca%22%3A%5B%7B%22id%22%3A%22226731%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22226731_600%22%7D%5D%7D',
            'origin': 'https://www.modechoc.ca',
            'priority': 'u=1, i',
            'referer': 'https://www.modechoc.ca/fr/products/fille/ado-fille/vetements/t-shirts-et-camisoles/manches-courtes/t-shirt-court-imprime-226731_600.html',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'pid': '10990811',
            'quantity': '1',
            'options': '[]',
        }

        async with session.post(
                'https://www.modechoc.ca/on/demandware.store/Sites-mode_choc_ca-Site/fr_CA/Cart-AddProduct',
                headers=headers,
                data=data) as response:
            r1_text = await response.text()

        headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-419,es;q=0.9',
                # 'cookie': 'dwac_0f076b3f9ccac72360fae64879=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo%3D|dw-only|||CAD|false|Etc%2FGMT%2D5|true; cqcid=bcrOZsCaSfXzkCY91XLI2o5tVk; cquid=||; sid=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo; dwanonymous_b5bceefea2182acea02b5269de6a14d9=bcrOZsCaSfXzkCY91XLI2o5tVk; __cq_dnt=0; dw_dnt=0; dwsid=ywFykM0IIM-p7m6qYPGzmX-kqhtBF0uPQ7u4PQ1vXgSUDNYfK31bqC7Quve8G9ef-JNWhL1IWijSzpdfGQr7-Q==; _gcl_au=1.1.1957434750.1722700261; _ga=GA1.1.898551656.1722700261; _fbp=fb.1.1722700261759.241625233546480700; _hjSession_3849731=eyJpZCI6IjcyOTdhMDlhLTgzMDctNDUyYS05YWFlLWI0NTc0NDA2ZjA2ZCIsImMiOjE3MjI3MDAyNjE5NDIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __cq_uuid=bcrOZsCaSfXzkCY91XLI2o5tVk; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; __kla_id=eyJjaWQiOiJaVEpqTm1GaE0yRXRZbUV5T1MwME9EUTBMVGc0WWpJdFpqTmpNamM0TXpKbU9HWTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjI3MDAyNjEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1vZGVjaG9jLmNhLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyMjcwMDM2MCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cubW9kZWNob2MuY2EvIn19; _ga_4G9RQHE7QG=GS1.1.1722700261.1.1.1722700359.59.0.0; _hjSessionUser_3849731=eyJpZCI6IjJlZGJhY2ZiLTYwMDQtNWNlMC1hMjNjLWFmYTQyYzNmYTM1NCIsImNyZWF0ZWQiOjE3MjI3MDAyNjE5NDEsImV4aXN0aW5nIjp0cnVlfQ==; __cq_bc=%7B%22bjvk-mode_choc_ca%22%3A%5B%7B%22id%22%3A%22226731%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22226731_600%22%7D%5D%7D',
                'priority': 'u=0, i',
                'referer': 'https://www.modechoc.ca/fr/products/fille/ado-fille/vetements/t-shirts-et-camisoles/manches-courtes/t-shirt-court-imprime-226731_600.html',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
            }

        async with session.get('https://www.modechoc.ca/fr/checkout', headers=headers) as response:
            r2_text = await response.text()
            crf = find_between(r2_text, '<input type="hidden" name="csrf_token" value="', '"')
            shipment = find_between(r2_text, '<div data-shipment-uuid="', '"')
            print(f"CSRF: {crf}")
            print(f"SHIPMENT: {shipment}")

        headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'dwac_0f076b3f9ccac72360fae64879=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo%3D|dw-only|||CAD|false|Etc%2FGMT%2D5|true; cqcid=bcrOZsCaSfXzkCY91XLI2o5tVk; cquid=||; sid=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo; dwanonymous_b5bceefea2182acea02b5269de6a14d9=bcrOZsCaSfXzkCY91XLI2o5tVk; __cq_dnt=0; dw_dnt=0; dwsid=ywFykM0IIM-p7m6qYPGzmX-kqhtBF0uPQ7u4PQ1vXgSUDNYfK31bqC7Quve8G9ef-JNWhL1IWijSzpdfGQr7-Q==; _gcl_au=1.1.1957434750.1722700261; _ga=GA1.1.898551656.1722700261; _fbp=fb.1.1722700261759.241625233546480700; _hjSession_3849731=eyJpZCI6IjcyOTdhMDlhLTgzMDctNDUyYS05YWFlLWI0NTc0NDA2ZjA2ZCIsImMiOjE3MjI3MDAyNjE5NDIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __cq_uuid=bcrOZsCaSfXzkCY91XLI2o5tVk; _hjSessionUser_3849731=eyJpZCI6IjJlZGJhY2ZiLTYwMDQtNWNlMC1hMjNjLWFmYTQyYzNmYTM1NCIsImNyZWF0ZWQiOjE3MjI3MDAyNjE5NDEsImV4aXN0aW5nIjp0cnVlfQ==; __cq_bc=%7B%22bjvk-mode_choc_ca%22%3A%5B%7B%22id%22%3A%22226731%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22226731_600%22%7D%5D%7D; __cq_seg=0~0.41!1~0.10!2~0.11!3~0.29!4~0.56!5~-0.37!6~0.13!7~-0.24!8~-0.36!9~-0.27; __kla_id=eyJjaWQiOiJaVEpqTm1GaE0yRXRZbUV5T1MwME9EUTBMVGc0WWpJdFpqTmpNamM0TXpKbU9HWTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjI3MDAyNjEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1vZGVjaG9jLmNhLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyMjcwMDk0OCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cubW9kZWNob2MuY2EvIn19; __cq_seg=0~0.41!1~0.10!2~0.11!3~0.29!4~0.56!5~-0.37!6~0.13!7~-0.24!8~-0.36!9~-0.27; _ga_4G9RQHE7QG=GS1.1.1722700261.1.1.1722700949.57.0.0',
                'origin': 'https://www.modechoc.ca',
                'priority': 'u=1, i',
                'referer': 'https://www.modechoc.ca/fr/checkout?stage=customer',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
            }

        data = {
                'dwfrm_coCustomer_email': 'daw23423234@gmail.com',
                'csrf_token': crf,
            }

        async with session.post(
                'https://www.modechoc.ca/on/demandware.store/Sites-mode_choc_ca-Site/fr_CA/CheckoutServices-SubmitCustomer',
                headers=headers,
                data=data) as response:
            r3_text = await response.text()

        headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'dwac_0f076b3f9ccac72360fae64879=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo%3D|dw-only|||CAD|false|Etc%2FGMT%2D5|true; cqcid=bcrOZsCaSfXzkCY91XLI2o5tVk; cquid=||; sid=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo; dwanonymous_b5bceefea2182acea02b5269de6a14d9=bcrOZsCaSfXzkCY91XLI2o5tVk; __cq_dnt=0; dw_dnt=0; dwsid=ywFykM0IIM-p7m6qYPGzmX-kqhtBF0uPQ7u4PQ1vXgSUDNYfK31bqC7Quve8G9ef-JNWhL1IWijSzpdfGQr7-Q==; _gcl_au=1.1.1957434750.1722700261; _ga=GA1.1.898551656.1722700261; _fbp=fb.1.1722700261759.241625233546480700; _hjSession_3849731=eyJpZCI6IjcyOTdhMDlhLTgzMDctNDUyYS05YWFlLWI0NTc0NDA2ZjA2ZCIsImMiOjE3MjI3MDAyNjE5NDIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __cq_uuid=bcrOZsCaSfXzkCY91XLI2o5tVk; _hjSessionUser_3849731=eyJpZCI6IjJlZGJhY2ZiLTYwMDQtNWNlMC1hMjNjLWFmYTQyYzNmYTM1NCIsImNyZWF0ZWQiOjE3MjI3MDAyNjE5NDEsImV4aXN0aW5nIjp0cnVlfQ==; __cq_bc=%7B%22bjvk-mode_choc_ca%22%3A%5B%7B%22id%22%3A%22226731%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22226731_600%22%7D%5D%7D; __cq_seg=0~0.41!1~0.10!2~0.11!3~0.29!4~0.56!5~-0.37!6~0.13!7~-0.24!8~-0.36!9~-0.27; __kla_id=eyJjaWQiOiJaVEpqTm1GaE0yRXRZbUV5T1MwME9EUTBMVGc0WWpJdFpqTmpNamM0TXpKbU9HWTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjI3MDAyNjEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1vZGVjaG9jLmNhLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyMjcwMDk4NCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cubW9kZWNob2MuY2EvIn0sIiRleGNoYW5nZV9pZCI6IjI2bXpSVXl5MFVzZTV6clUyMlB4VTAxUUIzcUtVcUU1SUpHQWV0TXBwTkEuVmVmd3ZaIn0=; _ga_4G9RQHE7QG=GS1.1.1722700261.1.1.1722701227.60.0.0',
                'origin': 'https://www.modechoc.ca',
                'priority': 'u=1, i',
                'referer': 'https://www.modechoc.ca/fr/checkout?stage=shipping',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
            }

        data = {
                'originalShipmentUUID': shipment,
                'shipmentUUID': shipment,
                'storeId': '',
                'dwfrm_shipping_shippingAddress_shippingMethodID': '001',
                'shipmentSelector': 'new',
                'dwfrm_shipping_shippingAddress_addressFields_firstName': 'juan ',
                'dwfrm_shipping_shippingAddress_addressFields_lastName': 'perez',
                'dwfrm_shipping_shippingAddress_addressFields_address1': '399 5 rg de Milton',
                'dwfrm_shipping_shippingAddress_addressFields_address2': '',
                'dwfrm_shipping_shippingAddress_addressFields_country': 'CA',
                'dwfrm_shipping_shippingAddress_addressFields_states_stateCode': 'QC',
                'dwfrm_shipping_shippingAddress_addressFields_city': 'Roxton Pond',
                'dwfrm_shipping_shippingAddress_addressFields_postalCode': 'J0E 1Z0',
                'dwfrm_shipping_shippingAddress_addressFields_phone': '4503611524',
                'csrf_token': crf,
            }

        async with session.post(
                'https://www.modechoc.ca/on/demandware.store/Sites-mode_choc_ca-Site/fr_CA/CheckoutShippingServices-SubmitShipping',
                headers=headers,
                data=data) as response:
            r4_text = await response.text()

        headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'dwac_0f076b3f9ccac72360fae64879=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo%3D|dw-only|||CAD|false|Etc%2FGMT%2D5|true; cqcid=bcrOZsCaSfXzkCY91XLI2o5tVk; cquid=||; sid=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo; dwanonymous_b5bceefea2182acea02b5269de6a14d9=bcrOZsCaSfXzkCY91XLI2o5tVk; __cq_dnt=0; dw_dnt=0; dwsid=ywFykM0IIM-p7m6qYPGzmX-kqhtBF0uPQ7u4PQ1vXgSUDNYfK31bqC7Quve8G9ef-JNWhL1IWijSzpdfGQr7-Q==; _gcl_au=1.1.1957434750.1722700261; _ga=GA1.1.898551656.1722700261; _fbp=fb.1.1722700261759.241625233546480700; _hjSession_3849731=eyJpZCI6IjcyOTdhMDlhLTgzMDctNDUyYS05YWFlLWI0NTc0NDA2ZjA2ZCIsImMiOjE3MjI3MDAyNjE5NDIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __cq_uuid=bcrOZsCaSfXzkCY91XLI2o5tVk; _hjSessionUser_3849731=eyJpZCI6IjJlZGJhY2ZiLTYwMDQtNWNlMC1hMjNjLWFmYTQyYzNmYTM1NCIsImNyZWF0ZWQiOjE3MjI3MDAyNjE5NDEsImV4aXN0aW5nIjp0cnVlfQ==; __cq_bc=%7B%22bjvk-mode_choc_ca%22%3A%5B%7B%22id%22%3A%22226731%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22226731_600%22%7D%5D%7D; __cq_seg=0~0.41!1~0.10!2~0.11!3~0.29!4~0.56!5~-0.37!6~0.13!7~-0.24!8~-0.36!9~-0.27; __kla_id=eyJjaWQiOiJaVEpqTm1GaE0yRXRZbUV5T1MwME9EUTBMVGc0WWpJdFpqTmpNamM0TXpKbU9HWTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjI3MDAyNjEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1vZGVjaG9jLmNhLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyMjcwMDk4NCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cubW9kZWNob2MuY2EvIn0sIiRleGNoYW5nZV9pZCI6IjI2bXpSVXl5MFVzZTV6clUyMlB4VTAxUUIzcUtVcUU1SUpHQWV0TXBwTkEuVmVmd3ZaIn0=; _ga_4G9RQHE7QG=GS1.1.1722700261.1.1.1722701243.44.0.0',
                'origin': 'https://www.modechoc.ca',
                'priority': 'u=1, i',
                'referer': 'https://www.modechoc.ca/fr/checkout?stage=payment',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
            }

        data = {
                'addressSelector': shipment,
                'dwfrm_billing_addressFields_firstName': 'juan',
                'dwfrm_billing_addressFields_lastName': 'perez',
                'dwfrm_billing_addressFields_address1': '399 5 rg de Milton',
                'dwfrm_billing_addressFields_address2': '',
                'dwfrm_billing_addressFields_country': 'CA',
                'dwfrm_billing_addressFields_states_stateCode': 'QC',
                'dwfrm_billing_addressFields_city': 'Roxton Pond',
                'dwfrm_billing_addressFields_postalCode': 'J0E 1Z0',
                'csrf_token': crf,
                'localizedNewAddressTitle': 'Nouvelle adresse',
                'dwfrm_billing_contactInfoFields_phone': '4503611524',
                'dwfrm_billing_paymentMethod': 'MONERIS_PAYMENT',
            }

        async with session.post(
                'https://www.modechoc.ca/on/demandware.store/Sites-mode_choc_ca-Site/fr_CA/CheckoutServices-SubmitPayment',
                headers=headers,
                data=data) as response:
            r5_text = await response.text()
        resp2 = r5_text
        ticket = find_between(resp2, '"ticket": "', '"')
        print(F"TICKET: {ticket}")

        headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'es-419,es;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://gateway.moneris.com',
                'Referer': F'https://gateway.moneris.com/chktv2/display/index.php?tck={ticket}',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

        data = {
                'pan': cc,
                'ticket': ticket,
                'action': 'get_card_type',
            }

        async with session.post('https://gateway.moneris.com/chktv2/display/request.php', headers=headers, data=data) as response:
            r6_text = await response.text()

        headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'es-419,es;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://gateway.moneris.com',
                'Referer': f'https://gateway.moneris.com/chktv2/display/index.php?tck={ticket}',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

        data = {
                'ticket': ticket,
                'action': 'validate_transaction',
                '': 'Payer',
                'cardholder': 'juan perez',
                'pan': cc,
                'expiry_date': f'{mes}'f'{ano_modificado}',
                'cvv': cvv,
                'gift_card_entry': '',
                'gift_card_cvv_entry': '',
                'currency_code': 'CAD',
                'wallet_details': '{}',
                'gift_details': '{}',
                'card_data_key': 'new',
            }

        async with session.post('https://gateway.moneris.com/chktv2/display/request.php', headers=headers, data=data) as response:
            r7_text = await response.text()

        headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'es-419,es;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://gateway.moneris.com',
                'Referer': f'https://gateway.moneris.com/chktv2/display/index.php?tck={ticket}',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
                'X-Requested-With': 'XMLHttpRequest',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

        data = {
                'ticket': ticket,
                'action': 'process_transaction',
                '': 'Payer',
                'cardholder': 'juan perez',
                'pan': cc,
                'expiry_date': f'{mes}'f'{ano_modificado}',
                'cvv': cvv,
                'gift_card_entry': '',
                'gift_card_cvv_entry': '',
                'currency_code': 'CAD',
                'wallet_details': '{}',
                'gift_details': '{}',
                'card_data_key': 'new',
            }

        async with session.post('https://gateway.moneris.com/chktv2/display/request.php', headers=headers, data=data) as response:
            r8_text = await response.text()

        headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9',
                # 'content-length': '0',
                # 'cookie': 'dwac_0f076b3f9ccac72360fae64879=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo%3D|dw-only|||CAD|false|Etc%2FGMT%2D5|true; cqcid=bcrOZsCaSfXzkCY91XLI2o5tVk; cquid=||; sid=VdsxsdnhEeJ-b9DhHpQ-OOF-6TpV_nqilDo; dwanonymous_b5bceefea2182acea02b5269de6a14d9=bcrOZsCaSfXzkCY91XLI2o5tVk; __cq_dnt=0; dw_dnt=0; dwsid=ywFykM0IIM-p7m6qYPGzmX-kqhtBF0uPQ7u4PQ1vXgSUDNYfK31bqC7Quve8G9ef-JNWhL1IWijSzpdfGQr7-Q==; _gcl_au=1.1.1957434750.1722700261; _ga=GA1.1.898551656.1722700261; _fbp=fb.1.1722700261759.241625233546480700; _hjSession_3849731=eyJpZCI6IjcyOTdhMDlhLTgzMDctNDUyYS05YWFlLWI0NTc0NDA2ZjA2ZCIsImMiOjE3MjI3MDAyNjE5NDIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; __cq_uuid=bcrOZsCaSfXzkCY91XLI2o5tVk; _hjSessionUser_3849731=eyJpZCI6IjJlZGJhY2ZiLTYwMDQtNWNlMC1hMjNjLWFmYTQyYzNmYTM1NCIsImNyZWF0ZWQiOjE3MjI3MDAyNjE5NDEsImV4aXN0aW5nIjp0cnVlfQ==; __cq_bc=%7B%22bjvk-mode_choc_ca%22%3A%5B%7B%22id%22%3A%22226731%22%2C%22type%22%3A%22vgroup%22%2C%22alt_id%22%3A%22226731_600%22%7D%5D%7D; __cq_seg=0~0.41!1~0.10!2~0.11!3~0.29!4~0.56!5~-0.37!6~0.13!7~-0.24!8~-0.36!9~-0.27; __kla_id=eyJjaWQiOiJaVEpqTm1GaE0yRXRZbUV5T1MwME9EUTBMVGc0WWpJdFpqTmpNamM0TXpKbU9HWTUiLCIkcmVmZXJyZXIiOnsidHMiOjE3MjI3MDAyNjEsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm1vZGVjaG9jLmNhLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcyMjcwMDk4NCwidmFsdWUiOiIiLCJmaXJzdF9wYWdlIjoiaHR0cHM6Ly93d3cubW9kZWNob2MuY2EvIn0sIiRleGNoYW5nZV9pZCI6IjI2bXpSVXl5MFVzZTV6clUyMlB4VTAxUUIzcUtVcUU1SUpHQWV0TXBwTkEuVmVmd3ZaIn0=; _ga_4G9RQHE7QG=GS1.1.1722700261.1.1.1722701375.60.0.0',
                'origin': 'https://www.modechoc.ca',
                'priority': 'u=1, i',
                'referer': 'https://www.modechoc.ca/fr/checkout?stage=placeOrder',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
                'x-requested-with': 'XMLHttpRequest',
            }

        async with session.post(
                'https://www.modechoc.ca/on/demandware.store/Sites-mode_choc_ca-Site/fr_CA/CheckoutServices-PlaceOrder',
                headers=headers) as response:
            r9_text = await response.text()
            error = find_between(r9_text, '"errorMessage": "', '"')
            print(f"RESPONSE: {error}")


if __name__ == '__main__':
    asyncio.run(main())