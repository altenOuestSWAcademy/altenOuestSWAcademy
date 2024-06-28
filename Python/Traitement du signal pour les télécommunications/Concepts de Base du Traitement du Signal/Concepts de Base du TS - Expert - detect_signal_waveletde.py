import pywt
import numpy as np
import matplotlib.pyplot as plt

def detect_signal_wavelet(signal, wavelet, level):
    # Décomposition du signal en utilisant la transformée en ondelettes
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    # Calcul du seuil
    sigma = np.median(np.abs(coeffs[-1] - np.median(coeffs[-1]))) / 0.6745
    threshold = sigma * np.sqrt(2 * np.log(len(signal)))
    # Seuil en mode soft pour chaque niveau de coefficient
    denoised_coeffs = list(map(lambda x: pywt.threshold(x, threshold, mode='soft'), coeffs))
    # Reconstruction du signal débruité
    denoised_signal = pywt.waverec(denoised_coeffs, wavelet)
    return denoised_signal

def generate_sine_wave(freq, sample_rate, duration):
    # Génération d'un signal sinusoïdal
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    x = np.sin(2 * np.pi * freq * t)
    return t, x

# Générer un signal sinusoïdal de 10Hz
t, x = generate_sine_wave(10, 10000, 1)

# Ajouter du bruit au signal sinusoïdal
noise = np.random.normal(0, 0.5, x.shape)
x_noisy = x + noise

# Détection de signaux en utilisant la transformée en ondelettes
denoised_x = detect_signal_wavelet(x_noisy, 'db4', 5)

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
