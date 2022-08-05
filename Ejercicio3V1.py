import math

numPrimos=[]
factores=[]

def hacerListaPrimos(cant):
    i=2
    num=2
    while i<int(math.sqrt(cant)):
        fact=math.factorial(num-1)
        if fact%num==(num-1):
            numPrimos.append(num)
            i+=1
        num+=1

cant=int(input("Digite un numero entero: "))
hacerListaPrimos(cant)

for num in numPrimos:
    while cant%num==0:
        factores.append(num)
        cant=cant/num

print(factores)
