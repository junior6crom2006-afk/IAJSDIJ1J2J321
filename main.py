import logging
from os import name as os_name, system as os_system
from huepy import bold, green
from functions.variables import API_ID, API_HASH, BOT_TOKEN, NAME_BOT
from pyrogram import Client
from pyrogram.enums import ParseMode
import json
from functools import wraps
from watcher import start_watcher_in_thread
import os

# CLEAR CONSOLE
if os_name == "nt": os_system("cls") 
else: os_system("clear")

# LOGS

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)


# CONFIGURE CLIENT
app = Client(
    NAME_BOT,
    api_id =  API_ID,
    api_hash = API_HASH,
    bot_token = BOT_TOKEN,
    plugins = dict(root="plugins"),
    parse_mode=ParseMode.HTML
)

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    watcher = start_watcher_in_thread(current_directory)
    
    try:
        print(bold(green(f"Iniciando Zyrex Checker 1.0 Beta 「♚」")))
        app.run()
    except KeyboardInterrupt:
        watcher.stop()