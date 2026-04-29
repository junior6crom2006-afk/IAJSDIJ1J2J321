import requests
import uuid
import base64

# Configuración inicial de la sesión
web = requests.Session()

# Generación de un email aleatorio
email = uuid.uuid4().hex[:8] + '@gmail.com'

def braintree_generate_uuid():
    return str(uuid.uuid4())

response = web.get("https://randomuser.me/api/1.2/?nat=US")
user = response.text
street = user.split('"street":"')[1].split('"')[0]
city = user.split('"city":"')[1].split('"')[0]
state1 = user.split('"state":"')[1].split('"')[0]
zipcode = user.split('"postcode":')[1].split(',')[0]
phone = user.split('"phone":"')[1].split('"')[0]
name = user.split('"first":"')[1].split('"')[0]
last = user.split('"last":"')[1].split('"')[0]

print(street, city, state1, zipcode, phone, name, last)
