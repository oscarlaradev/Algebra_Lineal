
import numpy as np

m11 = [[5, 2, 4],[3, 5, 1],[0,4,-1]]
m11 = np.array(m11)
m11 = np.linalg.det(m11)
print(m11)

m12 = [[-2, 2, 4],[2, 5, 1],[-3,4,-1]]
m12 = np.array(m12)
print(m12)
m12 = np.linalg.det(m12)
print(m12) #76

m13 = [[-2, 5, 4],[2, 3, 1],[-3,0,-1]]
m13 = np.array(m13)
m13 = np.linalg.det(m13)
print(m13)

m14 = [[-2, 5, 2],[2, 3, 5],[-3,0,4]]
m14 = np.array(m14)
m14 = np.linalg.det(m14)
print(m14) #-41


A = [[3, 0, 1, -2],[-2, 5, 2, 4],[2,3, 5, 1], [-3, 0, 4, -1]]
A = np.array(A)
print(A)
A = np.linalg.det(A)
print(A)




