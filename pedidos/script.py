import requests

web = requests.Session()


headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://subscribe.mycentraljersey.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://subscribe.mycentraljersey.com/subscribe/?productId=1200095847&genesysSourceCode=W&sourceCode=W&marketId=PCNJ&unitNumber=1171&promoCodeOverride=FR&gps-source=CPMASTHEAD&cards=UserRegistration&expandedSourceCode=CPMASTHEAD&productUsageType=Special%20Offer&submarketId=EBR&rateCode=FR&publicationCode=HN&fodCode=SO&form-name=UserRegistration',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'accountNumber': '0',
    'fireflyUserId': '1222763286',
    'unitNumber': '1171',
    'publicationCode': 'HN',
    'fodCode': 'SO',
    'rateCode': 'FR',
    'marketId': 'CN',
    'subMarketId': 'EBR',
    'firstName': 'Sebastian',
    'lastName': 'scarlatmario4@tiktok.tf',
}

response = web.post('https://subscribe.mycentraljersey.com/userService/', headers=headers, data=data)


headers = {
    'accept': 'application/vnd.subscriptions.v2',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://subscribe.mycentraljersey.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://subscribe.mycentraljersey.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

data = {
    'form-name': 'CheckoutPrint',
    'cards': 'UserRegistration', 
    'publicationId': '',
    'expandedSourceCode': 'CPMASTHEAD',
    'sourceCode': 'W',
    'productUsageType': 'Special Offer',
    'productId': '1200095847',
    'marketId': 'CN',
    'submarketId': 'EBR',
    'promotionCode': 'FR',
    'publicationCode': 'HN',
    'unitNumber': '1171',
    'fodCode': 'SO',
    'emailConfirm': '',
    'passwordConfirm': '',
    'firstName': 'Sebastian',
    'gender': '',
    'action': '',
    'birthYear': '',
    'lastName': 'scarlatmario4@tiktok.tf',
    'password': '',
    'email': 'scarlatma1232131rio4@tiktok.tf',
    'fireflyUserId': '1222763286',
    'gettax-ready': '',
    'validate-subscription-ready': 'true',
    'addressLine1': '103-105 Central Ave',
    'addressLine2': '',
    'country': 'US',
    'city': 'Orange',
    'stateSelect': 'NJ',
    'state': 'NJ',
    'zipCode': '07050-3824',
    'phone': '5059947000',
    'startDate': '20241122',
    'startDatePhony': 'Friday, November 22, 2024',
    'accountNumber': '0',
    'creditCardNumber': '370194007785051',
    'creditCardExpirationMonth': '1',
    'creditCardExpirationYear': '2026',
    'billingAddressLine1': '103-105 Central Ave',
    'billingAddressLine2': '',
    'billingCountry': 'US',
    'billingCity': 'Orange',
    'billing-stateSelect': 'NJ',
    'billingState': 'NJ',
    'billingZipCode': '07050-3824',
    'billingPhone': '5059947000'
}

req = web.post('https://subscription-self-serve.gannett.com/createSubscription', headers=headers, data=data)
print(req.text)