x=int(input("Ingrese el numero: "))
n=int(input("Ingrese la potencia: "))

def bases(n):
    coci=n//2
    residuos=[]
    while(not(coci==0)):
        residuos.append(n%2)
        n=coci
        coci=n//2
    if(coci==0):
        residuos.append(n%2)
        residuos.reverse()
        return residuos

lista=bases(n)
lista1=[]
j=0

for i in range(len(lista)-1,-1,-1):
    num=pow(2,j)*lista[i]
    lista[0]=1
    if(not (lista[i]==0)):
        lista1.append(num)
    j+=1

for j in range(len(lista1)):
    print(x,"^",lista1[j], end=" ")

