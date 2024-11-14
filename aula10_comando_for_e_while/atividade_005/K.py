#Crie um programa que pede que o usuário digite um nome ou uma frase, verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

import os

os.system('cls')


while(True):
    frase = str(input('Digite um nome ou frase: ')).lower().strip(' ')
    inve = frase[::-1]

    if frase ==inve:
        print('é um palindromo' )

    else:
        print('não é um palindromo')