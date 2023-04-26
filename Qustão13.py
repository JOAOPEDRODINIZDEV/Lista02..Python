dicionario = {}

for i in range(1):
    chave = input("Digite a Chave: ")
    valores = int(input("Digite Um Valor: "))
    dicionario[chave]=valores 
    

    if 'profisão' in chave:
        print("O Nome 'profisão' Está Sim No Dicionario")
    else:
        print("O Nome 'Profisão' Não Está No Dicionario")