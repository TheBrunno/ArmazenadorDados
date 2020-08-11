from time import sleep
def leiaInt(msg, maxi=999, mini=0):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31m=-' * 15)
            print('\033[1;31mDIGITE UM VALOR INTEIRO')
            print('\033[1;31m=-\033[m' * 15)
        else:
            if num > maxi or num < mini:
                print('\033[1;31m=-' * 15)
                print(f'\033[1;31mDIGITE UM VALOR ENTRE {mini} À {maxi}')
                print('\033[1;31m=-\033[m' * 15)
            else:
                return int(num)

def MenuError(msg, car='='):
    tam = len(msg)
    print(f'\033[1;31m{car[0]}' * (tam + 4))
    print(f'  {msg}')
    print(f'\033[1;31m{car[0]}\033[m' * (tam + 4))

class Client:
    def __init__(self, arquivo):
        self.__arquivo = f'{arquivo}.txt'
        self.__clientes = open(f'{self.__arquivo}', 'a+')
        self.__read = open(f'{self.__arquivo}', 'r')
        self.__ind = []
        self.__indc = []

    def CadastroCliente(self):
        nome = str(input('Nome do cliente: '))
        while nome.isnumeric():
            MenuError('DIGITE UM NOME VALIDO', '=')
            nome = str(input('Nome do cliente: '))
        ind = leiaInt('Indice do cliente: ')
        for en, line in enumerate(self.__read):
            if en % 2 == 0:
                if int(line) == ind:
                    while int(line) == ind:
                        MenuError('DIGITE UM INDICE NAO REPETIDO ANTES', '=')
                        ind = leiaInt('ID do cliente: ')
        self.__clientes.write(f'{ind}\n{nome}\n')
        self.__clientes.seek(0)

    def ListarClientes(self):
        __name = []
        self.__clientes = open(self.__arquivo, 'r')
        for ind, line in enumerate(self.__clientes):
            if ind % 2 == 0:
                self.__ind.append(line.replace('\n', ''))
            else:
                __name.append(line.replace('\n', '').title())
        print('Nome'.ljust(25), end='')
        print('Id')
        print('-' * 28)
        for ind, name in enumerate(__name):
            print(f'{name.ljust(25)}{self.__ind[ind]}')
            sleep(0.3)
        print('-' * 28)

    def DeletarCadastro(self):
        __id = leiaInt('Digite o id: ')
        __idsDel = []
        __namesDel = []
        arq = open(self.__arquivo)
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
        else:
            __edits = open(f'{self.__arquivo}', 'w')
            del __idsDel[pos]
            del __namesDel[pos]
            contname = contid = 0
            for idss in range(len(__idsDel) + len(__namesDel)):
                if idss % 2 == 0:
                    __edits.write(str(__idsDel[contid]))
                    contid += 1
                else:
                    __edits.write(str(f'\n{__namesDel[contname]}\n'))
                    contname += 1

def menu(lst):
    print('-=' * 15)
    for ind, el in enumerate(lst):
        print(f'\033[33m{ind + 1}\033[m - \033[34m{el}\033[m')
    print('-=' * 15)

while True:
    Usuarios = Client('Usuarios')
    lista = ['Mostrar Clientes', 'Cadastrar Clientes', 'Deletar Cadastro']
    menu(lista)
    op = leiaInt('Digite sua opçao: ', len(lista), 1)
    if op == 1:
        Usuarios.ListarClientes()
    if op == 2:
        Usuarios.CadastroCliente()
    if op == 3:
        Usuarios.ListarClientes()
        Usuarios.DeletarCadastro()

