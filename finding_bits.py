''' This is where all the functions to decide bits will be'''
###
# We get 2 numpy arrays, with time and amplitude.
# The goal is to find out the bits we were sent using cross correlation.
# We use two main functions, calc_integral and find bits
import numpy as np
import math

from numpy.ma.extras import average
from scipy.signal import correlate
from scipy.fft import fft, ifft
from collections import Counter

from CONSTANTS import *


def numpy_calc_integral(time_axis: np.ndarray, amp_axis: np.ndarray, func, initial_ind: int, final_ind: int) -> float:
    """
    :param func: A function composing of sin and cos waves
    :param time_axis: The time axis of the wave
    :param amp_axis: The Y axis of the wave representing amplitude
    :param initial_ind: The index to start integral from
    :param final_ind: The index to end integral
    :return: The area under the graph of the func * wave
    """
    # Setting initial time for phase adjustment
    initial_time = time_axis[initial_ind]

    # Vectorized operation: Calculate the function values and multiply by the amplitudes
    time_diff = time_axis[initial_ind:final_ind] - initial_time
    func_vals = func(time_diff)
    area = np.sum(amp_axis[initial_ind:final_ind] * func_vals)  # Sum over the product

    return area




def parity_bits(bits_array : list) :
        '''

        :param bits_array: Array of functions representing bits
        :return: Most common function

        '''
        counter = Counter(bits_array)

        # Get the most common element and its count
        most_common_element, count = counter.most_common(1)[0]
        return most_common_element

def numpy_find_bits(message_length: int, t_bit: float, time_axis: np.ndarray, amp_axis: np.ndarray, func_array: list) -> list:
    """
    :param t_bit: Time for each bit
    :param time_axis: The time axis of the wave
    :param amp_axis: The Y axis of the wave representing amplitude
    :param func_array: All funcs we want to check
    :param message_length: Number of bits
    :return: Array of funcs with the highest integral
    """
    # Making an array for correct / correlating funcs
    corr_funcs = []

    # Calculate the constants
    time_interval = time_axis[1] - time_axis[0]  # Time between each measurement
    bit_array_length = int(t_bit / time_interval)  # Number of indexes for each bit
    db = int((t_bit * CUT_PERCENT)/ time_interval)

    bits = []

    for i in range(message_length):
        start_ind = i * bit_array_length + db
        end_ind = (i + 1) * bit_array_length - db


        # DSSS Experiments
        mini_bit = [] # mini bit array, representing a bit
        certainty_array = [] # Certainty values array

        for k in range(BIT_LENGTH):
            possible_bits = FUNCTION_ARRAY[k] # Array of two tuples representing 0 and 1
            # Now we need to change func array in next for loop to possible bits
            area_zero = (numpy_calc_integral(time_axis, amp_axis, possible_bits[0][0], start_ind, end_ind) ** 2) + (
                        numpy_calc_integral(time_axis, amp_axis, possible_bits[0][1], start_ind, end_ind) ** 2)

            area_one = (numpy_calc_integral(time_axis, amp_axis, possible_bits[1][0], start_ind, end_ind) ** 2) + (
                    numpy_calc_integral(time_axis, amp_axis, possible_bits[1][1], start_ind, end_ind) ** 2)

            if area_zero < area_one:
                mini_bit.append(1)
                # Checking how sure I am that the bit is actually the bit
                certainty = 1 - (area_zero / area_one)
            else:
                mini_bit.append(-1)
                certainty = 1 - (area_one / area_zero)
            # Keeping track of how sure I am in each bit
            certainty_array.append(certainty)

        # Calculating bit_value by multiplying the two arrays.
        mini_bit = np.array(mini_bit)
        certainty_array = np.array(certainty_array)
        bit_value = np.sum(mini_bit * certainty_array)

        if bit_value < 0:
            bits.append(0)
        else:
            bits.append(1)



    return bits

