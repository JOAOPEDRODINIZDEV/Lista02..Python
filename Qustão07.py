lista = []
 
for i in range(5):
    n = int(input("Digite um numero: "))
    lista.append(n)
     
tupla = tuple(lista)
     
print("O primerio valor é:",tupla[0])