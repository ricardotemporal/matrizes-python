from random import random

LA = int(input("Digite o número de linhas da matriz A: "))
CA = int(input("Digite o número de colunas da matriz A: "))
A = [None] * LA
for i in range(len(A)):
    A[i] = [None] * CA

for i in range(len(A)):
    for j in range(len(A[i])):
        A[i][j] = int(random() * 10)

LB = int(input("Digite o número de linhas da matriz B: "))
CB = int(input("Digite o número de colunas da matriz B: "))
B = [None] * LB
for i in range(len(B)):
    B[i] = [None] * CB

for i in range(len(B)):
    for j in range(len(B[i])):
        B[i][j] = int(random() * 10)


def imprimir(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if j < len(M[i]) - 1:
                print(M[i][j], end="   ")
            else:
                print(M[i][j])


print()
print(">>>>>>>>>>>>>>> MATRIZES FORMADAS <<<<<<<<<<<<<<<")
print()
print("<-- MATRIZ A -->")
imprimir(A)
print()
print("<-- MATRIZ B -->")
imprimir(B)
print()


def timesescalar():
    print("/////////////// Função times escalar ///////////////")
    print()
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))
    print()

    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = A[i][j] * x
    print(f"<-- MATRIZ A x {x} -->")
    imprimir(A)
    print()
    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] = B[i][j] * y
    print(f"<-- MATRIZ B x {y} -->")
    imprimir(B)
    print()
    print("/" * 40)


def timesmatriz():
    print("/////////////// Função times matriz ///////////////")
    print()
    C = [None] * len(A)
    for i in range(len(C)):
        C[i] = [None] * len(A[0])
    for i in range(len(C)):
        for j in range(len(C[0])):
            C[i][j] = A[i][j] * B[i][j]
    print(f"<-- MATRIZ A x MATRIZ B -->")
    imprimir(C)
    print()
    print("/" * 40)


def transpose():
    print("/////////////// Função transpose ///////////////")
    print()
    C = [None] * len(A[0])
    for i in range(len(C)):
        C[i] = [None] * len(A)
    for i in range(len(C)):
        for j in range(len(C[i])):
            C[i][j] = A[j][i]
    print("<-- MATRIZ A TRANSPOSTA -->")
    imprimir(C)
    print()


def sum():
    print("/////////////// Função sum ///////////////")
    print()
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        soma = [None] * len(A)
        for i in range(len(soma)):
            soma[i] = [None] * len(A[0])
        for i in range(len(soma)):
            for j in range(len(soma[i])):
                soma[i][j] = A[i][j] + B[i][j]
        print("<-- MATRIZ SOMA -->")
        imprimir(soma)
    else:
        print("As linhas e colunas de A devem ser iguais as linhas e colunas de B")
    print()
    print("/" * 40)


def dot():
    print("/////////////// Função dot ///////////////")
    print()
    if len(A[0]) == len(B):
        Y = [None] * len(A)
        for i in range(len(Y)):
            Y[i] = [None] * len(B[0])
        for i in range(len(Y)):
            for j in range(len(Y[i])):
                s = 0
                for k in range(len(B)):
                    s += A[i][k] * B[k][j]
                Y[i][j] = s
        print("<-- MATRIZ RESULTANTE -->")
        imprimir(Y)
    else:
        print("Ordens de matrizes não casam para produto matricial")
    print()
    print("/" * 40)


def get(M, i, j):
    print("/////////////// Função get ///////////////")
    print()
    if i >= 0 and i < len(M) and j >= 0 and j < len(M[0]):
        print(M[i][j])
    else:
        print("Índices fora do limite da matriz")
    print()
    print("/" * 40)


def set(M, i, j, value):
    print("/////////////// Função set ///////////////")
    print()
    if i >= 0 and i < len(M) and j >= 0 and j < len(M[0]):
        M[i][j] = value
        print(f"Valor atualizado na posição ({i}, {j})")
        imprimir(M)
    else:
        print("Índices fora do limite da matriz")
    print()
    print("/" * 40)


while True:
    print("/" * 40)
    print()
    print("DIGITE '0' PARA PARAR O PROGRAMA")
    print(">>>>> 1 - Times Escalar")
    print(">>>>> 2 - Times Matriz")
    print(">>>>> 3 - Transposta")
    print(">>>>> 4 - Soma")
    print(">>>>> 5 - Resultante da matriz")
    print(">>>>> 6 - Método get")
    print(">>>>> 7 - Método set")
    print()
    print("/" * 40)
    print()
    f = int(input("DIGITE O NÚMERO --> "))
    print()
    if f == 0:
        break
    elif f == 1:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        print("<-- MATRIZ B -->")
        imprimir(B)
        print()
        timesescalar()
    elif f == 2:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        print("<-- MATRIZ B -->")
        imprimir(B)
        print()
        timesmatriz()
    elif f == 3:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        transpose()
    elif f == 4:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        print("<-- MATRIZ B -->")
        imprimir(B)
        print()
        sum()
    elif f == 5:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        print("<-- MATRIZ B -->")
        imprimir(B)
        print()
        dot()
    elif f == 6:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        i = int(input("Digite o índice da linha: "))
        j = int(input("Digite o índice da coluna: "))
        get(A, i, j)
    elif f == 7:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        i = int(input("Digite o índice da linha: "))
        j = int(input("Digite o índice da coluna: "))
        value = int(input("Digite o valor a ser armazenado: "))
        set(A, i, j, value)
    print()
