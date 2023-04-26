lista = []
print("DIGITE 5 NÚMEROS\n\n")
for i in range(5):
    numeros = int(input("Digite um número: "))
    lista.append(numeros)
remover = set(lista)
    
remover_numero = int(input("Digite o número que deseja remover: "))

remover.discard(remover_numero)

print("Conjunto de números são: ",remover)