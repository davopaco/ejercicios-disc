"""

@author: David Cárdenas
"""

import msvcrt
from prettytable import PrettyTable

tauto=[]
tauto2=[]

def P():
    Eq=(not s or (p and not r)) and ((not p or (r or q)) and s)
    return Eq

def Q():
    Eq2=p or t
    return Eq2

valores=[True, False]
print("===CALCULADORA DE VERDADES===")
cant:int(input("Cantidad de variables que desea poner: "))

for p in valores:
    for q in valores:
        for r in valores:
            for s in valores:
                for t in valores:
                    R=(not P() or Q()) and (not Q() or P())
                    print(p,q,r,s,t,R, sep="\t")
                    tauto.append(R)
                

if tauto.count(False)>0:
    print("\t\nNo es una tautología")
else:
    print("\t\nEs una tautología")