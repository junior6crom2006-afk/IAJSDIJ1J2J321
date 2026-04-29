import asyncio
import httpx
import requests




web = requests.session()

proxies = {
    'http': 'http://mr41753pF1Q:MS2ykJLzdM_country-us@91.239.130.17:44443',
    'https': 'http://mr41753pF1Q:MS2ykJLzdM_country-us@91.239.130.17:44443',
}


headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.milestonebooks.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.milestonebooks.com/item/16-2-42353/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'ajaxRefererTarget': 'product',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = ''

data = {
    'target': 'cart',
    'action': 'add',
    'mode': 'search',
    'product_id': '1826',
    'category_id': '132',
    'returnURL': '/item/16-2-42353/',
    'amount': '1',
}



req1 = web.post('https://www.milestonebooks.com/xcart/', params=params, headers=headers, data=data, proxies=proxies)

params = {
    'target': 'checkout',
}

req2 = web.get('https://www.milestonebooks.com/xcart/cart.php', params=params, headers=headers, proxies=proxies)

form_id = req2.text.split("form_id: '")[1].split("'")[0]
print(form_id)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://www.milestonebooks.com/xcart/cart.php?target=checkout',
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

params = {
    'target': 'checkout',
    'action': 'update_profile',
    'email': '',
    'same_address': '1',
    'xcart_form_id': form_id,
}

req3 = web.get('https://www.milestonebooks.com/xcart/cart.php', params=params, headers=headers, proxies=proxies)

params = {
    'target': 'checkout',
}

req4 = web.get('https://www.milestonebooks.com/xcart/cart.php', params=params, headers=headers, proxies=proxies)


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.milestonebooks.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.milestonebooks.com/xcart/cart.php?target=checkout',
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

params = ''

data = {
    'target': 'checkout',
    'action': 'checkout',
    'xcart_form_id': form_id,
    'returnURL': '/xcart/cart.php?target=checkout',
    'mpx_number': '4758330024053024',
    'mpx_month': '10',
    'mpx_year': '2027',
    'mpx_ccv': '333',
    'notes': '',
    'subscribeToAll': '',
    'pcp_on_approve_data': '',
    'pcp_funding_data': '',
}

req5 = web.post('https://www.milestonebooks.com/xcart/', params=params, headers=headers, data=data, proxies=proxies)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.milestonebooks.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.milestonebooks.com/xcart/?',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'action': 'MilestonePaymentProcess',
}

data = {
    'returnURL': 'https://www.milestonebooks.com/xcart/cart.php?target=payment_return&txn_id_name=transactionID',
    'transactionID': '311862-EBOM',
    'orderNumber': '365962',
    'b_email': 'trpprooite@gmail.com',
    'b_firstname': 'Sebastian',
    'b_lastname': 'Gutierrez',
    'b_phone': '5059947000',
    'b_street': '103-105 Central Avenue',
    'b_city': 'Orange',
    'b_zip': '07050-3824',
    'b_country_code': '840',
    's_firstname': 'Sebastian',
    's_lastname': 'Gutierrez',
    's_phone': '5059947000',
    's_street': '103-105 Central Avenue',
    's_city': 'Orange',
    's_zip': '07050-3824',
    's_country_code': '840',
    'amount': '8.22',
    'mpx_number': '4758330024053024',
    'mpx_month': '10',
    'mpx_year': '2027',
    'mpx_ccv': '333',
}

req6 = web.post('https://www.milestonebooks.com/xcart/XCart.php',params=params,headers=headers,data=data, proxies=proxies)
print(req6.text)