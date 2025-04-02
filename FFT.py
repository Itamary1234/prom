import numpy as np
import matplotlib.pyplot as plt

from decode import *

def plot_fft(time_axis, amp_axis):
    # Calculate the FFT of the signal
    N = len(time_axis)
    fft_vals = np.fft.fft(amp_axis)

    # Calculate the corresponding frequencies
    sample_rate = 1 / (time_axis[1] - time_axis[0])  # Assuming uniform time intervals
    freq_axis = np.fft.fftfreq(N, d=(time_axis[1] - time_axis[0]))  # Frequency axis

    # Only take the positive frequencies (real part)
    positive_freqs = freq_axis[:N // 2]
    positive_fft_vals = np.abs(fft_vals[:N // 2])  # Magnitude of the FFT

    # Plot the FFT
    plt.figure(figsize=(10, 6))
    plt.plot(positive_freqs, positive_fft_vals)
    plt.title('FFT of the Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()


