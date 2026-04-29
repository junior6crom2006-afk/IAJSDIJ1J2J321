import requests
import asyncio
import capsolver

web = requests.session()

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryEXtL6PAe3MBF6ej2',
    # 'Cookie': 'woocommerce_recently_viewed=7104%7C6472; _ga=GA1.1.1757994270.1732397351; _ga_9H7PT3RBJ1=GS1.1.1732397350.1.0.1732397350.0.0.0; _gcl_au=1.1.1934659956.1732397351; _hjSessionUser_5071276=eyJpZCI6IjBiYzVjNTk4LWFhY2QtNTU5MC04OTdiLWFmNzZkNjRiOWU1NyIsImNyZWF0ZWQiOjE3MzIzOTczNTE2NzksImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_5071276=eyJpZCI6IjJmY2M5ZjgxLTYzNzMtNDI4YS05MzMzLTE2ZmEwM2QzYzQ3NiIsImMiOjE3MzIzOTczNTE2ODAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://hogarmas.pe/product/set-de-2-botellas-dispensadoras-verdes-para-cocina/; last_pysTrafficSource=direct; last_pys_landing_page=https://hogarmas.pe/product/set-de-2-botellas-dispensadoras-verdes-para-cocina/; _fbp=fb.1.1732397351690.6313965990; _fbp=fb.1.1732397351690.6313965990; pbid=a2b7ce32b53a1e527cdb6d0677f5295b873abb8a8a18bacfeadf3d87175df8ac',
    'Origin': 'https://hogarmas.pe',
    'Pragma': 'no-cache',
    'Referer': 'https://hogarmas.pe/product/set-de-2-botellas-dispensadoras-verdes-para-cocina/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

files = {
    'attribute_promocion': (None, 'Pedir un embudo de silicona a S/16'),
    'quantity': (None, '1'),
    'add-to-cart': (None, '6472'),
    'product_id': (None, '6472'),
    'variation_id': (None, '6479'),
}

req1 = web.post('https://hogarmas.pe/product/set-de-2-botellas-dispensadoras-verdes-para-cocina/',headers=headers,files=files,)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'woocommerce_recently_viewed=7104%7C6472; _ga=GA1.1.1757994270.1732397351; _gcl_au=1.1.1934659956.1732397351; _hjSession_5071276=eyJpZCI6IjJmY2M5ZjgxLTYzNzMtNDI4YS05MzMzLTE2ZmEwM2QzYzQ3NiIsImMiOjE3MzIzOTczNTE2ODAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; pys_session_limit=true; pys_start_session=true; pys_first_visit=true; pysTrafficSource=direct; pys_landing_page=https://hogarmas.pe/product/set-de-2-botellas-dispensadoras-verdes-para-cocina/; last_pysTrafficSource=direct; last_pys_landing_page=https://hogarmas.pe/product/set-de-2-botellas-dispensadoras-verdes-para-cocina/; _fbp=fb.1.1732397351690.6313965990; _fbp=fb.1.1732397351690.6313965990; pbid=a2b7ce32b53a1e527cdb6d0677f5295b873abb8a8a18bacfeadf3d87175df8ac; woocommerce_items_in_cart=1; wp_woocommerce_session_883abf5350028feb8a12b28930383597=t_24894c326cf5e2a2e6dc2c12136de7%7C%7C1732570167%7C%7C1732566567%7C%7C6d826775830d52fb7818d6fde710d622; woocommerce_cart_hash=d5210f41c5dda14e8e50236f82ce45cb; _hjSessionUser_5071276=eyJpZCI6IjBiYzVjNTk4LWFhY2QtNTU5MC04OTdiLWFmNzZkNjRiOWU1NyIsImNyZWF0ZWQiOjE3MzIzOTczNTE2NzksImV4aXN0aW5nIjp0cnVlfQ==; pysAddToCartFragmentId=d5210f41c5dda14e8e50236f82ce45cb; _ga_9H7PT3RBJ1=GS1.1.1732397350.1.1.1732397407.0.0.0',
    'Pragma': 'no-cache',
    'Referer': 'https://hogarmas.pe/product/set-de-2-botellas-dispensadoras-verdes-para-cocina/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

req2 = web.get('https://hogarmas.pe/checkout/', headers=headers)
with open('checkout.html', 'w', encoding='utf-8') as f:
    f.write(req2.text)
print(req2.text)
