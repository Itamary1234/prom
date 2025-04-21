import sounddevice as sd
from scipy.io.wavfile import write
from CONSTANTS import *


def record():
    recording_duration = 10  # seconds

    print("Recording...")
    audio = sd.rec(int(recording_duration * RATE), samplerate=RATE, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save to WAV
    write("test_recordings/recording_from_python1.wav", RATE, audio)