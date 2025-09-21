#Sâo listas não ordenadas que contem chave e valor

pessoa = {"nome": "Alex", "idade": 39, "cidade":"Recife"}

print("Meu dicionário de exemplo: ", pessoa)

#acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])


#adicionando itens ao dicionario
pessoa["sobrenome"] = "Lopes"
print("Sobrenome:", pessoa["sobrenome"])


pessoa["idade"] = 40
print("Idade atualizada: ", pessoa["idade"])

del pessoa["sobrenome"]
print("Meu dicionário de exemplo: ", pessoa)

