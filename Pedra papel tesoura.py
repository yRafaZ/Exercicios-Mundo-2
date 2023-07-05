import random
print("Suas opções:")
print("[ 1 ] PEDRA")
print("[ 2 ] PAPEL")
print("[ 3 ] TESOURA")

jogador = int(input("Qual você escolhe? "))
escolhas = ["PEDRA" , "PAPEL" , "TESOURA"]
# Fazendo a escolha do computador
computador = random.choice(escolhas)
# Mudando 1 , 2 e 3 por pedra papel ou tesoura
if jogador == 1:
    jogadora = "PEDRA"
if jogador == 2:
    jogadora = "PAPEL"
if jogador == 3:
    jogadora = "TESOURA"

# Caso o jogo empate.
while jogador == 1 and computador == "PEDRA" or jogador == 2 and computador == "PAPEL" or jogador == 3 and computador == "TESOURA":
    print("Parece que o jogo empatou, tente novamente!")
    jogador = int(input("Qual você escolhe? "))
    escolhas = ["PEDRA" , "PAPEL" , "TESOURA"]
    computador = random.choice(escolhas)

# Quando o jogador ganha.
if jogador == 1 and computador == "TESOURA" or jogador == 2 and computador == "PEDRA" or jogador == 3 and computador == "PAPEL":
    print("-=" * 12)
    print("Computador jogou {}".format(computador))
    print("Jogador jogou {}".format(jogadora))
    print("-=" * 12)
    print("Jogador ganhou!")

# Quando o computador ganha.
if jogador == 1 and computador == "PAPEL" or jogador == 2 and computador == "TESOURA" or jogador == 3 and computador == "PEDRA":
    print("-=" * 12)
    print("Computador jogou {}".format(computador))
    print("Jogador jogou {}".format(jogadora))
    print("-=" * 12)
    print("Computador ganhou!")
    

