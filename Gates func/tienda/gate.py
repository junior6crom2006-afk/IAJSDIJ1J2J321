import requests

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
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        # 'cookie': '_vid_t=LVepzSe8AXLFKmTuaiwbA1CuP6I80e8QKUoMIIhH4wehkQuZB7T08+snOTFg15OjjriZgW3eI8/Bxw==; ember_simple_auth-session=%7B%22authenticated%22%3A%7B%7D%7D; ember_simple_auth-session-expiration_time=Session; latestCartHash1372={%22reference%22:%2201be4690-59f7-4d2f-902a-b43b015f0104%22%2C%22grandTotal%22:0%2C%22timeSlotId%22:%229679400e-e977-4aa8-8fab-b39f012f04f7%22%2C%22timeSlotDate%22:%222026-04-30T09:00:00-04:00%22%2C%22fulfillmentMethod%22:%22Pickup%22%2C%22customerId%22:1207883%2C%22version%22:6}; aws-waf-token=a4a59185-0b4f-4d1b-83bd-d6e4c5248070:EQoAh/ueY8shAAAA:iT3sU1pN0cDPJm52hiKvPdbxuI+SjzcsN/3xeD8mp6BuueiHNK3gofrMolglTo/EEj4jETBWrv6zaUpCPshJ6hOjhHhmDI/MGjMkviksD52ezXQ9GizduYaw3ypPzCNs2cN9Z4ocPhJSRrtJ+6hhwIH0Jb95DvXs66ohU7qFtPlMD3fWF0ZIGV1cMNhBVY/inBZqhWswF42wBqzMH8teFWJ+Fg==',
    }

    response = session.get('https://shop.fooddepot.com/online/fooddepot25windyhill/home', headers=headers).text

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'es-ES,es;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://shop.fooddepot.com',
        'priority': 'u=1, i',
        'referer': 'https://shop.fooddepot.com/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'x-app-environment': 'browser',
        'x-app-version': 'v4.19.3',
    }

    json_data = {
        'FirstName': 'Oklahoma',
        'LastName': 'Evan Hicks',
        'Email': 'example@gmail.com',
        'Phone': '9497674837',
        'DateOfBirth': '2000-07-04',
        'LoyaltyMembershipNumber': '',
        'FranchiseId': 406,
        'StoreId': 1372,
        'Password': '@Example1234',
        'ReceiveCommunications': True,
        'ReceiveWeeklySpecials': True,
    }

    response = session.post(
        'https://production-us-1.noq-servers.net/api/v1/application/customer/customers',
        headers=headers,
        json=json_data,
    ).json()

    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.6',
        'origin': 'https://shop.fooddepot.com',
        'priority': 'u=1, i',
        'referer': 'https://shop.fooddepot.com/',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    params = {
        'client': 'browser',
    }

    response = session.get(
        'https://70641926058a.bb81f591.us-east-1.token.awswaf.com/70641926058a/inputs',
        params=params,
        headers=headers,
    ).text

    print(response)

main()