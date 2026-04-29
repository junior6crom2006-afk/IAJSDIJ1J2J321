from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import Message
from functions.database import Database
from functions.functions import (
    get_bin_info,
    GetCC,
    ProxyRandom,
    get_text_from_pyrogram,
    Symbol,
    AntiSpam
)
from functions.variables import PREFIXES
from time import perf_counter   
from functions.gates_for_mass import (
    gateway_stripe3,
    chase2, 
    nmi1, 
    authnet, 
    stripeauth,
    authnet555,
    chaseccnauth,
    b3gateavs,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

# Botones
button = InlineKeyboardMarkup([[
    InlineKeyboardButton(text="Buy Chk", url="https://t.me/tocandotee"),
    InlineKeyboardButton(text="Reference", url="https://t.me/ZyrexRefes"),
]])

button1 = InlineKeyboardMarkup([[
    InlineKeyboardButton(text="Credits for $5", url="https://t.me/tocandotee"),
    InlineKeyboardButton(text="Reference", url="https://t.me/ZyrexRefes"),
]])

#

msg_error = """<b>
{} Format: /mass [Comando]
{} card|month|year|cvv
{} card|month|year|cvv</b>"""

# Función para procesar tarjetas
async def process_card(cc, bins, ccs_findeds, user_id):
    cc = await GetCC(cc)
    if not cc:
        return
        
    card = cc[0]
    resp = await get_bin_info(card[0:6])
    if resp is None:
        return
        
    if cc in ccs_findeds:
        return
        
    brand = resp["brand"]
    country_name = resp["country_name"]
    country_flag = resp["flag"]
    flag = resp["flag"] if resp["flag"] else "UNAVAILABLE"
    bank = resp["bank_name"]
    level = resp["level"] if resp["level"] else "UNAVAILABLE"
    typea = resp["type"] if resp["type"] else "UNAVAILABLE"
    banned_bin = resp["banned"]
    
    if user_id not in [6712112939] and (
        banned_bin or "prepaid" in level.lower() or "prepaid" in typea.lower()
    ):
        return
        
    bins[card[0:6]] = resp
    ccs_findeds.append(cc)

@Client.on_message(filters.command(["mass1", "mass2", "mass3", "mass4", "mass5", "mass6", "mass7", "mass8", "mass9", "mass10", "mass11", "mass12", "mass13", "mass14", "mass15"], PREFIXES))
async def mass_checker(client: Client, m: Message):
    try:
        symbol = await Symbol()
        error_msg = msg_error.format(symbol, symbol, symbol)
        
        # Mapeo de comandos a gates
        gates = {
            "mass1": (gateway_stripe3, "Stripe CCN 3$"),
            "mass2": (klk, "Braintree CCN"),
            "mass3": (chase2, "B3 AVS"),
            "mass4": (nmi1, "NMI"),
            "mass5": (authnet, "Auth Net"),
            "mass7": (stripeauth, "Stripe 1$ Charged"),
            "mass9": (authnet555, "Authorize.Net Auth"),
            "mass12": (b3gateavs, "B3 AVS")
        }

        # Verificar usuario premium
        user_id = m.from_user.id
        with Database() as db:
            if not db.is_premium(user_id):
                return await m.reply(
                    f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No eres premium. Contacta a @tocandotee\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0",
                    reply_markup=button,
                    quote=True,
                )
            user_info = db.get_info_user(user_id)
            rol = user_info["MEMBERSHIP"]

        # Verificar créditos
        credits = user_info.get("CREDITS", 0)
        if credits < 4:
            return await m.reply(
                "<b>More than 2 credits are needed to be able to use this command.</b>",
                reply_markup=button1,
                quote=True,
            )

        # Verificar antispam
        antispam = await AntiSpam(user_id, is_mass=True, membership=user_info["MEMBERSHIP"])
        if antispam:
            return await m.reply(f"<b>Please Wait [<code>{antispam}s</code>] After Checking ⚠️</b>")

        # Obtener comando y tarjetas
        cmd = m.command[0].lower()
        text = await get_text_from_pyrogram(m)
        
        # Obtener la tarjeta
        if len(m.command) > 1:  # Si hay algo después del comando
            cc = m.command[1]  # Tomar el texto después del comando como tarjeta
            ccs = [cc]  # Poner la tarjeta en la lista
            if len(text.split("\n")) > 1:  # Si hay más tarjetas en líneas siguientes
                ccs.extend(text.split("\n")[1:])
        else:  # Si no hay tarjeta después del comando
            if len(text.split("\n")) < 2:
                return await m.reply(f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Formato: <code>/mass [Comando] cc|mm|yy|cvv</code>\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0", reply_markup=button, quote=True)
            ccs = text.split("\n")[1:]  # Tomar las tarjetas de las líneas siguientes

        if cmd not in gates:
            return await m.reply(error_msg, reply_markup=button, quote=True)

        gate, gate_name = gates[cmd]
        
        # Procesar tarjetas
        ccs_findeds = []
        bins = {}

        # Crear y ejecutar tareas para procesar tarjetas
        tasks = []
        for cc in ccs:
            tasks.append(process_card(cc, bins, ccs_findeds, user_id))
        await asyncio.gather(*tasks)

        if not (0 < len(ccs_findeds) <= 15):
            return await m.reply(error_msg, reply_markup=button, quote=True)

        # Iniciar chequeo
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

        # Procesar tarjetas
        text_ccs = ""
        errors = approveds = deads = creditos_removidos = 0

        tasks = []
        for cc in ccs_findeds:
            card, mes, ano, cvv = cc
            proxy = await ProxyRandom()
            tasks.append(gate(card, mes, ano, cvv, proxy))

        results = await asyncio.gather(*tasks)

        for i, result in enumerate(results):
            cc = ccs_findeds[i]
            card, mes, ano, cvv = cc
            
            try:
                if isinstance(result, tuple):
                    status, msg = result
                else:
                    status = result.get("status", "Error")
                    msg = result.get("response", "Unknown Error")

                if "approved" in status.lower():
                    Database().remove_credits(user_id, credits=3)
                    approveds += 1
                    creditos_removidos += 3
                elif "declined" in status.lower():
                    Database().remove_credits(user_id, credits=1)
                    deads += 1
                    creditos_removidos += 1
                else:
                    errors += 1

                bin_info = bins.get(card[:6], {})
                text_ccs += f"""<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{card}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>{status}</b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Response: <code>{msg}</code>
━━━━━━━━━━━━━━━━━━━━
"""

            except Exception as e:
                errors += 1
                print(f"Error checking card: {str(e)}")

        # Resultados finales
        final = perf_counter() - ini
        
        text = f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Mass Results
━━━━━━━━━━━━━━━━━━━━
{text_ccs}━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{m.from_user.username} [{rol}]
<a href="https://t.me/zyrexnews">ゕ</a>﹒Gateway: <code>{gate_name}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Time: <code>{final:0.2}s</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Results: {approveds} ✅ | {deads} ❌ | {errors} ⚠️
<a href="https://t.me/zyrexnews">ゕ</a>﹒Credits Left: <code>{credits}</code>
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""

        await msg_bot.edit(text, reply_markup=button)

    except Exception as e:
        print(f"Error in mass checker: {str(e)}")
        await m.reply(f"❌ Error: {str(e)}") 