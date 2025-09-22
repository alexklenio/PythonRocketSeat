#declaração

nome_sobrenome = "Alex Lopes"

nome_completo_aspas = """Alex Klenio
Ferreira Lopes"""

numero_completo_quebra = "Alex \
    Lopes"

nome = "Alex"
sobrenome = "Lopes"


# Formatação

print("Nome completo (1º forma):", nome_sobrenome)

print("Nome completo (2º forma):" + nome_sobrenome)

print("Nome completo (3º forma):" + "Alex" + "Lopes")

print("Nome completo (4º forma):", nome_completo_aspas)

print("Nome completo (5º forma):", numero_completo_quebra)

print(f"Nome completo (3º forma): {nome} {sobrenome}")

nome_sobrenome.count("a") #conta a incidencia do parâmetro fornecido

nome_sobrenome.find("a") # Informa a posição da primeira aparição

nome_sobrenome.encode()

nome_sobrenome.replace("a","c")