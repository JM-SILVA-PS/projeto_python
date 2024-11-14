#Faça um programa que imprima os valores no intervalo definidos pelo usuário.  Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

import os

os.system('cls')

cc =int(input('A contagem começa em... '))
cf = int(input('A contagem termina em...'))

for a in range (cc,cf +1):
    if a == 7:
        continue

    elif a == 23:
            continue
    elif a == 43:
         continue
    print(f'{a}', end = "|")

