from scipy.signal import firwin, lfilter
import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    x = np.sin(2 * np.pi * freq * t)
    return t, x

def apply_fir_filter(signal, cutoff_freq, sample_rate, numtaps):
    fir_coeff = firwin(numtaps, cutoff_freq, fs=sample_rate)
    filtered_signal = lfilter(fir_coeff, 1.0, signal)
    return filtered_signal

# Générer un signal sinusoïdal de 5Hz
t, x = generate_sine_wave(5, 1000, 1)
# Appliquer un filtre FIR passe-bas
filtered_x = apply_fir_filter(x, 5, 1000, 101)

# Tracé des signaux
plt.figure(figsize=(15, 5))

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Signal original')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, filtered_x)
plt.title('Signal avec filtre numérique FIR')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
