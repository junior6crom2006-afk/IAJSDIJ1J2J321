import requests
import asyncio
import capsolver

web = requests.Session()


headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'xid=dcd566f7d017c72c54c119f2a3ad6773; RefererCookie=https%3A%2F%2Fstore.parkswest.com%2FeOfficeProducts%2Fproduct.php%3Fproductid%3D66386%26cat%3D154%26page%3D1; store_language=en; vmv=20241116062045',
    'Origin': 'https://store.parkswest.com',
    'Pragma': 'no-cache',
    'Referer': 'https://store.parkswest.com/eOfficeProducts/product.php?productid=56269&cat=28&page=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'mode': 'add',
    'productid': '56269',
    'cat': '28',
    'page': '1',
    'amount': '1',
    'uom_selection': 'EA',
}

req1 = web.post('https://store.parkswest.com/eOfficeProducts/cart.php', headers=headers, data=data)

params = {
    'mode': 'checkout',
}

req2 = web.get('https://store.parkswest.com/eOfficeProducts/cart.php', params=params, headers=headers)