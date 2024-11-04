import os
import math
import cmath

os.system('cls')

valor = float(input("Digite o valor para calcular a raiz quadrada: "))

# Verificação de número negativo
if valor < 0:
    print("O resultado será um número complexo.")
    raiz = cmath.sqrt(valor)
    print(f"A raiz quadrada complexa de {valor} é: {raiz}")
else:
    # Cálculo da raiz quadrada para números positivos
    raiz = valor ** (1/2)

    # Verifica se a raiz é exata
    if raiz.is_integer():
        print(f"A raiz quadrada exata de {valor} é: {int(raiz)}")
    else:
        # Arredondamento para cima e para baixo
        arredondar_pra_cima = math.ceil(raiz)
        arredondar_pra_baixo = math.floor(raiz)

        print(f"A raiz quadrada aproximada de {valor} é: {raiz}")
        print(f"Arredondada para cima: {arredondar_pra_cima}")
        print(f"Arredondada para baixo: {arredondar_pra_baixo}")
481