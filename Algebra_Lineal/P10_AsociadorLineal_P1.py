
archivo = open("iris_completa.csv")
contenido_archivo = archivo.readlines()
print(contenido_archivo)

del contenido_archivo[0] #elimina los encabezados -primera linea

matrizEntradas = []
matrizSalidas = []
for linea in contenido_archivo:
    #print(linea, end="")
    #print(linea)

    #split
    componentes = linea.split(",")
    #print(componentes)

    #slicing
    entrada = componentes[0:len(componentes)-1] #todos menos el ultimo
    salida = componentes[len(componentes)-1]

    #transformacion
    entrada = list(map(float,entrada))

    matrizEntradas.append(entrada)

    #print()

for entrada in matrizEntradas:
    pass
    #print(entrada)


import numpy as np

X = np.array(matrizEntradas)
print(X)

x_pinv = np.linalg.pinv(X)

print(x_pinv)

"""
print("Comprobacion:")
C = x_pinv.dot(X)
C = np.round(C, 2)

print("Xpseudo.dot(X)")
print(C)

"""



