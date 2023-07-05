soma = 0 
cont = 0
for c in range(1, 7):
    bah = int(input("Coloque os seis números: "))
    if bah % 2 == 0:
        cont += 1
        soma += bah
print("Você forneceu {} números pares e a soma deles foram de {}".format(cont, soma))
    