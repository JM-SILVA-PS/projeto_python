import os 

os.system('cls')

print('Estrutura de controle while else continue')

print()

contador = 0

while (contador <= 10):

        contador +=1

        if (contador % 2 == 0):
            continue
        print(f'Contador = {contador}')

else:
      print(f'Bloco do while...else: contador em {contador}!')

      