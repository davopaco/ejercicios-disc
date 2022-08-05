import math
import msvcrt

numPrimos=[]
factores=[]

def hacerListaPrimos(n):
    if n==1:
        print("1 no es primo ni compuesto.")
    i=2
    for i in range (2,int(math.sqrt(n))):
        if n%i==0:
            numPrimos.append(i)
    if len(numPrimos)==0:
        numPrimos.append(n)

cant=int(input("Digite un numero entero: "))
hacerListaPrimos(cant)

for num in numPrimos:
    while cant%num==0:
        factores.append(num)
        cant=cant/num

print(factores)

msvcrt.getch()