import os, sys
from functions.database import Database
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
from functions.variables import PREFIXES

@Client.on_message(filters.command("reiniciar", PREFIXES))
async def rbot(client: Client, m: Message):
    with Database() as db:
        if not db.is_owner(m.from_user.id):
            return
    m1 = await m.reply("<b>Restarting bot...</b>", quote=True)
    await sleep(1.5)
    await m1.edit("<b>Bot restarted ✅ Please wait 3 seconds</b>")
    os.execl(sys.executable, sys.executable, "-B", *sys.argv)