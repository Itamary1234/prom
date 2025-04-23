import numpy as np
RATE = 48000
message_array = [0,1,0,1,0,1] * 30
MESSAGE_LENGTH = len(message_array)
T_BIT = 0.1 # Time for each bit
T_WORD = 1 # Time for opening word
INITIAL_TIME = 5
PARITY_BIT = 1
CUT_PERCENT = 0.1


def start_func(t):
    return 2310 * np.sin(t * 800 * np.pi)
def test_func(t):
    return 30000 * np.sin(t * 2000 * np.pi)

# freq0 = 1031
# freq1 = 1231

freq0 = 2000
freq1 = 2250


AMP = 2000
def func0(t):
    return AMP * np.sin(t*freq0)
def func1(t):
    return AMP * np.sin(t*freq1)


def func0_cos(t):
    return AMP * np.cos(t*freq0)
def func1_cos(t):
    return AMP * np.cos(t*freq1)


word = start_func # Function to open message
MESSAGE_END = int(MESSAGE_LENGTH * T_BIT * RATE) # Total indexes of message

function_dictionary = {(func0,func0) : 0, (func1,func1) : 1} # All bits possible given as functions
# Tuple for cosinus correlation too
FUNCTION_ARRAY = [(func0,func0),(func1,func1)]

errors_dictionary = {}

ENCODING_FILE = 'test_recordings/song_2_shakira.wav'
DECODING_FILE = 'test_recordings/shakira_out.wav'


CHAR_TO_BINARY = {
    '~': [0,0,0,0,0],
    'a': [0,0,0,0,1],
    'b': [0,0,0,1,0],
    'c': [0,0,0,1,1],
    'd': [0,0,1,0,0],
    'e': [0,0,1,0,1],
    'f': [0,0,1,1,0],
    'g': [0,0,1,1,1],
    'h': [0,1,0,0,0],
    'i': [0,1,0,0,1],
    'j': [0,1,0,1,0],
    'k': [0,1,0,1,1],
    'l': [0,1,1,0,0],
    'm': [0,1,1,0,1],
    'n': [0,1,1,1,0],
    'o': [0,1,1,1,1],
    'p': [1,0,0,0,0],
    'q': [1,0,0,0,1],
    'r': [1,0,0,1,0],
    's': [1,0,0,1,1],
    't': [1,0,1,0,0],
    'u': [1,0,1,0,1],
    'v': [1,0,1,1,0],
    'w': [1,0,1,1,1],
    'x': [1,1,0,0,0],
    'y': [1,1,0,0,1],
    'z': [1,1,0,1,0],
    ' ': [1,1,0,1,1],
    '.': [1,1,1,0,0],
    '?': [1,1,1,0,1],
    '!': [1,1,1,1,0],
    '-': [1,1,1,1,1],
}

BINARY_TO_CHAR = {tuple(v): k for k, v in CHAR_TO_BINARY.items()}










































