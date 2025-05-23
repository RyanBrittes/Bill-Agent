import requests
from dotenv import load_dotenv
import os

load_dotenv()

class SendWP:
    def __init__(self):
        self.key = os.getenv('apikey')
        self.url = os.getenv('linkurl')
        self.headers = {"apikey": "key123","Content-Type": "application/json"}

    def enviar(self,numero_cliente: str, nome_cliente: str, nome_fatura: str, vencimento: str):
        payload = {
            "number": f"{numero_cliente}",
            "text": f"Caro cliente {nome_cliente},\nA {nome_fatura} venceu {vencimento}, por gentileza verificar e quitar os débitos o quanto antes possível, obrigado!\n*Att, Financeiro*.",
            "delay": 2000,
            "linkPreview": True,
            "mentionsEveryOne": True,
        }
        response = requests.post(self.url, json=payload, headers=self.headers)
        print("Whatsapp enviado!")