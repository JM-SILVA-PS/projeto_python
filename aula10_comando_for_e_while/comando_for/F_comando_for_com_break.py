import os

os.system('cls')

print('Estrutura de controle: break')
print()

for c in range(0,10):

    print(f'Valor: {c}')

    if (c == 4):
        print(f'Contagem interrompida no {c}')
        break
