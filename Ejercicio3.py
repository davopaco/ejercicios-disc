from prettytable import PrettyTable

numPrimos=[]
i=1

while True:
    try:
        num=int(input("Digite el número entero: "))
        for i in range(2, num+1):
            while num%i==0:
                numPrimos.append(i)
                num=int(num/i)
        break
    except:
        print("El número debe ser entero.")

print(numPrimos)
