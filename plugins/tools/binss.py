from pyrogram import Client, filters
from functions.database import Database
from functions.variables import PREFIXES
from functions.functions import get_bin_info
import json

@Client.on_message(filters.command("bin", PREFIXES))
async def bin_lookup(client, message):
    # Check bot status
    try:
        with open("functions/botstatus.json", "r") as file:
            bot_state = json.load(file)
        if bot_state.get("state"):
            return await message.reply(f"El bot se encuentra en mantenimiento\nRazón: {bot_state['reason']}")
    except Exception:
        pass

    # Basic validation
    if len(message.command) < 2 or len(message.command[1]) < 6:
        return await message.reply(
            f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Bin Lookup\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Uso: <code>/bin [BIN]</code>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"࿔ Bot Version: 1.0",
            disable_web_page_preview=True
        )

    bin_number = message.command[1][:6]
    user_id = message.from_user.id

    # Database verification
    with Database() as db:
        if not db.get_info_user(user_id):
            return await message.reply("<b>You are not registered, use /register to start.</b>")
        if not db.is_authorized(user_id, message.chat.id):
            return await message.reply("<b>Unauthorized user or chat.</b>")

    try:
        # Fetch BIN data using existing project function
        data = await get_bin_info(bin_number)
        
        if data:
            # Handle both possible API response formats and local DB fallback
            bin_data = data.get('BIN', data)
            brand = bin_data.get('scheme') or bin_data.get('brand', 'N/A')
            ctype = bin_data.get('type') or bin_data.get('category', 'N/A')
            level = bin_data.get('level', 'N/A')

            # Extract issuer and country safely
            issuer = bin_data.get('issuer')
            bank = 'N/A'
            if isinstance(issuer, dict):
                bank = issuer.get('name') or bin_data.get('bank_name') or bin_data.get('bank') or 'N/A'
            else:
                bank = bin_data.get('bank_name') or bin_data.get('bank') or 'N/A'

            country_obj = bin_data.get('country')
            if isinstance(country_obj, dict):
                country = country_obj.get('name') or bin_data.get('country_name') or 'N/A'
                flag = country_obj.get('flag') or bin_data.get('flag', '')
            else:
                country = bin_data.get('country_name') or bin_data.get('country', 'N/A')
                flag = bin_data.get('flag', '')

            response = (
                f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Bin Lookup\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒<b>Bin</b>: <code>{bin_number}</code>\n"
                f"<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒<b>Info</b>: <code>{brand} - {ctype} - {level}</code>\n"
                f"<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒<b>Bank</b>: <code>{bank}</code>\n"
                f"<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒<b>Country</b>: <code>{country} {flag}</code>\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"࿔ Bot Version: 1.0"
            )
            return await message.reply(response, disable_web_page_preview=True)
            
        else:
            return await message.reply(
                f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Razón: <code>Bin no encontrado.</code>\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"࿔ Bot Version: 1.0",
                disable_web_page_preview=True
            )

    except Exception as e:
        return await message.reply(
            f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Razón: <code>Error conectando a la API: {str(e)}</code>\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"࿔ Bot Version: 1.0",
            disable_web_page_preview=True
        )
