def cria_baralho():
    valores = ['A'] + [str(a) for a in range(2, 11)] + ['J', 'Q', 'K']
    naipes = ['♠', '♥', '♣', '♦']
    baralho = []
    for valor in valores:
        for naipe in naipes:
            baralho.append(valor + naipe)
    return baralho


def naipe(carta):
    return carta[-1]


def valor(carta):
    return carta[:-1]
