##########################
# This file is a mvp for decoding signals which aren't trying to be hidden
# It searches for an opening word, and then it is looking for bits
# Imports
import numpy as np

from finding_start import *
from insert_bits import *
from CONSTANTS import *
##########################


rate, data, time = read_wav_file('song_2_shakira.wav')
plot(time, data)
#data = np.zeros(5000000)
#time = get_time(rate, data)
encrypt(time, data)
plot(time, data)

write_wav_file('song_2_shakira_out.wav',rate,data)
# Data from file
time_axis = time


coded_amps = data
print('Data Encoded, Here We GO')
# Finding the start of the message (index) using the find start function
message_start = rec_find_start(T_WORD, time_axis, coded_amps, word) + T_WORD * rate
print("message_end = " +str(message_start))

# Creating message graph
message_time = time_axis[message_start:message_start + MESSAGE_END]
message_amp = coded_amps[message_start:message_start + MESSAGE_END]

# Finding bits using find bits functions

bits_array = find_bits(MESSAGE_LENGTH, T_BIT, message_time, message_amp, function_array)
print(bits_array)
for i in range(MESSAGE_LENGTH):
    if message_array[i] != function_dictionary[bits_array[i]]:
        print('Real Bit = ' + str(message_array[i]) + ' Decode Bit = ' + str(function_dictionary[bits_array[i]]))


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
    # message_end = message_length * 0.1 * rate  # Total indexes of message