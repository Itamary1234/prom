''' This is where all the functions to decide bits will be'''
###
# We get 2 numpy arrays, with time and amplitude.
# The goal is to find out the bits we were sent using cross correlation.
# We use two main functions, calc_integral and find bits
import numpy as np
import math
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
    ###### Trying to use scipy library

    ###################
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

    # Precompute the area values for each bit window
    areas = np.zeros((message_length, len(func_array)))

    for i in range(message_length):
        start_ind = i * bit_array_length + db
        end_ind = (i + 1) * bit_array_length - db

        # For each function in func_array, calculate the area
        for j, func in enumerate(func_array):
            # Trying to correlate with cos too
            areas[i, j] = (numpy_calc_integral(time_axis, amp_axis, func[0], start_ind, end_ind)**2) + (numpy_calc_integral(time_axis, amp_axis, func[1], start_ind, end_ind)**2)

    # Select the best matching function for each bit
    for i in range(message_length):
        max_area_index = np.argmax(areas[i, :])  # Find the index of the maximum area
        # Added[0] for cos correlation
        corr_funcs.append(func_array[max_area_index])  # Append the corresponding function

    # Adding parity bit for error correction
    if PARITY_BIT != 1:
        bits = []
        for i in range(0, len(corr_funcs) - PARITY_BIT, PARITY_BIT):
            bits.append(parity_bits(corr_funcs[i : i + PARITY_BIT]))
        return bits

    return corr_funcs

