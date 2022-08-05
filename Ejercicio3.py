from prettytable import PrettyTable

numPrimos=[]
c=[]
i=1
tabla=PrettyTable()

while True:
    try:
        num=int(input("Digite el número entero: "))
        for i in range(2, num+1):
            while num%i==0:
                numPrimos.append(num)
                numPrimos.append(i)
                c.append(numPrimos)
                numPrimos=[]
                num=int(num/i)
        break
    except:
        print("El número debe ser entero.")

tabla.field_names=["Cocientes","Primos"]
tabla.add_rows(c)
print(tabla)
