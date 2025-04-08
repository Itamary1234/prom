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

from CONSTANTS import PARITY_BIT


def calc_integral(time_axis : list, amp_axis : list, func, initial_ind : int, final_ind : int) -> float:
    '''
    :param func: A function composing of sin and cos waves
    :param time_axis: The time axis of the wave
    :param amp_axis: The Y axis of the wave representing amplitude
    :param initial_ind: The index to start integral from
    :param final_ind: The index to end integral
    :return: The area under the graph of the func * wave
    '''
      # Setting a variable for the area.
    area = 0
    # Acounting for phase
    initial_time=time_axis[initial_ind]
    for i in range(initial_ind,final_ind):
        # Setting variables for convenience
        time = time_axis[i]
        amp = amp_axis[i]
        # Calculating function value at time, when setting 0 at the beginning
        func_val = func(time-initial_time)
        # Adding to area
        area += amp * func_val
    return area


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


def find_bits(message_length : int, t_bit : float, time_axis : list, amp_axis : list, func_array : list) -> list:
    '''

    :param t_bit: Time for each bit
    :param time_axis: The time axis of the wave
    :param amp_axis: The Y axis of the wave representing amplitude
    :param func_array: All funcs we want to check
    :param message_length: Number of bits
    :return: Array of funcs with the highest integral
    '''
    # Making an array for correct / correlating funcs
    corr_funcs = []
    # Calculating some constants
    time_interval = time_axis[1] - time_axis[0] # Time between each measurement

    bit_array_length = int(t_bit / time_interval) # Number of indexes for each bit

    # Going through each bit
    for i in range(message_length):

        max_area = 0
        correlating_function = None
        # Checking correlation with each function
        for func in func_array:
            # Calculating area of multiplication of wave by function
            area = calc_integral(time_axis, amp_axis, func, i * bit_array_length, (i + 1) * bit_array_length)
            # If this function fits better, keep it
            if area > max_area:
                max_area = area
                correlating_function = func
        corr_funcs.append(correlating_function)

    return corr_funcs


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

    # Precompute the area values for each bit window
    areas = np.zeros((message_length, len(func_array)))

    for i in range(message_length):
        start_ind = i * bit_array_length
        end_ind = (i + 1) * bit_array_length

        # For each function in func_array, calculate the area
        for j, func in enumerate(func_array):
            areas[i, j] = numpy_calc_integral(time_axis, amp_axis, func, start_ind, end_ind)

    # Select the best matching function for each bit
    for i in range(message_length):
        max_area_index = np.argmax(areas[i, :])  # Find the index of the maximum area
        corr_funcs.append(func_array[max_area_index])  # Append the corresponding function

    # Adding parity bit for error correction
    if PARITY_BIT != 1:
        bits = []
        for i in range(0, len(corr_funcs) - PARITY_BIT, PARITY_BIT):
            bits.append(parity_bits(corr_funcs[i : i + 3]))
        return bits

    return corr_funcs

