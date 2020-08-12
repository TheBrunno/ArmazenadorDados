from time import sleep


def MenuError(msg, car='='):
    tam = len(msg)
    print(f'\033[1;31m{car[0]}' * (tam + 4))
    print(f'  {msg}')
    print(f'\033[1;31m{car[0]}\033[m' * (tam + 4))


def leiaInt(msg, maxi=999, mini=0):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            MenuError('DIGITE UM VALOR INTEIRO')
        else:
            if num > maxi or num < mini:
                MenuError(f'DIGITE UM VALOR ENTRE {mini} À {maxi}')
            else:
                return int(num)



class Client:
    def __init__(self, arquivo):
        self.__arquivo = f'{arquivo}.txt'
        self.__clientes = f'{self.__arquivo}'
        self.__ind = []
        self.__indc = []

    def CadastroCliente(self):
        nome = str(input('Nome do cliente: '))
        if nome == '':
            nome = '<desconhecido>'
        while nome.isnumeric():
            MenuError('DIGITE UM NOME VALIDO', '=')
            nome = str(input('Nome do cliente: '))
        ind = leiaInt('ID do cliente: ')
        while ind == 999:
            MenuError('DIGITE OUTRO ID')
            sleep(1)
            print()
            ind = leiaInt('ID do cliente: ')
        arqread = open(self.__clientes, 'r')
        for en, line in enumerate(arqread):
            if en % 2 == 0:
                if int(line) == ind:
                    while int(line) == ind:
                        MenuError('DIGITE UM INDICE NAO REPETIDO ANTES', '=')
                        ind = leiaInt('ID do cliente: ')
        with open(self.__clientes, 'a+') as arq:
            arq.write(f'{ind}\n{nome}\n')
            arq.seek(0)
            sleep(1)
            print(f'\033[1;32mO cliente \'{nome.title()}\' foi cadastrado com sucesso\033[m')
            sleep(2)
        arqread.close()

    def ListarClientes(self):
        __name = []
        with open(self.__clientes, 'r') as arqv:
            for ind, line in enumerate(arqv):
                if ind % 2 == 0:
                    self.__ind.append(line.replace('\n', ''))
                else:
                    __name.append(line.replace('\n', '').title())
            print('\033[37;4m Nome'.ljust(40), end='')
            print('Id \033[m')
            for ind, name in enumerate(__name):
                print(f'\033[36m{name.ljust(32)}\033[m\033[33m{self.__ind[ind]}\033[m')
                sleep(0.3)
            print('\033[37;4m \033[m' * 38)
            print()

    def DeletarCadastro(self):
        while True:
            print('\033[1;31m       999 Para sair\033[m')
            __id = leiaInt('Digite o id: ')
            __idsDel = []
            __namesDel = []
            if __id == 999:
                break
            with open(self.__clientes) as arq:
                for indc, line in enumerate(arq):
                    if indc % 2 == 0:
                        line.replace('\n', '')
                        __idsDel.append(int(line))
                    else:
                        __namesDel.append(line.replace('\n', ''))

            try:
                pos = __idsDel.index(__id)
            except ValueError:
                MenuError('NAO FOI ENCONTRADO ESSE ID', '=')
                continue
            else:
                __edits = open(f'{self.__arquivo}', 'w')
                del __idsDel[pos]
                exx = __namesDel[pos]
                del __namesDel[pos]
                contname = contid = 0
                for idss in range(len(__idsDel) + len(__namesDel)):
                    if idss % 2 == 0:
                        __edits.write(str(__idsDel[contid]))
                        contid += 1
                    else:
                        __edits.write(str(f'\n{__namesDel[contname]}\n'))
                        contname += 1
                sleep(1)
                print(f'\033[1;31mO cliente \'{exx.title()}\' foi excluido com sucesso\033[m')
                sleep(2)
                __edits.close()
                break

def menu(lst):
    print('-=' * 15)
    for ind, el in enumerate(lst):
        print(f'\033[33m{ind + 1}\033[m - \033[34m{el}\033[m')
    print('-=' * 15)

def NameMenu(msg, car='='):
    tam = len(msg)
    print(f'{car}' * (tam + 4))
    print(f'  {msg}')
    print(f'{car}' * (tam + 4))

while True:
    Usuarios = Client('Usuarios')
    lista = ['Ver Clientes Cadastrados', 'Cadastrar Novos Clientes', 'Deletar Cadastro', 'Sair do Sistema']
    menu(lista)
    op = leiaInt('Digite sua opçao: ', len(lista), 1)
    if op == 1:
        sleep(1)
        NameMenu(lista[0])
        print()
        Usuarios.ListarClientes()
    if op == 2:
        sleep(1)
        NameMenu(lista[1])
        print()
        Usuarios.CadastroCliente()
    if op == 3:
        sleep(1)
        MenuError(lista[2])
        print()
        Usuarios.ListarClientes()
        Usuarios.DeletarCadastro()
    if op == 4:
        sleep(2)
        MenuError(lista[3], car='-')
        sleep(1)
        break

