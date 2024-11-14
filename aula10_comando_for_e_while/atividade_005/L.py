#Faça um programa que verifique se o usuário e senha estão inseridos em um banco de dados (fake). O usuário só terá acesso se digitar os dados corretos e, assim, sair do laço.

import os

os.system('cls')



while (True):
    nome = 'João Marcos'
    passworld = 'limonations'

    lno = input('insira o nome de usuario: ')
    lp = input('Insira a senha: ')

    if lno != nome and  lp != passworld:
        print('Suma daqui')
        continue
    else:
        print('Bem vindo!!!')
        break