import numpy as np
RATE = 48000
message_array = [0,1,0,1,0,1] * 30
MESSAGE_LENGTH = len(message_array) # Number of bits sent

T_BIT = 0.1 # Time for each bit
T_WORD = 1 # Time for opening word
INITIAL_TIME = 5
PARITY_BIT = 1


def start_func(t):
    return 1310 * np.sin(t * 800 * np.pi)

# freq0 = 1031
# freq1 = 1231
# freq2 = 1441
# freq3 = 1741

freq0 = 200 / T_BIT
freq1 = 225 / T_BIT
freq2 = 250 / T_BIT
freq3 = 275 / T_BIT


AMP = 1000
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

function_dictionary = {(func0,func0_cos) : 0, (func1,func1_cos) : 1, (func2,func2_cos) : 2, (func3,func3_cos) : 3} # All bits possible given as functions
# Tuple for cosinus correlation too
FUNCTION_ARRAY = [(func0,func0_cos),(func1,func1_cos)]

errors_dictionary = {}

ENCODING_FILE = 'test_recordings/song_2_shakira.wav'
DECODING_FILE = 'test_recordings/shakira_out.wav'













































