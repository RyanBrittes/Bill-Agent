#Bibliotecas necessárias
import psycopg2
import os
from dotenv import load_dotenv

#Carregamento das variáveis de ambiente
load_dotenv()

#Criação da conexão com o banco de dados
class database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database= os.getenv("db_name"),
            user= os.getenv("db_user"),
            password= os.getenv("db_pass")
        )
        #Criação do cursor
        self.cur = self.conn.cursor()

    def consultar_cliente_debito(self):
        self.cur.execute("SELECT Cl_ID FROM TB_FATURA WHERE DC_Situacao = 'Não pago' AND DC_Vencimento < CURRENT_DATE;")
        return self.cur.fetchall()
    
    def consultar_email_cliente(self, x: int):
        self.cur.execute(f"SELECT Cl_Email FROM TB_Cliente WHERE Cl_ID = {x};")
        cliente_Email = self.cur.fetchone()
        return cliente_Email[0]
    
    def consultar_nome_cliente(self, x: int):
        self.cur.execute(f"SELECT Cl_Nome FROM TB_Cliente WHERE Cl_ID = {x};")
        cliente_Nome = self.cur.fetchone()
        return cliente_Nome[0]

    def close(self):
        self.cur.close()
        self.conn.close()