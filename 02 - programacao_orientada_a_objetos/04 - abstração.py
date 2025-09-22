from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod    
    def desligar(self):
        pass



class Carro(Veiculo):
   def __init__ (self):
    pass
   
   def ligar(self):
      return "Carro ligado."
   
   def desligar(self):
      return "Carro desligado"
   

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())