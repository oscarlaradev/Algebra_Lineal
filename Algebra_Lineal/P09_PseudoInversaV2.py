X = [
[82,	84,	2,	97,	80],
[6,	83,	66,	99,	43],
[25,	51,	79,	84,	88],
[28,	100,	92,	31,	66],
[98,	58,	4,	76,	100],
[50,	55,	61,	81,	100],
[54,	53,	96,	68,	38],
[8,	28,	45,	72,	100],
[83,	59,	45,	62,	34],
[50,	7,	14,	65,	64],
[3,	11,	17,	36,	37],
[84,	2,	26,	11,	67],
[46,	68,	100,	7,	80],
[19,	77,	99,	29,	4],
[10,	24,	95,	51,	0],
[79,	81,	84,	99,	20],
[83,	38,	46,	50,	60],
[67,	78,	92,	23,	25],
[28,	31,	86,	72,	52],
[52,	67,	59,	100,	95]
]

import numpy as np

X = np.array(X)
print(X)

#Xinv = np.linalg.inv(X)
#print(Xinv)

#Pseudoinversa
Xpseudoinv = np.linalg.pinv(X)
print(Xpseudoinv)

print("Comprobacion:")
C = X.dot(Xpseudoinv)
C = np.round(C, 2)
C2 = Xpseudoinv.dot(X)
C2 = np.round(C2, 2)

print("X.dot(PseudoX)")
print(C)
print("Xpseudo.dot(X)")
print(C2)
