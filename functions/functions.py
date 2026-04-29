import re, datetime, sqlite3, random, json, re, asyncio
import random
import string
from asyncio import sleep as asyncio_sleep
from json import load as json_load
from html import unescape
from time import time
from .generator_cc import Utils as Gen
from datetime import date, datetime
from httpx import AsyncClient
from .variables import LINK_CHANNEL_INFO, SYMBOL,SYMBOL2

import csv
from functools import lru_cache
TIMES = {}
USERS_INFO = {}

## BINS
DICTIONARY_BINS = {}
@lru_cache(maxsize=None)
def GetBinCountry(country_code):
    x = {'Afghanistan': 'AF',
         'Albania': 'AL',
         'Algeria': 'DZ',
         'American Samoa': 'AS',
         'Andorra': 'AD',
         'Angola': 'AO',
         'Anguilla': 'AI',
         'Antarctica': 'AQ',
         'Antigua and Barbuda': 'AG',
         'Argentina': 'AR',
         'Armenia': 'AM',
         'Aruba': 'AW',
         'Australia': 'AU',
         'Austria': 'AT',
         'Azerbaijan': 'AZ',
         'Bahamas': 'BS',
         'Bahrain': 'BH',
         'Bangladesh': 'BD',
         'Barbados': 'BB',
         'Belarus': 'BY',
         'Belgium': 'BE',
         'Belize': 'BZ',
         'Benin': 'BJ',
         'Bermuda': 'BM',
         'Bhutan': 'BT',
         'Bolivia, Plurinational State of': 'BO',
         'Bonaire, Sint Eustatius and Saba': 'BQ',
         'Bosnia and Herzegovina': 'BA',
         'Botswana': 'BW',
         'Bouvet Island': 'BV',
         'Brazil': 'BR',
         'British Indian Ocean Territory': 'IO',
         'Brunei Darussalam': 'BN',
         'Bulgaria': 'BG',
         'Burkina Faso': 'BF',
         'Burundi': 'BI',
         'Cambodia': 'KH',
         'Cameroon': 'CM',
         'Canada': 'CA',
         'Cape Verde': 'CV',
         'Cayman Islands': 'KY',
         'Central African Republic': 'CF',
         'Chad': 'TD',
         'Chile': 'CL',
         'China': 'CN',
         'Christmas Island': 'CX',
         'Cocos (Keeling) Islands': 'CC',
         'Colombia': 'CO',
         'Comoros': 'KM',
         'Congo': 'CG',
         'Congo, the Democratic Republic of the': 'CD',
         'Cook Islands': 'CK',
         'Costa Rica': 'CR',
         'Country name': 'Code',
         'Croatia': 'HR',
         'Cuba': 'CU',
         'Curaçao': 'CW',
         'Cyprus': 'CY',
         'Czech Republic': 'CZ',
         "Côte d'Ivoire": 'CI',
         'Denmark': 'DK',
         'Djibouti': 'DJ',
         'Dominica': 'DM',
         'Dominican Republic': 'DO',
         'Ecuador': 'EC',
         'Egypt': 'EG',
         'El Salvador': 'SV',
         'Equatorial Guinea': 'GQ',
         'Eritrea': 'ER',
         'Estonia': 'EE',
         'Ethiopia': 'ET',
         'Falkland Islands (Malvinas)': 'FK',
         'Faroe Islands': 'FO',
         'Fiji': 'FJ',
         'Finland': 'FI',
         'France': 'FR',
         'French Guiana': 'GF',
         'French Polynesia': 'PF',
         'French Southern Territories': 'TF',
         'Gabon': 'GA',
         'Gambia': 'GM',
         'Georgia': 'GE',
         'Germany': 'DE',
         'Ghana': 'GH',
         'Gibraltar': 'GI',
         'Greece': 'GR',
         'Greenland': 'GL',
         'Grenada': 'GD',
         'Guadeloupe': 'GP',
         'Guam': 'GU',
         'Guatemala': 'GT',
         'Guernsey': 'GG',
         'Guinea': 'GN',
         'Guinea-Bissau': 'GW',
         'Guyana': 'GY',
         'Haiti': 'HT',
         'Heard Island and McDonald Islands': 'HM',
         'Holy See (Vatican City State)': 'VA',
         'Honduras': 'HN',
         'Hong Kong': 'HK',
         'Hungary': 'HU',
         'ISO 3166-2:GB': '(.uk)',
         'Iceland': 'IS',
         'India': 'IN',
         'Indonesia': 'ID',
         'Iran, Islamic Republic of': 'IR',
         'Iraq': 'IQ',
         'Ireland': 'IE',
         'Isle of Man': 'IM',
         'Israel': 'IL',
         'Italy': 'IT',
         'Jamaica': 'JM',
         'Japan': 'JP',
         'Jersey': 'JE',
         'Jordan': 'JO',
         'Kazakhstan': 'KZ',
         'Kenya': 'KE',
         'Kiribati': 'KI',
         "Korea, Democratic People's Republic of": 'KP',
         'Korea, Republic of': 'KR',
         'Kuwait': 'KW',
         'Kyrgyzstan': 'KG',
         "Lao People's Democratic Republic": 'LA',
         'Latvia': 'LV',
         'Lebanon': 'LB',
         'Lesotho': 'LS',
         'Liberia': 'LR',
         'Libya': 'LY',
         'Liechtenstein': 'LI',
         'Lithuania': 'LT',
         'Luxembourg': 'LU',
         'Macao': 'MO',
         'Macedonia, the former Yugoslav Republic of': 'MK',
         'Madagascar': 'MG',
         'Malawi': 'MW',
         'Malaysia': 'MY',
         'Maldives': 'MV',
         'Mali': 'ML',
         'Malta': 'MT',
         'Marshall Islands': 'MH',
         'Martinique': 'MQ',
         'Mauritania': 'MR',
         'Mauritius': 'MU',
         'Mayotte': 'YT',
         'Mexico': 'MX',
         'Micronesia, Federated States of': 'FM',
         'Moldova, Republic of': 'MD',
         'Monaco': 'MC',
         'Mongolia': 'MN',
         'Montenegro': 'ME',
         'Montserrat': 'MS',
         'Morocco': 'MA',
         'Mozambique': 'MZ',
         'Myanmar': 'MM',
         'Namibia': 'NA',
         'Nauru': 'NR',
         'Nepal': 'NP',
         'Netherlands': 'NL',
         'New Caledonia': 'NC',
         'New Zealand': 'NZ',
         'Nicaragua': 'NI',
         'Niger': 'NE',
         'Nigeria': 'NG',
         'Niue': 'NU',
         'Norfolk Island': 'NF',
         'Northern Mariana Islands': 'MP',
         'Norway': 'NO',
         'Oman': 'OM',
         'Pakistan': 'PK',
         'Palau': 'PW',
         'Palestine, State of': 'PS',
         'Panama': 'PA',
         'Papua New Guinea': 'PG',
         'Paraguay': 'PY',
         'Peru': 'PE',
         'Philippines': 'PH',
         'Pitcairn': 'PN',
         'Poland': 'PL',
         'Portugal': 'PT',
         'Puerto Rico': 'PR',
         'Qatar': 'QA',
         'Romania': 'RO',
         'Russian Federation': 'RU',
         'Rwanda': 'RW',
         'Réunion': 'RE',
         'Saint Barthélemy': 'BL',
         'Saint Helena, Ascension and Tristan da Cunha': 'SH',
         'Saint Kitts and Nevis': 'KN',
         'Saint Lucia': 'LC',
         'Saint Martin (French part)': 'MF',
         'Saint Pierre and Miquelon': 'PM',
         'Saint Vincent and the Grenadines': 'VC',
         'Samoa': 'WS',
         'San Marino': 'SM',
         'Sao Tome and Principe': 'ST',
         'Saudi Arabia': 'SA',
         'Senegal': 'SN',
         'Serbia': 'RS',
         'Seychelles': 'SC',
         'Sierra Leone': 'SL',
         'Singapore': 'SG',
         'Sint Maarten (Dutch part)': 'SX',
         'Slovakia': 'SK',
         'Slovenia': 'SI',
         'Solomon Islands': 'SB',
         'Somalia': 'SO',
         'South Africa': 'ZA',
         'South Georgia and the South Sandwich Islands': 'GS',
         'South Sudan': 'SS',
         'Spain': 'ES',
         'Sri Lanka': 'LK',
         'Sudan': 'SD',
         'Suriname': 'SR',
         'Svalbard and Jan Mayen': 'SJ',
         'Swaziland': 'SZ',
         'Sweden': 'SE',
         'Switzerland': 'CH',
         'Syrian Arab Republic': 'SY',
         'Taiwan, Province of China': 'TW',
         'Tajikistan': 'TJ',
         'Tanzania, United Republic of': 'TZ',
         'Thailand': 'TH',
         'Timor-Leste': 'TL',
         'Togo': 'TG',
         'Tokelau': 'TK',
         'Tonga': 'TO',
         'Trinidad and Tobago': 'TT',
         'Tunisia': 'TN',
         'Turkey': 'TR',
         'Turkmenistan': 'TM',
         'Turks and Caicos Islands': 'TC',
         'Tuvalu': 'TV',
         'Uganda': 'UG',
         'Ukraine': 'UA',
         'United Arab Emirates': 'AE',
         'United Kingdom': 'GB',
         'United States': 'US',
         'United States Minor Outlying Islands': 'UM',
         'Uruguay': 'UY',
         'Uzbekistan': 'UZ',
         'Vanuatu': 'VU',
         'Venezuela, Bolivarian Republic of': 'VE',
         'Viet Nam': 'VN',
         'Virgin Islands, British': 'VG',
         'Virgin Islands, U.S.': 'VI',
         'Wallis and Futuna': 'WF',
         'Western Sahara': 'EH',
         'Yemen': 'YE',
         'Zambia': 'ZM',
         'Zimbabwe': 'ZW',
         'Åland Islands': 'AX'}
    if country_code in x.values():
        for pais, codigo in x.items():
            if codigo == country_code: return pais.upper()    
            


async def get_bin_info(bin: str) -> dict | None:
    bin = bin[0:6]
    async with AsyncClient(follow_redirects=True, verify=False) as s:
        response = await s.get(
            f"https://zyrex.qzz.io/v1/Tools/bin?bin={bin}",
            headers={
                "Authorization": "Bearer zyrex_84g9BVyproH7AIqtKrVuCtWQ3JvM7H6Y"
            }
        )
        if response.status_code != 200:
            res = get_bin_info_of_database(bin)
            if res: res['api_code'] = response.status_code
            return res
        response_text = response.text
        response_json = json.loads(response_text)
        banned_bins = json.load(open("json/banned_bins.json", "r"))

        country_name = (
            response_json.get("BIN", {})
            .get("country", {})
            .get("name", "")
            .upper()
        )

        banned = False
        if str(bin) in banned_bins or "BRAZIL" in country_name:
            banned = True
        response_json["banned"] = banned
        response_json["api_code"] = 200
        return response_json

db_bins = sqlite3.connect("db/bins.db")
cursor_bins = db_bins.cursor()


def get_bin_info_of_database(bin: str) -> dict | None:
    bin = bin[0:6]

    result = cursor_bins.execute("SELECT * FROM bins WHERE bin=?", (bin,))
    result = result.fetchone()
    if result is None:
        return None
    banned_bins = json.load(open("json/banned_bins.json", "r"))
    banned = False
    if str(bin) in banned_bins:
        banned = True
    return {
        "bin": result[0],
        "brand": result[1],
        "country_name": result[5],
        "flag": result[8].strip(),
        "bank_name": result[4],
        "level": result[3],
        "type": result[2],
        "banned": banned,
    }




async def get_text_from_pyrogram(m, no_command: bool = False) -> str:
    "Returns the text used in the command if no message is being responded to"
    text = m.text
    if hasattr(m.reply_to_message, "text") and m.reply_to_message.text:
        text = m.reply_to_message.text
    if no_command:
        text = text[len(m.command[0]) + 2 :].strip()
    return text

async def FindText(value1, value2, text):
    return str(text).split(str(value1))[1].split(str(value2))[0]

async def CleanText(text):
    return " ".join(re.sub(r"<.*?>|\n", " ", text).split())

async def TwoCaptcha(api_key, url, site_key, en):
    async with AsyncClient(follow_redirects=True, verify=False) as session:
        if en:
            url = f"https://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={site_key}&pageurl={url}&enterprise=1"
        else:
            url = f"https://2captcha.com/in.php?key={api_key}&method=userrecaptcha&googlekey={site_key}&pageurl={url}"
        r = await session.get(url)
        t = r.text
        task_id = t.split("|")[1]
        attempts = 0
        while True:
            r2 = await session.get(f"https://2captcha.com/res.php?key={api_key}&action=get&id={task_id}")
            t2 = r2.text
            st = t2.split("|")[0]
            if st == "OK":
                captcha = t2.split("|")[1]
                return captcha
            else:
                attempts += 1
                if attempts >= 50:
                    return False, "Error"
                await asyncio_sleep(5)

async def AntiSpam(user: int, limit: int = 60, free_user=False, times: dict = TIMES, is_mass: bool = False, membership: str = "Free user") -> bool | int:
    assert isinstance(user, int), "User ID must be an integer"
    
    now = time()
    user_info = times.get(user, {"last": 0, "checks": 0})
    last = user_info["last"]
    
    membership_lower = membership.lower()
    if is_mass:
        if "vip" in membership_lower: limit = 15
        elif "premium" in membership_lower: limit = 30
        else: limit = 60
    else:
        if "vip" in membership_lower: limit = 5
        elif "premium" in membership_lower: limit = 15
        else: limit = 60

    checks = user_info["checks"]
    diff = now - last
    if diff >= limit:
        checks = 0
        
    if checks >= 1:
        return int(limit - diff)
        
    checks += 1
    times[user] = {"last": now, "checks": checks}
    return False

async def GetTelegramID(user_id, name):
    return f"<a href='tg://user?id={user_id}'>{name}</a>"

async def Symbol():
    return f"[<a href='{LINK_CHANNEL_INFO}'>{SYMBOL}</a>]"

async def Symbol2():
    return f"[<a href='{LINK_CHANNEL_INFO}'>{SYMBOL2}</a>]"

async def GetCCs(text):
    lines = text.strip().split('\n')
    results = []
    for line in lines:
        cc_info = await GetCC(line)
        if cc_info:
            results.append(cc_info)
    return results

def is_luhn_valid(cc):
    """Función para validar si un número de tarjeta cumple con el algoritmo Luhn"""
    num = [int(d) for d in str(cc)]
    checksum = num[-1]
    num = num[:-1]
    
    for i in range(len(num) - 1, -1, -2):
        num[i] *= 2
        if num[i] > 9:
            num[i] -= 9
            
    total = sum(num) + checksum
    return total % 10 == 0

async def GetCC(text):
    try:
        if not text:
            return
            
        text = text.strip()
        # Modificar el patrón para incluir ':' como separador
        card_pattern = r'[0-9]+[|:][0-9]+[|:][0-9]+[|:][0-9]+'
        
        cc = None
        if re.search(card_pattern, text):
            card_data = re.findall(card_pattern, text)[0]
            cc, mes, ano, cvv = card_data.replace('|', ':').split(':')  # Reemplazar '|' por ':' para unificar el formato
        else:
            cc = re.sub("[^0-9]", "", text)
            if len(cc) < 15: return
            
            if cc[0] == "3":
                mes = cc[15:17]
                ano = cc[17:19]
                cvv = cc[19:23]
                cc = cc[:15]
            else:
                mes = cc[16:18]
                ano = cc[18:20]
                cvv = cc[20:23]
                cc = cc[:16]
                
        if not cc or not mes or not ano or not cvv:
            return
            
        invalid_cc = lambda cc: ((cc[0] == "3" and len(cc) != 15) or (cc[0] != "3" and len(cc) != 16)) or not is_luhn_valid(cc)
            
        if invalid_cc(cc):
            return
            
        if len(mes) == 1: mes = "0" + mes
        if len(ano) == 2: ano = "20" + ano
            
        return cc, mes, ano, cvv
        
    except Exception as e:
        print(f"Error en GetCC: {str(e)}")
        return None


def get_gate_by_cmd(cmd_to_find: str, gates_data) -> dict | None:
    for gate in gates_data:
        if gate["cmd"] == cmd_to_find:
            return gate
    return None

def random_email() -> str:
    return (
        "".join(random.choice(string.ascii_letters) for x in range(15))
    ) + "@gmail.com"


def random_street():
    return f"{random.randint(1, 999)} W {random.randint(10, 999)}nd St"


def random_phone():
    return f'+1{"%010d" % random.randint(0, 9999999999)}'


def random_word(length):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))


def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )




async def handler_gate(gate, shopify: bool, *args) -> str | bool | Exception:
    try:
        if shopify:
            response = await gate(*args)
        else:
            response = await gate(*args)
        if not response:
            return False
        return response
    except Exception as e:
        return e



async def RandomAddress(country):
    countrys = json_load(open("countrys.json", "r"))
    if country in countrys:
        country_name = countrys[country]
        async with AsyncClient(follow_redirects=True, verify=False) as s:
            response = await s.get(f"https://www.worldnamegenerator.com/All_countries/address/country/{country_name}")#,params={"domain": country},)
            response = response.text
            if "Page not exists!" in response:
                return None
            try:
                name = await FindText("<td><span>Full Name</span></td>", "</tr>", response)
                name = await FindText("<td><b>", "</b></td>", name)
                name = await CleanText(unescape(name))

                gender = await FindText("<td><span>Gender</span></td>", "</tr>", response)
                gender = await FindText("<td><b>", "</b></td>", gender)
                gender = await CleanText(unescape(gender))

                birthday = await FindText("<td><span>Birthday</span></td>", "</tr>", response)
                birthday = await FindText("<td><b>", "</b></td>", birthday)
                birthday = await CleanText(unescape(birthday))

                street = await FindText("<td>Street</td>", "</tr>", response)
                street = await FindText("<td><b>", "</b></td>", street)
                street = await CleanText(unescape(street))
                
                city = await FindText("<td>City/town</td>", "</tr>", response)
                city = await FindText("<td><b>", "</b></td>", city)
                city = await CleanText(unescape(city))
                
                state = await FindText("<td>State/Province/Area</td>", "</tr>", response)
                state = await FindText("<td><b>", "</b></td>", state)
                state = await CleanText(unescape(state))
                
                zip = await FindText("<td>Zip Code/Post Code</td>", "</tr>", response)
                zip = await FindText("<td><b>", "</b></td>", zip)
                zip = await CleanText(unescape(zip))

                phone = await FindText("<td>Phone Number</td>", "</tr>", response)
                phone = await FindText("<td><b>", "</b></td>", phone)
                phone = await CleanText(unescape(phone))

                phone_code = await FindText("<td>Country Dialing Code</td>", "</tr>", response)
                phone_code = await FindText("<td><b>", "</b></td>", phone_code)
                phone_code = await CleanText(unescape(phone_code))
                
                return {
                    "name": name,
                    "gender": gender,
                    "birthday": birthday,
                    "street": street,
                    "city": city,
                    "state": state,
                    "zip": zip,
                    "phone": f"{phone_code} {phone}",
                }
            except:
                return None
    else: return None

def proxy_x():
    countries = [
        ("US", "🇺🇸"),
        ("AU", "🇦🇺"),
        ("UK", "🇬🇧"), 
        ("ES", "🇪🇸"),
        ("DE", "🇩🇪"),
        ("CA", "🇨🇦"),
        ("FR", "🇫🇷"),
        ("IT", "🇮🇹"),
        ("JP", "🇯🇵"),
        ("BR", "🇧🇷")
    ]
    
    # Seleccionar un país aleatorio
    country, flag = random.choice(countries)
    
    # Generar IP aleatoria con el formato específico
    ip = f"{random.randint(100, 255)}.x{random.randint(0, 99)}.{random.randint(0, 9)}xx.{random.randint(0, 99)}"
    
    return f"✅"

def clean_text(text):
    text_cleaned = " ".join(re.sub(r"<.*?>|\n", " ", text).split())
    return text_cleaned


async def ProxyRandom(): 
    with open("proxy/proxys.txt", "r") as archivo:
        proxy_lines = archivo.read().splitlines()
        while True:
            proxy_line = random.choice(proxy_lines)
            parts = proxy_line.split(":")
            if len(parts) >= 4:  
                host, puerto, username, password = parts[:4]
                scheme = "socks5" if "socks" in host.lower() or (len(parts) == 5 and "socks" in parts[4].lower()) else "http"
                proxy_url = f"{scheme}://{username}:{password}@{host}:{puerto}"
                return {"http://": proxy_url, "https://": proxy_url}
            

async def ProxyRandomFromFile(): 
    with open("proxy/proxys.txt", "r") as archivo:
        proxy_lines = archivo.read().splitlines()
        while True:
            proxy_line = random.choice(proxy_lines)
            parts = proxy_line.split(":")
            if len(parts) >= 4:  
                host, puerto, username, password = parts[:4]
                scheme = "socks5" if "socks" in host.lower() or (len(parts) == 5 and "socks" in parts[4].lower()) else "http"
                proxy_url = f"{scheme}://{username}:{password}@{host}:{puerto}"
                return {"http://": proxy_url, "https://": proxy_url}
            

async def ProxyRandomKev(): 
    with open("proxy/proxys.txt", "r") as archivo:
        proxy_lines = archivo.read().splitlines()
        while True:
            proxy_line = random.choice(proxy_lines)
            parts = proxy_line.split(":")
            if len(parts) >= 4:  
                host, puerto, username, password = parts[:4]
                scheme = "socks5" if "socks" in host.lower() or (len(parts) == 5 and "socks" in parts[4].lower()) else "http"
                proxy_url = f"{scheme}://{username}:{password}@{host}:{puerto}"
                return {"http://": proxy_url, "https://": proxy_url}

async def ProxyRandomIPv4():
    proxies = "proxy/proxys.txt"
    with open(proxies) as a:
        proxy_line = random.choice(a.read().splitlines()).strip()
    
    ip, port = proxy_line.split(":")
    proxy_url = f"http://{ip}:{port}"
    
    return {
        "http://": proxy_url,
        "https://": proxy_url
    }

async def RandomPene3(): 
    with open("proxy/proxys.txt", "r") as archivo:
        proxy_lines = archivo.read().splitlines()
        while True:
            proxy_line = random.choice(proxy_lines)
            parts = proxy_line.split(":")
            if len(parts) >= 4:  
                host, puerto, username, password = parts[:4]
                scheme = "socks5" if "socks" in host.lower() or (len(parts) == 5 and "socks" in parts[4].lower()) else "http"
                proxy_url = f"{scheme}://{username}:{password}@{host}:{puerto}"
                return {"http://": proxy_url, "https://": proxy_url}

def proxyperudanger(for_aiohttp: bool = False) -> dict:
    proxies = "proxy/proxys.txt"
    with open(proxies) as a:
        prox1 = f"{random.choice(a.read().splitlines()).strip()}:http"

    proxy_parts = prox1.split(":")
    if for_aiohttp:
        proxy = f"{proxy_parts[-1]}://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}"
        return proxy

    proxy = f"{proxy_parts[-1]}://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}"
    return {"http://": proxy, "https://": proxy}

    
    
def bright_data_proxy(for_aiohttp: bool = False) -> dict | str:
    proxies_file = "proxy/proxys.txt"
    with open(proxies_file) as file:
        proxy_line = random.choice(file.read().splitlines()).strip()

    proxy_parts = proxy_line.split(":")
    PROXY_HOST = f"{proxy_parts[0]}:{proxy_parts[1]}"
    PROXY_AUTH = f"{proxy_parts[2]}:{proxy_parts[3]}"
    PROXY_URL = f"http://{PROXY_AUTH}@{PROXY_HOST}"
    
    if for_aiohttp:
        return PROXY_URL
        
    return {
        "http://": PROXY_URL,
        "https://": PROXY_URL
    }

def proxyuhq(for_aiohttp: bool = False) -> dict | str:
    PROXY_HOST = "brd.superproxy.io:22225"
    PROXY_AUTH = "brd-customer-hl_509b395c-zone-thinker:m74qoifr3hi0"
    PROXY_URL = f"http://{PROXY_AUTH}@{PROXY_HOST}"
    
    if for_aiohttp:
        return PROXY_URL
        
    return {
        "http://": PROXY_URL,
        "https://": PROXY_URL
    }

async def ProxyRandom3():
    with open("proxy/proxys3.txt", "r") as archivo:
        proxies = [line.split()[0] for line in archivo.read().splitlines() if line.strip()]
        if not proxies:
            raise ValueError("No hay pos.")
        ip, puerto, username, password = random.choice(proxies).split(":")
        proxy_url = f"http://{username}:{password}@{ip}:{puerto}"
        return {"http://": proxy_url, "https://": proxy_url}
    
def random_proxy2(for_aiohttp: bool = False) -> dict | str:
    proxies = "proxy/proxys.txt"
    with open(proxies) as a:
        prox1 = random.choice(a.read().splitlines()).strip()

    parts = prox1.split(":")
    if len(parts) >= 4:
        host, puerto, username, password = parts[:4]
        scheme = "socks5" if "socks" in host.lower() or (len(parts) == 5 and "socks" in parts[4].lower()) else "http"
        proxy_url = f"{scheme}://{username}:{password}@{host}:{puerto}"
        
        if for_aiohttp:
            return proxy_url

        return {"http://": proxy_url, "https://": proxy_url}
    return None

def random_proxy(for_aiohttp: bool = False) -> dict:
    proxies = "proxy/proxys.txt"
    with open(proxies) as a:
        prox1 = random.choice(a.read().splitlines()).strip()

    parts = prox1.split(":")
    if len(parts) >= 4:
        host, puerto, username, password = parts[:4]
        scheme = "socks5" if "socks" in host.lower() or (len(parts) == 5 and "socks" in parts[4].lower()) else "http"
        proxy_url = f"{scheme}://{username}:{password}@{host}:{puerto}"

        if for_aiohttp:
            return proxy_url

        return {"http://": proxy_url, "https://": proxy_url}
    return None



def random_proxy_sh() -> dict:
    with open("proxy/proxys.txt") as a:
        prox1 = random.choice(a.read().splitlines()).strip()

    proxy_parts = prox1.split(":")
    proxy_url = f"http://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}"

    return {"http://": proxy_url, "https://": proxy_url}