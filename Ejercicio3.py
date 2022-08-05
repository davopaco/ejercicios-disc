from prettytable import PrettyTable
import msvcrt

numPrimos=[]
c=[]
i=1
tabla=PrettyTable()

while True:
    try:
        num=int(input("Digite el número entero: "))
        if num<0:
            raise Exception()
        for i in range(2, num+1):
            while num%i==0:
                numPrimos.append(num)
                numPrimos.append(i)
                c.append(numPrimos)
                numPrimos=[]
                num=int(num/i)
        break
    except:
        print("El número debe ser entero positivo.")

tabla.field_names=["Cocientes","Primos"]
tabla.add_rows(c)
print(tabla)

msvcrt.getch()
