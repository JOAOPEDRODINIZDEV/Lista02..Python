lista = []

for i in range(5):
    numeros = input("Digite um número: ")
    lista.append(numeros)
    
conjunto = set(lista)

quantidade =len(conjunto)

print(f"o conjunto possui {quantidade} elementos.")

