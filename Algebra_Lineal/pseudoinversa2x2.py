import numpy as np

a=np.array([[3,5,2], 
            [1,4,6]])

a_pseudoinversa = np.linalg.pinv(a)

print("la pseudoinversa es:")
print(a_pseudoinversa)


ide = np.dot(a, a_pseudoinversa)
print("el producto de A por su pseudoinversa es:"   )
print(ide)