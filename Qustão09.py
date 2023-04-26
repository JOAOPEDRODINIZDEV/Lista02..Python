lista = set() 

for i in range(3):
    numeros = int(input("Digite um número: "))
    lista.add(numeros)
for numero in lista.copy():
    if numero % 2 == 0:
        lista.remove(numero)
        
print("Os números imapres são: ",lista)
    