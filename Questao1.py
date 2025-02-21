# Questão 1:

nomes = []
lista = []
duplicada = []


def trocar(valores, posX, posY):
    temp = valores[posX]
    valores[posX] = valores[posY]
    valores[posY] = temp
    return None


def particiona(valores, inicio, fim):
    pivo = valores[inicio]
    i = inicio + 1
    j = fim
    while i < j:
        while i < fim and valores[i] < pivo:
            i += 1
        while j > inicio and valores[j] >= pivo:
            j -= 1
        if i < j:
            trocar(valores, i, j)
    if pivo > valores[j]:
        trocar(valores, inicio, j)
    return j


def quickSort(valores, inicio, fim):
    if inicio < fim:
        posPivo = particiona(valores, inicio, fim)
        quickSort(valores, inicio, posPivo - 1)
        quickSort(valores, posPivo + 1, fim)
    return None


def ordenar(valores):
    quickSort(valores, 0, len(valores) - 1)
    return None


def formalista(nomes):
    indice = 0
    while indice < len(nomes):
        for item in nomes[indice]:
            lista.append(item)
        indice += 1
    return None


def achaDuplicatas(nomes):
    indice = 0
    while indice < len(nomes):
        if len(nomes[indice]) > 2:
            if nomes.count(nomes[indice]) == 1:
                indice += 1
            elif duplicada.count(nomes[indice]) == 1:
                indice += 1
            else:
                duplicada.append(nomes[indice])
                indice += 1
        else:
            indice += 1
    return None


def ler(lida):
    while True:
        if lida == "":
            return None
        else:
            nomes.append(lida.split())
            lida = input()


# Programa Principal
lida = input()
ler(lida)
formalista(nomes)
achaDuplicatas(lista)
ordenar(duplicada)
for item in range(len(duplicada)):
    print(duplicada[item])
