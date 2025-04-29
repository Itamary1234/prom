import numpy as np
RATE = 48000
MESSAGE_ARRAY = [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1,
                        1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1,
                        1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1,
                        0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0,
                        1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0,
                        1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0,
                        0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1,
                        1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1,
                        1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1,
                        1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1]



MESSAGE_LENGTH = 420
T_BIT = 0.3 # Time for each bit
T_WORD = 1 # Time for opening word
INITIAL_TIME = 5
PARITY_BIT = 1
CUT_PERCENT = 0
DIVISOR = 1
RECORDING_TIME = MESSAGE_LENGTH * T_BIT +INITIAL_TIME +3

AMP = 1000


def start_func(t):
    return 2010 * np.sin(t * 800 * np.pi)
def test_func(t):
    return 30000 * np.sin(t * 2000 * np.pi)

# freq0 = 1031
# freq1 = 1231

freq0 = 1900 * np.pi
freq1 = 700 * np.pi


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


freq0_0 = 1000 * np.pi
freq0_1 = 900 * np.pi
freq0_2 = 800 * np.pi
freq0_3 = 700 * np.pi

freq1_0 = 600 * np.pi
freq1_1 = 500 * np.pi
freq1_2 = 400 * np.pi
freq1_3 = 300 * np.pi



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


# MINI_BIT_FUNCTION_ARRAY = [[(func0_0_sin,func0_0_cos),(func1_0_sin,func1_0_cos)],
#                            [(func0_1_sin,func0_1_cos),(func1_1_sin,func1_1_cos)],
#                            [(func0_2_sin, func0_2_cos), (func1_2_sin, func1_2_cos)],
#                            [(func0_3_sin, func0_3_cos), (func1_3_sin, func1_3_cos)],]


# MINI_BIT_FUNCTION_ARRAY = [[(func0_0_sin,func0_0_cos),(func0_1_sin,func0_1_cos)],
#                            [(func0_1_sin,func0_1_cos),(func1_1_sin,func1_1_cos)],
#                            [(func1_2_sin, func1_2_cos), (func0_3_sin, func0_3_cos)],
#                            [(func0_2_sin, func0_2_cos), (func1_3_sin, func1_3_cos)],
#                            [(func0_3_sin, func0_3_cos), (func0_1_sin, func0_1_cos)],
#                            [(func1_3_sin, func1_3_cos), (func1_1_sin, func1_1_cos)],
#                            [(func0_1_sin, func0_1_cos), (func1_2_sin, func1_2_cos)],
#                            [(func1_1_sin, func1_1_cos), (func0_3_sin, func0_3_cos)],
#                            [(func1_2_sin, func1_2_cos), (func0_1_sin, func0_1_cos)],
#                            [(func1_3_sin, func1_3_cos), (func0_3_sin, func0_3_cos)],
#                            ]#this is 10 crazy matches


# MINI_BIT_FUNCTION_ARRAY = [[(func0,func0_cos),(func1,func1_cos)],
#                            [(func0,func0_cos),(func1,func1_cos)]]#this is same func only twice in one bit

MINI_BIT_FUNCTION_ARRAY1 = [[(func0,func0_cos),(func1,func1_cos)],
                           [(func0,func0_cos),(func1,func1_cos)],
                           [(func0,func0_cos),(func1,func1_cos)]]

MINI_BIT_FUNCTION_ARRAY2 = [[(func0,func0_cos),(func1,func1_cos)],
                           [(func0,func0_cos),(func1,func1_cos)],
                           [(func0,func0_cos),(func1,func1_cos)]]



#
# MINI_BIT_FUNCTION_ARRAY = [[(func0,func0_cos),(func1,func1_cos)],
#                            [(func1,func1_cos),(func0,func0_cos)]]#this is same func only twice in one bit
# MINI_BIT_FUNCTION_ARRAY = [[(func0,func0_cos),(func1,func1_cos)],
#                            [(func0,func0_cos),(func1,func1_cos)],
#                            [(func0,func0_cos),(func1,func1_cos)],
#                            [(func0,func0_cos),(func1,func1_cos)],
#                            [(func0,func0_cos),(func1,func1_cos)],

                           # ]#this is same func 10 times in one bit

# MINI_BIT_FUNCTION_ARRAY = [[(func0, func0_cos), (func1,func1_cos)],
#                            [(func1, func1_cos), (func0,func0_cos)],
#                            [(func0, func0_cos), (func1, func1_cos)],
#                            [(func1, func1_cos), (func0, func0_cos)],
#                            [(func0, func0_cos), (func1, func1_cos)],
#                            [(func1, func1_cos), (func0, func0_cos)],
#                            [(func0, func0_cos), (func1, func1_cos)],
#                            [(func1, func1_cos), (func0, func0_cos)],
#                            [(func0, func0_cos), (func1, func1_cos)],
#                            [(func1, func1_cos), (func0, func0_cos)]
#                            ]#opposite bits so ignore noise 8 times

# MINI_BIT_FUNCTION_ARRAY = [[(func0,func0_cos),(func1,func1_cos)]]




BIT_LENGTH = len(MINI_BIT_FUNCTION_ARRAY1)
T_MINI_BIT = T_BIT/BIT_LENGTH










CHAR_TO_BINARY = {
    'e': [0,0,0,0],
    'a': [0,0,0,1],
    'r': [0,0,1,0],
    'i': [0,0,1,1],
    'o': [0,1,0,0],
    't': [0,1,0,1],
    'n': [0,1,1,0],
    's': [0,1,1,1],
    'l': [1,0,0,0],
    'c': [1,0,0,1],
    'u': [1,0,1,0],
    'd': [1,0,1,1],
    'p': [1,1,0,0],
    'm': [1,1,0,1],
    'h': [1,1,1,0],
    ' ': [1,1,1,1],
}#eariotnslcudpmh

BINARY_TO_CHAR = {tuple(v): k for k, v in CHAR_TO_BINARY.items()}


MINI_MESSAGE_ARRAY = [bit for bit in MESSAGE_ARRAY for _ in range(BIT_LENGTH)]








































