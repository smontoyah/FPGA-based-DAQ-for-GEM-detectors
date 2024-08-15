import numpy as np
import matplotlib.pyplot as plt

# Configuración de la señal de reloj
t = np.linspace(0, 10, 1000)  # Tiempo de 0 a 10 con 1000 puntos
clock_signal = 0.5 * (1 + np.sign(np.sin(2 * np.pi * t)))  # Señal de reloj (onda cuadrada)

# Configuración de la señal digital con duraciones no uniformes en los ciclos
data_signal = np.piecewise(t, 
                           [t < 0.5, 
                            (t >= 0.5) & (t < 1.5), 
                            (t >= 1.5) & (t < 2), 
                            (t >= 2) & (t < 3.5), 
                            (t >= 3.5) & (t < 4), 
                            (t >= 4) & (t < 5.2), 
                            (t >= 5.2) & (t < 6), 
                            (t >= 6) & (t < 7.8), 
                            (t >= 7.8) & (t < 8.5), 
                            t >= 8.5],
                           [0, 1, 0, 1, 0, 1, 0, 1, 0, 1])

# Crear la figura y los ejes
fig, axs = plt.subplots(2, 1, figsize=(10, 5), sharex=True)

# Señal de reloj
axs[0].plot(t, clock_signal, drawstyle='steps-pre', color='blue')
axs[0].set_ylim(-0.1, 1.1)
axs[0].set_ylabel('Señal de Reloj')
axs[0].grid(True)

# Señal digital con duraciones no uniformes
axs[1].plot(t, data_signal, drawstyle='steps-pre', color='red')
axs[1].set_ylim(-0.1, 1.1)
axs[1].set_ylabel('Señal Digital')
axs[1].set_xlabel('Tiempo')
axs[1].grid(True)

# Mostrar el diagrama de tiempo
plt.tight_layout()
plt.show()
