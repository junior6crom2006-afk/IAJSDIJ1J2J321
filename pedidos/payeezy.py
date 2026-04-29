import requests
import capsolver
import asyncio

async def payeezy():

    web = requests.session()
    req = web.get('https://youthrenewalfund.org/donate-now/')
    cstoken = req.text.split('name="cstoken" value="')[1].split('"/>')[0]
    print(cstoken)
    headers = {
        'accept': '*/*',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_fbp=fb.1.1731492640591.67093909880991642; PHPSESSID=5b400d50226828b90b63f4904634701d; _gid=GA1.2.1945724994.1731814274; _ga_6LVGZRGPTV=GS1.1.1731814273.3.1.1731814540.0.0.0; _ga=GA1.1.1696407287.1731492641',
        'origin': 'https://youthrenewalfund.org',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://youthrenewalfund.org/donate-now/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'cstoken': cstoken,
        'fname': 'Sebastian',
        'lname': 'Gutierrez',
        'email': 'scarlatmario4@tiktok.tf',
        'phone': '5059947000',
        'street': '103-105 Central Ave',
        'city': 'Orange',
        'state': 'NJ',
        'zip': '07050-3824',
        'amount': 'other',
        'other': '20',
        'donate_ack[]': 'Email',
        'message': '',
        'sentmail': 'sent',
        'x_show_form': 'PAYMENT_FORM',
    }

    req1 = web.post('https://youthrenewalfund.org/wp-content/themes/wp-pray-child/proc.php',headers=headers,data=data)
    print(req1.text)

if __name__ == '__main__':
    asyncio.run(payeezy())
