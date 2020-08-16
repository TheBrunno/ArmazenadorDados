from time import sleep
from Class import *

while True:
    Usuarios = Client('Usuarios')
    lista = ['MENU PRINCIPAL', 'Ver Clientes Cadastrados', 'Cadastrar Novos Clientes', 'Deletar Cadastro', 'Editar Cadastros','Sair do Sistema']
    menu(lista)
    op = leiaInt('Digite sua opção: ', len(lista) - 1, 1)
    if op == 1:
        sleep(1)
        MenuError(lista[1])
        print()
        Usuarios.ListarClientes()
    elif op == 2:
        sleep(1)
        MenuError(lista[2])
        print()
        Usuarios.CadastroCliente()
    elif op == 3:
        sleep(1)
        MenuError(lista[3])
        print()
        Usuarios.ListarClientes()
        Usuarios.DeletarCadastro()
    elif op == 4:
        while True:
            sleep(1)
            lstta = ['EDITAR CLIENTES', 'Marcar um cliente', 'Desmarcar um cliente', 'Voltar para o menu principal']
            menu(lstta)
            opc = leiaInt('Qual sua opção: ', len(lstta) - 1, 1)
            if opc == 1:
                Usuarios.ListarClientes(False, True)
                Usuarios.MarcarCliente()
            elif opc == 2:
                Usuarios.ListarClientes(True, False)
                Usuarios.DesmarcarCliente()
            elif opc == 3:
                sleep(1)
                print()
                break
    elif op == 5:
        sleep(1)
        MenuError(lista[5], car='-')
        sleep(1)
        break