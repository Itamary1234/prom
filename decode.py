##########################
# This file is a mvp for decoding signals which aren't trying to be hidden
# It searches for an opening word, and then it is looking for bits
# Imports
import numpy as np

from finding_start import *
from insert_bits import *
from record_sound import *
from CONSTANTS import *
##########################



def decode(file_path_in : str) -> list:
    '''
    :param file_path_in: File of song or recording to encode data on message
    :param file_path_out: File to write encoded data on

    :return: Array of functions code thinks
    '''

    # Getting data, plotting it
    rate, coded_amps, time_axis = read_wav_file(file_path_in)

    print('Data Read, Here We GO')
    # Finding the start of the message (index) using the find start function

    message_start = rec_find_start(T_WORD, time_axis, coded_amps, word) + T_WORD * rate

    print("initial time = " + str((message_start/rate)-T_WORD))
    print("message_end = " +str(message_start))


    # Creating message graph
    message_time = time_axis[message_start:message_start + MESSAGE_END]
    message_amp = coded_amps[message_start:message_start + MESSAGE_END]

    # Finding bits using find bits functions
    bits_array = numpy_find_bits(MESSAGE_LENGTH, T_BIT, message_time, message_amp, FUNCTION_ARRAY)
    return bits_array


def encode(file_path_in : str, file_path_out : str):
    # Getting data, plotting it
    rate, coded_amps, time_axis = read_wav_file(file_path_in)
    plot(time_axis, coded_amps)

    # Encoding signal in data and plotting it
    encrypt(time_axis, coded_amps)
    plot(time_axis, coded_amps)

    # Writing into file so we could hear that recording is hidden
    write_wav_file(file_path_out, rate, coded_amps)
    return rate, coded_amps, time_axis


if __name__ == '__main__':
    # print("starting")
    # record()
    # print("finished recording")
    # encode(ENCODING_FILE,DECODING_FILE)
    # print("encode finished")
    print("starting decode")
    bits_array = decode("test_recordings/recording_from_python1.wav")
    print("decode finished")

     # Checking for errors
    errors = 0
    for i in range(0,MESSAGE_LENGTH, PARITY_BIT):
        try:

            if message_array[i] != function_dictionary[bits_array[i//PARITY_BIT]]:
                 errors += 1
                 print('Real Bit = ' + str(message_array[i]) + ' Decode Bit = ' + str(function_dictionary[bits_array[i//PARITY_BIT]]))
        except Exception as e:
            print('error, problem in loading decoded bits')
    print('Number of errors: ' + str(errors))
    plot_file("test_recordings/recording_from_python1.wav")
