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


def questao1():
    print("/////////////// QUESTÃO 1 ///////////////")
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


def questao2():
    print("/////////////// QUESTÃO 2 ///////////////")
    print()
    C = [None] * len(A[0])
    for i in range(len(C)):
        C[i] = [None] * len(A)
    for i in range(len(C)):
        for j in range(len(C[i])):
            C[i][j] = A[j][i]
    D = [None] * len(B[0])
    for i in range(len(D)):
        D[i] = [None] * len(B)
    for i in range(len(D)):
        for j in range(len(D[i])):
            D[i][j] = B[j][i]
    print("<-- MATRIZ A TRANSPOSTA -->")
    imprimir(C)
    print()
    print("<-- MATRIZ B TRANSPOSTA -->")
    imprimir(D)
    print()
    print("/" * 40)


def questao3():
    print("/////////////// QUESTÃO 3 ///////////////")
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


def questao4():
    print("/////////////// QUESTÃO 4 ///////////////")
    print()
    if len(A) == len(A[0]):
        print("<-- DIAGONAL PRINCIPAL MATRIZ A -->")
        print()
        for i in range(len(A)):
            for j in range(len(A[i])):
                if i == j:
                    print(A[i][j], end="  ")
                else:
                    print(end="   ")
            print()
        print()
        print("<-- DIAGONAL SECUNDÁRIA MATRIZ A -->")
        print()
        for i in range(len(A)):
            for j in range(len(A[i])):
                if j == len(A) - 1 - i:
                    print(A[i][j], end="  ")
                else:
                    print(end="   ")
            print()
    else:
        maior = A[0][0]
        pi = 0
        pj = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] > maior:
                    maior = A[i][j]
                    pi = i
                    pj = j
        print(f"Maior elemento de A: {maior} e está na posição i{pi}, j{pj}.")
    print()
    print("/" * 40)


def questao5():
    print("/////////////// QUESTÃO 5 ///////////////")
    print()
    if len(B) == len(B[0]):
        print("<-- DIAGONAL PRINCIPAL MATRIZ B -->")
        print()
        for i in range(len(B)):
            for j in range(len(B[i])):
                if i == j:
                    print(B[i][j], end="  ")
                else:
                    print(end="   ")
            print()
        print()
        print("<-- ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL MATRIZ B -->")
        print()
        for i in range(len(B)):
            for j in range(len(B[0])):
                if i < j:
                    print(B[i][j], end="  ")
                else:
                    print(end="   ")
            print()
        print()
        print("<-- ELEMENTOS ABAIXO DA DIAGONAL PRINCIPAL MATRIZ B -->")
        print()
        for i in range(len(B)):
            for j in range(len(B[0])):
                if i > j:
                    print(B[i][j], end="  ")
                else:
                    print(end="   ")
            print()
    else:
        menor = B[0][0]
        pi = 0
        pj = 0
        for i in range(len(B)):
            for j in range(len(B[i])):
                if B[i][j] < menor:
                    menor = B[i][j]
                    pi = i
                    pj = j
        print(f"Menor elemento de B: {menor} e está na posição i{pi}, j{pj}.")
    print()
    print("/" * 40)


def questao6():
    print("/////////////// QUESTÃO 6 ///////////////")
    print()
    if len(A) == 1:
        soma = 0
        quantidade = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                soma += A[i][j]
                quantidade += 1
        print(f"Média dos valores no vetor linha: {soma/quantidade:.1f}")
    elif len(A[0]) == 1:
        soma = 0
        quantidade = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                soma += A[i][j]
                quantidade += 1
        print(f"Média dos valores no vetor coluna: {soma/quantidade:.1f}")
    print()
    print("/" * 40)


def questao7():
    print("/////////////// QUESTÃO 7 ///////////////")
    print()
    if len(B) != len(B[0]):
        if len(B) != 1 or len(B[0]) != 1:
            X = [None] * len(B[0])
            for i in range(len(X)):
                X[i] = [None] * len(B)
            for i in range(len(X)):
                for j in range(len(X[i])):
                    X[i][j] = B[j][i] * 2.5
            print("<-- MATRIZ B TRANSPOSTA x 2.5 -->")
            imprimir(X)
    else:
        quantidade = 0
        for i in range(len(B)):
            for j in range(len(B[i])):
                n = 0
                cont = 1
                while cont <= B[i][j]:
                    if B[i][j] % cont == 0:
                        n += 1
                    cont += 1
                if n == 2:
                    quantidade += 1
        print(f"A matriz B possui {quantidade} números primos.")
    print()
    print("/" * 40)


def questao9():
    print("/////////////// QUESTÃO 9 ///////////////")
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


while True:
    print("/" * 40)
    print()
    print("DIGITE '0' PARA PARAR O PROGRAMA")
    print(">>>>> QUESTÃO 1 (Multiplicando matrizes) ")
    print(">>>>> QUESTÃO 2 (Matrizes transpostas)")
    print(">>>>> QUESTÃO 3 (Somando matrizes)")
    print(">>>>> QUESTÃO 4 (Diagonal matriz A)")
    print(">>>>> QUESTÃO 5 (Diagonal matriz B e elementos)")
    print(">>>>> QUESTÃO 6 (Vetores(linhas/coluna) média)")
    print(">>>>> QUESTÃO 7 (Transposta e primo)")
    print(">>>>> QUESTÃO 9 (Resultante da matriz)")
    print()
    print("/" * 40)
    print()
    f = int(input("DIGITE O NÚMERO DA QUESTÃO DESEJADA --> "))
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
        questao1()
    elif f == 2:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        print("<-- MATRIZ B -->")
        imprimir(B)
        print()
        questao2()
    elif f == 3:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        print("<-- MATRIZ B -->")
        imprimir(B)
        print()
        questao3()
    elif f == 4:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        questao4()
    elif f == 5:
        print("<-- MATRIZ B -->")
        imprimir(B)
        print()
        questao5()
    elif f == 6:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        questao6()
    elif f == 7:
        print("<-- MATRIZ B -->")
        imprimir(B)
        print()
        questao7()
    elif f == 9:
        print("<-- MATRIZ A -->")
        imprimir(A)
        print()
        print("<-- MATRIZ B -->")
        imprimir(B)
        print()
        questao9()
    print()
