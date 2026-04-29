from pyrogram import Client, filters
from functions.database import Database
from functions.variables import PREFIXES, CHANNEL_ID_MEMBER_CONTROL
from functions.functions import Symbol as GetSymbol, GetTelegramID

@Client.on_message(filters.command("reset", PREFIXES))
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
        ## CHECK IF YOU REPLY TO A FORWARDED MESSAGE AND YOU HAVE THE DAYS AND CREDITS
        if hasattr(message.reply_to_message, "from_user") and message.reply_to_message.id:
            try:
                CLIENT_ID = int(message.reply_to_message.from_user.id)
            except:
                return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Verify that it is a numeric</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
        ## CHECK IF YOU HAVE THE DAYS, CREDITS AND THE ID
        elif len(message.command) > 1:
            try:
                CLIENT_ID = int(message.command[1])
            except:
                return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Verify that it is a numeric</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                           quote=True, disable_web_page_preview=True)
        ## ELSE
        else:
            return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Reply, forward and reply to the message or send the id of the one you want to remove premium <code>/{message.command[0]} [ID]</code></b>
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
        
        TEXT = f"""<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Delete Premium</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒User to who premium was deleted: @{CLIENT_USERNAME} | <code>{CLIENT_ID}</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Added by: {await GetTelegramID(USER_ID, USER_FIRST_NAME)} [{USER_INFO_DB.get("RANK").upper() if "¿?" == USER_INFO_DB.get("NICK") else USER_INFO_DB.get("NICK")}]</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
"""
        
        DELETE_PREMIUM = db.rename_premium(CLIENT_ID)
        if DELETE_PREMIUM is None:
            return await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Not registered</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                       quote=True, disable_web_page_preview=True)
        
        if DELETE_PREMIUM:
            await message.reply(f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒User {CLIENT_ID} has been removed from premium</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
""",
                                quote=True, disable_web_page_preview=True)
        
        await CLIENT.send_message(CHANNEL_ID_MEMBER_CONTROL, TEXT)
