import random
from pyrogram import Client, filters
from httpx import AsyncClient
from functions.variables import PREFIXES

# Basic list of fake names since the new API doesn't provide them
NAMES = [
    "John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", 
    "William Brown", "Jessica Garcia", "David Martinez", 
    "Sarah Rodriguez", "James Lee", "Ashley Walker"
]

@Client.on_message(filters.command(['dir'], PREFIXES))
async def rand_direction(client, message):
    # Standard Zyrex wait message
    msgedit = await message.reply_text(
        "<b>Please wait a moment while we generate your information...</b>",
        reply_to_message_id=message.id
    )
    
    # Extract the country code and default to US if not provided
    parts = message.text.split()
    prefix = parts[-1].upper() if len(parts) > 1 else "US"
    
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            async with AsyncClient(verify=False) as session:
                url = f"https://zyrex.qzz.io/v1/Tools/dir?country={prefix}"
                headers = {
                    "Authorization": "Bearer zyrex_84g9BVyproH7AIqtKrVuCtWQ3JvM7H6Y"
                }
                
                response = await session.get(url, timeout=10, headers=headers)
                response.raise_for_status()  
                
                # The API returns a proper JSON structure now, not a raw string
                data = response.json()
                
                # Safely extract data objects
                address_info = data.get("address", {})
                country_info = data.get("country", {})
                
                # Map fields
                name = random.choice(NAMES)
                street = address_info.get("street", "N/A")
                city = address_info.get("city", "N/A")
                state = address_info.get("state", "N/A")
                zipcode = address_info.get("zip", "N/A")
                phone = data.get("phone", "N/A")
                
                country_code = country_info.get("code", prefix)
                country_flag = country_info.get("flag", "")
                
                username = message.from_user.username if message.from_user.username else message.from_user.id
                
                # Apply Zyrex premium template
                response_text = f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Address Generator
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Name</b>: <code>{name}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Street</b>: <code>{street}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>City</b>: <code>{city}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>State</b>: <code>{state}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Zip Code</b>: <code>{zipcode}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Country</b>: <code>{country_code} {country_flag}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Phone</b>: <code>{phone}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Req</b>: @{username}
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""
                
                await msgedit.edit_text(text=response_text, disable_web_page_preview=True)
                return  # Success, exit the loop entirely
                
        except Exception as e:
            retry_count += 1
            if retry_count == max_retries:
                error_msg = f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Razón: <code>Fallo en la API ({str(e)})</code>
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""
                await msgedit.edit_text(text=error_msg, disable_web_page_preview=True)
                return
            
            await msgedit.edit_text(f"<b>⚠️ Reintentando... ({retry_count}/{max_retries})</b>")
