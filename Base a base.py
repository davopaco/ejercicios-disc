import math

def bases(n,b_from,b_to):
    coci=n//b_to
    residuos=[]
    if not(b_from>1 and b_to>1):
        print("La base no puede ser menor.")
        return
    while(not(coci==0)):
        residuos.append(n%b_to)
        n=coci
        coci=n//b_to
    if(coci==0):
        residuos.append(n%b_to)
        residuos.reverse()
        return residuos


n=int(input("Digita un numero a convertir a una base: "))
lista=bases(n,6,5)
print(lista)
