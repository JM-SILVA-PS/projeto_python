import os

os.system('cls')

print('Estrutura de controle validação e casting')

for c in range(0,5):

    numero = input('Digite um numero [0-10]:')
    if(not(numero.isnumeric())):
        print(f'"{numero}" Entrada invalida!!!')
        print()
    else:
        numero = int(numero)

        if(numero >= 0 and numero <= 10):
            print(f'o numero {numero} está dentro do intervalo [0-10]!')
            print()

        else:
            print(f'"{numero}" entrada invalida!')
            print()

