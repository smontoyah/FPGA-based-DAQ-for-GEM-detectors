import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter1d

# Environment setup
np.random.seed(0)  # For reproducibility

# Simulation parameters
sample_rate = 1000  # Hz
duration = 1        # seconds
n_samples = int(sample_rate * duration)
time = np.linspace(0, duration, n_samples, endpoint=False)

# Simulated sensor signal (sine wave + noise)
frequency = 5       # Frequency of the signal in Hz
signal = np.sin(2 * np.pi * frequency * time)  # Sine wave signal
noise = np.random.normal(0, 0.5, size=n_samples)  # Noise
sensor_signal = signal + noise  # Sensor signal

# Apply simple moving average filter
window_size = 10
filtered_signal = uniform_filter1d(sensor_signal, size=window_size)

# Plot the signals
plt.figure(figsize=(12, 6))

# Original signal plot
plt.subplot(2, 1, 1)
plt.plot(time, sensor_signal, label='Original Signal', color='b')
plt.title('Simulated Sensor Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Filtered signal plot
plt.subplot(2, 1, 2)
plt.plot(time, filtered_signal, label='Filtered Signal (Moving Average)', color='r')
plt.title('Signal Filtered with Moving Average Filter')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('SMA.png')
plt.show()
