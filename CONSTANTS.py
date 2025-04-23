import numpy as np
RATE = 48000
message_array = [0,1,0,1,0,1] * 30

MESSAGE_LENGTH = 196
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

function_dictionary = {(func0,func0_cos) : 0, (func1,func1_cos) : 1} # All bits possible given as functions
# Tuple for cosinus correlation too
FUNCTION_ARRAY = [(func0,func0_cos),(func1,func1_cos)]

errors_dictionary = {}

ENCODING_FILE = 'test_recordings/song_2_shakira.wav'
DECODING_FILE = 'test_recordings/shakira_out.wav'


freq0_0 = 2000
freq0_1 = 2300
freq0_2 = 2600
freq0_3 = 2900

freq1_0 = 4100
freq1_1 = 4400
freq1_2 = 4900
freq1_3 = 5200



def func0_0_sin(t):
    return AMP * np.sin(t*freq0_0)
def func0_1_sin(t):
    return AMP * np.sin(t*freq0_1)
def func0_2_sin(t):
    return AMP * np.sin(t*freq0_2)
def func0_3_sin(t):
    return AMP * np.sin(t*freq0_3)
def func1_0_sin(t):
    return AMP * np.sin(t*freq1_0)
def func1_1_sin(t):
    return AMP * np.sin(t*freq1_1)
def func1_2_sin(t):
    return AMP * np.sin(t*freq1_2)
def func1_3_sin(t):
    return AMP * np.sin(t*freq1_3)

def func0_0_cos(t):
    return AMP * np.cos(t*freq0_0)
def func0_1_cos(t):
    return AMP * np.cos(t*freq0_1)
def func0_2_cos(t):
    return AMP * np.cos(t*freq0_2)
def func0_3_cos(t):
    return AMP * np.cos(t*freq0_3)
def func1_0_cos(t):
    return AMP * np.cos(t*freq1_0)
def func1_1_cos(t):
    return AMP * np.cos(t*freq1_1)
def func1_2_cos(t):
    return AMP * np.cos(t*freq1_2)
def func1_3_cos(t):
    return AMP * np.cos(t*freq1_3)


MINI_BIT_FUNCTION_ARRAY = [[(func0_0_sin,func0_0_cos),(func1_0_sin,func1_0_cos)],
                           [(func0_1_sin,func0_1_cos),(func1_1_sin,func1_1_cos)],
                           [(func0_2_sin, func0_2_cos), (func1_2_sin, func1_2_cos)],
                           [(func0_3_sin, func0_3_cos), (func1_3_sin, func1_3_cos)],]




BIT_LENGTH = len(MINI_BIT_FUNCTION_ARRAY)
T_MINI_BIT = T_BIT/BIT_LENGTH










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










































