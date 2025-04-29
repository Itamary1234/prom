##########################
# This file is a mvp for decoding signals which aren't trying to be hidden
# It searches for an opening word, and then it is looking for bits
# Imports
import numpy as np
import pandas as pd

from FFT_FILTER import fft_decode
from finding_start import *
from insert_bits import *
from record_sound import *
from CONSTANTS import *
from hamming_code import *
from collections import defaultdict
##########################



def decode(file_path_in : str):
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
    bits_array1, errors_analyzing1= numpy_find_bits(message_time, message_amp, MINI_BIT_FUNCTION_ARRAY1)
    bits_array2, errors_analyzing2 = numpy_find_bits(message_time, message_amp, MINI_BIT_FUNCTION_ARRAY2)



    #bits,(mini_bits, certainty)
    return (bits_array1, errors_analyzing1), (bits_array2, errors_analyzing2)

def check_errors(errors : tuple):
    '''
    :param mini_bits_array: The bits we found, first in errors tuple
    :param certainty_array: The corresponding certainty of each bit, second in errors tuple
    :return: A dictionary where keys are certainty ranges and values are error percentages
    '''


    mini_bits_array = errors[0]
    certainty_array = errors[1]
    errors_total = 0
    # Prepare certainty ranges (0-0.05, 0.05-0.1, ..., 0.95-1.0)
    ranges = [(i/20, (i+1)/20) for i in range(20)]  # [(0, 0.05), (0.05, 0.1), ..., (0.95, 1.0)]

    # Initialize counters
    errors_in_range = defaultdict(int)
    total_in_range = defaultdict(int)

    for i in range(len(mini_bits_array)):
        bit = mini_bits_array[i]
        certainty = certainty_array[i]
        real_bit = MINI_MESSAGE_ARRAY[i]

        # Find the range
        for r_min, r_max in ranges:
            if r_min <= certainty < r_max or (r_max == 1.0 and certainty == 1.0):
                total_in_range[(r_min, r_max)] += 1
                if bit != real_bit:
                    errors_in_range[(r_min, r_max)] += 1
                break

    # Calculate error percentages
    error_percentages = {}
    for r in ranges:
        total = total_in_range[r]
        errors = errors_in_range[r]
        errors_total += errors
        if total > 0:
            error_percentages[f"{r[0]:.2f}-{r[1]:.2f}"] = errors / total
        else:
            error_percentages[f"{r[0]:.2f}-{r[1]:.2f}"] = None  # No data in this range


    # Saving data into an excel
    df = pd.DataFrame(list(error_percentages.items()), columns=["Certainty Range", "Error Percentage"])

    # Save it to an Excel file
    #df.to_excel("excels/cc_T_03_L_420_A_1300.xlsx", index=False)

    total_errors_per = errors_total / (BIT_LENGTH * MESSAGE_LENGTH)
    print('Error Percentage is: ' + str(total_errors_per))

    return error_percentages


def bit_errors(bits_array : list):
    errors = 0
    for i in range(MESSAGE_LENGTH):
        if bits_array[i] != MESSAGE_ARRAY[i]:
            errors += 1
    return errors / MESSAGE_LENGTH



if __name__ == '__main__':
    file_name="test_recordings/T_03_freq_1900_700_L_420.wav"
    print("starting")
    #record(file_name)
    print("finished recording")
    print("starting decode")
    bits1, bits2 = decode(file_name)

    print("decode finished")

    print()
    print('bits = ' + str(bits1[0]))
    sentence = decode_bits(bits1[0])

    print('Bit Errors = ' + str(bit_errors(bits1[0])))

    print('Sentence Decoded With Cross-Correlation: ' + sentence)
    channel_bits = mini_to_bits(bits1[1], bits2[1])
    print(str(channel_bits))
    print('Channel Bit Errors = ' + str(bit_errors(channel_bits)))


    #Checking errors
    check_errors(bits1[1])


