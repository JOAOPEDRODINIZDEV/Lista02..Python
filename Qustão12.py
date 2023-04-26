tupla = ()

for i in range(3):
    nomes = input(f"Digite {i+1} nome: ")
    tupla +=(nomes,)
    
    if 'Maria' in nomes:
        print(f"O nome 'Maria' esta na posição {i+1} pressente")
    else:
        print("O nome não esta presente")