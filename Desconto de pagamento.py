# Perguntando qual é a forma de pagamento
valor = float(input("Qual foi o valor das compras? "))
print("[ 1 ] Pagar com dinheriro/cheque á vista")
print("[ 2 ] Pagar com cartão á vista")
print("[ 3 ] Pagar com cartão até em 2 vezes")
print("[ 4 ] Pagar com cartão com 3 vezes ou mais")
metodo = int(input())

# Caso o usuário coloque um número inválido (!= 1 or 2 or 3 or 4)
while metodo != 1 and metodo != 2 and metodo != 3 and metodo != 4:
     print("Parece que você colocou uma opção inválida, tente novamente")
     metodo = int(input())
     if metodo == 1 or metodo == 2 or metodo == 3 or metodo == 4:
          break 

# Cálculo do desconto ou juros da compra
if metodo == 1:
     desconto = valor - (valor * 10 / 100)
     print("Com o desconto aplicado as suas compras ficaram no valor de: {:.2f}".format(desconto))
elif metodo == 2:
     desconto = valor - (valor * 5 / 100)
     print("Com o desconto aplicado, suas compras ficaram no valor de: {:.2f}".format(desconto))
elif metodo == 3:
     print("Suas compras ficaram no valor de {}".format(valor))
elif metodo == 4:
     desconto = valor * 20 / 100 + valor
     print("Suas compras parceladas em 3 vezes ou mais ficaram no valor de: {}".format(desconto))
