import os
import math 
os.system('cls')
valora=int(input('valor a '))
valorb=int(input('valor b '))

resultado = valora/valorb

if resultado < 0:
   arredondarpracima = math.ceil(resultado)
   arredondarprabaixo = math.floor(resultado)

else:
    print(f'o resultado da divisão é {resultado}')