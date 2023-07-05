from datetime import date
ano = int(input("Qual ano você nasceu? "))
anoatual = date.today().year
idade = anoatual - ano
falta = 18 - idade
bah = falta *-1
if idade < 18:
    print("Quem nasceu no ano de {} tem atualmente em {} {} anos.".format(ano , anoatual , idade))
    print("Quem tem {} anos ainda faltam {} anos para completar 18 anos.".format(idade , falta))
elif idade > 18:
    print("Quem nasceu no ano de {} tem atualmente em {} {} anos.".format(ano , anoatual , idade))
    print("Quem tem {} já deveria ter feito o alistamento há {} anos.".format(idade , bah ))
elif idade == 18:
    print("Quem nasceu no ano de {} tem atualmente em {} {} anos.".format(ano , anoatual , idade))
    print("Quem tem {} anos deve fazer imdeiatamente o alistamento.".format(idade))

