import numpy as np

a = np.array([[4, 2],
              [1, 3]
              ])

print("Matriz A:")
print(a)

a_inversa = np.linalg.inv(a)
print("La inversa de A es:")
print(a_inversa)

print(" ")


t=np.array([[3, 1, 0],
            [2, 4, 1],
            [-1, -2, 3]])

print("Matriz A:")
print(t)

e_inversa = np.linalg.inv(t)
print("La inversa de A es:")
print(e_inversa)