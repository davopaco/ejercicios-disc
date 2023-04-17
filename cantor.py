import pyfiglet
def cantor(x):
    nums=[]
    coci=x
    i=2
    while coci!=0:
        x=coci%i
        coci=coci//i
        i+=1
        nums.append(x)
    return(nums)

print(pyfiglet.figlet_format("EXPANSION DE CANTOR"))
n=int(input("Ingresa el numero para mostrar la expresion de Cantor: "))
j=cantor(n)
k=len(j)
print("\nRespuesta:")
print(n," = ",end="")
for i in range(len(j),0,-1):
    if i==1:
        print("(",j[i-1],")(",k,")!")
        break
    print("(",j[i-1],")","(",k,")! + ",end="")
    k-=1
print()
