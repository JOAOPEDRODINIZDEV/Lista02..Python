grafo = {}

num_vertices = int(input("Digite o número de vertices do grafo: "))
for i in range(num_vertices):
    vertice = input(f"Digite o nome do vertice {i+1}: ")
    grafo[vertice] = []
    
num_arestas = int(input("Digite o número de arestas de grafo: "))
for i in range(num_arestas):
    origem, destino = input(f"Digite os vertices que foram a aresta {i+1}: ").split()
    grafo[origem].append(destino)
    grafo[destino].append(origem)

o , d = input("Digite os vertices que formam a aresta a ser removida: ").split()
if o in grafo and d in grafo:
    grafo[o].remove(d)
    grafo[d].remove(o)
    
print(grafo)