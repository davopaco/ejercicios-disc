import math

def es_primo(num1):
    fact=math.factorial(num1-1)
    if fact%num1==(num-1):
        return True
    else:
        return False

def det_divisores(num1):
    lista_divisores=[1]
    for i in range(2,num1+1):
        if(num1%i==0):
            lista_divisores.append(i)
    return lista_divisores


print("===DETERMINAR NUMERO PRIMITIVOS===")
try:
    num=input("Digite el numero entero primitivo a evaluar: ")
except:
    "El numero debe ser entero."

if(es_primo(num)):
    print("El numero es primitivo.")
else:
    print("El numero es compuesto.")

print("Los divisores son: ")
print(det_divisores(num))
