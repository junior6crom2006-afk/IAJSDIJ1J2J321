from functions.autosh import autoshopify
from json import load
from pyrogram.types import Message
from functions.functions import get_bin_info, Symbol
from functions.database import Database

with open("json/gates.json", "r", encoding="utf-8-sig") as json_file:
    gates_data = load(json_file)

cmds = set(gate["cmd"] for gate in gates_data)
HEADERS_BASE = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "es,es-ES;q=0.9,en;q=0.8,pt;q=0.7,am;q=0.6",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


async def get_response_gate(
    cmd: str,
    card: str,
    month: str,
    year: str,
    cvv: str,
    is_premium: bool,
    credits: int,
    user_id: int,
) -> str:
    if cmd not in cmds:
        raise ValueError("Cmd not found")
    gate = get_gate_by_cmd(cmd, gates_data)
    # Verificar que el gate obtenido es el correcto
    if gate is None:
        return "<b>Gate not found for the provided cmd</b>"
    site = gate["site"]
    product = gate["product"]

    if not site.startswith("https://"):
        site = "https://" + site
    name_gateway = gate["gate"]


    # BIN INFO SAFETY HANDLER
    bin_info = await get_bin_info(card[0:6])
    if bin_info is None:
        return "<b>Incorrect or non-existent bin 🔹</b>"
    
    bin_data = bin_info.get("BIN", bin_info)
    serie = bin_data.get("bin", card[0:6])
    brand = bin_data.get("brand", "N/A")
    country = bin_data.get("country", {}).get("name", "N/A") if isinstance(bin_data.get("country"), dict) else bin_data.get("country_name", "N/A")
    flag = bin_data.get("country", {}).get("flag", "") if isinstance(bin_data.get("country"), dict) else bin_data.get("flag", "")
    bank = bin_data.get("issuer", {}).get("name", "N/A") if isinstance(bin_data.get("issuer"), dict) else bin_data.get("bank_name", "N/A")
    level = bin_data.get("level", "N/A")
    type_v = bin_data.get("type", "N/A")

    try:
        response = await autoshopify(
            site, card, month, year, cvv, is_premium, credits, product
        )
    except Exception as e:
        return e

    response_gate = (
        response["response"] if response and "response" in response else "UNAVAILABLE"
    )
    total_price = (
        response["total"] if response and "total" in response else "UNAVAILABLE"
    )
    time = response["time"] if response and "time" in response else "UNAVAILABLE"

    if cmd in ["py"]:
        if "Address not Verified - Insufficient Funds" in response_gate:
            Database().remove_credits(user_id, credits=2)
        elif f"Charged ${total_price[:2]}" in response_gate:
            Database().remove_credits(user_id, credits=2)
        elif "Address not Verified - Approved" in response_gate:
            Database().remove_credits(user_id, credits=2)
        elif "Transaction Normal - Insufficient Funds" in response_gate:
            Database().remove_credits(user_id, credits=2)
        else:
            Database().remove_credits(user_id, credits=1)
    cc_formatted = f"{card}|{month}|{year}|{cvv}"

    # Final Premium Response
    return f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | {name_gateway} [<code>${total_price[:2]}</code>] (/{cmd})
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{cc_formatted}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>{response['status']}</b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Response: <code>{response_gate}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{serie}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{brand}</code> - <code>{level}</code> - <code>{type_v}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{bank}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{country}</code> - <code>{flag}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: Live!✅
<a href="https://t.me/zyrexnews">ゕ</a>﹒Time: <code>{time}s</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @%s
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""


def get_gate_by_cmd(cmd_to_find: str, gates_data) -> dict | None:
    for gate in gates_data:
        if gate["cmd"] == cmd_to_find:
            return gate
    return None