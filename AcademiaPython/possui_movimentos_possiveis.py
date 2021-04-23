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
