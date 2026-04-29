from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from functions.variables import PREFIXES
from functions.functions import get_text_from_pyrogram, get_bin_info
from functions.generator_cc import Utils
from functions.database import Database
import json 
import re

@Client.on_message(filters.command('gen', PREFIXES))
async def gen_command(client, m):
    # Check bot status
    try:
        with open("functions/botstatus.json", "r") as file:
            bot_state = json.load(file)
        if bot_state.get("state"):
            return await m.reply(f"El bot se encuentra en mantenimiento\nRazón: {bot_state['reason']}")
    except Exception:
        pass

    try:
        text = await get_text_from_pyrogram(m, True)
        if not text:
            return await m.reply(
                f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Generator\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Uso: <code>/gen [BIN]</code>\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"࿔ Bot Version: 1.0",
                disable_web_page_preview=True
            )

        # Process components
        parts = text.replace('/', ' ').replace(':', ' ').split()
        cc_number = parts[0]
        
        if len(parts) >= 2:
            mes = parts[1]
            ano = parts[2] if len(parts) > 2 else '2024'
            if len(ano) == 2: ano = f"20{ano}"
            if len(cc_number) < 16: cc_number = f"{cc_number}{'x' * (16-len(cc_number))}"
            display_text = f"{cc_number}|{mes}|{ano}|rnd"
        else:
            display_text = text
            
        # Database check
        with Database() as db:
            userid = m.from_user.id
            if not db.is_premium(userid):
                return await m.reply(
                    f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No eres premium. Contacta a @tocandotee\n"
                    f"━━━━━━━━━━━━━━━━━━━━\n"
                    f"࿔ Bot Version: 1.0",
                    disable_web_page_preview=True
                )
        
            # BIN validation
        bin_search = re.findall(r'^\d{6}', display_text.split('|')[0])
        if not bin_search:
            raise ValueError("Invalid BIN")
            
        bin_number = bin_search[0]
        bin_info = await get_bin_info(bin_number)
        if not bin_info:
            return await m.reply("<b>Bin not found</b>", quote=True)
            
        # Generate Cards
        ccs = Utils.cc_genv(display_text)
        if not ccs:
            raise ValueError("Invalid Format")
            
        formatted_ccs = "\n".join([f"<code>{cc}</code>" for cc in ccs])
        
        # Robust extraction for template
        bin_data = bin_info.get("BIN", bin_info)
        brand = bin_data.get("brand", "N/A")
        type_v = bin_data.get("type", "UNAVAILABLE")
        level = bin_data.get("level", "UNAVAILABLE")
        
        # Extract Bank (Issuer)
        issuer = bin_data.get("issuer", {})
        bank = issuer.get("name") if isinstance(issuer, dict) else bin_data.get("bank_name", "N/A")
        if not bank: bank = bin_data.get("bank_name", "N/A")
        
        # Extract Country and Flag
        country_obj = bin_data.get("country", {})
        country = country_obj.get("name") if isinstance(country_obj, dict) else bin_data.get("country_name", "N/A")
        if not country: country = bin_data.get("country_name", "N/A")
        
        flag = country_obj.get("flag") if isinstance(country_obj, dict) else bin_data.get("flag", "")
        if not flag: flag = bin_data.get("flag", "")
        
        response_text = f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Generator
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Bin</b>: <code>{display_text}</code>
━━━━━━━━━━━━━━━━━━━━
{formatted_ccs}
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Info</b>: <code>{brand} - {type_v} - {level}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Bank</b>: <code>{bank}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Country</b>: <code>{country} {flag}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Req by</b>: @{m.from_user.username if m.from_user.username else m.from_user.id}
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""

        buttons = InlineKeyboardMarkup([[
            InlineKeyboardButton("Re-gen", callback_data=f"regen_{display_text}"),
            InlineKeyboardButton("Updates", callback_data="https://t.me/zyrexnews")
        ]])
        
        await m.reply(response_text, quote=True, reply_markup=buttons, disable_web_page_preview=True)
        
    except Exception:
        return await m.reply(
            f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Formato inválido: <code>/gen 412345667</code>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"࿔ Bot Version: 1.0",
            disable_web_page_preview=True
        )
