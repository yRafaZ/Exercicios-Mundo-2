import sys
print("Coloque 3 segmentos de reta para ver se eles conseguem formar um triângulo.")
seg1 = float(input("Segmento 1: "))
seg2 = float(input("Segmento 2: "))
seg3 = float(input("Segmento 3: "))

if seg1 > seg2 + seg3 or seg3 > seg1 + seg2 or seg2 > seg1 + seg3:
    print("Eles não podem formar um triângulo.")
    sys.exit() # Se esse if for exexutado o "sys.exit()" é executado, esse comando faz o código terminar.

if seg1 == seg2 and seg1 == seg3 and seg3 == seg2:
    print("É possivel formar um triângulo, esse triângulo vai ser equilátero.")

elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
    print("É possivel formar um triângulo, esse triângulo é um isósceles.")

elif seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
    print("É possivel formar um triângulo, esse triângulo é um escaleno.")
    
if seg1 > seg2 + seg3 and seg3 > seg1 + seg2 and seg2 > seg1 + seg3:
    print("Eles não podem formar um triângulo.")