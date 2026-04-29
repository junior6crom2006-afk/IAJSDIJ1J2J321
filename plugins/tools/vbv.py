from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from gates.payflowpro import payflow
from functions.functions import ProxyRandom, GetCC, Symbol, get_bin_info, AntiSpam
from functions.database import Database
from functions.variables import PREFIXES
import time
import httpx
import json
keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Buy", url="https://t.me/tocandotee"),
        InlineKeyboardButton("Channel", url="https://t.me/ZyrexRefes")
    ]
])

@Client.on_message(filters.command('vbv', PREFIXES))
async def gate_vbv (client, message):
    with open("functions/botstatus.json", "r") as file:
        bot_state = json.load(file)
    
    if bot_state["state"]:
        return await message.reply(f"El bot Se Encuentra En Mantenimiento\nRazón: {bot_state['reason']}")
    with Database() as db:
        userid = message.from_user.id
        symbol = await Symbol()
        if not db.is_premium(userid):
            return await message.reply(f"{symbol} No eres premium Contacta A @tocandotee")
        
        user_info = db.get_info_user(userid)
        antispam = await AntiSpam(userid, is_mass=False, membership=user_info["MEMBERSHIP"])
        if antispam:
            return await message.reply(f"{symbol}<b>[ANTISPAM] ESPERE {antispam}s PARA EL PROXIMO CHECKEO</b>")
        
        start_time = time.time()
        kk = await GetCC(message.text)
        if not kk:
            await message.reply(f"{symbol}<b>Please Enter A Valid Card! ⚠️</b>", quote=True)
            return
        
        cc, mes, ano, cvv = kk
        card = f"{cc}|{mes}|{ano}|{cvv}"
        serie = cc[:6]
        resp = await get_bin_info(serie)
        if resp is None:
            return await message.reply("<b>Bin Not Found ⚠️</b>", quote=True)
        
        if message.from_user.id not in [6712112939] and (resp["banned"] or "prepaid" in resp["level"].lower() or "prepaid" in resp["type"].lower()):
            return await message.reply(f"<b>Bin: <code>{resp['bin']}</code>\nBin banned, operation prohibited</b>")
        
        msgedit = await client.send_message(chat_id=message.chat.id, text=f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | B3 VBV (/vbv)
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{card}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>Checking...</b>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{serie}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{resp['brand']}</code> - <code>{resp['level']}</code> - <code>{resp['type']}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{resp.get('bank_name', 'N/A')}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{resp.get('country_name', 'N/A')}</code> - <code>{resp.get('flag', '')}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: Live!✅
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{message.from_user.username} [{user_info["RANK"].capitalize()}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0""", reply_to_message_id=message.id)

        async with httpx.AsyncClient() as session:
            vbv_response = await session.get(f"https://minostbug.com/api/vbv.php?bin={serie}")
            vbv_data = vbv_response.json()
            vbv_status = vbv_data[0]["resultado"] if isinstance(vbv_data, list) and vbv_data else "No data"

        if "Authenticate Successful ✅" in vbv_status:
            response = "Approved ✅"
        elif "Authenticate Attempt Successful ✅" in vbv_status:
            response = "Approved ✅"
        else:
            response = "Declined ❌"

        taken = round(time.time() - start_time, 2)
        await msgedit.edit_text(text=f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | B3 VBV (/vbv)
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{card}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>{response}</b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Response: <code>{vbv_status}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{serie}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{resp['brand']}</code> - <code>{resp['level']}</code> - <code>{resp['type']}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{resp.get('bank_name', 'N/A')}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{resp.get('country_name', 'N/A')}</code> - <code>{resp.get('flag', '')}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: Live!✅
<a href="https://t.me/zyrexnews">ゕ</a>﹒Time: <code>{taken}s</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{message.from_user.username} [{user_info["RANK"].capitalize()}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0""", reply_markup=keyboard)
