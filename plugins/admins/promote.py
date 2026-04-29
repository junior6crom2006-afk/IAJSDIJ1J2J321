from pyrogram import Client, filters
from functions.database import Database
from functions.variables import PREFIXES, CHANNEL_ID_MEMBER_CONTROL
from functions.functions import Symbol as GetSymbol, GetTelegramID

@Client.on_message(filters.command("promote", PREFIXES))
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
    STAFF = db.is_owner(USER_ID)
    if STAFF:
        ## VERIFIES IF YOU REPLY TO A MESSAGE AND HAVE THE RANK
        if hasattr(message.reply_to_message, "from_user") and message.reply_to_message.id and len(message.command) > 1:
            RANK = message.text[len(message.command[0]) + 2:].strip()
            CLIENT_ID = message.reply_to_message.from_user.id
        ## CHECK IF IT HAS THE RANK AND ID
        elif len(message.command) > 2:
            RANK = message.command[2]
            try:
                CLIENT_ID = int(message.command[1])
            except:
                return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Verify that it is a numeric ID</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
        ## ELSE
        else:
            return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Reply, forward and reply to the message or send the id of the one you want to promote <code>/{message.command[0]} [ID] [RANK]</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                       quote=True, disable_web_page_preview=True)
    
        RANK = str(RANK).upper()
        if RANK in ["ADMIN", "SELLER"]:
            CLIENT_INFO_DB = db.get_info_user(CLIENT_ID)
            if CLIENT_INFO_DB is None:
                return await message.reply(f"<b>{await GetSymbol()} Not registered</b>",
                                           quote=True, disable_web_page_preview=True)
            
            CLIENT_ID = CLIENT_INFO_DB.get("ID")
            CLIENT_USERNAME = CLIENT_INFO_DB.get("USERNAME")
            
            TEXT = f"""<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Promote</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Promoted user: @{CLIENT_USERNAME} | <code>{CLIENT_ID}</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Promoted by: {await GetTelegramID(USER_ID, USER_FIRST_NAME)} [{USER_INFO_DB.get("RANK").upper() if "¿?" == USER_INFO_DB.get("NICK") else USER_INFO_DB.get("NICK")}]</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
"""
            
            if RANK == "ADMIN":
                PROMOTE = db.promote_to_admin(CLIENT_ID)
                if PROMOTE:
                    await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Successfully promoted to administrator</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                        quote=True, disable_web_page_preview=True)
                elif PROMOTE is None:
                    return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Not registered</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                               quote=True, disable_web_page_preview=True)
                
            elif RANK == "SELLER":
                PROMOTE = db.promote_to_seller(CLIENT_ID)
                if PROMOTE:
                    await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Successfully promoted to seller</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                        quote=True, disable_web_page_preview=True)
                elif PROMOTE is None:
                    return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Not registered</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                               quote=True, disable_web_page_preview=True)

            if CHANNEL_ID_MEMBER_CONTROL:
                try:
                    await CLIENT.send_message(CHANNEL_ID_MEMBER_CONTROL, TEXT)
                except Exception as e:
                    print(f"Error sending log to channel: {e}")

        else:
            return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Only two roles are supported: Admin and Seller.</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                       quote=True, disable_web_page_preview=True)
