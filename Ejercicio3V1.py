import math
import msvcrt

numPrimos=[]
factores=[]

def hacerListaPrimos(cant):
    i=2
    num=2
    if cant==1:
        print("1 no es primo ni compuesto.")
    while i<int(math.sqrt(cant)):
        fact=math.factorial(num-1)
        if fact%num==(num-1):
            numPrimos.append(num)
            i+=1
        num+=1
    if len(numPrimos)==0:
        numPrimos.append(num)

cant=int(input("Digite un numero entero: "))
hacerListaPrimos(cant)
print(numPrimos)

for num in numPrimos:
    while cant%num==0:
        factores.append(num)
        cant=cant/num

print(factores)

msvcrt.getch()
