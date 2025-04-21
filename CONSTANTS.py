import numpy as np
RATE = 48000
message_array = [0,1,0,1,0,1] * 30
MESSAGE_LENGTH = len(message_array)
T_BIT = 0.1 # Time for each bit
T_WORD = 1 # Time for opening word
INITIAL_TIME = 5
PARITY_BIT = 1


def start_func(t):
    return 1310 * np.sin(t * 800 * np.pi)
def test_func(t):
    return 30000 * np.sin(t * 2000 * np.pi)

# freq0 = 1031
# freq1 = 1231

freq0 = 2000
freq1 = 2250


AMP = 1000
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



















# def func0(t):
#     return AMP * (np.sin(t*freq0) + np.sin(t*(freq0+20)) + np.sin(t*(freq0+40)) + np.sin(t*(freq0+60)))
# def func1(t):
#     return AMP * (np.sin(t*freq1) + np.sin(t*(freq1+20)) + np.sin(t*(freq1+40)) + np.sin(t*(freq1+60)))
#
#
# def func0_cos(t):
#     return AMP * (np.cos(t*freq0) + np.cos(t*(freq0+20)) + np.cos(t*(freq0+40)) + np.cos(t*(freq0+60)))
# def func1_cos(t):
#     return AMP * (np.cos(t*freq1) + np.cos(t*(freq1+20)) + np.cos(t*(freq1+40)) + np.cos(t*(freq1+60)))


























