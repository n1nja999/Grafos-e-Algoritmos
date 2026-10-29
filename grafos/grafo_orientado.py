# Grafo nao orientado
# Matriz de Adjacencia e Lista de Adjacência
# Com validacao das arestas

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

print("\nMATRIZ DE ADJACÊNCIA")
for linha in matriz:
    print(linha)

print("\nLISTA DE ADJACÊNCIA")
for i in range(n):
    print(f"{i + 1} -> {lista[i]}")
