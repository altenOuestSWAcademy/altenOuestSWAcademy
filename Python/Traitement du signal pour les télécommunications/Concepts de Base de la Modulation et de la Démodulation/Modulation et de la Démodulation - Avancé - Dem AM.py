import numpy as np
import matplotlib.pyplot as plt

def am_modulate(carrier_freq, modulating_signal, sample_rate):
    t = np.arange(len(modulating_signal)) / sample_rate
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    modulated_signal = (1 + modulating_signal) * carrier
    return modulated_signal

def am_demodulate(am_signal, carrier_freq, sample_rate):
    t = np.arange(len(am_signal)) / sample_rate
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    demodulated_signal = am_signal * carrier
    demodulated_signal = np.convolve(demodulated_signal, np.ones(100)/100, mode='same')
    return demodulated_signal

# Définir les paramètres
sample_rate = 1000
t = np.arange(0, 1, 1/sample_rate)  # 1 seconde de signal
modulating_freq = 5  # fréquence de modulation

# Créer le signal modulant
modulating_signal = np.sin(2 * np.pi * modulating_freq * t)

# Moduler le signal avec une fréquence porteuse de 100 Hz
carrier_freq = 100
am_signal = am_modulate(carrier_freq, modulating_signal, sample_rate)

# Démoduler le signal AM
demodulated_signal = am_demodulate(am_signal, 100, 1000)

plt.plot(t, modulating_signal)
# Afficher le signal modulé
plt.plot(t, am_signal)
# Afficher le signal modulé
plt.plot(t, demodulated_signal)
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.title('Signal AM modulé')
plt.show()
