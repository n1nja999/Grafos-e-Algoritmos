import heapq


def ler_inteiro(mensagem, minimo, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"Digite um valor maior ou igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Digite um valor menor ou igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Erro! Digite um número inteiro válido.")


def ler_peso():
    while True:
        try:
            peso = float(input("Peso da aresta (número positivo): "))
            if not (0 <= peso < float("inf")):
                print("O peso deve ser finito e não negativo.")
                continue
            return peso
        except ValueError:
            print("Erro! Digite um peso numérico válido.")


def prim(grafo, inicio=0):
    visitados = set()
    fila = [(0, inicio, -1)]
    arvore = []
    custo_total = 0

    while fila:
        peso, atual, origem = heapq.heappop(fila)
        if atual in visitados:
            continue
        visitados.add(atual)

        if origem != -1:
            arvore.append((origem, atual, peso))
            custo_total += peso

        for vizinho, peso_aresta in grafo[atual]:
            if vizinho not in visitados:
                heapq.heappush(fila, (peso_aresta, vizinho, atual))

    if len(visitados) != len(grafo):
        return None, None

    return arvore, custo_total


print("=== ALGORITMO DE PRIM ===")
print("Grafo não orientado")

n = ler_inteiro("Digite o número de vértices: ", 1)
max_arestas = n * (n - 1) // 2
m = ler_inteiro(f"Digite o número de arestas (máximo {max_arestas}): ", 0, max_arestas)

grafo = [[] for _ in range(n)]
arestas_cadastradas = set()

for i in range(m):
    print(f"\nAresta {i + 1}:")
    while True:
        u = ler_inteiro(f"Digite o vértice de origem (0 a {n - 1}): ", 0, n - 1)
        v = ler_inteiro(f"Digite o vértice de destino (0 a {n - 1}): ", 0, n - 1)

        if u == v:
            print(
                "Aresta inválida! Não é permitido criar "
                "arestas entre o mesmo vértice."
            )
            continue

        aresta = tuple(sorted((u, v)))

        if aresta in arestas_cadastradas:
            print("Aresta já cadastrada! Digite uma aresta diferente.")
            continue

        peso = ler_peso()
        arestas_cadastradas.add(aresta)

        grafo[u].append((v, peso))
        grafo[v].append((u, peso))

        break

print("\n=== GRAFO CADASTRADO ===")
for vertice in range(n):
    print(f"Vértice {vertice}: {grafo[vertice]}")

arvore, custo_total = prim(grafo)

print("\n=== ÁRVORE GERADORA MÍNIMA ===")
if arvore is None:
    print("O grafo não é conexo. " "Não é possível gerar uma árvore geradora mínima.")

else:
    for u, v, peso in arvore:
        print(f"Aresta: {u} -- {v}, Peso: {peso:g}")

    print(f"Peso total da AGM: {custo_total:g}")
    print(f"Quantidade de arestas da AGM: {len(arvore)}")
