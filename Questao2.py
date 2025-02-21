# Questão 2:


def imprimir(pessoas, virus):
    if len(pessoas) == 0:
        print("Nenhuma pessoa infectada com", virus[0], "\n")
    else:
        print("Passoa(s) infectada(s) por", virus[0], ":")
        for item in range(len(pessoas)):
            print(pessoas[item])
        print()
    return None


def contaminado(virus):
    CPF = []  # Quantas pessoas estao contaminadas
    arqui = open(arquivo2, "r")
    linha = arqui.readline()
    while linha != "":
        DNA = linha.split("#")
        contadorVirus = virus[1]
        contadorDNA = DNA[1]
        contadorNucleosBase = 0
        for item in range(len(contadorVirus)):
            if contadorVirus[item] == contadorDNA[item]:
                contadorNucleosBase += 1
        if contadorNucleosBase - 1 > len(contadorVirus) / 2:
            CPF.append(DNA[0])
        linha = arqui.readline()
    arqui.close()
    return CPF


def lendoVirus(arquivo):
    dados = open(arquivo, "r")
    linha = dados.readline()
    while linha != "":
        virus = linha.split("#")
        imprimir(contaminado(virus), virus)
        linha = dados.readline()
    dados.close()
    return None


# Programa Principal
arquivo1 = input()  # Nome do arquivo: virus.txt  vírus#RNA
arquivo2 = input()  # Nome do arquivo: cpf.txt CPF#DNA
lendoVirus(arquivo1)


