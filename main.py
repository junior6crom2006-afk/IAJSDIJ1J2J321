import logging
import threading
import os
from flask import Flask

from huepy import bold, green
from functions.variables import API_ID, API_HASH, BOT_TOKEN, NAME_BOT
from pyrogram import Client
from pyrogram.enums import ParseMode
from watcher import start_watcher_in_thread

# LOGS
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# FLASK APP (para Render)
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot activo ✅"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host="0.0.0.0", port=port)

# BOT
app = Client(
    NAME_BOT,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins"),
    parse_mode=ParseMode.HTML
)

def run_bot():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    watcher = start_watcher_in_thread(current_directory)

    print(bold(green("Iniciando Zyrex Checker 1.0 Beta 「♚」")))

    try:
        app.run()
    except KeyboardInterrupt:
        watcher.stop()

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    run_bot()