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

def hacer_tablalinda(tauto4):
    tauto3=PrettyTable()
    tauto3.field_names=["p","q","r","s","t","Equivalencia"]
    for i in tauto4:
        tauto3.add_row(i)
    return tauto3


print("===EJERCICIO 51===")

valores=[True, False]

for p in valores:
    for q in valores:
        for r in valores:
            for s in valores:
                for t in valores:
                    R=(not P() or Q()) and (not Q() or P())
                    tauto.append(str(p))
                    tauto.append(str(q))
                    tauto.append(str(r))
                    tauto.append(str(s))
                    tauto.append(str(t))
                    tauto.append(str(R))
                    tauto2.append(tauto)
                    tauto=[]

print(hacer_tablalinda(tauto2))
if tauto.count(False)>0:
    print("\t\nNo es una tautología")
else:
    print("\t\nEs una tautología")