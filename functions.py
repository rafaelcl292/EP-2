import random
import colorama
# from goto import goto, label
from time import sleep
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def cria_baralho():
    valores = [str(a) for a in range(2, 11)] + ['J', 'Q', 'K', 'A']
    naipes = ['♠', '♥', '♣', '♦']
    baralho = []
    for valor in valores:
        for naipe in naipes:
            baralho.append(valor + naipe)
    random.shuffle(baralho)
    return baralho


def naipe(carta):
    return carta[-1]


def valor(carta):
    return carta[:-1]


def lista_movimentos_possiveis(baralho, i):
    if i != 0:
        if i <= 2:
            if baralho[i][-1] == baralho[i-1][-1] or baralho[i][:-1] == baralho[i-1][:-1]:
                return [1]
        else:
            if (baralho[i][-1] == baralho[i-1][-1] or baralho[i][:-1] == baralho[i-1][:-1]) and (baralho[i][-1] == baralho[i-3][-1] or baralho[i][:-1] == baralho[i-3][:-1]):
                return [1, 3]
            if baralho[i][-1] == baralho[i-1][-1] or baralho[i][:-1] == baralho[i-1][:-1]:
                return [1]
            if baralho[i][-1] == baralho[i-3][-1] or baralho[i][:-1] == baralho[i-3][:-1]:
                return [3]
    return []


def empilha(baralho, origem, destino):
    baralho[destino] = baralho[origem]
    del(baralho[origem])
    return baralho


def lista_movimentos_possiveis(baralho, i):
    if i != 0:
        if i <= 2:
            if baralho[i][-1] == baralho[i-1][-1] or baralho[i][:-1] == baralho[i-1][:-1]:
                return [1]
        else:
            if (baralho[i][-1] == baralho[i-1][-1] or baralho[i][:-1] == baralho[i-1][:-1]) and (baralho[i][-1] == baralho[i-3][-1] or baralho[i][:-1] == baralho[i-3][:-1]):
                return [1, 3]
            if baralho[i][-1] == baralho[i-1][-1] or baralho[i][:-1] == baralho[i-1][:-1]:
                return [1]
            if baralho[i][-1] == baralho[i-3][-1] or baralho[i][:-1] == baralho[i-3][:-1]:
                return [3]
    return []


def possui_movimentos_possiveis(baralho):
    possui = False
    i = 0
    for _ in baralho:
        if lista_movimentos_possiveis(baralho, i) != []:
            possui = True
        i += 1
    return possui


def imprime_baralho(baralho):
    for i, carta in enumerate(baralho):
        if naipe(carta) == '♣' or naipe(carta) == '♠':
            color = Fore.BLACK
        else:
            color = Fore.RED
        i += 1
        if i < 10:
            i = f' {i}'
        if len(valor(carta)) == 2:
            print(f'\n{i}. {Back.WHITE}{color} {valor(carta)} {naipe(carta)}  ')
        else:
            print(f'\n{i}. {Back.WHITE}{color}  {valor(carta)} {naipe(carta)}  ')
    return


def imprime_baralho2(baralho):
    # Reescrever a função imprime_baralho para uma melhor visialização das cartas
    pass


def carta_formatada(baralho, i):
    carta = baralho[i]
    if naipe(carta) == '♣' or naipe(carta) == '♠':
        color = Fore.BLACK
    else:
        color = Fore.RED
    if len(valor(carta)) == 2:
        return f'{Back.WHITE}{color} {valor(carta)} {naipe(carta)}  {Style.RESET_ALL}'
    return f'{Back.WHITE}{color}  {valor(carta)} {naipe(carta)}  {Style.RESET_ALL}'


def jogar(baralho):
    while possui_movimentos_possiveis(baralho):
        print('\nO estado atual do baralho é: ')
        imprime_baralho(baralho)
        mov = int(input(f'\nEscolha uma carta(digite um número entre 1 e {len(baralho)}): ')) - 1
        movimentos = lista_movimentos_possiveis(baralho, mov)
        if movimentos == []:
            print(f'A carta {carta_formatada(baralho, mov)} não pode ser movida.')
        elif movimentos == [1]:
            empilha(baralho, mov, mov - 1)
        elif movimentos == [3]:
            empilha(baralho, mov, mov - 3)
        else:
            print(
                f'Sobre qual carta você quer empilhar o {carta_formatada(baralho, mov)} ?'
                f'\n1. {carta_formatada(baralho, mov - 1)}\n'
                f'\n2. {carta_formatada(baralho, mov - 3)}\n'
            )
            perg = input(
                f'Digite o número de sua escolha (1 ou 2): '
            )
            if perg == '1':
                empilha(baralho, mov, mov - 1)
            elif perg == '2':
                empilha(baralho, mov, mov - 3)
        sleep(1.5)


def jogar2(baralho):
    while possui_movimentos_possiveis(baralho):
        print('\nO estado atual do baralho é: ')
        imprime_baralho(baralho)
        mov = input(f'\nEscolha uma carta(digite um número entre 1 e {len(baralho)}): ')
        if mov.startswith("D") or mov.startswith("d"):
            break
        if not mov.isdigit():
            print(f"\nDigite um número entre 1 e {len(baralho)}\n")
        elif int(mov) > len(baralho):
            print("\nMovimento impossivel")
            print(f"Digite um número entre 1 e {len(baralho)}\n")
        else:
            mov = int(mov) - 1
            movimentos = lista_movimentos_possiveis(baralho, mov)
            if movimentos == []:
                print(f'A carta {carta_formatada(baralho, mov)} não pode ser movida.')
            elif movimentos == [1]:
                empilha(baralho, mov, mov - 1)
            elif movimentos == [3]:
                empilha(baralho, mov, mov - 3)
            else:
                print(
                    f'Sobre qual carta você quer empilhar o {carta_formatada(baralho, mov)} ?'
                    f'\n1. {carta_formatada(baralho, mov - 1)}\n'
                    f'\n2. {carta_formatada(baralho, mov - 3)}\n'
                )
                perg = input(
                    f'Digite o número de sua escolha (1 ou 2): '
                )
                if perg == '1':
                    empilha(baralho, mov, mov - 1)
                elif perg == '2':
                    empilha(baralho, mov, mov - 3)
        sleep(1.5)