tupla_nomes = ()
print("DIGITE 3 NOMES\n\n")
for i in range(3):
    nomes = input("Digite um nome: ")
    tupla_nomes += (nomes,)

print("Os nomes digitados foram:", tupla_nomes)

nome_antigo = input("")

if nome_antigo in nomes:
    indice = nomes.index(nome_antigo)
    novo_nome = input("Digite o novo nome: ")
    nomes = nomes[:indice] + (novo_nome,) + nomes[indice+1:]
    print("A nova lista de nomes é:", nomes)
else:
    print("O nome digitado não está na lista.")