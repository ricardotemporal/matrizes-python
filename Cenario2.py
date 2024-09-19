import numpy as np
import math


def translate2D(vetor, dx, dy):
    MatrizTranslacao = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
    VetorHomogeneo = np.append(vetor, 1)
    VetorTranslacao = np.dot(MatrizTranslacao, VetorHomogeneo)
    return VetorTranslacao[:2]


def translate3D(vetor, dx, dy, dz):
    MatrizTranslacao = np.array(
        [[1, 0, 0, dx], [0, 1, 0, dy], [0, 0, 1, dz], [0, 0, 0, 1]]
    )
    VetorHomogeneo = np.append(vetor, 1)
    VetorTranslacao = np.dot(MatrizTranslacao, VetorHomogeneo)
    return VetorTranslacao[:3]


def rotation2D(vetor, angulo):
    AnguloRadiano = math.radians(angulo)
    MatrizRotacao = np.array(
        [
            [math.cos(AnguloRadiano), -math.sin(AnguloRadiano), 0],
            [math.sin(AnguloRadiano), math.cos(AnguloRadiano), 0],
            [0, 0, 1],
        ]
    )
    VetorHomogeneo = np.append(vetor, 1)
    VetorRotacao = np.dot(MatrizRotacao, VetorHomogeneo)
    return VetorRotacao[:2]


def rotation3DX(vetor, angulo):
    AnguloRadiano = math.radians(angulo)
    MatrizRotacao = np.array(
        [
            [1, 0, 0, 0],
            [0, math.cos(AnguloRadiano), -math.sin(AnguloRadiano), 0],
            [0, math.sin(AnguloRadiano), math.cos(AnguloRadiano), 0],
            [0, 0, 0, 1],
        ]
    )
    VetorHomogeneo = np.append(vetor, 1)
    VetorRotacao = np.dot(MatrizRotacao, VetorHomogeneo)
    return VetorRotacao[:3]


def rotation3DY(vetor, angulo):
    AnguloRadiano = math.radians(angulo)
    MatrizRotacao = np.array(
        [
            [math.cos(AnguloRadiano), 0, math.sin(AnguloRadiano), 0],
            [0, 1, 0, 0],
            [-math.sin(AnguloRadiano), 0, math.cos(AnguloRadiano), 0],
            [0, 0, 0, 1],
        ]
    )
    VetorHomogeneo = np.append(vetor, 1)
    VetorRotacao = np.dot(MatrizRotacao, VetorHomogeneo)
    return VetorRotacao[:3]


def rotation3DZ(vetor, angulo):
    AnguloRadiano = math.radians(angulo)
    MatrizRotacao = np.array(
        [
            [math.cos(AnguloRadiano), -math.sin(AnguloRadiano), 0, 0],
            [math.sin(AnguloRadiano), math.cos(AnguloRadiano), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )
    VetorHomogeneo = np.append(vetor, 1)
    VetorRotacao = np.dot(MatrizRotacao, VetorHomogeneo)
    return VetorRotacao[:3]


def reflection2DX(vetor):
    MatrizReflexao = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
    VetorHomogeneo = np.append(vetor, 1)
    VetorReflexao = np.dot(MatrizReflexao, VetorHomogeneo)
    return VetorReflexao[:2]


def reflection2DY(vetor):
    MatrizReflexao = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    VetorHomogeneo = np.append(vetor, 1)
    VetorReflexao = np.dot(MatrizReflexao, VetorHomogeneo)
    return VetorReflexao[:2]


def reflection3DX(vetor):
    MatrizReflexao = np.array(
        [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]
    )
    VetorHomogeneo = np.append(vetor, 1)
    VetorReflexao = np.dot(MatrizReflexao, VetorHomogeneo)
    return VetorReflexao[:3]


def reflection3DY(vetor):
    MatrizReflexao = np.array(
        [[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]
    )
    VetorHomogeneo = np.append(vetor, 1)
    VetorReflexao = np.dot(MatrizReflexao, VetorHomogeneo)
    return VetorReflexao[:3]


def reflection3DZ(vetor):
    MatrizReflexao = np.array(
        [[-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    )
    VetorHomogeneo = np.append(vetor, 1)
    VetorReflexao = np.dot(MatrizReflexao, VetorHomogeneo)
    return VetorReflexao[:3]


def projection2DX(vetor):
    MatrizProjecao = np.array([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
    VetorHomogeneo = np.append(vetor, 1)
    VetorProjecao = np.dot(MatrizProjecao, VetorHomogeneo)
    return VetorProjecao[:2]


def projection2DY(vetor):
    MatrizProjecao = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 1]])
    VetorHomogeneo = np.append(vetor, 1)
    VetorProjecao = np.dot(MatrizProjecao, VetorHomogeneo)
    return VetorProjecao[:2]


def projection3DX(vetor):
    MatrizProjecao = np.array([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    VetorHomogeneo = np.append(vetor, 1)
    VetorProjecao = np.dot(MatrizProjecao, VetorHomogeneo)
    return VetorProjecao[:3]


def projection3DY(vetor):
    MatrizProjecao = np.array([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])
    VetorHomogeneo = np.append(vetor, 1)
    VetorProjecao = np.dot(MatrizProjecao, VetorHomogeneo)
    return VetorProjecao[:3]


def projection3DZ(vetor):
    MatrizProjecao = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    VetorHomogeneo = np.append(vetor, 1)
    VetorProjecao = np.dot(MatrizProjecao, VetorHomogeneo)
    return VetorProjecao[:3]


def shearing(vetor, kx, ky):
    MatrizCisalhamento = np.array([[1, kx, 0], [ky, 1, 0], [0, 0, 1]])
    VetorHomogeneo = np.append(vetor, 1)
    VetorCisalhamento = np.dot(MatrizCisalhamento, VetorHomogeneo)
    return VetorCisalhamento[:2]


while True:
    print("/" * 40)
    print()
    print("DIGITE '0' PARA PARAR O PROGRAMA")
    print(">>>>> 1 = Translação 2D")
    print(">>>>> 2 = Translação 3D")
    print(">>>>> 3 = Rotação 2D")
    print(">>>>> 4 = Rotação 3DX")
    print(">>>>> 5 = Rotação 3DY")
    print(">>>>> 6 = Rotação 3DZ")
    print(">>>>> 7 = Reflexão 2DX")
    print(">>>>> 8 = Reflexão 2DY")
    print(">>>>> 9 = Reflexão 3DX")
    print(">>>>> 10 = Reflexão 3DY")
    print(">>>>> 11 = Reflexão 3DZ")
    print(">>>>> 12 = Projeção 2DX")
    print(">>>>> 13 = Projeção 2DY")
    print(">>>>> 14 = Projeção 3DX")
    print(">>>>> 15 = Projeção 3DY")
    print(">>>>> 16 = Projeção 3DZ")
    print(">>>>> 17 = Cisalhamento")
    print()
    print("/" * 40)
    print()
    f = int(input("DIGITE O NÚMERO DA FUNÇÃO DESEJADA --> "))
    print()
    if f == 0:
        break
    elif f == 1:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        vetor = np.array([x, y])
        dx = int(input("Digite o valor de dx: "))
        dy = int(input("Digite o valor de dy: "))
        VetorTranslacao = translate2D(vetor, dx, dy)
        print("Vetor original:", vetor)
        print("Vetor traduzido:", VetorTranslacao)
    elif f == 2:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        vetor = np.array([x, y, z])
        dx = int(input("Digite o valor de dx: "))
        dy = int(input("Digite o valor de dy: "))
        dz = int(input("Digite o valor de dz: "))
        VetorTranslacao = translate3D(vetor, dx, dy, dz)
        print("Vetor original:", vetor)
        print("Vetor traduzido:", VetorTranslacao)
    elif f == 3:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        vetor_2d = np.array([x, y])
        angulo_2d = int(input("Digite o valor do ângulo: "))
        print("Rotação 2D:", rotation2D(vetor_2d, angulo_2d))
    elif f == 4:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        vetor_3d = np.array([x, y, z])
        angulo_3d = int(input("Digite o valor do ângulo: "))
        print("Rotação 3D em torno do eixo X:", rotation3DX(vetor_3d, angulo_3d))
    elif f == 5:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        vetor_3d = np.array([x, y, z])
        angulo_3d = int(input("Digite o valor do ângulo: "))
        print("Rotação 3D em torno do eixo Y:", rotation3DY(vetor_3d, angulo_3d))
    elif f == 6:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        vetor_3d = np.array([x, y, z])
        angulo_3d = int(input("Digite o valor do ângulo: "))
        print("Rotação 3D em torno do eixo Z:", rotation3DZ(vetor_3d, angulo_3d))
    elif f == 7:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        vetor_2d = np.array([x, y])
        print("Reflexão 2D no eixo X:", reflection2DX(vetor_2d))
    elif f == 8:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        vetor_2d = np.array([x, y])
        print("Reflexão 2D no eixo Y:", reflection2DY(vetor_2d))
    elif f == 9:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        vetor_3d = np.array([x, y, z])
        print("Reflexão 3D no eixo X:", reflection3DX(vetor_3d))
    elif f == 10:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        vetor_3d = np.array([x, y, z])
        print("Reflexão 3D no eixo Y:", reflection3DY(vetor_3d))
    elif f == 11:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        vetor_3d = np.array([x, y, z])
        print("Reflexão 3D no eixo Z:", reflection3DZ(vetor_3d))
    elif f == 12:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        vetor_2d = np.array([x, y])
        print("Projeção 2D no eixo X:", projection2DX(vetor_2d))
    elif f == 13:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        vetor_2d = np.array([x, y])
        print("Projeção 2D no eixo Y:", projection2DY(vetor_2d))
    elif f == 14:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        vetor_3d = np.array([x, y, z])
        print("Projeção 3D no eixo X:", projection3DX(vetor_3d))
    elif f == 15:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        vetor_3d = np.array([x, y, z])
        print("Projeção 3D no eixo Y:", projection3DY(vetor_3d))
    elif f == 16:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        z = int(input("Digite o valor de z: "))
        vetor_3d = np.array([x, y, z])
        print("Projeção 3D no eixo Z:", projection3DZ(vetor_3d))
    elif f == 17:
        print()
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        vetor_2d = np.array([x, y])
        kx = int(input("Digite o valor de kx: "))
        ky = int(input("Digite o valor de ky: "))
        print("Vetor após cisalhamento:", shearing(vetor_2d, kx, ky))
    print()
