
X = [] # lista
y = [] # lista

#x -10 a 10
X = [v for v in range(-10, 11, 1)]
print(X)

#y = x^2 + 3
y = [x**2 + 3 for x in X]
print(y)

from matplotlib import pyplot as plt
plt.plot(X, y)
plt.grid(True)
plt.show()