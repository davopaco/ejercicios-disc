import os
import sympy as sp
import numpy as np
from prettytable import PrettyTable

def representacionMatricial(sistema, simbolos):
    # Método en el que se cogen las ecuaciones lineales, se agarran los símbolos usando Sympy y se pasa a forma de matriz aumentada.
    a, b = sp.linear_eq_to_matrix(sistema, simbolos)
    return np.asarray(a.col_insert(len(simbolos), b), dtype=np.int64)

def diagonalSuperiorMatriz(M):
    # Mueve los ceros al final de la matriz
    M = np.concatenate((M[np.any(M != 0, axis=1)], M[np.all(M == 0, axis=1)]), axis=0)

    # For que itera por cada fila de la matriz
    for i in range(0, M.shape[0]):

        j = 1
        # Selecciona el valor del pivot. Aquí el pivot permite que el algoritmo pueda hacer sustitución hacia atrás para la eliminación de Gauss.
        pivot = M[i][i]
        while pivot == 0 and i + j < M.shape[0]:
            # Se hace el cambio de filas
            M[[i, i + j]] = M[[i + j, i]]
            j += 1

            # Se obtiene el nuevo valor del pivot.
            pivot = M[i][i]

        # Si el pivot es 0, entonces las demás filas serán 0
        if pivot == 0:
            return M

        fila = M[i]
        #En esta fila pone 1 sobre la diagonal.
        M[i] = fila / pivot

        #Itera por las demás filas.
        for j in range(i + 1, M.shape[0]):
            #Resta la fila actual con las restantes.
            M[j] = M[j] - M[i] * M[j][i]

    return M

#Este método constituye a un algoritmo de sustitución hacia atrás
def sustitucionTrasera(M, simbs):
    for i, fila in reversed(list(enumerate(M))):
        ecn = -M[i][-1]
        for j in range(len(simbs)):
            ecn += simbs[j] * fila[j]
        simbs[i] = sp.solve(ecn, simbs[i])[0]
    return simbs


def validarSolucion(sistema, soluciones, tolerancia=1e-6):
    
    #Itera todas las ecuaciones lineales.
    for ecn in sistema:
        #Prueba si la ecuación está resulta.
        assert ecn.subs(soluciones) < tolerancia


#Resuelve el sistema usando NumPy que es una clase incluida en Python.
def solucionarLineal(system, syms):

    M, c = sp.linear_eq_to_matrix(system, syms)
    M, c = np.asarray(M, dtype=np.int64), np.asarray(c, dtype=np.int64)
    return np.linalg.solve(M, c)


if __name__ == '__main__':

    #Variables simbólicas para las ecuaciones lineales.
    x1, x2, x3, x4, x5, x6, x7 = sp.symbols('x1 x2 x3 x4 x5 x6 x7')
    variablesX = [x1, x2, x3, x4, x5, x6, x7]

    # Aquí está el sistema de ecuaciones.
    ecuaciones = [x1-x4+200, x2-x4+x5-100, x3+x5-700, x1-x6-100, x2-x6+x7-600, x3+x7-900]

    aum=PrettyTable()
    sol=PrettyTable()
    aum.field_names=["x1","x2","x3","x4","x5","x6","x7","Constante"]
    sol.field_names=["x1","x2","x3","x4","x5","x6","x7","Constante"]

    #La matriz aumentada
    matrizAumentada = representacionMatricial(sistema=ecuaciones, simbolos=variablesX)
    print('\nAsi es la matriz aumentada:\n')
    aum.add_rows(matrizAumentada)
    print(aum)

    #La forma de la diagonal superior.
    matrizDiagSup = diagonalSuperiorMatriz(matrizAumentada)
    print('\nMatriz resuelta:\n')
    sol.add_rows(matrizDiagSup)
    print(sol)

    #Remueve filas de 0s
    matrizSusti = matrizDiagSup[np.any(matrizDiagSup != 0, axis=1)]

    #Inicializa el arreglo para las soluciones numéricas en tal caso de que hayan.
    solucionNum = np.array([0., 0., 0.])

    if matrizSusti.shape[0] != len(variablesX):
        print('\nHay un infinito número de soluciones.')
    elif not np.any(matrizSusti[-1][:len(variablesX)]):
        print('No hay solución.')
    else:
        solucionNum = sustitucionTrasera(matrizSusti, variablesX)
        print(f'\nLas soluciones al sistema son:\n{solucionNum}')