print("===EJERCICIO MCD===")

def mcd(a,b):
    while not(a%b==0) and a>b:
        b=a%b
    return b
    


a=int(input("Digite un numero entero: "))
b=int(input("Digite otro numero entero: "))

c=mcd(a,b)

print(c)

