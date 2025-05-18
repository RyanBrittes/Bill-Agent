#Bibliotecas necessárias
import psycopg2
import os
from dotenv import load_dotenv

#Carregamento das variáveis de ambiente
load_dotenv()

#Criação da conexão com o banco de dados
class Database:
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
   
    def consultar_informacoes_clientes(self):
        self.cur.execute("SELECT Cl_Nome, Cl_Email, DC_Nome, DC_Vencimento FROM TB_Cliente A JOIN TB_Fatura B ON A.Cl_ID = B.Cl_ID WHERE DC_Vencimento < CURRENT_DATE AND DC_Situacao = 'Não pago';")
        return self.cur.fetchall()
    
    def close(self):
        self.cur.close()
        self.conn.close()
        