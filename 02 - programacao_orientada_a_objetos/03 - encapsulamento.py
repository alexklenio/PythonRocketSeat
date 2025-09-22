print("-="*30)
print("Exemplo de encapsulamento")
print("-="*30)
class ContaBancaria:
    def __init__(self,saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    
    def consultar_saldo(self):
        return self.__saldo
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor = 500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor = 200) 
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")