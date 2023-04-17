print("===PSEUDOALEATORIO===")

def factores_primos(m):
    numPrimos=[]
    c=[]
    i=1
    while True:
        for i in range(2, m+1):
            while m%i==0:
                if len(c)>0:
                    if i==c[len(c)-1]:
                        m=m//i
                        continue
                c.append(i)
                m=m//i
        return c

x1=45
m=int(input("Ingrese el numero mayor: "))
n=int(input("Ingrese cantidad de numeros: "))
c=m-1
continuar=True
a=5
while continuar:
    for i in factores_primos(m):
        if(pow(a,i)-1)%m==0:
            continuar=False
    a+=1

if not(m%4):
    a+=1

for i in range(n):
    x=(a*x1+c)%m
    x1=x
    if(i==n-1):
        print(x)
        break
    print(x, end=",")



