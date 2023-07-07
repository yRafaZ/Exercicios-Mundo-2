fra = str(input("Digite uma frase: ")).strip().upper()
dividido = fra.split()
junto = ''.join(dividido)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += letra[junto]

    if inverso == junto:
        print("A frase digitada é igual quando de trás para frente, ou seja há um palíndromo!")
    elif inverso != junto:
        print("A frase digitada é diferente de quanto colocada de trás para frente, então não há um palíndromo.")