#Bibliotecas necessárias
import psycopg2
import os
from dotenv import load_dotenv

#Carregamento das variáveis de ambiente
load_dotenv()

#Criação da conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database= os.getenv("db_name"),
    user= os.getenv("db_user"),
    password= os.getenv("db_pass")
)

#Criação do cursor
cur = conn.cursor()

#Consulta no Banco de Dados
cur.execute("SELECT Cl_Email FROM TB_Cliente WHERE Cl_ID = 1;")

DB_email = cur.fetchone()[0]
print(DB_email)

cur.close()
conn.close()