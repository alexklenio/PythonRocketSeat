custo = float(input())
percentual = float(input())

lucro_percentual = (percentual / 100) * custo
valor_final = lucro_percentual + custo

print(f"Valor final do produto: R$ {valor_final:.4f}.")