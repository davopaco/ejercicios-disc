print("===EJERCICIO MCD===")

def mcd(a,b):
    if(a>b):
        while not(a%b==0):
            prev=b
            b=a%b
            a=prev
        return b
    elif(b>a):
        while not(b%a==0):
            prev=a
            a=b%a
            b=prev
        return a
    else:
        return a

while True:
    try:
        a=int(input("Digite un numero entero: "))
        b=int(input("Digite otro numero entero: "))
        break
    except:
        print("El numero debe ser entero.")

c=mcd(a,b)

print("El mcd es: ")
print(c)

