import requests, uuid

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
        'accept-language': 'es-ES,es;q=0.6',
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
        # 'cookie': 'donationExit=true; SessionKeyCookie=; dy_form_url=https://act.audubon.org/a/donate; _dyjsession=cs87vmvbbw3cq0pl9qhgd3imfehlgu0u; DY_ea_form_exit=1; dy_frequency=0; _dy_soct=1777166427!!cs87vmvbbw3cq0pl9qhgd3imfehlgu0u~3342176.-48; dy_amount=100',
    }

    response = session.get('https://act.audubon.org/a/donate', headers=headers).text

    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.6',
        'cache-control': 'max-age=0',
        'if-none-match': 'W/"95-hLw66Y0Ej5LpWaLMPSFuj3bHbSw"',
        'origin': 'https://act.audubon.org',
        'priority': 'u=1, i',
        'referer': 'https://act.audubon.org/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-storage-access': 'none',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    params = {
        'tokenPool': 'Paragon',
    }

    response = session.get('https://fastaction.ngpvan.com/api/v3/profile', params=params, headers=headers).text

    sessionid = find_between(response, '"fastActionSessionId":"', '"')


    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es-ES,es;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://js.verygoodvault.com',
        'priority': 'u=1, i',
        'referer': 'https://js.verygoodvault.com/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'vgs-client': 'source=vgs-collect&medium=vgs-collect&content=2.18.4&dataHashIndex=1&randIdentifier=1777166529555&vgsCollectSessionId=31fceb6d-3ade-4e66-bc91-69ecf9808bea&tr=default',
    }

    json_data = {
        'Account': '4266841804356051',
        'ExpirationDate': {
            'ExpirationMonth': '05',
            'ExpirationYear': '30',
        },
    }

    response = session.post('https://tntw1pznlam.live.verygoodproxy.com/post', headers=headers, json=json_data).json()

    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://act.audubon.org',
        'priority': 'u=1, i',
        'referer': 'https://act.audubon.org/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-storage-access': 'none',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    data = {
        'ProcessingCurrency': 'USD',
        'SmsSubscribeMobilePhone': 'true',
        'designationName': 'National Audubon Society',
        'SelectedFrequency': '0',
        'Amount': '5.00',
        'IsRecurring': 'false',
        'PaymentMethod': 'creditcard',
        'FirstName': 'Oklahoma',
        'LastName': 'Evan Hicks',
        'AddressLine1': 'Eason Rd 5460',
        'PostalCode': '55573',
        'City': 'Phoenix',
        'StateProvince': 'CT',
        'EmailAddress': 'example@gmail.com',
        'MobilePhoneCountryCode': 'us',
        'MobilePhoneInternationalDialingPrefix': '1',
        'MobilePhone': '9497674837',
        'YesSignMeUpForUpdatesForBinder': 'true',
        'Interest_4353230': 'false',
        'Interest_4332347': 'false',
        'Interest_4332345': 'false',
        'Interest_4332349': 'false',
        'Interest_4332351': 'false',
        'Interest_4352435': 'false',
        'Interest_4332353': 'false',
        'Interest_4349160': 'false',
        'Interest_4352227': 'false',
        'Interest_4352221': 'false',
        'Interest_4332355': 'false',
        'Interest_4352193': 'false',
        'Interest_4352025': 'false',
        'Interest_4332357': 'false',
        'Interest_4332359': 'false',
        'Interest_4332375': 'false',
        'Interest_4351318': 'false',
        'Interest_4337974': 'false',
        'Interest_4345009': 'false',
        'Interest_4356205': 'false',
        'Interest_4351051': 'false',
        'Interest_4332383': 'false',
        'Interest_5157143': 'false',
        'Interest_4879166': 'false',
        'Interest_4353233': 'false',
        'Interest_4354348': 'false',
        'Interest_4355488': 'false',
        'Interest_4333728': 'false',
        'Interest_4358917': 'false',
        'Interest_4352438': 'false',
        'Interest_4347561': 'false',
        'Interest_4349163': 'false',
        'Interest_4352226': 'false',
        'Interest_4352225': 'false',
        'Interest_4358628': 'false',
        'Interest_4352195': 'false',
        'Interest_4352211': 'false',
        'Interest_4352027': 'false',
        'Interest_4343238': 'false',
        'Interest_4343240': 'false',
        'Interest_4343241': 'false',
        'Interest_4351321': 'false',
        'Interest_4340411': 'false',
        'Interest_4354630': 'false',
        'Interest_4356204': 'false',
        'Interest_4351054': 'false',
        'Interest_4343239': 'false',
        'Account': '4266841804356051',
        'ExpirationMonth': '05',
        'ExpirationYear': '30',
        'RedactedAccount': '4266841804356051',
        'RedactedExpirationMonth': '05',
        'RedactedExpirationYear': '30',
        'FormVersion': '2/27/2026 2:42:04 PM|4/21/2026 11:24:59 AM',
        'type': 'ContributionForm',
        'FormSessionId': str(uuid.uuid4()),
        'ClientSubmissionId': str(uuid.uuid4()),
        'BrowserName': 'chrome',
        'DeviceType': 'desktop',
        'MarketSource': 'digital-fund-audubonweb-x',
        'autoCreateAccount': 'true',
        'fastActionSessionId': f'{sessionid}$f',
        'endpoint': 'https://secure.everyaction.com/v2/Forms/QUPul7FoFk2LGYLtNaWzXA2',
        'XFromApp': 'ActionTag',
        'ActionTagBaseUrl': 'https://static.everyaction.com/ea-actiontag/',
    }

    response = session.post('https://secure.everyaction.com/v2/Forms/QUPul7FoFk2LGYLtNaWzXA2', headers=headers, data=data).text
    mensage = find_between(response, '"severity":"Critical","text":"', '"')

    print(mensage)


main()