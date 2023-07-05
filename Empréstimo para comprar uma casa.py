vc = int(input("\33[30mQual o valor da casa?\33[m \33[1;32mR$\33[m "))
mes = int(input("\33[30mQuanto você ganha por mês?\33[m \33[1;32mR$\33[m "))
ano = int(input("\33[30mEm quanto tempo você quer pagar essa casa?\33[m \33[1;32mR$\33[m "))
prestaçao = vc / (12 * ano) # Aqui estou calculando quantos reais vai custar cada mês da prestação. 12 meses vezes o tanto de anos, vai dar o tanto de meses.
minimo = mes * 30 / 100 # Aqui estou vendo quanto é 30% do salário mensal do usuário.
va = vc / (ano*12)
if prestaçao < minimo: 
    print("O valor do empréstimo vai ser de \33[1;32mR$\33[m{:.2f} para paga a casa de \33[1;32mR$\33[m{}, o seu empréstimo foi\33[m \33[1;32maprovado\33[m.".format(va , vc))
else: 
    print("O valor do empréstimo seria de \33[1;32mR$\33[m{:.2f}, para pagar a casa de \33[1;32mR$\33[m{}, porém o empréstimo foi\33[m \33[1;31mnegado\33[m.".format(va , vc))