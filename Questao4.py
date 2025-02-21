# Questão 4:

import struct

palavrasSemPontuacao = []


def retiraPontuacao(item):
    sempontuacao = ''
    for letra in item:
        if letra in "abcdefghijklmnopqrstuvwxyz0123456789":
            sempontuacao += letra
    return palavrasSemPontuacao.append(sempontuacao)


# Programa Principal
arquivoTexto = input()  # "uma_carta.txt"

dados = open(arquivoTexto, "r")
linha = dados.readline()
while linha != "":
    palavra = linha.lower().split()
    for item in palavra:
        retiraPontuacao(item)
    linha = dados.readline()
dados.close()

total = 0
try:
    with open("referencia.bin", "rb") as arq:
        bloco = arq.read(256)
        while bloco != b"":
            palavraImposto = bloco.decode().rstrip(chr(0)).lower()
            valorImposto = struct.unpack("d", arq.read(8))[0]
            if palavrasSemPontuacao.count(palavraImposto) >= 2:
                total += 2 * valorImposto
            elif palavrasSemPontuacao.count(palavraImposto) == 1:
                total += valorImposto
            bloco = arq.read(256)
except IOError:
    print("Erro ao abrir ou ao manipular o arquivo.")

try:
    with open("imposto.bin", "wb") as imp:
        bloco = struct.pack("=d", total)
        imp.write(bloco)
except IOError:
    print("Erro ao abrir ou ao manipular o arquivo.")
