nota1 = float(input("Coloque a primeira nota: "))
nota2 = float(input("Coloque a segunda nota:  "))
media = (nota1 + nota2) / 2

while nota1 >= 10.1 or nota2 >= 10.1:
    print("Parece que alguma nota está incorreta, tente novamente.")
    nota1 = float(input("Coloque a primeira nota: "))
    nota2 = float(input("Coloque a segunda nota:  "))
    media = nota1 + nota2 / 2
if media == 5 or media == 4:
    print("Sua média foi {}, por isso você ainda pode ir para a recuperação".format(media))
elif media < 4:
    print("Sua média foi de {}, por isso você foi reprovado.".format(media))
elif media >= 8:
    print("Parabéns! Sua nota foi de {}, uma nota bem alta.".format(media))
elif media >= 6:
    print("Sua média foi de {}, por isso foi aprovado!".format(media))
