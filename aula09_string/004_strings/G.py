import os 
os.system('cls')

numero = int(input('insira um numero inteiro:'))

unidade = (numero%10) // 1
dezena = (numero%100) // 10
centena = (numero%1000) // 100
milhar = (numero) // 1000

if numero > 9999 or numero<0:
    print(f'numero invalido')

else:

  print(f'o numero :{numero} possui {unidade} unidades {dezena} dezenas \
{centena} centenas {milhar} milhares')