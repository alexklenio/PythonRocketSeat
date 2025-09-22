#declaração

minha_lista = [1, 2, 3, 4, 5, "Alex", True, False]

#exibindo a lista
print("Minha Lista de Exemplo", minha_lista)

#exibindi os elementos
print("Minha lista[0]:", minha_lista[0])
print("Minha lista[5]:", minha_lista[5])

#fatiamento
print("Minha lista[1:7]:", minha_lista[1:7])
print("Minha lista[:6]:", minha_lista[:6])
print("Minha lista[2:]:", minha_lista[2:])

#mudando os elementos
minha_lista[0] = "Python"
print(minha_lista[0])

#metodos
minha_lista.append(6) #Adiciona um item ao final da lista

indice = minha_lista.index(6) #localiza o index do elemento fornecido
print("Indice do elemento 6:", indice)


minha_lista.insert(2,10) #troca o item do index informado pelo valor também informado
print(minha_lista)

elemento_removido = minha_lista.pop(3) #remove o elemento do index informado
print("Elemento removido: ", elemento_removido)

minha_lista.remove(True) #remove a primeira aparição do valor informado

minha_lista.sort() #organiza a lista emordem crescente

