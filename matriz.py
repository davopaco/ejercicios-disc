import numpy as np
    
def main():

    n= int(input("Ingrese un número para el tamaño de la matriz: "))
    j=0
    matriz1=np.empty((n,n), dtype=int)

    while True:
        print("Digita los datos de la fila ",j+1)
        for k in range(n):
            r=int(input())
            matriz1[j,k]=r
        if j+1==n:
            break
        j+=1
        
    for i in matriz1:
        print(i,sep=", ")



if __name__=='__main__':
    main()