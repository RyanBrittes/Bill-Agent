from database import Database
from send import Send

class Main():
    #Carregamento de dados e métodos de instanciamentos
    def __init__(self):
        self.query = Database()
        self.sender = Send()
        self.info = self.query.consultar_informacoes_clientes()
        self.clientes = self.query.consultar_cliente_debito()
    #Verificação e acionamento de e-mails
    def acionar(self):
        verificacao = self.clientes
        if verificacao:
            dados_clientes = self.info
            for row in dados_clientes:
                self.sender.enviar_email(row[0], row[1], row[2], row[3])
                print(row)
        else:
            print("Nenhum cliente está em débito")
