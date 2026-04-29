from pyrogram import Client, filters
from functions.database import Database
from functions.variables import PREFIXES
from functions.functions import Symbol, Symbol2, GetTelegramID

@Client.on_message(filters.command(['pkwex'], PREFIXES))
async def promote_kwex(client, message):
    try:
        # INFO
        USER_INFO = message.from_user
        USER_FIRST_NAME = USER_INFO.first_name
        USER_ID = USER_INFO.id

        # VERIFICACIÓN EN LA BASE DE DATOS
        db = Database()
        USER_INFO_DB = db.get_info_user(USER_ID)
        
        if USER_INFO_DB is None:
            return await message.reply(
                f"<b>{await Symbol()} No estás registrado, usa el comando /register para registrarte</b>",
                quote=True
            )

        # VERIFICAR SI TIENE PERMISOS
        if not db.is_owner(USER_ID):
            return await message.reply(
                f"<b>{await Symbol()} Solo los owners pueden usar este comando</b>",
                quote=True
            )

        # VERIFICAR SI SE RESPONDIÓ A UN MENSAJE O SE DIO UN ID
        if message.reply_to_message and hasattr(message.reply_to_message, "from_user"):
            CLIENT_ID = message.reply_to_message.from_user.id
        elif len(message.command) > 1:
            try:
                CLIENT_ID = int(message.command[1])
            except:
                return await message.reply(
                    f"<b>{await Symbol()} Verifica que sea un ID numérico</b>",
                    quote=True
                )
        else:
            return await message.reply(
                f"<b>{await Symbol()} Responde a un mensaje o envía el ID del usuario que quieres promover</b>",
                quote=True
            )

        # VERIFICAR SI EL USUARIO EXISTE EN LA DB
        CLIENT_INFO_DB = db.get_info_user(CLIENT_ID)
        if CLIENT_INFO_DB is None:
            return await message.reply(
                f"<b>{await Symbol()} Usuario no registrado</b>",
                quote=True
            )

        # PROMOVER AL USUARIO
        PROMOTE = db.promote_to_keyword_extractor(CLIENT_ID)
        if PROMOTE:
            await message.reply(
                f"<b>{await Symbol()} Usuario promovido exitosamente a Keyword Extractor</b>",
                quote=True
            )

    except Exception as e:
        await message.reply(f"<b>{await Symbol()} Error: {str(e)}</b>", quote=True)
