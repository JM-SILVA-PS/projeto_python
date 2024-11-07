#ORDEM DEPRIMENTE 
import os

os.system('cls')

numa =int(input('primeiro numero: '))
numb = int(input('segundo numero'))
numc = int( input('terceiro numero'))

if numa > numb and numa >numc and numb > numc:
    print(f'{numa},{numb},{numc} ')

elif numa> numb and numa>numc and numc> numb:
    print(f'{numa},{numc},{numb}')

elif numb > numa and numb > numc and numa > numc:
    print(f'{numb},{numa},{numc}')
elif numb > numa and numb > numc and numc > numa:
    print(f'{numb},{numc},{numa}')
