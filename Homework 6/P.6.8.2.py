import numpy as np
import matplotlib.pyplot as plt

# Constants
T = 1        # Period
v = 1        # Frequency (cycle frequency)
t_points = 2048  # Number of time points for high-resolution plot

# Time array from 0 to 2 with 2048 points
t = np.linspace(0, 2, t_points)

# Define the square wave function f_sq(t)
def square_wave(t):
    return np.where((t % T) < T/2, 1, -1)

# Generate the square wave
f_sq = square_wave(t)

# Plot the square wave
plt.figure(figsize=(12, 4))
plt.plot(t, f_sq, label="Square Wave $f_{sq}(t)$")
plt.xlabel("Time $t$")
plt.ylabel("$f_{sq}(t)$")
plt.title("Square Wave with T = 1")
plt.grid(True)
plt.legend()
plt.show()

# Define the Fourier expansion of the square wave truncated at n_terms terms
def fourier_expansion(t, n_terms):
    f_approx = np.zeros_like(t)
    for k in range(1, n_terms + 1):
        n = 2 * k - 1
        f_approx += (4 / (np.pi * n)) * np.sin(2 * np.pi * n * v * t)
    return f_approx

# Plot Fourier expansion for 3, 9, and 18 terms
n_terms_list = [3, 9, 18]
plt.figure(figsize=(12, 8))
for n_terms in n_terms_list:
    f_approx = fourier_expansion(t, n_terms)
    plt.plot(t, f_approx, label=f"Fourier Expansion with {n_terms} terms")
plt.plot(t, f_sq, 'k--', label="Square Wave $f_{sq}(t)$", alpha=0.6)
plt.xlabel("Time $t$")
plt.ylabel("Amplitude")
plt.title("Fourier Expansion of Square Wave")
plt.grid(True)
plt.legend()
plt.show()

# Compute the DFT of the square wave
f_sq_dft = np.fft.fft(f_sq) / t_points
freqs = np.fft.fftfreq(t_points, d=(t[1] - t[0]))

# Plot the magnitude of the DFT of the square wave
plt.figure(figsize=(12, 6))
plt.stem(freqs[:t_points // 2], np.abs(f_sq_dft[:t_points // 2]), basefmt=" ")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("DFT of the Square Wave")
plt.grid(True)
plt.show()

# Compute and plot the DFTs for truncated Fourier series with 3, 9, and 18 terms
plt.figure(figsize=(12, 6))
for n_terms in n_terms_list:
    f_approx = fourier_expansion(t, n_terms)
    f_approx_dft = np.fft.fft(f_approx) / t_points
    plt.stem(freqs[:t_points // 2], np.abs(f_approx_dft[:t_points // 2]),
             label=f"DFT of Fourier Expansion with {n_terms} terms", basefmt=" ")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("DFT of Truncated Fourier Series of Square Wave")
plt.legend()
plt.grid(True)
plt.show()
