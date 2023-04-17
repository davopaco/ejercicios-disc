def euc(a,b):

    x1,y1,x2,y2=1,0,0,1
    a,b=max(a,b),min(a,b)
    val_a=a
    val_b=b
    while not(a%b==0):
        floor_fun=a//b

        x1=x1-floor_fun*y1
        temp1=x1
        x1,y1=y1,temp1

        x2=x2-floor_fun*y2
        temp2=x2
        x2,y2=y2,temp2
        a,b=b,a%b
    print(val_a,"(",temp1,") + ",val_b,"(",temp2,")")

a=int(input("Ingrese un numero a: "))
b=int(input("Ingrese un numero b: "))
euc(a,b)



    