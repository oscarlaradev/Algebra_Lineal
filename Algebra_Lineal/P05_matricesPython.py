import numpy

print("A en forma de lista de python")
A = [["Oscar", 4, 5], ["Lara", 5, 6]]
print(A)
print("A en forma matricial")
A = numpy.array(A)
print(A)

orden = A.shape
print("Orden:" + str(orden))



