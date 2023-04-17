import numpy as np

def multiplicar(matriz1, matriz2):
    return np.matmul(matriz1,matriz2,dtype=int)

def main():
    exp= int(input("Ingrese la longitud de camino: "))
    print("Ingrese el tamaño de la matriz 1: ")
    n1= int(input())
    j=0

    print("===DATOS PARA LA MATRIZ 1===")
    matriz1=np.empty((n1,n1), dtype=int)
    while True:
        print("Digita los datos de la fila ",j+1)
        for k in range(n1):
            r=int(input())
            matriz1[j,k]=r
        if j+1==n1:
            break
        j+=1

    matriz2=multiplicar(matriz1, matriz1)

    for i in range(exp-1):
        matriz2=multiplicar(matriz1, matriz2)
        for j in matriz2:
            print(j, sep=" ")
        print()
    
    for j in matriz2:
        print(j, sep=" ")

if __name__=='__main__':
    main()



    
    