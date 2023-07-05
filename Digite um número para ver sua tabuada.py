num = float(input("Digite um número para ver sua tabuada: "))
vezes = 1
pipiu = num * vezes
for c in range(1, 10+1):
    print('{} x {} = {:.2f}'.format(num,vezes,pipiu))
    vezes += 1
    pipiu = num * vezes