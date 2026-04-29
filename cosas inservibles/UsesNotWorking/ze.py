from pyrogram import Client, filters
from gates.ad import pf
from functions.functions import ProxyRandom, GetCC, Symbol, AntiSpam
from functions.database import Database
from functions.variables import PREFIXES
import time

@Client.on_message(filters.command('ze', PREFIXES,))
async def gate_kv(client, message):
    with Database() as db:
         userid = message.from_user.id
         kk = db.is_premium(userid)
         if False == kk:
             return await message.reply(f"{symbol} No eres premium Contacta A @tocandotee")
         else:
            user_info = db.get_info_user(userid)
            is_free_user = user_info["MEMBERSHIP"]
            is_free_user = is_free_user.lower() == "free user"
            rol = user_info["RANK"]
    antispam = await AntiSpam(userid, user_info["ANTISPAM"], is_free_user)
    if antispam != False: 
        return await message.reply(f"{symbol}<b>[ANTISPAM] ESPERE {antispam}s PARA EL PROXIMO CHECKEO</b>")
    start_time = time.time()
    symbol = await Symbol()
    kk = await GetCC(message.text)
    if not kk:
        await message.reply(f"{symbol}<b> Inserta Una CC en este formato : CC|MONTH|YEAR|CVV</b>", quote=True)
        return
    cc = kk[0]
    mes = kk[1]
    ano = kk[2]
    cvv = kk[3]

    card = f"{cc}|{mes}|{ano}|{cvv}"
    serie = cc[0:6]

    # Send initial message
    symbol = await Symbol()
    msgedit = await client.send_message(chat_id=message.chat.id, text=f"""
<b>{symbol} <b>Gateway: Payflow + B3 CCN </b> (/ze) 
<b>{symbol} <b>Status: Apagado ⚠️</b>
<b>{symbol} <b>Razon: Sitio DD ⚠️</b>""", reply_to_message_id=message.id)