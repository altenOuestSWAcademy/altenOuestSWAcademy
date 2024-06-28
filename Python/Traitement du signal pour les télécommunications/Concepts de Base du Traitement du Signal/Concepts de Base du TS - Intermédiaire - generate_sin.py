import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    x = np.sin(2 * np.pi * freq * t)
    return t, x

# Générer un signal sinusoïdal de 5Hz
t, x = generate_sine_wave(5, 1000, 1)
plt.plot(t, x)
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.show()
