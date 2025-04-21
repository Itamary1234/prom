import numpy as np
RATE = 48000
MESSAGE_LENGTH = 1800 # Number of bits sent
message_array = [0,0,0,1,1,1] * 300
T_BIT = 0.1 # Time for each bit
T_WORD = 1 # Time for opening word
INITIAL_TIME = 2.3
PARITY_BIT = 1


def start_func(t):
    return 531 * np.sin(t * 2 * np.pi)

# freq0 = 1031
# freq1 = 1231
# freq2 = 1441
# freq3 = 1741

freq0 = 200 / T_BIT
freq1 = 225 / T_BIT
freq2 = 250 / T_BIT
freq3 = 275 / T_BIT


AMP = 1200
def func0(t):
    return AMP * np.sin(t*freq0)
def func1(t):
    return AMP * np.sin(t*freq1)
def func2(t):
    return AMP * np.sin(t*freq2)
def func3(t):
    return AMP * np.sin(t*freq3)

def func0_cos(t):
    return AMP * np.cos(t*freq0)
def func1_cos(t):
    return AMP * np.cos(t*freq1)
def func2_cos(t):
    return AMP * np.cos(t*freq2)
def func3_cos(t):
    return AMP * np.cos(t*freq3)

word = start_func # Function to open message
MESSAGE_END = int(MESSAGE_LENGTH * T_BIT * RATE) # Total indexes of message

function_dictionary = {(func0,func0) : 0, (func1,func1) : 1, (func2,func2) : 2, (func3,func3) : 3} # All bits possible given as functions
# Tuple for cosinus correlation too
FUNCTION_ARRAY = [(func0,func0),(func1,func1),(func2,func2),(func3,func3)]

errors_dictionary = {}

ENCODING_FILE = 'test_recordings/song_2_shakira.wav'
DECODING_FILE = 'test_recordings/shakira_out.wav'













































