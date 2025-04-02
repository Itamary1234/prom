##########################
# This file is a mvp for decoding signals which aren't trying to be hidden
# It searches for an opening word, and then it is looking for bits
# Imports

from finding_start import *
##########################

# Some decided beforehand constants
RATE = 48000
MESSAGE_LENGTH = 50 # Number of bits sent
T_BIT = 0.1 # Time for each bit
T_WORD = 1 # Time for opening word
word = None # Function to open message
MESSAGE_END = MESSAGE_LENGTH * 0.1 * RATE # Total indexes of message
function_array = None # All bits possible given as functions

# Data from file
time_axis = None
og_amp = None
coded_amps = None

# Finding the start of the message (index) using the find start function
message_start = find_start(T_WORD, time_axis, coded_amps, word)
print(message_start)

# Creating message graph
message_time = time_axis[message_start:message_start + MESSAGE_END]
message_amp = coded_amps[message_start:message_start + MESSAGE_END]

# Finding bits using find bits functions

bits_array = find_bits(MESSAGE_LENGTH, T_BIT, message_time, message_amp, function_array)
print(bits_array)

def decode(file_path : str, function_array : list, message_length : int, t_bit : float, t_word : float, word_func) -> list:
    '''

    :param file_path: File of encoded message
    :param function_array: All possible bits given as functions
    :param message_length: Number of bits in message
    :param t_bit: Time for each bit
    :param t_word: Time for opening word
    :param word_func: Word given as func
    :return:
    '''
    # Pseudo code for now
     # amps, rate, time = read_wave('file_path') # Getting data from filepath