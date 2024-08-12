import numpy as np
import matplotlib.pyplot as plt

# Crear un rango de valores x
x = np.logspace(-3, 6, 1000)

# Definir las diferentes partes de la curva con funciones personalizadas
def curve1(x):
    return 150 * np.exp(-((np.log10(x) + 2)**2))  # Pico inicial y caída

def curve2(x):
    return 10 / x  # Zona de caída suave

def curve3(x):
    return 1 + 0.1 * np.log10(x)  # Zona lineal

def curve4(x):
    return 1e-4 * np.exp(0.6 * np.log10(x))  # Aumento exponencial

# Combinar las curvas utilizando np.piecewise
y = np.piecewise(x,
                 [x < 0.01, (x >= 0.01) & (x < 1), (x >= 1) & (x <= 1000), x > 1000],
                 [curve1, curve2, curve3, curve4])

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar la curva
ax.plot(x, y, color='black')

# Escala logarítmica en los ejes
ax.set_xscale('log')
ax.set_yscale('log')

# Etiquetas de los ejes
ax.set_xlabel(r'Muon momentum [MeV/c, GeV/c, TeV/c]')
ax.set_ylabel(r'Stopping power [MeV cm$^2$/g]')

# Ticks personalizados en x
ax.set_xticks([1e-3, 1e-2, 1e-1, 1, 10, 100, 1000, 1e4, 1e5, 1e6])
ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())

# Límites de los ejes
ax.set_xlim([1e-3, 1e6])
ax.set_ylim([1, 1000])

# Mostrar la cuadrícula
ax.grid(True, which="both", ls="--")

# Mostrar la gráfica
plt.show()
