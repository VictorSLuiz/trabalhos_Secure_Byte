idade = int(input("Digite a sua idade: "))

if idade < 12:
    print("Classificacao: Crianca")
elif 12 <= idade < 18:
    print("Classificacao: Adolescente")
elif 18 <= idade < 60:
    print("Classificacao: Adulto")
else:
    print("Idoso")
