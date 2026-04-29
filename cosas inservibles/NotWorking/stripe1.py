import requests
from httpx import AsyncClient
import capsolver
import asyncio

capsolver.api_key = "CAP-02DB3E5188C3DDD58C43DCF9B69FE560"

async def payaconnect():
    g_response = (await asyncio.to_thread(lambda: capsolver.solve({
    "type": "ReCaptchaV3TaskProxyLess",
    "websiteKey": '6Lf6MX8bAAAAAI6xsDInJIH8HOMYvsWoB2Zy8GnK',
    "websiteURL": 'https://fanshaweretail.ca',
    })))['gRecaptchaResponse']

    web = requests.session()

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://fanshaweretail.ca',
        'Pragma': 'no-cache',
        'Referer': 'https://fanshaweretail.ca/Item?item=88870040880',
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
        'item': '88870040880',
        'qty': '1',
        'view': 'Json',
        'template': 'Json',
    }

    req1 = web.post('https://fanshaweretail.ca/Basket/ajaxAddItem', headers=headers, data=data)
    res = web.get('https://fanshaweretail.ca/Basket')
    data = {
    'item': '88870005173',
    'qty': '1',
    'view': 'Json',
    'template': 'Json',
    }

    req2 = web.post('https://fanshaweretail.ca/Basket/ajaxAddItem', headers=headers, data=data)
    res1 = web.get('https://fanshaweretail.ca/Checkout/billing')

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'PHPSESSID=dbf6786d03ac245258c51740de8c1214; _ga=GA1.1.2002717569.1731250548; _ga_ZY91F1QDTT=GS1.1.1731250548.1.1.1731251148.0.0.0',
        'Origin': 'https://fanshaweretail.ca',
        'Pragma': 'no-cache',
        'Referer': 'https://fanshaweretail.ca/Checkout/billing',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'order_type': 'p',
        'first_name': 'SEBASTIAN',
        'last_name': 'GUTIERREZ',
        'company': 'HUNTER',
        'email': 'scarlatmario4@tiktok.tf',
        'email_confirm': 'scarlatmario4@tiktok.tf',
        'country': 'UNITED STATES',
        'extra_field': 'Sebastian Gutierrez',
        'address': '103-105 CENTRAL AVENUE',
        'address2': '',
        'city': 'ORANGE',
        'province': 'NJ',
        'province-other': '',
        'postal_code': '07050-3824',
        'daytime_phone1': '505',
        'daytime_phone2': '994',
        'daytime_phone3': '7000',
        'ext': '',
        'fax1': '',
        'fax2': '',
        'fax3': '',
        'submit': 'Continue',
    }

    req3 = web.post('https://fanshaweretail.ca/Checkout/billing',  headers=headers, data=data)
    res = web.get('https://fanshaweretail.ca/Checkout/shipping')
    data = {
    'email': 'scarlatmario4@tiktok.tf',
    'email_confirm': 'scarlatmario4@tiktok.tf',
    'order_type': 'p',
    'first_name': 'SEBASTIAN',
    'last_name': 'GUTIERREZ',
    'company': '',
    'address': '103-105 CENTRAL AVENUE',
    'address2': '',
    'city': 'Halton Hills',
    'country': 'CANADA',
    'province': 'ON',
    'province-other': '',
    'postal_code': 'L9T 2X7',
    'daytime_phone1': '505',
    'daytime_phone2': '994',
    'daytime_phone3': '7000',
    'ext': '',
    'fax1': '',
    'fax2': '',
    'fax3': '',
    'submit': 'Continue',
    }

    req4 = web.post('https://fanshaweretail.ca/Checkout/shipping',  headers=headers, data=data)
    
    data = {
        'action': 'giftcard',
        'special_instructions': '',
    }

    req5 = web.post('https://fanshaweretail.ca/OrderReview',  headers=headers, data=data)
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'PHPSESSID=dbf6786d03ac245258c51740de8c1214; _ga=GA1.1.2002717569.1731250548; _ga_ZY91F1QDTT=GS1.1.1731250548.1.1.1731251381.0.0.0',
        'Origin': 'https://fanshaweretail.ca',
        'Pragma': 'no-cache',
        'Referer': 'https://fanshaweretail.ca/OrderReview',
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
        'token': g_response,
    }

    req6 = web.post('https://fanshaweretail.ca/Checkout/captchavalidation', headers=headers, data=data)
    data = {
        'buyback_register': 'on',
    }

    req7 = web.post('https://fanshaweretail.ca/OrderReview/register',  headers=headers, data=data)
    
    params = {
    'action': 'payment',
    }

    req8 = web.get('https://fanshaweretail.ca/eSolution/secure/exact_payment.php',params=params,headers=headers,)
    print(req8.text)
    with open("exacto.txt", "+w",encoding="utf-8") as u:u.write(req7.text)
asyncio.run(payaconnect())