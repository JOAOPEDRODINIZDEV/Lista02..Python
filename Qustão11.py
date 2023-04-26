lista = []
print("DIGITE 10 NÚMEROS\n\n")
for i in range(10):
    numero = int(input(f"Digite o número {i+1}: "))
    lista.append(numero)

for numero in lista:
    if numero % 2 != 0:
        print(lista[numero])
