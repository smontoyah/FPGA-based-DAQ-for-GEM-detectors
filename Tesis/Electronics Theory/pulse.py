import numpy as np
import matplotlib.pyplot as plt

# Parámetros del pulso
A = 140  # Amplitud del pulso (mV)
tau_rise = 30  # Constante de tiempo de subida (ns)
tau_fall = 150  # Constante de tiempo de caída (ns)
baseline = -40  # Línea base (mV)
noise_level = 1  # Nivel de ruido

# Generar datos de tiempo
time = np.linspace(0, 1000, 1000)

# Crear el pulso con una subida rápida y una caída lenta
pulse = np.zeros_like(time)
t0 = 300  # Tiempo del inicio del pulso (ns)
pulse = A * (1 - np.exp(-(time - t0) / tau_rise)) * np.exp(-(time - t0) / tau_fall)
pulse[time < t0] = 0  # Pulso solo a partir de t0

# Añadir la línea base y el ruido
noise = np.random.normal(0, noise_level, len(time))
signal = baseline - pulse + noise  # Señal con el pulso invertido

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(time, signal, label="Señal")
plt.axhline(baseline, color='k', linestyle='-', label='Línea base')
plt.fill_between(time, baseline, signal, where=(signal < baseline), color='gray', alpha=0.5)

plt.xlabel('time (ns)')
plt.ylabel('amplitude (mV)')
plt.grid(True)

# Guardar la gráfica en alta resolución y en formato PNG
plt.savefig('grafica_pulso.png', dpi=300, format='png')

# Mostrar la gráfica
plt.show()
