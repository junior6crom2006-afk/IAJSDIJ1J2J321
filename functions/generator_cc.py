import random
import re

class Utils:
    @staticmethod
    def luhn_verification(num):
        num = [int(d) for d in str(num)]
        check_digit = num.pop()
        num.reverse()
        total = 0
        for i,digit in enumerate(num):
            if i % 2 == 0:
                digit = digit * 2
            if digit > 9:
                digit = digit - 9
            total += digit
        total = total * 9
        return (total % 10) == check_digit

    @staticmethod
    def regexcc(input_str):
        cc_pattern = re.compile(r'^[a-zA-Z0-9]{6,16}$')
        mes_pattern = re.compile(r'^\d{1,2}$')
        ano_pattern = re.compile(r'^\d{2,4}$')
        cvv_pattern = re.compile(r'^\w{3,4}$')

        parts = re.split(r'[|/,.*<>;: ]', input_str)
        
        cc = mes = ano = cvv = None
        
        for part in parts:
            if cc is None and cc_pattern.match(part):
                cc = part
            elif mes is None and mes_pattern.match(part) and Utils.is_valid_month(part):
                mes = part
            elif ano is None and ano_pattern.match(part) and Utils.is_valid_year(part):
                ano = part
            elif cvv is None and cvv_pattern.match(part):
                cvv = part

        if cc is None:
            cc = 'xxxx'
        if mes is None:
            mes = 'x'
        if ano is None:
            ano = 'xxxx'
        if cvv is None:
            cvv = 'xxx'

        if cvv == 'xxxx':
            cvv = parts[3]
        
        if len(cvv) >= 4:
            cvv = 'xxx'

        BIN = cc[:6]
        
        if not BIN.isdigit() or len(BIN) < 6:
            return None, None, None, None

        return cc, mes, ano, cvv

    @staticmethod
    def is_valid_month(month):
        return month.isdigit() and 1 <= int(month) <= 12
    
    @staticmethod
    def is_valid_year(year):
        if len(year) == 2:
            year = '20' + year
        return year.isdigit() and 2023 <= int(year) <= 2040

    @staticmethod
    def cc_genv(input_str):
        cc, mes, ano, cvv = Utils.regexcc(input_str)
        ccs = []

        while len(ccs) < 10:
            card = str(cc)
            digits = '0123456789'
            list_digits = list(digits)
            random.shuffle(list_digits)
            string_digits = ''.join(list_digits)
            card = card + string_digits
            new_list = list(card)
            list_emty = []
            for i in new_list:
                if i =='x':
                    list_emty.append(str(random.randint(0,9)))
                else:
                    list_emty.append(i)
            list_empty_string = ''.join(list_emty)
            card = list_empty_string
            if card[0] == '3':
                card = card[0:15]
            else:
                card = card[0:16]

            if mes == 'x' or mes is None:
                mes_gen = random.randint(1,12)
                if len(str(mes_gen)) == 1:
                    mes_gen = '0' + str(mes_gen)
            else:
                if len(mes) == 1:
                    mes_gen = "0"+mes
                else:
                    mes_gen = mes

            if ano == 'xxxx' or ano is None:
                ano_gen = random.randint(2024,2031)
            else:
                ano_gen = ano
                if len(str(ano_gen)) == 2:
                    ano_gen = '20' + str(ano_gen)

            if cvv == 'xxx' or cvv is None:
                if card[0:1] == '3': 
                    cvv_gen = str(random.randint(1000, 9999))
                else: 
                    cvv_gen = str(random.randint(100, 999))
            else:
                if card[0:1] == '3':
                    cvv_gen = str(random.randint(1000, 9999))
                else:
                    cvv_gen = ""
                    for ch in cvv:
                        if ch.isalpha():
                            cvv_gen += str(random.randint(0, 9))
                        else:
                            cvv_gen += ch
            
            x = f"{card}|{mes_gen}|{ano_gen}|{cvv_gen}"
            if Utils.luhn_verification(card):
                ccs.append(x)
                
        return ccs