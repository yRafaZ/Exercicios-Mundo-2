from datetime import date
ano = int(input("Em que ano você nasceu? "))
anoatual = date.today().year
idade = anoatual - ano
if idade <= 9:
    print("Você é um atleta mirim")
elif idade <= 19:
    print("Você é um atleta infântil")
elif idade <= 19:
    print("Você é um atleta júnior")
elif idade <= 25:
    print("Você é um atleta sênior")
else:
    print("Você é um atleta master")
