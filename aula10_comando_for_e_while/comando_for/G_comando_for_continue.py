import os 

os.system('cls')

print('Estrutura de controle: continue')

print()

for c in range(1,11):
    if c == 5:

        print(f'O numero {c} esta fora do loop')
        continue

    print(f'o numero é {c}')

print()