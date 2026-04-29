import os
import re
import shutil

GATES_DIR = '/home/arkee/Downloads/Telegram Desktop/checkerxd/plugins/gates/'
USES_NOT_WORKING_DIR = os.path.join(GATES_DIR, 'UsesNotWorking')
os.makedirs(USES_NOT_WORKING_DIR, exist_ok=True)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Move to UsesNotWorking if OFFLINE
    if 'OFFLINE' in content or 'Apagado' in content:
        if 'Functions' not in filepath and '/au.py' not in filepath:
            if 'Status: <b>OFFLINE' in content or 'Gate Apagado' in content:
                print(f"Moving {filepath} to UsesNotWorking due to OFFLINE status.")
                shutil.move(filepath, os.path.join(USES_NOT_WORKING_DIR, os.path.basename(filepath)))
                return
        
    if 'from functions.global_manager import check_gate' in content:
        return 
        
    # Extract command
    match_cmd = re.search(r"filters\.command\(\['([^']+)'\]", content)
    if not match_cmd: return
    cmd = match_cmd.group(1)
    
    # Extract gateway name
    match_name = re.search(r"Gateway:\s+(.*?)\s+\(/" + cmd + r"\)", content)
    if not match_name: match_name = re.search(r"Gateway:\s+(.*?)\s+\[", content)
    
    gateway_name = "Gateway"
    if match_name:
        gateway_name = re.sub(r'</?b>', '', match_name.group(1).strip()).strip()
    if '<' in gateway_name: gateway_name = "Gateway"

    # Extract the main api call
    match_call = re.search(r'(status,\s*response\s*=\s*await[^\n]+)', content)
    if not match_call: return
    call_line = match_call.group(1).strip()

    # Imports selection
    lines = content.split('\n')
    final_imports = {'import asyncio', 'from pyrogram import Client, filters', 
                     'from functions.variables import PREFIXES', 
                     'from functions.global_manager import check_gate', 
                     'from functions.functions import ProxyRandom'}
    for line in lines:
        if ('import ' in line or 'from ' in line) and 'gates.' in line:
            final_imports.add(line.strip())

    import_section = "\n".join(sorted(final_imports))

    new_content = f"""{import_section}

# Función principal para manejar mensajes
@Client.on_message(filters.command(['{cmd}'], PREFIXES))
@check_gate(command="/{cmd}", gateway_name="{gateway_name}", required_credits=3)
async def gate_{cmd}(client, message):
    cc, mes, ano, cvv = message.cc, message.mes, message.ano, message.cvv
    
    retries = 0
    max_retries = 3
    while retries < max_retries:
        try:
            {call_line}
            break
        except Exception as e:
            retries += 1
            print(f"Retry {{retries}}/{{max_retries}} failed: {{str(e)}}")
            
        if retries >= max_retries:
            status = "Declined ❌"
            response = "Max retries exceeded"
            break
        await asyncio.sleep(2)

    return status, response
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Refactored {filepath}")

for filename in os.listdir(GATES_DIR):
    if filename.endswith('.py'):
        process_file(os.path.join(GATES_DIR, filename))
