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

    # Shift the zero-frequency component to the center
    fft_vals_shifted = np.fft.fftshift(fft_vals)
    freq_axis_shifted = np.fft.fftshift(freq_axis)

    # Plot the FFT with both positive and negative frequencies
    plt.figure(figsize=(10, 6))
    plt.plot(freq_axis_shifted, np.abs(fft_vals_shifted))
    plt.title('FFT of the Signal')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()



time_axis1 = np.linspace(0, 1, 1000, endpoint=False)  # 1 second duration, 1000 samples
amp_axis1 = np.sin(2 * np.pi * 50 * time_axis1)  # 50 Hz sine wave

plot_fft(time_axis1, amp_axis1)