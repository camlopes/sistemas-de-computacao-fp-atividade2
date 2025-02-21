# Questão 3:


def distancia(centroide):
    dados = open(raioEarquivo[1], "r")
    linha = dados.readline()
    while linha != "":
        pontos = linha.split()
        if ((float(pontos[0]) - centroide[0])**2 + (float(pontos[1]) - centroide[1])**2) <= int(raioEarquivo[0])**2:
            print(*pontos)
        linha = dados.readline()
    dados.close()
    return None


def centroide(raioEarquivo):
    dados = open(raioEarquivo[1], "r")
    linha = dados.readline()
    x = 0
    y = 0
    contador = 0
    while linha != "":
        pontos = linha.split()
        x += float(pontos[0])
        y += float(pontos[1])
        contador += 1
        linha = dados.readline()
    dados.close()
    centroide = x/contador, y/contador
    print("Centroide: (%.1f, %.1f)" % (x/contador, y/contador))
    return distancia(centroide)


# Programa Principal
raioEarquivo = input().split()
centroide(raioEarquivo)