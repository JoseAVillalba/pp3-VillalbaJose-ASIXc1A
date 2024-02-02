"""
Jose Villalba Gómez
pp3
MATRIU H
Programa que en una matriz hecha por 0s, la primera columna, la última y la fila central están foramdas por 1s.
"""
try:
    fila = int(input("Filas: "))
    column = int(input("Columnas: "))

    if fila == column and fila % 2 != 0:


        matriu = [[0]*column for i in range(fila)]

        for i in range(column):
            for j in range(fila):
                if i == (column-1)/2 or j == 0 or j == fila - 1:
                    matriu[i][j]=1

        for x in matriu:
            for ele in x:
                print(ele, end='')
            print()


    else:
        print("No has introducido valores senares o los dos valores no son iguales ")
except ValueError:
    print("No has introducido un número")

