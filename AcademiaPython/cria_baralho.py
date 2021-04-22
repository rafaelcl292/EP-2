def cria_baralho():
    valores = [str(a) for a in range(2, 11)] + ['Q', 'J', 'K', 'A']
    naipes = ['♠', '♥', '♣', '♦']
    baralho = []
    for valor in valores:
        for naipe in naipes:
            baralho.append(valor + naipe)
    return baralho
