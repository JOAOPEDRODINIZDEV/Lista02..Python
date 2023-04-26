grafo = {}

num_vertices = int(input("Digite o número de vertices do grafo: "))
for i in range(num_vertices):
    vertice = input(f"Digite o nome do vertice {i+1}: ")
    grafo[vertice] = []
    
num_arestas = int(input("Digite o número de arestas de grafo: "))
for i in range(num_arestas):
    origem, destino = input(f"Digite os vertices que foram a aresta {i+1}: ")
    grafo[origem].append(destino)
    grafo[destino].append(origem)

if 'C' in grafo['A']:
    print("A aresta AC está no grafo")
else:
    print("A aresta ac não está no grafo")