import os
import random

os.system('cls')

print('tente pensar o mesmo numero que a maquina ')
numero= int(input('Qual numero você escolhe? '))
numero_pc =random.randint(0,10)

if numero == numero_pc:
    print(f' Isso mesmo muito bem :)')

else:
    print(f'{numero_pc} tente novamente :( ')