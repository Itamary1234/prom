##########################
# This file is a mvp for decoding signals which aren't trying to be hidden
# It searches for an opening word, and then it is looking for bits
# Imports
import numpy as np

from finding_start import *
from insert_bits import *
from record_sound import *
from CONSTANTS import *
from hamming_code import *
##########################



def decode(file_path_in : str) -> list:
    '''
    :param file_path_in: File of song or recording to encode data on message
    :param file_path_out: File to write encoded data on

    :return: Array of functions code thinks
    '''

    # Getting data, plotting it
    rate, coded_amps, time_axis = read_wav_file(file_path_in)
    plot(time_axis, coded_amps)

    print('Data Read, Here We GO')
    # Finding the start of the message (index) using the find start function

    message_start = rec_find_start(time_axis, coded_amps) + T_WORD * rate

    print("initial time = " + str((message_start/rate)-T_WORD))
    print("message_end = " +str(message_start))


    # Creating message graph
    message_time = time_axis[message_start:message_start + MESSAGE_END]
    message_amp = coded_amps[message_start:message_start + MESSAGE_END]

    # Finding bits using find bits functions
    bits_array = numpy_find_bits(message_time, message_amp)
    return bits_array





if __name__ == '__main__':
    # print("starting")
    # record()
    # print("finished recording")
    # print("starting decode")
    bits = decode("test_recordings/recording_from_python1.wav")
    print("decode finished")


    print('bits = '+str(bits))
    sentence = decode_bits(bits)
    print('Sentence Decoded: ' + sentence)

