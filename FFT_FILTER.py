import random

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from CONSTANTS import *

def cut_and_fft(wav_path, target_second, window_size=1.0):
    """
    Cuts a segment from a WAV file at a specific time and computes its FFT.

    Parameters:
    wav_path (str): Path to the WAV file.
    target_second (float): The second from which to start cutting.
    window_size (float): Duration in seconds of the segment to cut (default 1 second).

    Returns:
    freqs (numpy array): Array of frequencies.
    fft_magnitude (numpy array): Magnitude of the FFT.
    """
    # Read WAV file
    sample_rate, data = wavfile.read(wav_path)

    # Calculate start and end sample indices
    start_sample = int(target_second * sample_rate)
    end_sample = int((target_second + window_size) * sample_rate)

    # Cut the segment
    segment = data[start_sample:end_sample]

    # Apply FFT
    fft_result = np.fft.fft(segment)
    fft_magnitude = np.abs(fft_result)
    freqs = np.fft.fftfreq(len(segment), d=1/sample_rate)

    # Return only the positive frequencies
    pos_mask = freqs >= 0
    return freqs[pos_mask], fft_magnitude[pos_mask]



def get_average_magnitude(freqs, magnitude, target_freq, bin_range=5):
    idx = np.argmin(np.abs(freqs - target_freq))
    start = max(idx - bin_range, 0)
    end = min(idx + bin_range + 1, len(magnitude))
    return np.mean(magnitude[start:end])




def fft_decode(wav_path : str, message_start : float):
    ''' This function will decode using fft, message start will be given in seconds '''

    bit_array = []
    mini_bits_array = []
    certainty_array = []
    for i in range(MESSAGE_LENGTH):
        bit = 0
        for j in range(BIT_LENGTH):
            start_time = message_start + i * T_BIT + j * T_MINI_BIT
            freqs, magnitude = cut_and_fft(wav_path, start_time, T_MINI_BIT)

            # Getting magnitude of FFT from data
            freq_0_mag = get_average_magnitude(freqs, magnitude, freq0)
            freq_1_mag = get_average_magnitude(freqs, magnitude, freq1)
            # Checking which bit is more likely to be sent
            if freq_1_mag > freq_0_mag:
                mini_bits_array.append(1)
                bit += 1
                certainty = 1 - (freq_0_mag / freq_1_mag)
            else:
                mini_bits_array.append(0)
                certainty = 1 - (freq_1_mag / freq_0_mag)
                bit -= 1

            certainty_array.append(certainty)

        # Appending to bits according to the sum.
        if bit > 0:
            bit_array.append(1)
        elif bit < 0:
            bit_array.append(0)
        else:
            bit_array.append(random.randint(0, 1))

    return bit_array, (mini_bits_array, certainty_array)