#Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, solicite ao usuário digitar uma letra. Caso a letra seja o “f" finalize a aplicação. Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os

os.system('cls')


while (True):
    
    blabla =input('Digite uma letra: ').lower().strip()

    if blabla == 'f':
        print('Você saiu do loop')
        break

    else: 
        print('estou em looping')
        continue


