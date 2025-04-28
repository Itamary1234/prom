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
    bits_array, errors_analyzing= numpy_find_bits(message_time, message_amp)


    fft_bits = fft_decode(file_path_in, time_axis[message_start])
    print(fft_bits)
    #(bits,(mini_bits, certainty)), (fft_bits, (fft_mini_bits, fft_certainty))
    return (bits_array, errors_analyzing), fft_bits

def check_errors(errors : tuple):
    '''
    :param mini_bits_array: The bits we found, first in errors tuple
    :param certainty_array: The corresponding certainty of each bit, second in errors tuple
    :return: A dictionary where keys are certainty ranges and values are error percentages
    '''


    mini_bits_array = errors[0]
    certainty_array = errors[1]

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
        if total > 0:
            error_percentages[f"{r[0]:.2f}-{r[1]:.2f}"] = errors / total
        else:
            error_percentages[f"{r[0]:.2f}-{r[1]:.2f}"] = None  # No data in this range

    total_errors_per = sum(mini_bits_array[i] != MINI_MESSAGE_ARRAY[i] for i in range(len(mini_bits_array))) / len(MINI_MESSAGE_ARRAY)

    # Saving data into an excel
    df = pd.DataFrame(list(error_percentages.items()), columns=["Certainty Range", "Error Percentage"])

    # Save it to an Excel file
    df.to_excel("error_percentages.xlsx", index=False)


    return error_percentages, total_errors_per






if __name__ == '__main__':
    file_name="test_recordings/recording_from_python_half_bit_0_2.wav"
    print("starting")
    # record(file_name)
    print("finished recording")
    print("starting decode")
    bits, fft_bits = decode(file_name)

    print("decode finished")

    print()
    print('bits = '+str(bits))
    sentence = decode_bits(bits[0])
    print('Sentence Decoded: ' + sentence)

    # Checking errors
    print(check_errors(bits[1]))
    print(check_errors(fft_bits[1]))

