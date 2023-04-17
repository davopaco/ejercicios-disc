def bases(n, b):
    coci=n//b
    residuos=[]
    if not(b>1):
        print("La base no puede ser menor.")
        return
    while(not(coci==0)):
        residuos.append(n%b)
        n=coci
        coci=n//b
    if(coci==0):
        residuos.append(n%b)
        residuos.reverse()
        return residuos

def conv_hexa(a):
    hexa={
        10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"
    }
    for i in range(0,len(a),1):
        if(a[i]<10 and a[i]>=0):
            continue
        a[i]=hexa.get(a[i])
    return a

def conv_un(a):
    un={
        10:"A"
    }
    for i in range(0,len(a),1):
        if(a[i]<10 and a[i]>=0):
            continue
        a[i]=un.get(a[i])
    return a

def conv_duo(a):
    duo={
        10:"A",11:"B"
    }
    for i in range(0,len(a),1):
        if(a[i]<10 and a[i]>=0):
            continue
        a[i]=duo.get(a[i])
    return a

def conv_tri(a):
    tri={
        10:"A",11:"B",12:"C"
    }
    for i in range(0,len(a),1):
        if(a[i]<10 and a[i]>=0):
            continue
        a[i]=tri.get(a[i])
    return a

def conv_cuad(a):
    cuad={
        10:"A",11:"B",12:"C",13:"D"
    }
    for i in range(0,len(a),1):
        if(a[i]<10 and a[i]>=0):
            continue
        a[i]=cuad.get(a[i])
    return a

def conv_pent(a):
    un={
        10:"A",11:"B",12:"C",13:"D",14:"E"
    }
    for i in range(0,len(a),1):
        if(a[i]<10 and a[i]>=0):
            continue
        a[i]=un.get(a[i])
    return a


n=int(input("Digita un numero a convertir a una base: "))
b=int(input("Digita la base: "))
lista=bases(n,b)
if b==16:
    print(*conv_hexa(lista),sep=" ")
elif b==11:
    print(*conv_un(lista),sep=" ")
elif b==12:
    print(*conv_duo(lista),sep=" ")
elif b==13:
    print(*conv_tri(lista),sep=" ")
elif b==14:
    print(*conv_cuad(lista),sep=" ")
elif b==15:
    print(*conv_pent(lista),sep=" ")
else:
    print(*lista,sep=" ")
