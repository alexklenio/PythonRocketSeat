

def saudacao(nome):
    print(f"Olá, {nome}!")

print("\n Chamando a saldação:")
saudacao("Alice")
saudacao("Bob")


#funcap com retorno
def quadrado(numero):
    resultado = numero **2
    return resultado

print("\nCHamando função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da função quadrado:", resultado_quadrado)