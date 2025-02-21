# Questão 5:

binario = []


def divisao(n, w):
    if n == 0:
        return print("%.4f" % w)
    else:
        w += 1 / n
        divisao(n-1, w)


def multiplicacao(b, x):
    if int(b) == 1:
        return print(x)
    else:
        multiplicacao(int(b)-1, x+int(c))


def passarParaBinario(a):
    if a == 0:
        return binario
    else:
        binario.insert(0, int(a % 2))
        passarParaBinario(int(a / 2))


# Programa Principal
a = int(input())
passarParaBinario(a)
print(*binario)

b, c = input().split()
x = int(c)
multiplicacao(b, x)

n = int(input())
w = 0
divisao(n, w)
