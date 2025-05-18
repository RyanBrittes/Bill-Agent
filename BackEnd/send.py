#Bibliotecas necessárias
import smtplib
import email.message
from dotenv import load_dotenv
import os

load_dotenv()

class Send:
    #Carregamento de variáveis de ambiente
    def __init__(self):
        self.mail = os.getenv('mail')
        self.pw = os.getenv('password')
    #Acionamento de e-mails com as devidas formatações
    def enviar_email(self, nome_cliente: str, email_cliente: str, nome_fatura: str, vencimento: str):
        corpo_email = f"""
        <p>Caro cliente {nome_cliente},</p>
        <p>A {nome_fatura} venceu {vencimento}, por gentileza verificar e quitar os débitos o quanto antes possível, obrigado!</p>
        <p>Att, Financeiro.</p>
        """

        msg = email.message.Message()
        msg['Subject'] = "Aviso de vencimento de fatura"
        msg['From'] = self.mail
        msg['To'] = email_cliente
        password = self.pw 
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email )

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        
        #Credenciais de login para enviar e-mails
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
        