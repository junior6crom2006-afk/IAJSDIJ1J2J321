import requests
from bs4 import BeautifulSoup

country_names = {
    "ar": "Argentina", "au": "Australia", "bd": "Bangladesh", "be": "Belgium", "br": "Brazil", "ca": "Canada",
    "cn": "China", "cz": "Czech Republic", "fr": "France", "de": "Germany", "gr": "Greece", "hu": "Hungary",
    "in": "India", "id": "Indonesia", "ir": "Iran", "it": "Italy", "jp": "Japan", "my": "Malaysia",
    "mx": "Mexico", "np": "Nepal", "nl": "Netherlands", "ng": "Nigeria", "pe": "Peru", "ph": "Philippines",
    "pl": "Poland", "pt": "Portugal", "ro": "Romania", "ru": "Russia", "sa": "Saudi Arabia", "sg": "Singapore",
    "za": "South Africa", "kr": "South Korea", "es": "Spain", "se": "Sweden", "th": "Thailand", "tr": "Turkey",
    "ug": "Uganda", "ua": "Ukraine", "uk": "United Kingdom", "us": "United States", "vn": "Vietnam"
}

def fakexy(country_prefix):
    normalurl = 'https://www.fakexy.com/'
    if country_prefix != 'us':
        url = f'{normalurl}fake-address-generator-{country_prefix}'
    else:
        url = normalurl

    session = requests.session()
    results = {
        "address": None,
        "city": None,
        "state": None,
        "zip_code": None,
        "phone_number": None,
        "error": None
    }

    try:
        response = session.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        tds = soup.find_all('td')

        def extract_info(label):
            for index, td in enumerate(tds):
                if td.text.strip() == label:
                    if index + 1 < len(tds):
                        value = tds[index + 1].text.strip()
                        if label == "Street":
                            results["address"] = value
                        elif label == "City/Town":
                            results["city"] = value
                        elif label == "State/Province/Region":
                            results["state"] = value
                        elif label == "Zip/Postal Code":
                            results["zip_code"] = value
                        elif label == "Phone Number":
                            results["phone_number"] = value

        labels = ["Street", "City/Town", "State/Province/Region", "Zip/Postal Code", "Phone Number"]

        for label in labels:
            extract_info(label)
        
    except Exception as e:
        results['error'] = str(e)

    return results

def get_country_name(country_prefix):
    return country_names.get(country_prefix, "Unknown")
