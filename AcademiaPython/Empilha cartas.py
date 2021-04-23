def empilha(baralho, origem, destino):
    carta_seleciona = baralho[origem]
    baralho[destino] = carta_seleciona
    del(baralho[origem])
    return baralho
