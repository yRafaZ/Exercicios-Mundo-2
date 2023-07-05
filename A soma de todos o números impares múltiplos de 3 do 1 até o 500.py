a = 0 # A soma de todos o números múltiplos de 3 do 1 até o 500 por em quanto 0
for c in range(1 , 500+1 , 2 ): 
    if c % 3 == 0:
        a = a + c
print("A soma de todos o números impares múltiplos de 3 do 1 até o 500 é de {}".format(a))
