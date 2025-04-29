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
    try:
        initial_time = time_axis[initial_ind]

        # Vectorized operation: Calculate the function values and multiply by the amplitudes
        time_diff = time_axis[initial_ind:final_ind] - initial_time
        func_vals = func(time_diff)
        area = np.sum(amp_axis[initial_ind:final_ind] * func_vals)  # Sum over the product
    except IndexError:
        print('Tried to reach invalid indexes')
        area=0.001

    return area


def numpy_calc_integral_average(time_axis: np.ndarray, amp_axis: np.ndarray, func, initial_ind: int, final_ind: int) -> float:
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

    bit_length = final_ind - initial_ind

    mini_bit_array_length = int(bit_length / DIVISOR)  # Number of indexes for each bit

    areas = []

    for i in range(DIVISOR):
        mini_start_ind = initial_ind + mini_bit_array_length * i
        mini_end_ind = initial_ind + mini_bit_array_length * (i + 1)
        area = np.sum(amp_axis[mini_start_ind:mini_end_ind] * func_vals[mini_start_ind:mini_start_ind])
        areas.append(area)

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

def numpy_find_bits(time_axis: np.ndarray, amp_axis: np.ndarray, mini_bit_funcs : list[list[tuple]] = MINI_BIT_FUNCTION_ARRAY1) -> (list, tuple):
    """
    :param T_BIT: Time for each bit
    :param time_axis: The time axis of the wave
    :param amp_axis: The Y axis of the wave representing amplitude
    :param mini_bit_funcs: The mini_bit function array we want to cross correlate with
    :return: Array of funcs with the highest integral
    """
    # Making an array for correct / correlating funcs
    corr_funcs = []

    # Calculate the constants
    time_interval = time_axis[1] - time_axis[0]  # Time between each measurement
    bit_array_length = int(T_BIT / time_interval)  # Number of indexes for each bit
    mini_bit_array_length = int(bit_array_length / BIT_LENGTH)  # Number of indexes for each bit

    db = int((T_BIT * CUT_PERCENT)/ (time_interval * BIT_LENGTH))

    bits = []
    mini_bits_array = [] # All mini_bits found
    mini_certainty_array = [] # All certainties found

    for i in range(MESSAGE_LENGTH):
        start_ind = i * bit_array_length + db
        end_ind = (i + 1) * bit_array_length - db


        # DSSS Experiments
        mini_bit = [] # mini bit array, representing a bit
        certainty_array = [] # Certainty values array

        # if BIT_LENGTH == 1:
        #     possible_bits = MINI_BIT_FUNCTION_ARRAY[0]
        #     area_zero = (numpy_calc_integral_average(time_axis, amp_axis, possible_bits[0][0], start_ind,
        #                                      end_ind) ** 2) + (
        #                         numpy_calc_integral(time_axis, amp_axis, possible_bits[0][1], start_ind,
        #                                             end_ind) ** 2)
        #
        #     area_one = (numpy_calc_integral_average(time_axis, amp_axis, possible_bits[1][0], start_ind,
        #                                     end_ind) ** 2) + (
        #                        numpy_calc_integral(time_axis, amp_axis, possible_bits[1][1], start_ind,
        #                                            end_ind) ** 2)
        #     for i in range(BIT_LENGTH):
        #


        for k in range(BIT_LENGTH):
            # Calculating index for each mini bit
            mini_start_ind = start_ind + mini_bit_array_length * k
            mini_end_ind = start_ind + mini_bit_array_length * (k+1)
            possible_bits = mini_bit_funcs[k] # Array of two tuples representing 0 and 1
            # Now we need to change func array in next for loop to possible bits
            area_zero = (numpy_calc_integral(time_axis, amp_axis, possible_bits[0][0], mini_start_ind, mini_end_ind) ** 2) + (
                        numpy_calc_integral(time_axis, amp_axis, possible_bits[0][1], mini_start_ind, mini_end_ind) ** 2)

            area_one = (numpy_calc_integral(time_axis, amp_axis, possible_bits[1][0], mini_start_ind, mini_end_ind) ** 2) + (
                    numpy_calc_integral(time_axis, amp_axis, possible_bits[1][1], mini_start_ind, mini_end_ind) ** 2)

            if area_zero < area_one:
                mini_bit.append(1)
                # Checking how sure I am that the bit is actually the bit

                certainty = (1 - (area_zero / area_one))**2
            else:
                mini_bit.append(-1)
                certainty = (1 - (area_one / area_zero))**2

            # Keeping track of how sure I am in each bit
            certainty_array.append(certainty)

        # Appending to big arrays for error analyzing


        mini_certainty_array += certainty_array

        # Calculating bit_value by multiplying the two arrays.

        mini_bit_numpy = np.array(mini_bit)
        certainty_array_numpy = np.array(certainty_array)
        bit_value = np.sum(mini_bit_numpy * certainty_array_numpy)

        # Mini bit array appending
        for l in range(BIT_LENGTH):
            if mini_bit[l] == -1:
                mini_bit[l] = 0

        mini_bits_array += mini_bit



        if bit_value < 0:
            bits.append(0)
        else:
            bits.append(1)



    return bits, (mini_bits_array, mini_certainty_array)

def mini_to_bits(channel1 : tuple, channel2 : tuple) -> list:
    '''

    :param channel1: A tuple consisting of mini_bits found from channel 1 and their certainties
    :param channel2:
    :return:
    '''
    mini_bit_array1 = np.array(channel1[0])
    mini_bit_array2 = np.array(channel2[0])
    certainty_array1 = np.array(channel1[1])
    certainty_array2 = np.array(channel2[1])


    bits = []
    # Running through each bit
    for i in range(0, MESSAGE_LENGTH * BIT_LENGTH, BIT_LENGTH):
        # Mini_bit and certainty array list slicing
        mini_bit_1 = mini_bit_array1[i: i + BIT_LENGTH]
        mini_bit_2 = mini_bit_array2[i: i + BIT_LENGTH]
        cer_1 = certainty_array1[i: i + BIT_LENGTH]
        cer_2 = certainty_array2[i: i + BIT_LENGTH]
        # Calculating average value of bit
        bit_value = np.sum((2*mini_bit_1-1) * cer_1) + np.sum((2*mini_bit_2-1) * cer_2)
        if bit_value < 0:
            bits.append(0)
        else:
            bits.append(1)

    return bits

