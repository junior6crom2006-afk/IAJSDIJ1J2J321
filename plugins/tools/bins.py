import re
from pyrogram import Client, filters
from httpx import AsyncClient

# Define tus prefijos (puedes agregar más: '/', '!', '.')
PREFIXES = ['/', '.', '!']

@Client.on_message(filters.command('binz', prefixes=PREFIXES))
async def binz(client, message):
    # Obtener el texto del mensaje (reply o directo)
    text = message.text
    if message.reply_to_message:
        text = message.reply_to_message.text

    # Buscar los primeros 6 dígitos (BIN)
    bin_match = re.findall(r'\d{6,}', text)
    if not bin_match:
        return await message.reply("❌ No se encontró un BIN válido. Formato: /binz 123456")
    
    bin_number = bin_match[0][:6]   # Solo primeros 6 dígitos

    async with AsyncClient() as session:
        try:
            response = await session.get(f"https://api.bins.zone/v2/bin/{bin_number}")
            if response.status_code != 200:
                return await message.reply("❌ Error en la API. Intenta más tarde.", quote=True)

            data = response.json()
            # Extraer datos con valores por defecto seguros
            bank = data.get("data", {}).get("bank", "N/A")
            brand = data.get("data", {}).get("brand", "N/A")
            country_name = data.get("data", {}).get("country", "N/A")
            country_flag = data.get("data", {}).get("country_flag", "🏳️")
            level = data.get("data", {}).get("level", "N/A")
            type_ = data.get("data", {}).get("type", "N/A")

            # Construir mensaje
            msg = f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Api Binz Zone 🔍
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Bin</b>: <code>{bin_number}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Country</b>: <code>{country_name}</code> - <code>{country_flag}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Vendor</b>: <code>{brand}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Type</b>: <code>{type_}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Level</b>: <code>{level}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Bank</b>: <code>{bank}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒<b>Req</b>: {message.from_user.mention}
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""
            await message.reply(msg, quote=True, disable_web_page_preview=True)

        except Exception as e:
            await message.reply(f"❌ Error interno: {str(e)}", quote=True)