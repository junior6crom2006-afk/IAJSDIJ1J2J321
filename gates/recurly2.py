import requests

web = requests.Session()

headers = {
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://pupbox.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://pupbox.com/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

params = {
    'cmd': 'shop-preview',
    'ctx': 'cart',
}

data = 'country=US&shipping_method=standard&cart[0][id]=442101&cart[0][href]=viv-bubbie-holiday-plaid-bandana&cart[0][qty]=1'

req1 = web.post('https://www.pupbox.com/ajax.php', params=params, headers=headers, data=data)

req2 = web.get('https://pupbox.com/checkout')

headers = {
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://api.recurly.com/js/v1/field.html',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

params = {
    'version': '4.32.2',
    'key': 'ewr1-SVjwyaSF4of0LquOF0PxlF',
    'deviceId': 'tuk9QzzRDnGtWF70',
    'sessionId': 'zjwrIZmNMSeQIEaY',
    'instanceId': 'MAj5XXyUnyixDmFM',
}

req3 = web.get('https://api.recurly.com/js/v1/risk/preflights', params=params, headers=headers)


headers = {
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://api.recurly.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://api.recurly.com/js/v1/field.html',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

data = {
    'first_name': 'Sebastian',
    'last_name': 'Gutierrez',
    'country': 'US',
    'postal_code': '07050-3824',
    'number': '4550271005309706',
    'browser': {
        'color_depth': '24',
        'java_enabled': 'false',
        'language': 'es-ES',
        'referrer_url': 'https://pupbox.com/checkout',
        'screen_height': '1080',
        'screen_width': '1920',
        'time_zone_offset': '420',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    },
    'month': '11',
    'year': '2024',
    'cvv': '',
    'version': '4.32.2',
    'key': 'ewr1-SVjwyaSF4of0LquOF0PxlF',
    'deviceId': 'tuk9QzzRDnGtWF70',
    'sessionId': 'zjwrIZmNMSeQIEaY',
    'instanceId': 'MAj5XXyUnyixDmFM'
}

req4 = web.post('https://api.recurly.com/js/v1/token', headers=headers, data=data)
print(req4.text)