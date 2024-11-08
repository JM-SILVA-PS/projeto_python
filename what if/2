import os 
import random

os.system('cls')

lista=['pedra','papel','tesoura']
escolha=input('escolha entre pedra papel e tesoura: ').strip().lower()
if escolha not in lista:
       print(f'escolha invalida!!!')
       exit()
else:
        pass
pedra=0
tesoura=1
papel=2
0>1
0<2
1>2
1<0
2>0
2<1

pedra_wins= pedra > tesoura
tesoura_wins= tesoura > papel
papel_wins= papel > pedra

pedra_lose=pedra<papel 
tesoura_lose=tesoura<pedra
papel_lose=papel < tesoura

eu_escolho=random.choice(lista)
print(f'O computador escolheu {eu_escolho}')

if eu_escolho > escolha:
              print(f'você perdeu :(')
elif eu_escolho == escolha:
              print(f'Empate')
else:
        print(f'Parabens!!! você ganhou :)')
