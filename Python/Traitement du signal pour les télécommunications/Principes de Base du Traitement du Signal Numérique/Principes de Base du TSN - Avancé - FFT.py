from scipy.signal import firwin, lfilter
import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    x = np.sin(2 * np.pi * freq * t)
    return t, x

def compute_fft(signal, sample_rate):
    signal_fft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1/sample_rate)
    return freqs, signal_fft

# Générer un signal sinusoïdal de 5Hz
t, x = generate_sine_wave(5, 1000, 1)
# Calculer la FFT du signal
freqs, signal_fft = compute_fft(x, 1000)


# Tracé des signaux
plt.figure(figsize=(15, 5))

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Signal original')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(freqs, np.abs(signal_fft))
plt.title('Signal avec filtre numérique FIR')
plt.xlabel('Fréquence [Hz]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
