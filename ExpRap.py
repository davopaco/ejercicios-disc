import math

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

n=int(input("Numero a elevar: "))
pot=int(input("Potencia: "))
lista=bases(pot)
lista1=[]
res=1
num=0
j=0
for i in range(len(lista)-1,-1,-1):
    num=pow(2,j)*lista[i]
    if(not (lista[i]==0)):
        lista1.append(num)
    j+=1
lista.reverse()
print(lista)
mults=[n]
i=0

while(True):
    if(len(mults)==len(lista)):
        break
    mults.append(mults[i]*mults[i])
    i+=1

print(mults)

lista[0]=1
for i in range(1,len(lista)):
    lista[i]=lista[i-1]*2

dict={}

for i in range(len(mults)):
    dict.update({lista[i]:mults[i]})

for i in range(len(lista1)):
    res=res*dict.get(lista1[i])

print(lista)
print(lista1)
print(dict)
print (res)
    
