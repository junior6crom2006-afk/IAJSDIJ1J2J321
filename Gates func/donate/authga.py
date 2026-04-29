import requests, uuid

def parseX(data, start, end):
    try:
        star = data.index(start) + len(start)
        last = data.index(end, star)
        return data[star:last]
    except ValueError:
        return "None"

def main():

    session = requests.Session()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-ES,es;q=0.7',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://unitedwayhouston.org/get-involved/donate-now/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    response = session.get('https://unitedwayhouston.org/get-involved/donate-now/give-now/', headers=headers).text
    uuidmensaje = parseX(response, "})('", "','")

    headers = {
        'accept': 'application/json',
        'accept-language': 'es-ES,es;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://assets.funraise.io',
        'priority': 'u=1, i',
        'referer': 'https://assets.funraise.io/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    response = session.get('https://platform.funraise.io/api/v2/spreedly/params', headers=headers).text

    tokencc = parseX(response, '"certificateToken":"', '"')
    signature = parseX(response, '"signature":"', '"')


    headers = {
        'accept': 'application/json',
        'accept-language': 'es-ES,es;q=0.7',
        'origin': 'https://assets.funraise.io',
        'priority': 'u=1, i',
        'referer': 'https://assets.funraise.io/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'x-org-id': uuidmensaje,
    }

    params = {
        's': str(uuid.uuid4()),
        'q': 'Eason Rd 5460',
    }

    response = session.get('https://platform.funraise.io/api/v1/address/autocomplete', params=params, headers=headers).text

    sessionid = parseX(response, '{"address":[{"full_address":"5460 Eason Rd, Wade, NC, USA","street_address":"5460 Eason Rd","secondary_address":"Wade, NC, USA","place_id":"', '"')

    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://core.spreedly.com',
        'priority': 'u=1, i',
        'referer': 'https://core.spreedly.com/v1/embedded/number-frame-1.183.html',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-storage-access': 'none',
        'sec-gpc': '1',
        'spreedly-environment-key': 'KvcTOx3FPBgscLs51rjT848DP7p',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    params = {
        'from': 'iframe',
        'v': '1.183',
    }

    json_data = {
        'environment_key': 'KvcTOx3FPBgscLs51rjT848DP7p',
        'nonce': str(uuid.uuid4()),
        'timestamp': '1777157012',
        'certificate_token': tokencc,
        'signature': signature,
        'payment_method': {
            'credit_card': {
                'number': '4266841804356051',
                'verification_value': '170',
                'first_name': 'Oklahoma',
                'last_name': 'Evan Hicks',
                'email': 'example@gmail.com',
                'month': '05',
                'year': '2030',
                'address1': '5460 Eason Road',
                'city': 'Wade',
                'state': 'NC',
                'zip': '28395',
                'country': 'US',
                'phone_number': '9497674837',
            },
        },
    }

    response = session.post(
        'https://core.spreedly.com/v1/payment_methods/restricted.json',
        params=params,
        headers=headers,
        json=json_data,
    ).json()


    headers = {
        'accept': 'application/json',
        'accept-language': 'es-ES,es;q=0.7',
        'content-type': 'application/json; charset=UTF-8',
        'origin': 'https://assets.funraise.io',
        'priority': 'u=1, i',
        'referer': 'https://assets.funraise.io/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'x-org-id': uuidmensaje,
    }

    json_data = {
        'address': '5460 Eason Road Eason Rd 5460',
        'shippingSameAsBilling': True,
        'addressId': f'{sessionid}',
        'addressValue': '5460 Eason Rd, Wade, NC, USA',
        'amount': '0.10',
        'anonymous': False,
        'answers': [
            {
                'question': {
                    'id': '9413',
                },
                'answer': None,
            },
        ],
        'bankAccountHolderType': 'personal',
        'bankAccountNumber': None,
        'bankAccountType': 'checking',
        'bankName': None,
        'bankRoutingNumber': None,
        'baseAmount': '0.10',
        'city': 'Wade',
        'clientUuid': str(uuid.uuid4()),
        'clientId': '66c89516a43d2a8a6c5729aa8800712a',
        'comment': None,
        'company': None,
        'companyId': None,
        'companyMatch': False,
        'country': 'US',
        'currency': 'USD',
        'dcfFeeAmount': '0.00',
        'dedicationEmail': None,
        'dedicationMessage': None,
        'dedicationName': None,
        'dedicationType': None,
        'donationAmount': 0.1,
        'donorCoveredFees': False,
        'donorCoversFeesVersion': 2,
        'email': 'example@gmail.com',
        'emailOptIn': True,
        'employeeEmail': None,
        'firstName': 'Oklahoma',
        'formAllocationId': '14491',
        'formId': 24953,
        'frequency': 'o',
        'hasComment': False,
        'isDedication': False,
        'institutionCategory': None,
        'institutionName': None,
        'intendedAmount': '0.10',
        'lastName': 'Evan Hicks',
        'match': False,
        'operationsTip': True,
        'organizationId': str(uuid.uuid4()),
        'pageId': None,
        'paymentTechnology': 'SPREEDLY',
        'paymentToken': f'{tokencc}',
        'cardType': 'visa',
        'paymentType': 'card',
        'phone': '9497674837',
        'postalCode': '28395',
        'recaptchaResponse': None,
        'recaptchaToken': '0cAFcWeA4q_MIQi4pVw0yE6RptP4aR6a-QB-VX0MuC8zsiqscjhIiOGI9c9xgLhcY2SNed5emIGNg72ijty1_NeD6hPQW1y3xNru88xvgFezkgYIKAlnfIBztgXj4FCzr2x5LfCA0ba0yTzcIETx7D6FmHEq3b4HaW3R7mrHgULWtu3ak2FnSbmnfEnzDF9g9DYmEDnFDMwSA6SwoGIcMyg_lQPO3qqlxiwPpxLxMwllFc044W_2imQa2U_elHRYICUsQYvmX3mgCMMqKgpLFILTzDW0_mHF830PjyGWTH0dDCnUpD4potc2c7KoB_Dq7VCESSCvowzhkm_3N9613GQgzCTOCpO0JIevnHGcge7ogwGCfEwzHKk1VyKJBA0ZAalJ4vpGmq1xSx4KS3kXyotJGD292uleVYS3nnI8fckwW1VhqSFtOPQS3h0EFwYBaXtXMhqtq9WyoUQBBxIZdy08P-z5MKR5MWq1HLBvgpUW1-Id8yFRuqKJDcD3sbF78xUKlRc6T9WkpukjjyqTAGVAJxsTWIBkupJqdbb1VQsL-wQcZaZ0c1-g1XLDXuBPRL4dD_a4N-axXeiNSzg8flll2Wi78VPIjsZvCywUT1KUOyQ6YuvXvX04k1T4BWFYxZY1UUdVvgnFI0Jmpqs0XYF9gaM8C7OuXawiNmu-OSo-ob4wNr3eskHBJ_42QMJkqML2l3fa0UyqFAphMVQcY10NpUJzTBENm_qpM80ExXXx_RwokI0CWv7XZaNJLRt5vPgH62Y1sIGZaOHgh1sr33i1gkQKodjI0aTbh0JQZYO8FGqYPwJQt7-Q42ztENETWjb3ix_LAksEui7tR3hS8aIdSz79L-4n2mKBA4OafJVkKLyavprPKEGi4L94GnzzePY6HvyFLiKnyLtrEts8o0A7hL9jqGDANxy2zMxi_qzyCxruvj_gXG6Gyu1gWeruK_x8GIYruZ082PLWF-nLlixH2oIWMJeN0EYnJUjLA7g11NV1zk2lvLorNAT-qDk5zLPK9nc2GOCvflm4VrsBewtxhjokh_cNm82g',
        'recurring': False,
        'referrer': 'https://unitedwayhouston.org/get-involved/donate-now/',
        'smsOptIn': True,
        'sourceUrl': 'https://unitedwayhouston.org/get-involved/donate-now/give-now/',
        'state': 'NC',
        'storeOrderAmount': '0.00',
        'suffix': None,
        'supportsDonorCoversFees': False,
        'tags': None,
        'tipAmount': '0.00',
        'tipPercent': 3,
        'titlePrefix': None,
        'storeOrderOffers': [],
        'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'utm': None,
        'stripeRadarSessionId': None,
        'softCreditSupporter': {
            'firstName': None,
            'lastName': None,
            'email': None,
            'address': None,
            'city': None,
            'state': None,
            'postalCode': None,
            'country': None,
        },
    }

    response = session.post('https://platform.funraise.io/api/v2/transaction', headers=headers, json=json_data).json()

    idtrasacion = response['id']


    headers = {
        'accept': 'application/json',
        'accept-language': 'es-ES,es;q=0.7',
        'origin': 'https://assets.funraise.io',
        'priority': 'u=1, i',
        'referer': 'https://assets.funraise.io/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    params = {
        'retryAttempt': '2',
    }


    response = session.get(
        'https://platform.funraise.io/api/v2/transaction/' + idtrasacion,
        params=params,
        headers=headers,
    )

    mensage = parseX(response.text, '{"message":"', '"')
    print(mensage)


main()