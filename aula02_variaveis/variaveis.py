import os

os.system('cls')

print('-'*70)
print('Estudo de variaveis')
print('='*70)

nome = 'Cleitin'
nascimento = 1995
altura = 1.68
peso = 50.9
doador = True
complexo = 3j
PI = 3.14

print('\033[0m \033[31mTipos declarados:\033[0m')
print('\033[0m A var \033[32m nome \033[0m é do tipo:', type(nome))
print('\033[0m A var \033[32m nascimento \033[0m é do tipo:', type(nascimento))
print('\033[0m A var \033[32m altura \033[0m é do tipo:', type(altura))
print('\033[0m A var \033[32m peso \033[0m é do tipo:', type(peso))
print('\033[0m A var \033[32m doador \033[0m é do tipo:', type(doador))
print('\033[0m A var \033[32m complexo \033[0m é do tipo:', type(complexo))
print('\033[0m A var \033[32m PI \033[0m é do tipo:', type(PI))
print('-'*70)
print('')