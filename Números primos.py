num = int(input("Digite um número: "))
idn = 0

for c in range(1, num + 1):

    if num % c == 0:
        print("\33[34m", end='')
        idn += 1

    else:
        print("\33[31m", end='')
    print("{} ".format(c), end='')

if idn == 2:
    print("\n\033\33[34mO número {} foi divisível {} vezes.".format(num,idn))
    print("\33[32mEle é um número primo.\33[m".format(num))
if idn != 2:
    print("\n\033\33[34mO número {} foi divisível {} vezes.".format(num,idn))
    print("\33[31mNão é um número primo.\33[m".format(num))
