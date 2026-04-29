import time, httpx
from pyrogram import Client, filters
from pyrogram.types import Message
from functions.database import Database
from functions.variables import PREFIXES
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import httpx
from httpx import Response

headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}




@Client.on_message(filters.command("broad", PREFIXES))
async def broad(client: Client, m: Message):
    with Database() as db:
        if not db.is_owner(m.from_user.id):
            return
        message_reply = m.reply_to_message
        msj = (
            m.reply_to_message.id
            if message_reply
            else m.text[len(m.command[0]) + 2 :].strip()
        )
        if not msj:
            return await m.reply("♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Error\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒No messages to send")
        chats_ids = db.get_chats_ids()
        succesfulls = 0
        client_http = httpx.Client(headers=headers)
        try:
            function_partial = partial(
                send_message, text=msj, client=client_http, bot_token=client.bot_token
            )

            if message_reply:
                function_partial = partial(
                    forward_message,
                    from_chat_id=m.chat.id,
                    message_id=msj,
                    client=client_http,
                    bot_token=client.bot_token,
                )
            with ThreadPoolExecutor() as executor:
                results = executor.map(function_partial, chats_ids)
                for r in results:
                    if r:
                        succesfulls += 1
        except BaseException as e:
            print(e)
        await m.reply(
            f"♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Success\n━━━━━━━━━━━━━━━━━━━━\n<a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Message successfully sent to <code>{succesfulls}</code> chats!",
            quote=True,
        )


def send_message(chat_id, text, client, bot_token) -> bool | httpx.Response:
    url_base = f"https://api.telegram.org/bot{bot_token}/"
    url = url_base + "sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
    }
    tries = 0
    while tries <= 3:
        if tries == 3:
            return False
        try:
            response = client.post(url, data=data, timeout=5)
            response_json = response.json()
            if response_json["ok"]:
                return response
            description_error = response_json["description"].lower()
            if (
                "forbidden" in description_error
                or "blocked" in description_error
                or "bad request" in description_error
            ):
                return False
            tries += 1
            time.sleep(5)
        except Exception as e:
            tries += 1
            time.sleep(5)


def forward_message(
    chat_id, from_chat_id, message_id, client, bot_token
) -> bool | httpx.Response:
    url_base = f"https://api.telegram.org/bot{bot_token}/"
    url = url_base + "forwardMessage"
    data = {
        "chat_id": chat_id,
        "from_chat_id": from_chat_id,
        "message_id": message_id,
    }
    tries = 0
    while tries <= 3:
        if tries == 3:
            return False
        try:
            response = client.post(url, data=data, timeout=5)
            response_json = response.json()
            if response_json["ok"]:
                return response
            description_error = response_json["description"].lower()
            if (
                "forbidden" in description_error
                or "blocked" in description_error
                or "bad request" in description_error
            ):
                return False
            tries += 1
            time.sleep(5)
        except Exception as e:
            tries += 1
            time.sleep(5)
