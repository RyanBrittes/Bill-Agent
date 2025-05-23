import requests

url = "http://localhost:8080/instance/create"

payload = {
    "instanceName": "teste",
    "token": "",
    "qrcode": True,
    "number": "5565984264261",
    "integration": "WHATSAPP-BAILEYS",
    "rejectCall": True,
    "msgCall": "",
    "groupsIgnore": True,
    "alwaysOnline": False,
    "readMessages": False,
    "readStatus": False,
    "syncFullHistory": True,
}
headers = {
    "apikey": "key123",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)