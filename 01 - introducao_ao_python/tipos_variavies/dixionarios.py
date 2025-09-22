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

#metodo: keys()
chaves = pessoa.keys()
print("chaves do dicionário: ", chaves)

chaves = list(pessoa.keys())
print("Primera chave: ", chaves[0])

#metodo: values()
valores = pessoa.values()
print("Valores do dicionário: ", valores)

valores = list(pessoa.values())
print("Primeiro valor do dicionário:", valores[0])

#motodo: itens()

itens = list(pessoa.items())
print("Pares chave-valor do dicionário: ", valores)
print(f"Primeiro valor: {itens[0][0]} = {itens[0][1]}")