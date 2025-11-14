import numpy as np
import matplotlib.pyplot as plt

# Definir la función del polinomio SUMA
def polinomio_suma(x):
    # P_final(x) = 7x^2 + x + 2
    return 7*x**2 + x + 2

# 1. Generar los puntos del eje X
# Usaremos un rango de -2 a 2 para tener una buena vista del vértice
x_valores = np.linspace(-2, 2, 100)

# 2. Calcular los puntos del eje Y
y_valores = polinomio_suma(x_valores)

# 3. Crear el gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_valores, y_valores, label='$P_{final}(x) = 7x^2 + x + 2$', color='purple', linewidth=2)

# 4. Personalizar y Mostrar
plt.title('Gráfico de la Suma de Polinomios')
plt.xlabel('Eje X')
plt.ylabel('$P_{final}(x)$')
plt.axhline(0, color='gray', linewidth=0.5, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()