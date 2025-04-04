import numpy as np
RATE = 48000
MESSAGE_LENGTH = 1000 # Number of bits sent
message_array = [0] * 260 + [1] * 260 + [2] * 240 + [3] * 240
T_BIT = 0.2 # Time for each bit
T_WORD = 1 # Time for opening word
INITIAL_TIME = 5.3


def start_func(t):
    return 531 * np.sin(t * 2 * np.pi)
def func0(t):
    return 1200 * np.sin(t*1031)
def func1(t):
    return 1205 * np.sin(t*1474)
def func2(t):
    return 1207 * np.sin(t*1221)
def func3(t):
    return 1203 * np.sin(t*1741)

word = start_func # Function to open message
MESSAGE_END = int(MESSAGE_LENGTH * T_BIT * RATE) # Total indexes of message

function_dictionary = {func0 : 0, func1 : 1, func2 : 2, func3 : 3} # All bits possible given as functions
FUNCTION_ARRAY = [func0, func1, func2, func3]

















































