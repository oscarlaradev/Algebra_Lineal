
import numpy as np
A = np.array([[1, 2],[2, 3]])
print(A)

Ainv = np.linalg.inv(A) #matriz inversa
print(Ainv)

#comprobacion:
print("Comprobacion:") #A*Ainv = I = Ainv*A
C = A.dot(Ainv)
C2 = Ainv.dot(A)

print(C)
print(C2)
