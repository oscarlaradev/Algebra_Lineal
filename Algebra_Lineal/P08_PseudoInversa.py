
X = [
    [82,	6,	25,	28,	98,	50,	54,	8,	83,	50,	3,	84,	46,	19,	10,	79,	83,	67,	28,	52],
    [84,	83,	51,	100,	58,	55,	53,	28,	59,	7,	11,	2,	68,	77,	24,	81,	38,	78,	31,	67],
    [2,	66,	79,	92,	4,	61,	96,	45,	45,	14,	17,	26,	100,	99,	95,	84,	46,	92,	86,	59],
    [97,	99,	84,	31,	76,	81,	68,	72,	62,	65,	36,	11,	7,	29,	51,	99,	50,	23,	72,	100],
    [80,	43,	88,	66,	100,	100,	38,	100,	34,	64,	37,	67,	80,	4,	0,	20,	60,	25,	52,	95]
    ]

import numpy as np

X = np.array(X)
print(X)

#Xinv = np.linalg.inv(X)
#print(Xinv)

#Pseudoinversa
Xpseudoinv = np.linalg.pinv(X)
print(Xpseudoinv)

print('Comprobacion:')
C = X.dot(Xpseudoinv)
C = np.round(C, 2)
C2 = Xpseudoinv.dot(X)
C2 = np.round(C2, 2)

print('X.dot(PseudoX)')
print(C)
print('Xpseudo.dot(X)')
print(C2)
