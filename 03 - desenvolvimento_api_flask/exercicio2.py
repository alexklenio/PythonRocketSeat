salario = float(input())
horas_por_dia = int(input())
dias_trabalhados = int(input())

horas_trabalhadas = dias_trabalhados * horas_por_dia
valor_hora = salario / horas_trabalhadas

print(f"Eu recebo uma mixuruca de R$ {valor_hora:.1f} por hora trabalhada.")