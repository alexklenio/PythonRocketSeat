
qtd_ingressos = int(input())
percent_meia =  int(input())

total_meia = qtd_ingressos * (percent_meia / 100)
total_inteira = qtd_ingressos - total_meia

valor_ingresso_inteira = float(input())
valor_ingresso_meia = valor_ingresso_inteira / 2

faturamento_meia = total_meia * valor_ingresso_meia
faturamento_inteira = total_inteira * valor_ingresso_inteira
faturamento_total = faturamento_inteira + faturamento_meia


print(f"Quantidade de ingressos meia-entrada: {total_meia}")
print(f"Quantidade de ingressos inteiros: {total_inteira}")

print(f"Faturamento com meia-entrada: R${faturamento_meia:.2f}")
print(f"Faturamento com inteira: R${faturamento_inteira:.2f}")
print(f"Faturamento total: R${faturamento_total:.2f}")

