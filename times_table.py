"Multiplication tables from 1 to 10 / Tabuada do 1 ao 10"

__version__ = "0.0.2"
__author = "Jennyfer"

# Creates a list of numbers from 1 to 10 / Cria uma lista de números de 1 a 10
numbers = list(range(1, 11))

for n1 in numbers:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    #print(f"{'Tabuada do ' + str(n1) :-^18}")
    for n2 in numbers:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#"*18)
