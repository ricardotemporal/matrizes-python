def normalizar(v):
    norma = sum(x * x for x in v) ** 0.5
    return [x / norma for x in v] if norma != 0 else v


def somas_colunas_normalizadas(A):
    colunas_soma = [sum(linha[i] for linha in A) for i in range(len(A[0]))]
    return normalizar(colunas_soma)


def dot(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(A[i]))) for i in range(len(A))]


def distancia_vetores(v1, v2):
    return sum((x - y) ** 2 for x, y in zip(v1, v2)) ** 0.5


def transposta(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def ordenar(vetor):
    return sorted(
        ((i + 1, score) for i, score in enumerate(vetor)),
        key=lambda x: x[1],
        reverse=True,
    )


def calcular_vetor_autoridade(A, iteracoes=1000, tolerancia=0.00001):
    a0 = somas_colunas_normalizadas(A)
    for _ in range(iteracoes):
        Av = dot(A, a0)
        AtAv = dot(transposta(A), Av)
        a1 = normalizar(AtAv)

        if distancia_vetores(a1, a0) < tolerancia:
            break

        a0 = a1
    return a0


def criar_matriz():
    while True:
        try:
            n = int(
                input("Insira o número de sites (nós) para a matriz de adjacência: ")
            )
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Por favor, insira um número inteiro positivo.")

    matriz = []
    print("Insira as linhas da matriz de adjacência, separando os números com espaços:")
    for i in range(n):
        while True:
            try:
                linha = input(f"Linha {i+1}: ").strip().split()
                if len(linha) != n or not all(elem.isdigit() for elem in linha):
                    raise ValueError
                matriz.append([int(elem) for elem in linha])
                break
            except ValueError:
                print(
                    f"Entrada inválida. Certifique-se de inserir {n} números (0 ou 1) separados por espaços."
                )

    return matriz


def menu():
    matrizes_adjacencia = {
        5: [[0, 0, 1, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]],
        6: [[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0]],
        7: [
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
        ],
        8: [
            [0, 1, 1, 0, 1, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 0, 0],
        ],
    }

    while True:
        escolha = input(
            "Escolha um número de 5 a 8 para calcular os vetor de autoridade, 'criar' para criar uma matriz própria, ou 'sair' para terminar: "
        ).strip()
        if escolha.lower() == "sair":
            print("Encerrando o programa.")
            break

        if escolha.lower() == "criar":
            matriz_usuario = criar_matriz()
            vetor = calcular_vetor_autoridade(matriz_usuario)
            vetor_ordenados = ordenar(vetor)
            print(f"\nvetor de autoridade para sua matriz criada:")
            for indice, score in vetor_ordenados:
                print(f"Site {indice}: {score:.4f}")
        elif escolha.isdigit() and int(escolha) in matrizes_adjacencia:
            exercicio = int(escolha)
            vetor = calcular_vetor_autoridade(matrizes_adjacencia[exercicio])
            vetor_ordenados = ordenar(vetor)
            print(f"\nvetor de autoridade ordenados para o exercício {exercicio}:")
            for indice, score in vetor_ordenados:
                print(f"Site {indice}: {score:.4f}")
        else:
            print(
                "Entrada inválida. Por favor, escolha um número de 5 a 8, 'criar' para criar uma matriz ou 'sair' para sair."
            )


menu()
