from scipy.signal import firwin, lfilter, wiener
from scipy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as plt
import pywt

import tkinter as tk
from tkinter import messagebox

def generate_sine_wave(freq, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    x = np.sin(2 * np.pi * freq * t)
    return t, x

def show_message():
    messagebox.showinfo("Message", "Hello World")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Hello World App")

# Définir la taille de la fenêtre (similaire à une fenêtre "Enregistrer sous")
window_width = 800
window_height = 600

# Obtenir les dimensions de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculer les coordonnées pour centrer la fenêtre
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# Définir la géométrie de la fenêtre
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Mettre la fenêtre au premier plan
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

# Ajouter un bouton qui affiche la boîte de dialogue
hello_button = tk.Button(root, text="Click Me", command=show_message, width=20, height=2)
hello_button.pack(expand=True)

# Démarrer la boucle principale de l'interface graphique
root.mainloop()
    
# Générer un signal sinusoïdal de 5Hz
t, x = generate_sine_wave(5, 1000, 1)
plt.plot(t, x)
plt.xlabel('Temps [s]')
plt.ylabel('Amplitude')
plt.show()

