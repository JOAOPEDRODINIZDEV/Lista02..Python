grafo = {}

num_vertices = int(input("Digite o número de vértices do grafo: "))
for i in range(num_vertices):
    vertice = input(f"Digite o nome do vértice {i+1}: ")
    grafo[vertice] = []

num_arestas = int(input("Digite o número de arestas do grafo: "))
for i in range(num_arestas):
    origem, destino = input(f"Digite os vértices que formam a aresta {i+1}: ").split()
    grafo[origem].append(destino)
    grafo[destino].append(origem)



aresta_remover = input("Digite a aresta que deseja remover (no formato 'origem destino'): ").split()
if aresta_remover[1] in grafo[aresta_remover[0]] and aresta_remover[0] in grafo[aresta_remover[1]]:
    grafo[aresta_remover[0]].remove(aresta_remover[1])
    grafo[aresta_remover[1]].remove(aresta_remover[0])
    print("Aresta removida com sucesso.")
    print(grafo)
else:
    print("Aresta não encontrada no grafo")
