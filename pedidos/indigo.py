import requests
import random
import string


def random_email() -> str:
    return (
        "".join(random.choice(string.ascii_letters) for x in range(15))
    ) + "@gmail.com"

email = random_email()

web = requests.session()


headers = {
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0NDE2MTkiLCJhcCI6IjExMDMxMjYxMTgiLCJpZCI6IjE4NzJlZjBhNGE5MzdkMjkiLCJ0ciI6IjZkYTk1M2I1ZDJhZGExZmI0ODI0MTMxZTk5NjFkMDUwIiwidGkiOjE3MzEzODY2MTU1MzgsInRrIjoiNTE3MTcwIn19',
    'origin': 'https://www.indigo.ca',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.indigo.ca/en-ca/gift-card/9781773937274.html/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-6da953b5d2ada1fb4824131e9961d050-1872ef0a4a937d29-01',
    'tracestate': '517170@nr=0-1-3441619-1103126118-1872ef0a4a937d29----1731386615538',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'isGiftCard': 'true',
    'pid': '9781773937274',
    'quantity': '1',
    'purchaseValue': '5',
    'sender': 'sadas',
    'recipient': 'asdasd',
    'recipientEmail': 'scarlatmario4@tiktok.tf',
    'giftMessage': 'sad ad ',
}

req1 = web.post('https://www.indigo.ca/on/demandware.store/Sites-Indigo-Site/en_CA/Cart-AddProduct',headers=headers,data=data,)

req2 = web.get('https://www.indigo.ca/en-ca/cart', headers=headers)

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.indigo.ca/en-ca/cart',
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

req3 = web.get('https://www.indigo.ca/en-ca/checkout', headers=headers)
csrf_token = req3.text.split('name="csrf_token" value="')[1].split('"')[0]
shipment_uuid = req3.text.split('name="originalShipmentUUID" value="')[1].split('"')[0]
print(csrf_token)
headers = {
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0NDE2MTkiLCJhcCI6IjExMDMxMjYxMTgiLCJpZCI6IjliZDRkYWJjMTYyNjkwOTYiLCJ0ciI6ImQwYjcyMzM5NzlmZWE4MGZkZWIwYmVjMWEzOWQ0M2MwIiwidGkiOjE3MzEzODY3OTgxMDEsInRrIjoiNTE3MTcwIn19',
    'origin': 'https://www.indigo.ca',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.indigo.ca/en-ca/checkout?stage=shipping',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-d0b7233979fea80fdeb0bec1a39d43c0-9bd4dabc16269096-01',
    'tracestate': '517170@nr=0-1-3441619-1103126118-9bd4dabc16269096----1731386798101',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'originalShipmentUUID': shipment_uuid,
    'shipmentUUID': shipment_uuid,
    'shipmentSelector': 'new',
    'dwfrm_shipping_shippingAddress_addressFields_email': email,
    'dwfrm_shipping_shippingAddress_giftMessage': '',
    'csrf_token': csrf_token,
}

req4 = web.post('https://www.indigo.ca/on/demandware.store/Sites-Indigo-Site/en_CA/CheckoutShippingServices-SubmitShipping',headers=headers,data=data,)

headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www3.moneris.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'input_data': '4678515007850787',
    'input_exp': '0429',
    'input_cvd': '333',
    'hpt_id': 'htOR6FSZO8YFCJT',
    'hpt_ticket': 'tt1731386911KYMm5pXVNF',
    'doTokenize': 'true',
}

req5 = web.post('https://www3.moneris.com/HPPtoken/request.php', headers=headers, data=data)
print(req5.text)