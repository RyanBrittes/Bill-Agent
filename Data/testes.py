from database import database

def main():
    x = 2
    query = database()
    print("ID de clientes em débito: ", query.consultar_cliente_debito())

    print("E-mail de clientes em débito: ", query.consultar_email_cliente(x))

    print("Nome dos clientes em débito: ", query.consultar_nome_cliente(x))

    

main()