################################
# This file is where we encode data
import numpy as np

from hamming_code import *
from insert_bits import *
from CONSTANTS import *

###################################


def encode(file_path_in : str, file_path_out : str, information : list):
    # Getting data, plotting it
    rate, coded_amps, time_axis = read_wav_file(file_path_in)
    plot(time_axis, coded_amps)
    # coded_amps = np.zeros(len(coded_amps))

    # Encoding signal in data and plotting it
    encrypt(time_axis, coded_amps, information)
    plot(time_axis, coded_amps)

    # Writing into file so we could hear that recording is hidden
    write_wav_file(file_path_out, rate, coded_amps)
    return rate, coded_amps, time_axis



if __name__ == '__main__':


    # Getting sentence to send
    sentence = "A composer builds music and tells stories in notes and chords" #input('Enter Sentence To Send: ')
    information = encode_string(sentence)
    encode(ENCODING_FILE, DECODING_FILE, information)
    print('number of bit = ' + str(len(information)))
    print('bits = ' + str(information))
    print('Encoded Information, Good Luck.')