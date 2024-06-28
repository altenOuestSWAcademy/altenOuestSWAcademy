import numpy as np
import matplotlib.pyplot as plt

def simulate_modem(data, carrier_freq, sample_rate, noise_level):
    t = np.arange(len(data)) / sample_rate
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    modulated_signal = data * carrier
    noisy_signal = modulated_signal + noise_level * np.random.normal(size=len(modulated_signal))
    demodulated_signal = noisy_signal * carrier
    demodulated_signal = np.convolve(demodulated_signal, np.ones(100)/100, mode='same')
    return demodulated_signal

# Paramètres
sample_rate = 1000
duration = 1  # durée en secondes
t = np.linspace(0, duration, sample_rate * duration, endpoint=False)
carrier_freq = 100  # Fréquence de la porteuse
noise_level = 0.5  # Niveau de bruit

# Générer des données
data = np.sin(2 * np.pi * 1 * t)  # Signal sinusoïdal de 1 Hz

# Simuler le modem radio
demodulated_signal = simulate_modem(data, carrier_freq, sample_rate, noise_level)

# Tracer les signaux
plt.figure(figsize=(15, 5))
plt.plot(t, data, label='Signal Original')
plt.plot(t, demodulated_signal, label='Signal Démodulé')
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Simulation du Modem Radio')
plt.show()
