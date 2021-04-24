from functions import *
from time import sleep

input(
    "\nPaciência Acordeão\n"
    "==================\n"
    "\n"
    "Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n"
    "\n"
    "Existem apenas dois movimentos possíveis:\n"
    "\n"
    "1. Empilhar uma carta sobre a carta imediatamente anterior;\n"
    "2. Empilhar uma carta sobre a terceira carta anterior.\n"
    "\n"
    "Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n"
    "\n"
    "1. As duas cartas possuem o mesmo valor ou\n"
    "2. As duas cartas possuem o mesmo naipe.\n"
    "\n"
    "Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n"
    "\n"
    "Aperte [Enter] para iniciar o jogo..."
)

baralho = cria_baralho()

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
