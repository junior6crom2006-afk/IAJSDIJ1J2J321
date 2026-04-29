import requests

web = requests.Session()

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }

response =  web.post('https://m.stripe.com/6', headers=headers)
data1 = response.json() 
muid = data1['muid']
sid = data1['sid']
guid = data1['guid']

print(muid, sid, guid)