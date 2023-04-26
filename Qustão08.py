dicionario = {}

while True:
    chave = input("Digite uma chave: ")
    idade = input("Digite uma idade: ")
    dicionario[chave] = idade
    
    if input("Deseja continuar (s/n)?: ") == 'n':
        break
    
    if 'idade' in dicionario:
        print(f"idade = {dicionario['idade']}")
    else:
        print("A chave 'idade' nao existe no dicionarrio " )
 