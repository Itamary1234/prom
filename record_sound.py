import sounddevice as sd
from scipy.io.wavfile import write
from CONSTANTS import *


def record():

    print("Recording...")
    audio = sd.rec(int(RECORDING_TIME * RATE), samplerate=RATE, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save to WAV
    write("test_recordings/recording_from_python1.wav", RATE, audio)

