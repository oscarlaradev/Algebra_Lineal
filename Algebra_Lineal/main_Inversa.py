import numpy as np

A = [[1,3, 2],
     [4, 2, 1],
     [5, 0, 2]]
A = np.array(A)
print(A)

inversa = np.linalg.inv(A)
print(inversa)

test = [
     [-4/25, 6/25, 1/25],
     [3/25, 8/25, -7/25],
     [10/25, -15/25, 10/25]]
test = np.array(test)

r = test.dot(A)
print(test)
print(r)

