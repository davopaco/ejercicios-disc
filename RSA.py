from random import randint
import math

def mcd(a,b):
    a,b=max(a,b),min(a,b)
    if(a>b):
        while not(a%b==0):
            prev=b
            b=a%b
            a=prev
        return b
    else:
        return a

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
    return temp2    

abecedario={
    "A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,
    "M":13,"N":14,"O":15,"P":16,"Q":17,"R":19,"S":20,"T":21,"U":22,"V":23,"W":24,"X":25,
    "Y":26,"Z":27
}

p=113
q=307
n=p*q
phi_n=(p-1)*(q-1)
cont=True

e=1007
d=euc(1007,13103)
if d<0:
    d=phi_n+d

m=input("Codigo a cifrar: ")

print(pow(abecedario.get(),1007)%n)
