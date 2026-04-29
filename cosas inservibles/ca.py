import requests

base_url = "https://ykz-apisites.sh-ykza-env.com"

endpoint = "/encrypt/payeezy"
url = base_url + endpoint

headers = {
    "apisites": "FREEXXXX1-SERVER-[0x10][0xf]"
}

payload = {
    "pk": "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUEzdzJTZk5HbUc0b3hJSzFlcE5mMwplUFJtS0F3eFFXQ1JEV1lpR3o1eXJ6S3dsTllDaEg3ajJyYXE1SjNrR2ptYWtlc0w4TXlnMk9GNmdRajJ6czYxCnQ4a0ZGKzEwMWd1ZlpxOE95eGV6YkRCM2NtWlBiMXViK3FRMWVpclpXaE1nVkVtQ3ZHU0hkR2srNzNqWUZvdysKYmU1dHBLZC9kdTVESTkvYUhEZyt3ZGJja056dDM2QW5wSjQ3VlZLUW9ueXFtR0RCbWMzWTRPcElRWWl1TVZUTgp6YXh4eE96cXJ2VTRZeXhVQ05iU0RkaC9kS1h6RWovcEZwRDNzUE5IdjUxWVBreDVpamczZ1BXZzRMYVlRa0NuCkZXcStjUGVXbURNNldKQ1JrVlorTnhsZ2lIN3JwYTBzWHJPMlcyZXVKQ3NOREdXRmIyNkJkUTRDaVczMjhJYUgKWXdJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t",
    "data": {"card":"44444444444444444","cvv":"000","exp":"0121","name":"Armando Bancos"}
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())