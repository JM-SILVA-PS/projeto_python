#importando biblioteca
import os 

#limpando terminal
os.system('cls')

#entrada de dados
numero = int(input('Digite um numero inteiro:'))
resposta = ''

#condicional
if numero % 2 == 0:
 resposta = f'o número {numero} é par'
else:
 resposta = f'o numero {numero} é ímpar'

#Saída
print('='*70)
print(resposta)