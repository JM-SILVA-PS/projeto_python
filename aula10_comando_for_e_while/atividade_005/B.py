#Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver  impresso.

import os

os.system('cls')

c = int(input('escolha até qual numero ira a contagem: ')) 
for a in range (1 , c +1):
    print(f'{a}',end = "|")
    

    

