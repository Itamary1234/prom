##########################
# This file is a mvp for decoding signals which aren't trying to be hidden
# It searches for an opening word, and then it is looking for bits
# Imports
import numpy as np

from finding_start import *
from insert_bits import *
from CONSTANTS import *
##########################



def decode(file_path_in : str, file_path_out : str) -> list:
    '''
    :param file_path_in: File of song or recording to encode data on message
    :param file_path_out: File to write encoded data on

    :return: Array of functions code thinks
    '''

    # Getting data, plotting it
    rate, coded_amps, time_axis = encode(file_path_in, file_path_out)

    print('Data Encoded, Here We GO')
    # Finding the start of the message (index) using the find start function
    message_start = rec_find_start(T_WORD, time_axis, coded_amps, word) + T_WORD * rate
    print("message_end = " +str(message_start))

    # Creating message graph
    message_time = time_axis[message_start:message_start + MESSAGE_END]
    message_amp = coded_amps[message_start:message_start + MESSAGE_END]

    # Finding bits using find bits functions
    bits_array = find_bits(MESSAGE_LENGTH, T_BIT, message_time, message_amp, FUNCTION_ARRAY)
    return bits_array


def encode(file_path_in : str, file_path_out : str):
    # Getting data, plotting it
    rate, coded_amps, time_axis = read_wav_file(file_path_in)
    plot(time_axis, coded_amps)

    # Encoding signal in data and plotting it
    encrypt(time_axis, coded_amps)
    plot(time_axis, coded_amps)

    # Writing into file so we could hear that recording is hidden
    write_wav_file(file_path_out, rate, data)
    return rate, coded_amps, time_axis

bits_array = decode('song_2_shakira.wav', 'song_2_shakira_out.wav')