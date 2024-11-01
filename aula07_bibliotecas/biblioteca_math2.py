import os
import math

os.system('cls')

print('-'*50)
print('Estudo da biblioteca matematica math')
print('='*50)
print()

numero_decimal = float(input('Entre com um numero decimal:'))

arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math .floor(numero_decimal)

print('-'*50)
print(f'O numero {numero_decimal} arredondado para cima é:{arredondar_para_cima}')
print(f'O numero {numero_decimal} arredondado para baixo é: {arredondar_para_baixo}')
print('-'*50)
