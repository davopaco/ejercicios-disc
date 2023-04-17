import numpy as np
print("Ingrese el tamaño de la matriz 1: ")
n1= int(input())
n2= int(input())
j=0

print("===DATOS PARA LA MATRIZ 1===")
matriz1=np.empty((n1,n2), dtype=int)
while True:
    print("Digita los datos de la fila ",j+1)
    for k in range(n2):
        r=int(input())
        matriz1[j,k]=r
    if j+1==n1:
        break
    j+=1
    
print("Ingrese el tamaño de la matriz 2: ")
n3= int(input())
n4= int(input())
j=0

print("===DATOS PARA LA MATRIZ 2===")
matriz2=np.empty((n3,n4), dtype=int)
while True:
    print("Digita los datos de la fila ",j+1)
    for k in range(n4):
        r=int(input())
        matriz2[j,k]=r
    if j+1==n3:
        break
    j+=1
    
matriz3=np.empty((n1,n3), dtype=int)
matriz3=np.matmul(matriz1,matriz2,dtype=int)

for i in matriz1:
    print(i, sep=" ")
print()
for i in matriz2:
    print(i, sep=" ")
print()
for i in matriz3:
    print(i, sep=" ")

