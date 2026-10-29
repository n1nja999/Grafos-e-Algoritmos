# GRAFO ORIENTADO
# Matriz de Adjacência
# Lista de Adjacência
# Busca em Profundidade (DFS)
# Busca em Largura (BFS)


def criar_grafo():
    n = int(input("Digite o número de vértices: "))

    matriz = []
    for i in range(n):
        matriz.append([0] * n)

    lista = []
    for i in range(n):
        lista.append([])

    arestas_cadastradas = set()
    quantidade = int(input("Digite o número de arestas: "))
    contador = 0

    while contador < quantidade:
        print(f"\nAresta {contador + 1}")
        origem = int(input("Vértice de origem: "))
        destino = int(input("Vértice de destino: "))

        if origem < 1 or origem > n or destino < 1 or destino > n:
            print("ERRO: vértice inválido!")
            print(f"Digite vértices entre 1 e {n}")
            continue

        if origem == destino:
            print("ERRO: não é permitido ligar um vértice a ele mesmo!")
            continue

        aresta = (origem, destino)

        if aresta in arestas_cadastradas:
            print("ERRO: esta aresta já foi cadastrada!")
            continue

        arestas_cadastradas.add(aresta)

        matriz[origem - 1][destino - 1] = 1

        lista[origem - 1].append(destino)
        contador += 1

    print("\nGrafo criado com sucesso!")
    return n, matriz, lista


def mostrar_grafo(n, matriz, lista):
    print("\nMATRIZ DE ADJACÊNCIA")
    for linha in matriz:
        print(linha)

    print("\nLISTA DE ADJACÊNCIA")
    for i in range(n):
        print(f"{i + 1} -> {lista[i]}")


def busca_profundidade(lista, inicio):
    visitados = set()

    def dfs(vertice):
        visitados.add(vertice)
        print(vertice, end=" ")
        for vizinho in lista[vertice - 1]:
            if vizinho not in visitados:
                dfs(vizinho)

    print("\nBUSCA EM PROFUNDIDADE:")
    dfs(inicio)
    print()


def busca_largura(lista, inicio):
    visitados = set()
    fila = []

    fila.append(inicio)
    visitados.add(inicio)

    print("\nBUSCA EM LARGURA:")
    while fila:
        vertice = fila.pop(0)
        print(vertice, end=" ")
        for vizinho in lista[vertice - 1]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    print()


n = 0
matriz = []
lista = []

while True:
    print("\n================== MENU - GRAFOS ==================")
    print("1 - Criar Grafo")
    print("2 - Mostrar Grafo")
    print("3 - Busca em Profundidade")
    print("4 - Busca em Largura")
    print("5 - Sair")
    print("===================================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        n, matriz, lista = criar_grafo()

    elif opcao == "2":
        if n == 0:
            print("ERRO: primeiro crie o grafo!")
        else:
            mostrar_grafo(n, matriz, lista)

    elif opcao == "3":
        if n == 0:
            print("ERRO: primeiro crie o grafo!")
        else:
            inicio = int(input("Digite o vértice inicial: "))
            if inicio < 1 or inicio > n:
                print("ERRO: vértice inválido!")
            else:
                busca_profundidade(lista, inicio)

    elif opcao == "4":
        if n == 0:
            print("ERRO: primeiro crie o grafo!")
        else:
            inicio = int(input("Digite o vértice inicial: "))
            if inicio < 1 or inicio > n:
                print("ERRO: vértice inválido!")
            else:
                busca_largura(lista, inicio)

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
