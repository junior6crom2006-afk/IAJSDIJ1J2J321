import json
import os
import traceback
from functions.autosh import autoshopify
from httpx import AsyncClient
from pyrogram import Client, filters
from pyrogram.types import Message
from functions.database import Database
from functions.functions import Symbol
from functions.variables import PREFIXES
from validators import url as url_validator
from bs4 import BeautifulSoup
import random
import sqlite3
import json
def get_db_connection():
    conn = sqlite3.connect('db/api_data.db')
    return conn

def load_api_data(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS api_data (user_id TEXT, url TEXT)")
    cursor.execute("SELECT url FROM api_data WHERE user_id = ?", (user_id,))
    urls = cursor.fetchall()
    conn.close()
    return [url[0] for url in urls]  

def save_api_data(user_id, url):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO api_data (user_id, url) VALUES (?, ?)", (user_id, url))
    conn.commit()
    conn.close()

async def check_site(url):
    async with AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10)
            return response.status_code == 200
        except Exception:
            return False

async def get_random_product(url):
    async with AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10)
            if response.status_code != 200:
                return None
            soup = BeautifulSoup(response.text, "html.parser")
            products = soup.select(
                'a[href*="/product/"], a[href*="/collections/"], a[href*="/shop/"]'
            )  
            if not products:
                return None
            random_product = random.choice(products)
            product_url = random_product["href"]
            if not product_url.startswith("http"):
                product_url = url.rstrip("/") + "/" + product_url.lstrip("/")
            return product_url
        except Exception:
            return None

@Client.on_message(filters.command(["make"], PREFIXES))
async def apiadd_command(client: Client, m: Message):
    with open("functions/botstatus.json", "r") as file:
        bot_state = json.load(file)
    
    if bot_state["state"]:
        return await m.reply(f"El bot Se Encuentra En Mantenimiento\nRazón: {bot_state['reason']}")
    user_id = str(m.from_user.id)
    with Database() as db:
        if not db.is_authorized(user_id, m.chat.id):
            return await m.reply(
                "<b>Usuario gratuito, si desea comprar el chkbot, por favor contacte a @tocandotee para conocer los precios y detalles.</b>",
                quote=True,
            )
        user_info = db.get_info_user(user_id)

    command_parts = m.text.split(maxsplit=2)
    symbol = await Symbol()  
    if len(command_parts) < 2:
        return await m.reply(
            f"""<b>{symbol} Por favor, proporciona un comando válido. </b>""",
            quote=True,
        )

    url = command_parts[1]
    if url.startswith("http://"):
        url = url.replace("http://", "https://")
    if not url.startswith("https://"):
        url = "https://" + url
    if not url_validator(url):
        return await m.reply(
            f"""<b>
{symbol} Error ❌  
{symbol} ¡Por favor, ingresa una URL válida!
</b>""",
            quote=True,
        )

    if not await check_site(url):
        return await m.reply(
            f"""<b>
{symbol} Error ❌
{symbol} El sitio no es accesible o no es válido.
</b>""",
            quote=True,
        )

    if "/product/" not in url and "/products/" not in url:
        return await m.reply(
            f"""<b>
{symbol} Error ❌
{symbol} Proporciona la URL de un producto para verificarlo y guardarlo.</b>""",
            quote=True,
        )

    rol = user_info["RANK"].capitalize()
    api_data = load_api_data(user_id)
    if url in api_data:
        return await m.reply(
            f"""<b>
{symbol} ¡Error!❌
{symbol} Ya tienes esta URL registrada. Si deseas añadir una nueva, elimina la existente.
</b>""",
            quote=True,
        )

    msg = await m.reply(
        f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Shopifys Added
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>Checking Site...</b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒URL: <code>{url}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{m.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0""",
        quote=True,
    )
    try:
        response = await autoshopify(
            url, "4271783821590119", "04", "2026", "660", True, 20
        )
    except Exception as e:
        message = "Graphql" if "graphql" in str(e) else "Error"
        traceback.print_exception(type(e), e, e.__traceback__)
        symbol = await Symbol()  
        return await msg.edit(
            f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Shopifys Added
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>Error ❌</b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Details: <code>Sitio con Graphql o /cn/ ({message})</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Site: <code>{url}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{m.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""
        )

    save_api_data(user_id, url)
    print(f"URL guardada para el usuario {user_id}: {url}")
    symbol = await Symbol()  
    await msg.edit(
        f"""♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Shopifys Added
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <b>Sitio añadido con éxito ✅</b>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Response: <code>{response['response']}</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Site: <code>{response['site']}</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Price: <code>{response['total'][:2]}$</code>
━━━━━━━━━━━━━━━━━━━━
<a href="https://t.me/zyrexnews">ゕ</a>﹒Time: <code>{response['time']}s</code>
<a href="https://t.me/zyrexnews">ゕ</a>﹒Req: @{m.from_user.username} [{rol}]
━━━━━━━━━━━━━━━━━━━━
࿔ Bot Version: 1.0"""
    )