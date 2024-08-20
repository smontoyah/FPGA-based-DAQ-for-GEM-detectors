import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
t = np.linspace(0, 5 * np.pi, 1000)  # Tiempo
signal = np.sin(t)  # Señal senoidal

# Agregar ruido a la señal para simular la salida de un sensor
noise = 0.05 * np.random.normal(size=t.size)
noisy_signal = signal + noise

# Definir los bordes de los intervalos para la suma de Riemann
bins = np.linspace(0, 5 * np.pi, 70)  # Más intervalos para barras más finas
bin_centers = (bins[:-1] + bins[1:]) / 2  # Centro de cada intervalo

# Alturas de las barras (evaluar la señal ruidosa en los centros de los intervalos)
heights = np.interp(bin_centers, t, noisy_signal)

# Gráfica
plt.figure(figsize=(10, 6))

# Graficar la señal ruidosa
plt.plot(t, noisy_signal, label="input signal", color="blue", alpha=0.5)

# Graficar el histograma como una suma de Riemann
plt.bar(bin_centers, heights, width=(bins[1] - bins[0]), alpha=0.5, align='center', edgecolor='black', label="digital output")

# Configuración de los ejes
plt.xticks([])  # Sin marcas en el eje x
plt.yticks([])  # Sin marcas en el eje y

# Etiquetas y formato
plt.xlabel("$t$")
plt.ylabel("$V_{in} [mV]$")
#plt.title("Señal Senoidal con Ruido y Suma de Riemann")
plt.legend()
plt.grid(False)  # Sin cuadrícula
plt.savefig('adc_output.png', dpi=300, format='png')
plt.show()
