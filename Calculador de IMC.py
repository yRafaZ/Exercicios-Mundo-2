peso = float(input("Coloque o seu peso: "))
altura = float(input("Coloque sua altura em metros: "))
while altura > 3.00:
    print("Parece que você colocou a altura em centimetros, tente novamente.")
    altura = float(input("Coloque sua altura em metros: "))
alt2 = altura * altura
imc = peso / alt2
print("O seu IMC é de {:.2f}".format(imc))
if imc < 18.5:
    print("O seu IMC de {:.2f} está muito baixo, está classificado como magreza.".format(imc))
elif imc < 24.9:
    print("O seu IMC de {:.2f} está normal, está classificado como normal.".format(imc))
elif imc < 29.9:
    print("O seu IMC de {:.2f} está um pouco acima da média, está classificado como sobrepeso.".format(imc))
elif imc < 34.9:
    print("O seu IMC de {:.2f} está acima do comum, está classificado como obesidade grau 1.".format(imc))
elif imc < 39.9:
    print("O seu IMC de {:.2f} está muito acima do comum, está classificado com obesidade grau 2.".format(imc))
elif imc < 60:
    ("O seu IMC de {:.2f} está extremamente alto, está classificado como obesidade extrema.".format(imc))
else:
    print("Parece que algo deu errado, tente novamente.")