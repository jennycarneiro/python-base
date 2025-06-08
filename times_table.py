"Multiplication tables from 1 to 10 / Tabuada do 1 ao 10"

__version__ = "0.0.1"
__author = "Jennyfer"

# Creates a list of numbers from 1 to 10 / Cria uma lista de números de 1 a 10
numeros = list(range(1, 11))

for numero in numeros:
    print("A tabuada do:", numero) # Prints the current multiplication table header / Exibe o número da tabuada atual
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("------------------")
