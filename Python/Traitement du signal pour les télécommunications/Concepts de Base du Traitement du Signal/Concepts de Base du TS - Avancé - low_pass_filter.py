from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt

def low_pass_filter(signal, cutoff_freq, sample_rate):
    freqs = np.fft.fftfreq(len(signal), 1/sample_rate)
    signal_fft = fft(signal)
    signal_fft[np.abs(freqs) > cutoff_freq] = 0
    filtered_signal = ifft(signal_fft)
    return filtered_signal

def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    x = np.sin(2 * np.pi * freq * t)
    return t, x

# Générer un signal sinusoïdal de 5Hz
t, x = generate_sine_wave(10, 1000, 1)
# Appliquer un filtre passe-bas à 5Hz
filtered_x = low_pass_filter(x, 5, 1000)
plt.plot(t, filtered_x.real)
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.show()
