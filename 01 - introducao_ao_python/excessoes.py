print("Exemplo de captura de excessões:")

try:
    numero = int(input("Diigite um número inteiro: "))
    resultado = 10 / numero

except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Tipo de condicionais incompatíveis")
    
except Exception as e:
    print(f"Erro: {e}")
    
else:
    print (f"Resultado {resultado}")
finally:
    print("Operação Finalizada")