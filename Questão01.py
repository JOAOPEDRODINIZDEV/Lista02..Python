lista = []
print("DIGITE 5 NÚMEROS\n\n\n")
for i in range(5):
    numeros = input("Digite um Número:")
    lista.append(numeros)

novo_numero = input("Digite um novo Número para ser adicionado no final da lista: ")

lista.append(novo_numero)

print(lista)