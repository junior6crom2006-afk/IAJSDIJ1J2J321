from urllib.parse import unquote

url = "https://api.payaconnect.com/hostedpaymentpagepayments?id=11ede43f448f396cbcf8ce98&data=U2FsdGVkX18xMWVkZTQzZk%2BzQ1g6cSRm37ok1mCYNzQv05335SsDbMCS%2Fr4Jwv4HD2sAPQn5ocUxRFKlqMXA9g%3D%3D"

# Extraer id y data usando split
id_part = url.split("id=")[1]
id_value = id_part.split("&data=")[0]
data_value = id_part.split("&data=")[1]

# Decodificar el valor de data
data_value_decoded = unquote(data_value)

print("El valor de 'id' es:", id_value)
print("El valor de 'data' decodificado es:", data_value_decoded)
