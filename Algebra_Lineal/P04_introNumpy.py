
#Libreria = Modulo en Python

#Numpy - Operaciones matematicas

mA = [3, 4, 5] #lista

mB = [1, 4, 6] #lista

print(mA)
print(mB)

import numpy as np #as = alias

mA = np.array(mA) #convierte la lista en una matriz unidimensional
mB = np.array(mB)

print(mA)
print(mB)

print("C en forma de lista de python")
C = [[2, 4], [1, 5]]
print(C)
print("C en forma matricial")
C = np.array(C)
print(C)




