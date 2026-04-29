import requests

def parseX(data, start, end):
    try:
        star = data.index(start) + len(start)
        last = data.index(end, star)
        return data[star:last]
    except ValueError:
        return "None"


def main():

    session = requests.Session()


    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = session.get('https://donate.mercycorps.org/payment', headers=headers).text
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://donate.mercycorps.org',
        'Referer': 'https://donate.mercycorps.org/payment',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = [
        ('TotalAmt', '1'),
        ('Sustainer', 'No'),
        ('DayOfMonth', '1'),
        ('Frequency', 'Monthly'),
        ('TotalAmt', '1'),
        ('DonorIntent', 'WhereMostNeeded'),
        ('OtherDonorIntent', ''),
        ('OtherHM', '-'),
        ('ProductID_1', 'honmem'),
        ('Item', '1'),
        ('MemorialName_1', ''),
        ('MHLastName_1', ''),
        ('Address1_1', ''),
        ('Address2_1', ''),
        ('City_1', ''),
        ('State_1', '0'),
        ('PostalCode_1', ''),
        ('Country_1', 'Dominican Republic'),
        ('Comments_1', ''),
        ('Title', ' '),
        ('FirstName', 'Oklahoma'),
        ('LastName', 'Evan Hicks'),
        ('Address1', 'Eason Rd 5460'),
        ('Address2', ''),
        ('City', 'Phoenix'),
        ('State', 'AR'),
        ('PostalCode', '55573'),
        ('WorkPhone', ''),
        ('EMail', 'example@gmail.com'),
        ('MailingList', 'No'),
        ('OtherMailingList', 'Yes'),
        ('CCNumber', '4046011203654467'),
        ('CSC', '566'),
        ('CCExpMonth', '08'),
        ('CCExpYear', '26'),
        ('CWSID', '78413a6ab3e8134d1c95ffdac8bf04fd'),
        ('c', '0'),
        ('n', '1'),
        ('f', 'index'),
        ('EventID', '2866'),
        ('!SButton', 'Donate Now >'),
    ]

    response = session.post('https://donate.mercycorps.org/index.htm', headers=headers, data=data).text

    mensaje = parseX(response, "<h2>", "</h2>")

    print(mensaje)


main()    