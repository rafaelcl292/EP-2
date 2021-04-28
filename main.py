from functions import *

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

while True:
    baralho = cria_baralho()
    jogar(baralho)
    if len(baralho) == 1:
        print("\nParabéns você venceu!")
    else:
        print("\nVocê perdeu :(\nMais sorte da próxima vez!")
    if input("Você deseja jogar novamente?\n(S/N): ") != 'S':
        break