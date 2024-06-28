from scipy.signal import wiener
from scipy.signal import firwin, lfilter
import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    x = np.sin(2 * np.pi * freq * t)
    return t, x

def adaptive_noise_reduction(signal):
    denoised_signal = wiener(signal)
    return denoised_signal

# Générer un signal sinusoïdal de 5Hz
t, x = generate_sine_wave(5, 1000, 1)
# Ajouter du bruit au signal sinusoïdal
noise = np.random.normal(0, 0.5, x.shape)
x_noisy = x + noise
# Réduction de bruit dans le signal
denoised_x = adaptive_noise_reduction(x)

# Tracé des signaux
plt.figure(figsize=(15, 5))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Signal original')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, x_noisy)
plt.title('Signal bruité')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, denoised_x)
plt.title('Signal débruité avec filtrage adaptatif')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
