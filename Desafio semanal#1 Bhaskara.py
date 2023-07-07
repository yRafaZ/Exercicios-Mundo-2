

import time
import math
import sys

time.sleep(0.5)
print('\33[36m=\33[m'*28)
print("     \33[34mFÓRMULA QUADRÁTICA\33[m")
print('\33[36m=\33[m'*28)
time.sleep(1.6)
print('')
print("\33[34mAntes, vamos calcular o delta!\33[m")
time.sleep(2)
print('')
a = int(input("\33[35mDigite o valor de A: "))
time.sleep(1)
b = int(input("Digite o valor de B: "))
time.sleep(1)
c = int(input("Digite o valor de C: "))
time.sleep(1)
delta = (b*b) - (4*a*c)
print('\33[m\33[34mO valor de delta é de {}.\33[34m'.format(delta))
print('')
if delta < 0:
    print("\33[31mParece que esse delta é negativo, ou seja não possui bhaskara.\33[m")
    sys.exit()
time.sleep(1.5)
print("\33[33mAgora vamos para o próximo passo.")
time.sleep(1.5)
raiz = math.sqrt(delta)
bahp = (-b + raiz) / (2*a)
bahn = (-b - raiz) / (2*a)
print("Fazendo o bhaskara com o +, o resultado é de: {:.2f}".format(bahp))
time.sleep(1.5)
print("Fazendo o bhaskara com o -, o resultado é de: {:.2f}".format(bahn))

