
import os

os.system('cls')

# Escreva um programa que testa se um número é divisível por 2, 3 ou 5. 
# A única linha dos casos de teste contém um número N 
# Imprima 3 linhas, na primeira linha escreva S se o número for divisível por 2 e N caso contrário,
 # na segunda linha faça o mesmo para 3 e na terceira linha para 5.

num =int(input('inira um numero inteiro: '))

if num %2==0 and num %3==0 and num %5==0:
    print(f'o numero {num} é divisivel por 2')
    print(f'o numero {num} é divisivel por 3')
    print(f'o numero {num} é divisivel por 5')
elif num %2!= 0 and num %3!=0 and num %5==0:
    print(f'o numero {num} não é divisivel por 2')
    print(f'o numero{num} não é divisivel por 3')
    print(f'o numero {num} é divisivel por 5')
    
elif num % 2==0 and num %3==0 and num %5!=0:
    print(f'o numero {num} é divisivel por 2')
    print(f'o numero {num} é divisivel por 3')
    print(f'o numero{num} não é divisivel por 5')

elif num % 2==0 and num %3!=0 and num %5==0:
    print(f'o numero {num} é divisivel por 2')
    print(f'o numero{num} não é divisivel por 3')
    print(f'o numero {num} é divisivel por 5')
elif num %2!= 0 and num %3==0 and num %5!=0:
    print(f'o numero {num} não é divisivel por 2')
    print(f'o numero {num} é divisivel por 3')
    print(f'o numero{num} não é divisivel por 5')

elif num %2!= 0 and num %3==0 and num %5==0:
    print(f'o numero {num} não é divisivel por 2')
    print(f'o numero {num} é divisivel por 3')
    print(f'o numero {num} é divisivel por 5')
else:
   
    print(f'o numero {num} não é divisivel por 2')
    print(f'o numero{num} não é divisivel por 3')
    print(f'o numero{num} não é divisivel por 5')


    



