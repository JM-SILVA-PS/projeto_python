# B) Crie um programa que pergunte o ano de nascimento do usuário e calcule sua idade atual.

# IMPORTANDO BIBLIOTEA
import os
import datetime

# LIMPANDO TERMINAL
os.system('cls')

# ENTRADA 
print('CÁLCULO DA IDADE ATUAL')

nascimento = int(input('Qual o ano de seu nascimento?: '))

# PROCESSAMENTO
ano_atual = datetime.datetime.now().year
idadeatual = int(ano_atual) - int(nascimento)

# SAÍDA 
print(f'Você tem ou irá fazer {idadeatual} anos!!')