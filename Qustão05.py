grafo = {}

num_vertices = int(input("Digite o número de vertices do grafo: "))
for i in range(num_vertices):
    vertice = input(f"Digite o nome do vertice {i+1}: ")
    grafo[vertice] = []
    
num_arestas = int(input("Digite o número de arestas do grafo: "))
for i in range(num_arestas):
    a, b = input(f"Digite os vertices que foram a aresta {i+1}: ")
    grafo[a].append(b)
    grafo[b].append(a)

print(grafo)