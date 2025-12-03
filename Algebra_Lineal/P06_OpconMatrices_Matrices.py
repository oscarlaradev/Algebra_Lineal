
#SUMA Y RESTA
#REQUIEREN QUE EL ORDEN DE LAS MATRICES SEA EL MISMO

#PUEDEN SER CUADRADAS O RECTANGULARES

import numpy as np
A = np.array([[1, 2],[2, 3]])
B = np.array([[3, 4],[5, 2]])

print(A)
print(B)

C = A + B
print("Resultado de la suma de A + B:")
print(C)

C = A - B
print("Resultado de la resta de A - B:")
print(C)

#Esto no es multiplicacion matricial
C = A * B
print("Multiplicacion de A * B:")
print(C)

C = A.dot(B)
print("Multiplicacion matricial de A * B:")
print(C)
