import numpy as np
import matplotlib.pyplot as plt

# Paramètres communs
fs = 48000  # Fréquence d'échantillonnage en Hz
duration = 0.050  # Durée de la sinusoïde en secondes (par exemple, 10 ms)
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Fonction pour générer une sinusoïde avec une fréquence et une phase spécifiée
def generate_sine_wave(frequency, phase_degree, sampling_rate, duration):
    phase_radians = np.deg2rad(phase_degree)
    return np.sin(2 * np.pi * frequency * t + phase_radians)

# Caractéristiques des sinusoïdes (incluant celle de 120 Hz avec phase 0° en début)
sinusoids = [
    (120, 0),    # Nouvelle sinusoïde ajoutée
    (260, 45),
    (1080, 10),
    (4120, 0),
    (440, 90),
    (2080, 30)
]

# Initialisation de la somme des sinusoïdes
sum_of_sinusoids = np.zeros_like(t)

# Calcul de la somme des sinusoïdes
for freq, phase in sinusoids:
    y = generate_sine_wave(freq, phase, fs, duration)
    sum_of_sinusoids += y

# Affichage de la somme des sinusoïdes
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, sum_of_sinusoids, color='red')
plt.title("Somme des sinusoïdes")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Application de la FFT
N = len(sum_of_sinusoids)
fft_result = np.fft.fft(sum_of_sinusoids)
fft_magnitude = np.abs(fft_result)[:N // 2]  # Prendre la moitié du spectre (symétrie)
frequencies = np.fft.fftfreq(N, 1/fs)[:N // 2]

# Affichage du spectre de la FFT
plt.subplot(2, 1, 2)
plt.plot(frequencies, fft_magnitude, color='purple')
plt.title("Spectre de fréquence de la somme des sinusoïdes (FFT)")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()