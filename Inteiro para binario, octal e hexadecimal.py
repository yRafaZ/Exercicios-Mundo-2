num = int(input("\33[4;34mColoque um número inteiro:\33[m "))

binario = bin(num)[2:] # O Pytho tem a função bin que já calcula o número binário, o [2:] é para começar pela segunda letra
octal = oct(num)[2:] # Assim como o bin o oct e o hex, tem funções que calculam o valor dessas contas. 
hexadecimal = hex(num)[2:] # Sem o [2:] a resposta ia ter um prefixo sinalizando que número é a quele (0x2a)

print("\33[34m[ 1 ]\33[m Converter para binário")
print("\33[36m[ 2 ]\33[m Converter para Octal")
print("\33[35m[ 3 ]\33[m Converter para Hexadecimal")

escolha = int(input("\33[32mSua escolha:\33[m "))

while escolha not in [1,2,3]:
    print("\33[1;31mParece que sua escolha é inválida, tente novamente.\33[m")
    escolha = int(input("\33[32mSua escolha:\33[m "))
'''
O comando 'while escolha not in [1,2,3]:' diz que se não houver 1, 2 ou 3 em escolha execute os seguintes códigos.
depois ele repete o input escolha, e caso novamente não houver 1,2 ou 3 em escolha ele vai repetir de novo.
'''

if escolha == 1:
    print("\33[34mO número {} transformado em binário é {}\33[m".format(num , binario))
elif escolha == 2:
    print("\33[36mO número {} transformado em octal é {}\33[m".format(num , octal))
elif escolha == 3:
    print("\33[35mO número {} transformado em hexadecimal é {}\33[m".format(num , hexadecimal))

