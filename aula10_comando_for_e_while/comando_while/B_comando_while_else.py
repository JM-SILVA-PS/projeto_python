import os

os.system('cls')

print('Estrutura de controle while else')

print()

contador = 1

while contador < 7:
    print('Contador é:', contador)
    contador += 1

    if contador == 4:
        print(f'Contador chegou em {contador}. break no while')
        break

else:
    print('While finalizado!!!')

print()