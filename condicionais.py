#id, elif, else

idade = int(input("Quantos anos você tem? "))


if idade >= 18:
    print("VOcê é maior de idade.")
elif idade >= 12:
    print("Você é um adolescente")
else:
    print("Você é maior de idade")


if idade == 19:
    print("Você tem 19 anos")

if idade < 18:
    print("Você é menor de idade")

if idade != 10:
    print("Você não tem 10 anos!")


mensagem = "maior de idade"if idade >= 18 else "Menor de idade"
print(mensagem)