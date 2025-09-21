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
print()
print()


print("\nFor utilizando a função range()")
for numero in range(0,5):
    print("Numero:", numero)
print()
print()

print("\nFor utilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
    print("Indice: ", indice, end='   ')
    print("Elemento: ", lista[indice])