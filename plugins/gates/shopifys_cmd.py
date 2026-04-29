import traceback, re, asyncio, time
from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from pyrogram.enums import ParseMode
from functions.database import Database
from functions.functions import (
    get_bin_info,
    GetCC,
    AntiSpam,
    get_text_from_pyrogram,
    ProxyRandom,
    Symbol,
)

async def user_not_premium(m: Message, button) -> Message:
    return await m.reply(
        f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No eres premium. Contacta a @tocandotee\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0",
        reply_markup=button,
        quote=True,
    )

async def user_not_vip(m: Message, button) -> Message:
    return await m.reply(
        f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No eres VIP. Contacta a @tocandotee\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0",
        reply_markup=button,
        quote=True,
    )


from functions.variables import PREFIXES
from gates.shopifys import get_response_gate, cmds, get_gate_by_cmd, gates_data
from os import getenv
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Buy", url="https://t.me/tocandotee"),
            InlineKeyboardButton(
                "Channel", url="https://t.me/ZyrexRefes"
            ),
        ],
    ]
)


button_explication = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Explicacion", "explication")]]
)

info_response_cache = {}
antispam_button = {}

ID_OWNER = getenv("ID_OWNER")


@Client.on_message(filters.command(list(cmds), PREFIXES))  # type: ignore
async def shopifys(client: Client, m: Message):
    with open("functions/botstatus.json", "r") as file:
        bot_state = json.load(file)
    
    if bot_state["state"]:
        return await m.reply(f"El bot Se Encuentra En Mantenimiento\nRazón: {bot_state['reason']}")
    symbol = await Symbol()
    user_id = m.from_user.id
    cmd = m.command[0]
    gateway = get_gate_by_cmd(cmd, gates_data)
    if gateway is None:
        return await m.reply("Gate not found")
    type_gate = gateway["type"].lower()  # type: ignore
    with Database() as db:
        is_premium = db.is_premium(user_id)
        user_info = db.get_info_user(user_id)
        if user_info is None:
            user_info = {}
        credits = int(user_info.get("CREDITS", 0))
        
        if cmd in ["sd", "gd"] and credits < 0: ## aqui pones los gate que quieres que cobren credito
            return await m.reply(
                f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No tienes créditos suficientes. Contacta a @tocandotee\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0",
                reply_markup=button,
                quote=True,
            )

        if type_gate == "premium":
            if not is_premium:
                await user_not_premium(m, button)
                return
        elif type_gate == "vip":
            if not db.is_vip(user_id):
                await user_not_vip(m, button)
                return
        elif type_gate == "free":
            if not db.is_authorized(user_id, m.chat.id):
                return await m.reply(
                    f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No estás autorizado en este chat.\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0",
                    reply_markup=button,
                    quote=True,
                )

        user_info = db.get_info_user(user_id)
        if user_info is None:
            user_info = {}
        membership = str(user_info.get("MEMBERSHIP", "free"))

    gateway_name = gateway["gate"]  # type: ignore
    site = gateway["site"]  # type: ignore
    text = await get_text_from_pyrogram(m)  # Asegúrate de esperar la corutina
    ccs = await GetCC(text)  # Asegúrate de esperar la corutina
    if not ccs:
        return await m.reply(
            f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Bin incorrecto o inexistente 🔹\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0",
            reply_markup=button,
            quote=True,
        )
    cc = ccs[0]  # type: ignore
    mes = ccs[1]  # type: ignore
    ano = ccs[2]  # type: ignore
    cvv = ccs[3]  # type: ignore
    start_time2 = time.time()
    resp = await get_bin_info(cc[0:6])
    if not isinstance(resp, dict):
        return await m.reply(
            f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Bin incorrecto o inexistente 🔹\n━━━━━━━━━━━━━━━━━━━━\n࿔ Bot Version: 1.0",
            quote=True,
        )
    bin_data = resp.get("BIN", resp)
    serie = bin_data.get("bin", cc[0:6])
    brand = bin_data.get("brand", "N/A")
    level = bin_data.get("level", "N/A")
    type_v = bin_data.get("type", "N/A")
    bank = bin_data.get("issuer", {}).get("name", "N/A") if isinstance(bin_data.get("issuer"), dict) else bin_data.get("bank_name", "N/A")
    country = bin_data.get("country", {}).get("name", "N/A") if isinstance(bin_data.get("country"), dict) else bin_data.get("country_name", "N/A")
    flag = bin_data.get("country", {}).get("flag", "") if isinstance(bin_data.get("country"), dict) else bin_data.get("flag", "")
    rol = str(user_info.get("RANK", "user")).capitalize()
    # nick = user_info["NICK"]
    if user_id not in [7882956639] and (
        resp.get("banned", False) or "prepaid" in level.lower() or "prepaid" in type_v.lower()
    ):
        return await m.reply(
            f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{serie}</code>\nBin banned, operation prohibited
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0""",
            reply_markup=button,
            quote=True,
        )  # check antispam
    antispam = await AntiSpam(user_id, is_mass=False, membership=membership)
    if antispam:
        return await m.reply(f"<b>[ANTISPAM] ESPERE {antispam}s PARA EL PROXIMO CHECKEO</b>")

    # Envío del mensaje inicial con indicador amarillo
    taken2 = round(time.time() - start_time2, 2) if 'start_time2' in locals() else 0.0
    msg_to_edit = await m.reply(
        f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | {gateway_name} (/{cmd})
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>Checking...</b>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{cc[:6]}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{brand}</code> - <code>{level}</code> - <code>{type_v}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{bank}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{country}</code> - <code>{flag}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: Live!✅
<a href="https://t.me/zyrexnews">ゕ</a>﹒Time: <code>{taken2}s</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{m.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0
""",
        reply_markup=button,
        quote=True,
    )

    # tries = k0
    # while tries < 3:
    #     try:

    #max_intentos = 10
    #intentos = 0

    result = await get_response_gate(cmd, cc, mes, ano, cvv, is_premium, credits, user_id)  # type: ignore
    if not result:
        return await msg_to_edit.edit(f"<b>Error!</b>")
    if isinstance(result, Exception):
        e = result

        try:
            await client.send_message(
                7882956639,  # Admin logs
                f"""Gate: /{cmd}
{e}
CC: <code>{cc}|{mes}|{ano}|{cvv}</code>""",
                disable_web_page_preview=True,
            )
        except Exception:
            pass
        traceback.print_exception(type(e), e, e.__traceback__)
        return await msg_to_edit.edit(
            f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | {gateway_name} (/{cmd})
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>Error ❌</b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Response: <code>{e}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{cc[:6]}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{brand}</code> - <code>{level}</code> - <code>{type_v}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{bank}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{country}</code> - <code>{flag}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: Live!✅
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{m.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""
        )

    result = result % f"{m.from_user.username} [{rol}]</b>"

    await msg_to_edit.edit(result, reply_markup=button, disable_web_page_preview=True)