print("=" * 26)
print("   10 TERMOS DE UM PA")
print("=" * 26)
num = int(input("Coloque um número para fazer a análise aritmétrica: "))
pri = int(input("Coloque o primeiro termo: "))
ult = int(input("Coloque o último termo: "))
for c in range(pri,ult+1,num):
    print(' {} '.format(c), end=' ➨ ')
print("Fim")
