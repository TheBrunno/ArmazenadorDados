from time import sleep

def menu(lst):
    print('-=' * 7, end='')
    print(f'{lst[0]} ', end='')
    print('-=' * 7)
    for ind, el in enumerate(lst[1:]):
        print(f'{ind + 1} - {el}')
    print('-=' * 15)

def MenuError(msg, car='='):
    tam = len(msg)
    print(f'{car[0]}' * (tam + 4))
    print(f'  {msg}')
    print(f'{car[0]}' * (tam + 4))


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
        try:
            open(self.__clientes)
        except FileNotFoundError:
            open(self.__clientes, 'x')

    def CadastroCliente(self):
        nome = str(input('Nome do cliente: ')).title()
        if nome == '':
            nome = '<desconhecido>'
        while nome.isnumeric():
            MenuError('DIGITE UM NOME VALIDO', '=')
            nome = str(input('Nome do cliente: '))
        ind = leiaInt('ID do cliente: ')
        while ind == 999 or ind == 998:
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
            print(f'O cliente \'{nome.title()}\' foi cadastrado com sucesso')
            sleep(2)
        arqread.close()

    def ListarClientes(self, __mostrarMarrc=True, __mostrarNormal=True):
        __name = []
        __ind = []
        with open(self.__clientes, 'r') as arqv:
            for ind, line in enumerate(arqv):
                if ind % 2 == 1:
                    if line[0] == '&':
                        if __mostrarMarrc:
                            __name.append(line.replace('\n', '').title())
                        else:
                            __ind.pop()
                    else:
                        if __mostrarMarrc and not __mostrarNormal:
                            __ind.pop()
                        elif __mostrarNormal and not __mostrarMarrc:
                            __name.append(line.replace('\n', '').title())
                        else:
                            __name.append(line.replace('\n', '').title())
                elif ind % 2 == 0:
                    __ind.append(line.replace('\n', ''))
            print(' Nome'.ljust(40), end='')
            print('Id ')
            for ind, name in enumerate(__name):
                if name[0].replace('\n', '') == '&':
                    print('_' * 45)
                    name = name.replace('&', '')
                    print(f'|{name.ljust(40)}{__ind[ind]}|')
                    print('-' * 45)
                    sleep(0.3)
                elif __ind[ind] != line.replace('&', ''):
                    print(f'{name.ljust(40)}{__ind[ind]}')
                    sleep(0.3)
            print()
            print()

    def DeletarCadastro(self):
        while True:
            print('       999 Para sair')
            print('       998 Excluir tudo')
            print()
            __id = leiaInt('Digite o id: ')
            __idsDel = []
            __namesDel = []
            Opcao = 'X'
            cont = 1
            if __id == 998:
                while True:
                    if Opcao == 'S':
                        print()
                        MenuError('Todos os dados foram excluidos.', car='~')
                        arqv = open(self.__clientes, 'w+')
                        arqv.close()
                        break
                    if Opcao == 'N':
                        MenuError('Nao foi excluido nenhum dado.', car='~')
                        break
                    else:
                        while Opcao not in 'SN':
                            if cont != 1:
                                MenuError('DIGITE APENAS [S/N].')
                            Opcao = input('Tem certeza que quer excluir todos os dados? [S/N]').strip().upper()[0]
                            cont += 1
            if __id == 999:
                break
            if Opcao == 'S':
                break
            with open(self.__clientes) as arq:
                for indc, line in enumerate(arq):
                    if indc % 2 == 0:
                        line.replace('\n', '')
                        __idsDel.append(int(line))
                    else:
                        __namesDel.append(line.replace('\n', ''))
            if Opcao not in 'SN':
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
                    exx = exx.replace('&', '')
                    print(f'O cliente \'{exx.title()}\' foi excluido com sucesso')
                    sleep(2)
                    __edits.close()
                    break


    def DesmarcarCliente(self):
        while True:
            print('         999 Para')
            __names = []
            __ids = []
            igual = False
            Desmarc = leiaInt('Pelo ID, qual cliente quer desmarcar: ')
            if Desmarc == 999:
                return
            with open(self.__clientes, 'r') as DesmarcArquivo:
                for enum, line in enumerate(DesmarcArquivo):
                    if enum % 2 == 0:
                        if int(line.replace('\n', '')) == Desmarc:
                            __ids.append(int(line.replace('\n', '')))
                            igual = True
                        else:
                            __ids.append(int(line.replace('\n', '')))
                    elif enum % 2 == 1:
                        if igual:
                            line = line.replace('\n', '')
                            igual = False
                            __names.append(line.replace('&', ''))
                            __Desmarcado = line.replace('&', '')
                        else:
                            __names.append(line.replace('\n', ''))
            with open(self.__clientes, 'w+') as Editable:
                for cont in range(0, len(__names)):
                    Editable.write(f'{str(__ids[cont])}\n')
                    Editable.write(f'{str(__names[cont])}\n')
            try:
                __ids.index(Desmarc)
            except:
                MenuError('ID NÃO ENCONTRADO')
            else:
                print(f'O cliente \'{__Desmarcado}\' foi desmarcado com sucesso')
                break

    def MarcarCliente(self):
        global __Marcado
        while True:
            __ids = []
            __name = []
            verdade = False
            print('         999 Para')
            marc = leiaInt('Pelo ID, qual cliente quer marcar: ')
            if marc == 999:
                return
            with open(self.__clientes, 'r') as arqv:
                for enu, line in enumerate(arqv):
                    if enu % 2 == 0:
                        line = line.replace('\n', '')
                        if int(line) == marc:
                            verdade = True
                            __ids.append(int(line))
                        else:
                            __ids.append(int(line))
                    elif enu % 2 == 1:
                        if verdade:
                            line = line.replace('\n', '')
                            __Marcado = f'&{line}'
                            __name.append(__Marcado)
                            __Marcado = __Marcado.replace('&', '')
                            verdade = False
                        else:
                            __name.append(line.replace('\n', ''))
            with open(self.__clientes, 'w+') as Arqvo:
                for cont in range(len(__name)):
                    Arqvo.write(f'{__ids[cont]}')
                    Arqvo.write(f'\n{__name[cont]}\n')
            try:
                __ids.index(marc)
            except:
                MenuError('ID NÃO ENCONTRADO')
            else:
                print(f'O cliente \'{__Marcado}\' foi marcado com sucesso')
                break

