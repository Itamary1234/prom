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



rate, amp_axis1, time_axis1 = read_wav_file('song_2_shakira_out.wav')

plot_fft(time_axis1, amp_axis1)