#for utilizando lista

lista = [1, 2, 3, 4, 5]
print("for utilizando lista:")
for elemento in lista:
    print(elemento, end=" ")
print()

tupla = (1, 2, 3, 4, 5, 6)
print("\nfor utilizando tupla:")
for elemento in tupla:
    print(elemento, end=' ')
print()
 
pessoa = {"nome": "joão", "idade":30, "Cidade": "Sâo Paulo"}

print("\nFor utilizando dicionário - chaves:")
for chave in pessoa.keys():
    print(chave, end=' ')
print()

print("\nFor utilizando dicionário - valores:")
for valores in pessoa.values():
    print(valores, end=' ')
print()
print()

print("\nFor utilizando dicionário - items(chave, valor):")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")