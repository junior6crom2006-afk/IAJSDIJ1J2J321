from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functions.variables import PREFIXES
from functions.functions import Symbol, Symbol2
from functions.gate_manager import GateManager
import pytz
from datetime import datetime
import json
import math
import os

# === MEDIA CACHE SYSTEM ===
MEDIA_CACHE_FILE = "database/media_cache.json"

def load_media_cache():
    if os.path.exists(MEDIA_CACHE_FILE):
        try:
            with open(MEDIA_CACHE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_media_cache(cache):
    with open(MEDIA_CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=4)

async def get_photo(client, path, cache):
    """Retorna el file_id si está en caché, o el path si no"""
    if path in cache:
        return cache[path]
    return path

def update_cache_from_msg(msg, path, cache):
    """Extrae el file_id del mensaje enviado y lo guarda en caché"""
    if hasattr(msg, "photo") and msg.photo:
        file_id = msg.photo.file_id
        cache[path] = file_id
        save_media_cache(cache)
        return file_id
    return None

# === FUNCIONES PARA GENERAR BOTONES CON USER_ID ===

def make_main_menu(user_id):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Gates", callback_data=f"Gates_{user_id}"),
            InlineKeyboardButton("Tools", callback_data=f"Tools_{user_id}")
        ],
        [
            InlineKeyboardButton("Canal", url="https://t.me/zyrexnews")
        ]
    ])

def make_section_buttons(user_id):
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("CCN", callback_data=f"CCN_{user_id}_1"),
            InlineKeyboardButton("AUTH", callback_data=f"AUTH_{user_id}_1"),
            InlineKeyboardButton("CHARGED", callback_data=f"CHARGED_{user_id}_1"),
        ],
        [
            InlineKeyboardButton("Mass Gates", callback_data=f"MASS_GATES_{user_id}_1"),
            InlineKeyboardButton("Home", callback_data=f"home_{user_id}"),
        ]
    ])

def make_home_btn(user_id):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Home", callback_data=f"home_{user_id}")]
    ])

def make_back_btn(user_id):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("↩️", callback_data=f"back_to_gates_{user_id}")]
    ])

def make_pagination_keyboard(section, user_id, current_page, total_pages):
    buttons = []
    
    # Fila de navegación
    nav_row = []
    if current_page > 1:
        nav_row.append(InlineKeyboardButton("⬅️", callback_data=f"{section}_{user_id}_{current_page-1}"))
    
    nav_row.append(InlineKeyboardButton(f"{current_page} / {total_pages}", callback_data="none"))
    
    if current_page < total_pages:
        nav_row.append(InlineKeyboardButton("➡️", callback_data=f"{section}_{user_id}_{current_page+1}"))
    
    if len(nav_row) > 1: # Solo añadir si hay más de una página o es necesario el indicador
        buttons.append(nav_row)
    
    # Fila de volver
    buttons.append([InlineKeyboardButton("↩️ Volver", callback_data=f"back_to_gates_{user_id}")])
    
    return InlineKeyboardMarkup(buttons)

# === VERIFICAR QUE SOLO EL AUTOR PUEDA USAR LOS BOTONES ===

def get_owner_id(callback_data):
    """Extrae el user_id del callback_data (penúltimo o último segmento)"""
    parts = callback_data.split("_")
    # Formatos posibles: 
    # home_ID
    # Gates_ID
    # CCN_ID_PAGE
    if len(parts) >= 2:
        # Buscamos el ID que suele ser el segundo o tercer elemento
        for p in parts:
            if p.isdigit() and len(p) > 5: # IDs de telegram son largos
                return int(p)
    return None

def get_page(callback_data):
    """Extrae el número de página (último segmento si existe)"""
    parts = callback_data.split("_")
    if len(parts) >= 3 and parts[-1].isdigit():
        return int(parts[-1])
    return 1

async def check_owner(callback_query):
    """Retorna True si el usuario puede usar el botón, False si no"""
    owner_id = get_owner_id(callback_query.data)
    if owner_id and callback_query.from_user.id != owner_id:
        await callback_query.answer("❌ Solo el autor del comando puede usar estos botones", show_alert=True)
        return False
    return True

# === COMANDO .cmds ===

@Client.on_message(filters.command('cmds', PREFIXES))
async def cmds(client, message):
    cache = load_media_cache()
    try:
        with open("functions/botstatus.json", "r") as file:
            bot_state = json.load(file)
        
        if bot_state["state"]:
            return await message.reply(f"El bot Se Encuentra En Mantenimiento\nRazón: {bot_state['reason']}")
    except (json.JSONDecodeError, FileNotFoundError):
        pass

    mencion = f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name
    iddelpapu = message.from_user.id
    
    path = "plugins/main/IMG/cmd.png"
    photo = await get_photo(client, path, cache)
    
    msg = await message.reply_photo(
        photo=photo, 
        caption=f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Panel Principal</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Selecciona una categoría para ver los comandos disponibles.</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒User: <code>{mencion}</code> | Id: <code>{iddelpapu}</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>  
        """,
        reply_markup=make_main_menu(iddelpapu),
        quote=True
    )
    
    # Si subimos un archivo nuevo, guardar el ID
    if photo == path:
        update_cache_from_msg(msg, path, cache)

# === CALLBACK: Gates ===

@Client.on_callback_query(filters.regex(r"^Gates_\d+$"))
async def gates_info(client, callback_query):
    if not await check_owner(callback_query):
        return
    
    owner_id = get_owner_id(callback_query.data)
    gates = GateManager.get_all_gates()
    
    # Conteo optimizado en un solo loop
    online_count = 0
    offline_count = 0
    ccn_count = 0
    auth_count = 0
    charged_count = 0
    
    for g in gates:
        if g.get('estado') == 'ON':
            online_count += 1
        else:
            offline_count += 1
            
        tipo = g.get('tipo')
        if tipo == 'CCN':
            ccn_count += 1
        elif tipo == 'AUTH':
            auth_count += 1
        elif tipo == 'CHARGED':
            charged_count += 1
    
    caption = f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Gates Info</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Gates Online: <code>{online_count}</code> | ✅</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Gates Apagados: <code>{offline_count}</code> | ❌</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Gates CCN: <code>{ccn_count}</code> | Credits</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Gates Auth: <code>{auth_count}</code> | Premium</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Gates Charged: <code>{charged_count}</code> | Premium</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
    """
    
    cache = load_media_cache()
    path = "plugins/main/IMG/gates.png"
    photo = await get_photo(client, path, cache)
    
    try:
        await callback_query.message.edit_caption(
            caption=caption,
            reply_markup=make_section_buttons(owner_id)
        )
    except Exception:
        await callback_query.message.delete()
        msg = await client.send_photo(
            chat_id=callback_query.message.chat.id,
            photo=photo,
            caption=caption,
            reply_markup=make_section_buttons(owner_id)
        )
        if photo == path:
            update_cache_from_msg(msg, path, cache)
    
    await callback_query.answer()

# === CALLBACK: Tools ===

@Client.on_callback_query(filters.regex(r"^Tools_\d+$"))
async def tools_info(client, callback_query):
    if not await check_owner(callback_query):
        return
    
    owner_id = get_owner_id(callback_query.data)
    
    caption = f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Tools Info</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Gen Bin: /gen 446540</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Check Bin: /bin 446540</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Check VBV: /vbv <code>card|mm|yy|cvv</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
    """
    
    cache = load_media_cache()
    path = "plugins/main/IMG/tools.png"
    photo = await get_photo(client, path, cache)
    
    try:
        await callback_query.message.edit_caption(
            caption=caption,
            reply_markup=make_home_btn(owner_id)
        )
    except Exception:
        await callback_query.message.delete()
        msg = await client.send_photo(
            chat_id=callback_query.message.chat.id,
            photo=photo,
            caption=caption,
            reply_markup=make_home_btn(owner_id)
        )
        if photo == path:
            update_cache_from_msg(msg, path, cache)
    
    await callback_query.answer()

# === CALLBACK: Home ===

@Client.on_callback_query(filters.regex(r"^home_\d+$"))
async def home(client, callback_query):
    if not await check_owner(callback_query):
        return
    
    owner_id = get_owner_id(callback_query.data)
    mencion = f"@{callback_query.from_user.username}" if callback_query.from_user.username else callback_query.from_user.first_name
    iddelpapu = callback_query.from_user.id
    
    caption = f"""
<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Panel Principal</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Selecciona una categoría para ver los comandos disponibles.</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒User: <code>{mencion}</code> | Id: <code>{iddelpapu}</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>  
"""
    
    cache = load_media_cache()
    path = "plugins/main/IMG/cmd.png"
    photo = await get_photo(client, path, cache)
    
    try:
        await callback_query.message.edit_caption(
            caption=caption,
            reply_markup=make_main_menu(owner_id)
        )
    except Exception:
        await callback_query.message.delete()
        msg = await client.send_photo(
            chat_id=callback_query.message.chat.id,
            photo=photo,
            caption=caption,
            reply_markup=make_main_menu(owner_id)
        )
        if photo == path:
            update_cache_from_msg(msg, path, cache)
    
    await callback_query.answer()

# === CALLBACK: Secciones (CCN, AUTH, CHARGED, MASS_GATES) con Paginación ===

@Client.on_callback_query(filters.regex(r"^(CCN|AUTH|CHARGED|MASS_GATES)_\d+_\d+$"))
async def sections_handler(client, callback_query):
    if not await check_owner(callback_query):
        return
    
    data = callback_query.data.split("_")
    section = data[0]
    owner_id = get_owner_id(callback_query.data)
    current_page = get_page(callback_query.data)
    
    if section == "MASS_GATES":
        text = f"""<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | Mass Gateways</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Mass Checker: /mass</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Format: <code>CC|MM|YY|CVV</code></b>
<b>━━━━━━━━━━━━━━━━━━━━</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Status: ON ✅ | [Premium ✅]</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>"""
        keyboard = make_back_btn(owner_id)
    else:
        all_gates = [g for g in GateManager.get_all_gates() if g.get('tipo') == section]
        total_gates = len(all_gates)
        gates_per_page = 5
        total_pages = math.ceil(total_gates / gates_per_page) or 1
        
        # Slicing de gates
        start_idx = (current_page - 1) * gates_per_page
        end_idx = start_idx + gates_per_page
        paged_gates = all_gates[start_idx:end_idx]
        
        text = f"""<b>♯𝗭𝘆𝗿𝗲𝘅 𝗖𝗵𝗸 | {section} Gateways</b>
<b>━━━━━━━━━━━━━━━━━━━━</b>"""

        if not paged_gates:
            text += f"\n<b><a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Ninguno en esta página</b>\n<b>━━━━━━━━━━━━━━━━━━━━</b>"
        else:
            for gate in paged_gates:
                estado = "ON ✅" if gate.get('estado') == "ON" else "OFF ❌"
                text += f"""
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒{gate.get('nombre', 'Unknown')}</b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Status: <code>{estado}</code></b>
<b><a href="https://t.me/zyrexnews">ゕ</a>﹒Cmd: <code>{gate.get('comando', 'Unknown')}</code></b>"""
                
                if gate.get('estado') == "OFF":
                    text += f"\n<b><a href=\"https://t.me/zyrexnews\">ゕ</a>﹒Razón: <code>{gate.get('razon') or 'No especificada'}</code></b>"
                
                text += f"\n<b>━━━━━━━━━━━━━━━━━━━━</b>"
        
        keyboard = make_pagination_keyboard(section, owner_id, current_page, total_pages)
    
    # Editar o enviar
    try:
        await callback_query.message.edit_caption(
            caption=text,
            reply_markup=keyboard
        )
    except Exception:
        # Si falla (ej: por MediaCaptionTooLong o porque no hay foto), enviar como texto
        try:
            await callback_query.message.delete()
        except:
            pass
        await client.send_message(
            chat_id=callback_query.message.chat.id,
            text=text,
            reply_markup=keyboard
        )
    
    await callback_query.answer()

# === CALLBACK: Volver a Gates ===

@Client.on_callback_query(filters.regex(r"^back_to_gates_\d+$"))
async def back_to_gates(client, callback_query):
    if not await check_owner(callback_query):
        return
    
    owner_id = get_owner_id(callback_query.data)
    callback_query.data = f"Gates_{owner_id}"
    await gates_info(client, callback_query)

@Client.on_callback_query(filters.regex("none"))
async def catch_none(client, callback_query):
    await callback_query.answer()