import math

def es_primo(num1):
    fact=math.factorial(num1-1)
    if fact%num1==(num-1):
        return True
    else:
        return False

print("===DETERMINAR NUMERO PRIMITIVOS===")

num=int(input("Digite el numero entero primitivo a evaluar: "))

if(es_primo(num)):
    print("El numero es primitivo.")
else:
    print("El numero es compuesto.")
