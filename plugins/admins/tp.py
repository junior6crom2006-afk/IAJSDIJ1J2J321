from pyrogram import Client, filters
from functions.database import Database
from functions.variables import PREFIXES, CHANNEL_ID_MEMBER_CONTROL
from functions.functions import Symbol as GetSymbol, GetTelegramID
import datetime

@Client.on_message(filters.command("tp", PREFIXES))
async def Admins(CLIENT, message):
    ## INFO
    USER_INFO = message.from_user
    USER_FIRST_NAME = USER_INFO.first_name
    USER_ID = USER_INFO.id

    ## VERIFICATION IN THE DATABASE
    db = Database()
    USER_INFO_DB = db.get_info_user(USER_ID)
    if USER_INFO_DB is None:
        return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒You are not registered, use the /register command to register</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                   quote=True, disable_web_page_preview=True)

    ## CHECK IF YOU HAVE PERMISSIONS
    STAFF = db.is_seller_or_owner(USER_ID)
    if STAFF:
        plan = "Premium"
        ## CHECK IF YOU REPLY TO A FORWARDED MESSAGE AND YOU HAVE THE DAYS
        if hasattr(message.reply_to_message, "from_user") and message.reply_to_message.id and len(message.command) > 1:
            try:
                DAY = int(message.command[1])
                CLIENT_ID = int(message.reply_to_message.from_user.id)
                if len(message.command) > 2 and message.command[2].upper() in ["PREMIUM", "VIP"]:
                    plan = message.command[2].capitalize()
            except ValueError:
                return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Verify that it is numeric</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
        ## CHECK IF YOU HAVE THE DAYS AND THE ID
        elif len(message.command) > 2:
            try:
                CLIENT_ID = int(message.command[1])
                DAY = int(message.command[2])
                if len(message.command) > 3 and message.command[3].upper() in ["PREMIUM", "VIP"]:
                    plan = message.command[3].capitalize()
            except ValueError:
                return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Verify that it is numeric</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
        ## ELSE
        else:
            return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Reply, forward and reply to the message or send the id of the one you want to add days <code>/{message.command[0]} [ID] [DAY] [PLAN]</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                       quote=True, disable_web_page_preview=True)
        
        CLIENT_INFO_DB = db.get_info_user(CLIENT_ID)
        if CLIENT_INFO_DB is None:
            return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Not registered</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                       quote=True, disable_web_page_preview=True)
        
        CLIENT_ID = CLIENT_INFO_DB.get("ID")
        CLIENT_USERNAME = CLIENT_INFO_DB.get("USERNAME")
        
        # Aquí se añade la lógica para sumar días sin reiniciar créditos
        current_expiration = CLIENT_INFO_DB.get("EXPIRATION")
        if current_expiration:
            current_expiration_date = datetime.datetime.strptime(current_expiration, "%Y-%m-%d %H:%M:%S")
            new_expiration_date = current_expiration_date + datetime.timedelta(days=DAY)
        else:
            new_expiration_date = datetime.datetime.now() + datetime.timedelta(days=DAY)

        # Convierte la nueva fecha de expiración a cadena
        new_expiration_date_str = new_expiration_date.strftime("%Y-%m-%d %H:%M:%S")

        # Actualiza la membresía con la nueva fecha de expiración
        ADD_PREMIUM = db.add_premium_membership(CLIENT_ID, new_expiration_date_str, plan)
        if ADD_PREMIUM is None:
            return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Not registered</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                       quote=True, disable_web_page_preview=True)
        
        await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒The user now has {DAY} additional days</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Plan: {plan}</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                            quote=True, disable_web_page_preview=True)
