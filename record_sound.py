import sounddevice as sd
from scipy.io.wavfile import write
from CONSTANTS import *


def record(file_name = "test_recordings/recording_from_python1.wav"):

    print("Recording...")
    audio = sd.rec(int(RECORDING_TIME * RATE), samplerate=RATE, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save to WAV
    write(file_name, RATE, audio)

