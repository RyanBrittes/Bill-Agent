#Bibliotecas necessárias
import smtplib
import email.message
from dotenv import load_dotenv
import os
import schedule
import time

#Carregamento das variáveis do dotenv
load_dotenv()

#Definindo variáveis do dotenv
mail = os.getenv('mail')
pw = os.getenv('password')

#Função responsável pelo envio do e-mail
def enviar_email():  
    corpo_email = """
    <p><b>Fatura 992</b></p>
    <p>Vencimento: 06/02/2025</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Cobrança de Fatura Atrasada"
    msg['From'] = mail
    msg['To'] = 'ryantestes910@gmail.com'
    password = pw 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

#Scheduller
schedule.every().day.at("16:06").do(enviar_email)

print("Agendador funcionando...")

#Loop que garante o update do agendador a cada 20 segundos
while True:
    print("entrou")
    schedule.run_pending()
    print("esperando time")
    time.sleep(20)

