import time
from functools import wraps
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functions.functions import Symbol, GetCC, get_bin_info, AntiSpam, proxy_x
from functions.gate_manager import GateManager
from functions.database import Database

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Buy", url="https://t.me/tocandotee"),
        InlineKeyboardButton("Channel", url="https://t.me/ZyrexRefes")
    ]
])

def check_gate(command: str, gateway_name: str = "Gateway", required_credits: int = 3):
    """
    Manager global para verificar el estado de los gates, si el usuario es premium
    y creditos necesarios. Implementa Zyrex aesthetics.
    El handler debe retornar un string y un mensaje: `return status, response`
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message, *args, **kwargs):
            symbol = await Symbol()
            userid = message.from_user.id
            
            # 1. Verificar estado del gate
            gate_info = GateManager.get_gate_info(command)
            if gate_info["estado"] == "OFF":
                await message.reply_text(f"""<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | {gateway_name} ({command})
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <code>OFF</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Reason: <code>{gate_info['razon']}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Last Revision: <code>{gate_info['ultima_revision']}</code>
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0</b>
""", reply_to_message_id=message.id)
                return

            # 2. DB, premium, creditos
            with Database() as db:
                is_premium = db.is_premium(userid)
                
                # Regla de DM: Solo para Premium o superior
                if message.chat.type.name == "PRIVATE":
                    if not is_premium:
                        await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Los mensajes directos (DM) sólo están habilitados para usuarios Premium y VIP.</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""", quote=True, disable_web_page_preview=True)
                        return
                
                # Regla del Gate
                req_premium = gate_info.get("premium", True)
                if req_premium and not is_premium:
                    await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒No eres premium, contacta a @tocandotee</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
                    return
                elif not req_premium and not is_premium:
                    if not db.is_authorized(userid, message.chat.id):
                        await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒No estás autorizado en este chat.</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""", quote=True, disable_web_page_preview=True)
                        return
                
                user_info = db.get_info_user(userid)
                credits = user_info.get("CREDITS", 0)
                if credits < required_credits:
                    await message.reply(
                        f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒No tienes creditos suficientes, contacta a @tocandotee</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
                    return

            # 3. Antispam
            antispam = await AntiSpam(userid, is_mass=False, membership=user_info["MEMBERSHIP"])
            if antispam:
                await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Debes esperar <code>{antispam}</code> segundos para volver a usar el checker</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
                return

            # 4. GetCC
            if message.reply_to_message and message.reply_to_message.text:
                card_details = await GetCC(message.reply_to_message.text)
            else:
                card_details = await GetCC(message.text)

            if not card_details:
                await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Please Enter A Valid Card! ⚠️</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
                return
            cc, mes, ano, cvv = card_details

            # 5. BIN
            serie = cc[:6]
            resp = await get_bin_info(serie)
            if resp is None:
                await message.reply("""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Bin Not Found ⚠️</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
                return
            
            if userid not in [] and (resp.get("banned") or "prepaid" in resp.get("level", "").lower() or "prepaid" in resp.get("type", "").lower()):
                await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Bin: <code>{resp.get('bin', serie)}</code>\nBin banned, operation prohibited</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
                return

            # Extraer información del BIN de forma robusta
            bin_data = resp.get("BIN", resp)
            brand = bin_data.get('scheme', 'Unknown')
            level = bin_data.get('level', 'Unknown')
            type_v = bin_data.get('type', 'Unknown')
            
            # Extraer banco (Issuer)
            issuer = bin_data.get('issuer', {})
            bank = issuer.get('name', 'Unknown') if isinstance(issuer, dict) else bin_data.get('bank_name', 'Unknown')
            
            # Extraer país y bandera
            country_obj = bin_data.get('country', {})
            country = country_obj.get('name', 'Unknown') if isinstance(country_obj, dict) else bin_data.get('country_name', 'Unknown')
            flag = country_obj.get('flag', '') if isinstance(country_obj, dict) else bin_data.get('flag', '')

            # Revisión de estado de la Proxy/API
            api_code = resp.get('api_code', 200) # Por defecto 200 si viene de DB local sin error
            if api_code == 200:
                ip_info = "Live! ✅"
            else:
                ip_info = f"Dead! ❌ (HTTP {api_code})"
                
            rol = user_info["RANK"]

            processing_text = f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | {gateway_name} ({command})
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>Checking...</b>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{brand}</code> - <code>{type_v}</code> - <code>{level}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{bank}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{country}</code> - <code>{flag}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: <code>{ip_info}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{message.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""
            
            msgedit = await client.send_message(
                chat_id=message.chat.id, 
                text=processing_text, 
                reply_to_message_id=message.id,
                disable_web_page_preview=True
            )
            
            message.symbol = symbol
            message.user_info = user_info
            message.cc, message.mes, message.ano, message.cvv = cc, mes, ano, cvv
            message.msgedit = msgedit

            # Ejecutar plugin gate
            start_time_total = time.time()
            result = await func(client, message, *args, **kwargs)
            
            if not isinstance(result, tuple) or len(result) != 2:
                # Si la funcion retorna algo diferente por x razón, no interfiere.
                return result
            
            status, response = result
            taken_total = round(time.time() - start_time_total, 2)
            
            # Cobro de créditos
            status_l = status.lower()
            if "approved" in status_l or "charged" in status_l or "✅" in status:
                with Database() as db:
                    db.remove_credits(userid, 3)
            elif "declined" in status_l or "❌" in status:
                with Database() as db:
                    db.remove_credits(userid, 1)

            processed_text = f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | {gateway_name} ({command})
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Card: <code>{cc}|{mes}|{ano}|{cvv}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <code>{status}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Response: <code>{response}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Type: <code>{brand}</code> - <code>{type_v}</code> - <code>{level}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Bank: <code>{bank}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Country: <code>{country}</code> - <code>{flag}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Proxy: <code>{ip_info}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Time: <code>{taken_total}s</code>   
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{message.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""
            
            await msgedit.edit_text(
                text=processed_text, 
                reply_markup=keyboard,
                disable_web_page_preview=True
            )
            
        return wrapper
    return decorator
