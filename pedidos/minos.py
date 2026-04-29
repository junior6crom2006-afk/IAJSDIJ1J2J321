import requests
import random
import string


def random_email() -> str:
    return "".join(random.choice(string.ascii_letters) for x in range(15)) + "@gmail.com"

email = random_email()

web = requests.session()

req1 = web.get('https://api.ccbill.com/wap-frontflex/flexforms/d6a40787-e32e-49f3-9b69-914223fc7a13')
eltokenmmgv = req1.text.split('name="_csrf" value="')[1].split('"')[0]
elexecution = req1.text.split('name="execution" value="')[1].split('"')[0]
print(elexecution)
print(eltokenmmgv)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'flexform-session-id=2263edd4-ad39-47a1-8854-9aeca21024ff; _ga=GA1.2.1254107156.1731225570; SESSION=YWFmNTdiMjctMmM4YS00ZjJiLTlkMjctOTQxZGYyODFlN2Vh; BIGipServerwap-frontflex-live-pool-10200=!jBX4Pja0ySlkcPsra9ClrhmY0Cv/qv7PwBEd2eEX/I3ggw+enkZrtCzzqqkMbxPqAC7EgLPscJJbaw==; _gid=GA1.2.85363301.1731396618; _ga_TB1GSRQ8MV=GS1.2.1731396618.3.1.1731396726.0.0.0',
    'Origin': 'https://api.ccbill.com',
    'Pragma': 'no-cache',
    'Referer': 'https://api.ccbill.com/wap-frontflex/flexforms/d6a40787-e32e-49f3-9b69-914223fc7a13',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = [
    ('1', elexecution),
    ('selectedCurrencyId', '840'),
    ('selectedPricingSubacc', '89-0-840'),
    ('walletUserName', ''),
    ('walletPassword', ''),
    ('paymentMethodType', 'existing'),
    ('firstName', 'Sebastian'),
    ('lastName', 'Gutierrez'),
    ('phone', ''),
    ('emailAddress', email),
    ('address', ''),
    ('city', ''),
    ('state', 'NJ'),
    ('postalCode', '07050-3824'),
    ('country', 'US'),
    ('selectedPaymentType', 'CREDIT'),
    ('creditCardNum', '5315910012517248'),
    ('cardExpirationMonth', '09'),
    ('cardExpirationYear', '2029'),
    ('cvv2', '222'),
    ('_markedDefault', 'on'),
    ('selectedAccountType', 'Checking'),
    ('accountNumber', ''),
    ('routingNumber', ''),
    ('_markedDefault', 'on'),
    ('ibanBankNumber', ''),
    ('_eventId_placeOrder', 'Enviar'),
    ('clientAccnum', '948980'),
    ('phoneRule', 'noDisplay'),
    ('emailRule', 'displayRequiredEnabled'),
    ('cvv2Rule', 'displayRequiredEnabled'),
    ('captchaRule', 'noDisplay'),
    ('addressRule', 'noDisplay'),
    ('cityRule', 'noDisplay'),
    ('stateRule', 'noDisplay'),
    ('secondaryCardRule', '1'),
    ('captcha', ''),
    ('billingDescriptorType', 'MAIN_ACCOUNT'),
    ('mainClientAccnum', '948980'),
    ('betaFeatureRule', 'On'),
    ('onlyVerifiedACHAccounts', 'All'),
    ('pushPaymentsAllowed', 'No'),
    ('pullPaymentsAllowed', 'Yes'),
    ('emailValidationCode', ''),
    ('threedsApplicable', 'false'),
    ('threedsSuccess', ''),
    ('threedsClientTransactionId', ''),
    ('threedsOriginalDenialSubId', ''),
    ('threedsAmount', ''),
    ('threedsCurrency', ''),
    ('threedsSdkTransId', ''),
    ('threedsAcsTransId', ''),
    ('threedsDsTransId', ''),
    ('threedsAuthenticationValue', ''),
    ('threedsAuthenticationType', ''),
    ('threedsCardToken', ''),
    ('threedsStatus', ''),
    ('threedsXid', ''),
    ('threedsCavv', ''),
    ('threedsCavvAlgorithm', ''),
    ('threedsEci', ''),
    ('threedsVersion', ''),
    ('threedsResponse', ''),
    ('threedsError', ''),
    ('threedsErrorDetail', ''),
    ('threedsErrorCode', ''),
    ('policyToken', ''),
    ('psd2RequirementType', ''),
    ('threedsMerchant', ''),
    ('registeredURL', 'http://www.camsoda.com'),
    ('walletCheckAdded', 'false'),
    ('walletPaymentMethodId', ''),
    ('walletPaymentMethodAdded', 'false'),
    ('walletPaymentMethodExpired', 'false'),
    ('walletPaymentMethodEdited', 'false'),
    ('newWallet', 'false'),
    ('usingWallet', 'false'),
    ('ccbill_referer', ''),
    ('priceAmountByCurrency', '{"89-36":"1.59-0.00","89-124":"1.46-0.00","89-978":"0.98-0.00","89-840":"1.00-0.00","89-392":"161-0","89-826":"0.81-0.00"}'),
    ('isSandboxMode', 'false'),
    ('googleAnalyticsId', 'UA-1582409-10'),
    ('status', ''),
    ('_csrf', eltokenmmgv),
]

req2 = web.post('https://api.ccbill.com/wap-frontflex/flexforms/d6a40787-e32e-49f3-9b69-914223fc7a13',headers=headers,data=data,)
with open("ccbill.txt", "+w",encoding="utf-8") as u:u.write(req2.text)
