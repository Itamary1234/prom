import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile

from insert_bits import plot


def filter_wav_by_frequency(input_path, output_path, freq_low, freq_high):
    # Read WAV file
    rate, data = wavfile.read(input_path)
    print(f"Sample rate: {rate} Hz")

    # If stereo, take only one channel
    if len(data.shape) == 2:
        data = data[:, 0]

    # FFT
    fft_data = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(fft_data), d=1 / rate)

    # Create a mask for the desired frequency band
    band_mask = (np.abs(freqs) <= freq_high)

    # Apply the mask
    filtered_fft = fft_data * band_mask

    # Inverse FFT to get time-domain signal
    filtered_data = np.fft.ifft(filtered_fft).real

    # Convert to original dtype
    # filtered_data = np.int16(filtered_data / np.max(np.abs(filtered_data)) * 32767)

    plt.figure(figsize=(10, 4))
    plt.plot(filtered_data)
    plt.title("Filtered Audio Waveform")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Save the filtered WAV file
    wavfile.write(output_path, rate, filtered_data)

# Example usage:
# filter_wav_by_frequency("input.wav", "output_filtered.wav", 1000, 2000)

filter_wav_by_frequency("test_recordings/recording_from_python_half_bit_0_4.wav",
                        "test_recordings/recording_from_python_half_bit_0_4_FFT.wav", 0, 1000)
