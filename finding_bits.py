''' This is where all the functions to decide bits will be'''
###
# We get 2 numpy arrays, with time and amplitude.
# The goal is to find out the bits we were sent using cross correlation.
# We use two main functions, calc_integral and find bits
import numpy as np
import math

#
def calc_integral(time_axis : list, amp_axis : list, func) -> float:
    '''
    :param func: A function composing of sin and cos waves
    :param time_axis: The time axis of the wave
    :param amp_axis: The Y axis of the wave representing amplitude
    :return: The area under the graph of the func * wave
    '''
      # Setting a variable for the area.
    area = 0
    for i in range(len(time_axis)):
        # Setting variables for convenience
        time = time_axis[i]
        amp = amp_axis[i]
        # Calculating function value at time
        func_val = func(time)
        # Adding to area
        area += amp * func_val
    return area

def calc_integral_with_indexes(time_axis : list, amp_axis : list, func, initial_ind, final_ind) -> float:
    '''
    :param func: A function composing of sin and cos waves
    :param time_axis: The time axis of the wave
    :param amp_axis: The Y axis of the wave representing amplitude
    :return: The area under the graph of the func * wave
    '''
      # Setting a variable for the area.
    area = 0
    for i in range(initial_ind,final_ind):
        # Setting variables for convenience
        time = time_axis[i]
        amp = amp_axis[i]
        # Calculating function value at time
        func_val = func(time)
        # Adding to area
        area += amp * func_val
    return area

def find_bits(message_length : int, t_bit : float, time_axis : list, amp_axis : list, func_array : list) -> list:
    '''

    :param t_bit: Time for each bit
    :param time_axis: The time axis of the wave
    :param amp_axis: The Y axis of the wave representing amplitude
    :param func_array: All funcs we want to check
    :param message_length: Number of bits
    :return: Array of funcs with highest integral
    '''
    # Making an array for correct / correlating funcs
    corr_funcs = []
    # Calculating some constants
    time_interval = time_axis[1] - time_axis[0] # Time between each measurement

    bit_array_length = int(round(t_bit / time_interval)) # Number of indexes for each bit

    for i in range(message_length):
        # Creating arrays for the specific bit
        bit_time_array = time_axis[i * bit_array_length : (i + 1) * bit_array_length]
        bit_amp_array = amp_axis[i * bit_array_length: (i + 1) * bit_array_length]
        # Checking each func
        area = 0
        correlating_function = None
        for func in func_array:
            # Calculating area of multiplication of wave by function
            area1 = calc_integral(bit_time_array, bit_amp_array, func)
            # If this function fits better, keep it
            if area1 > area:
                area = area1
                correlating_function = func
        corr_funcs.append(correlating_function)

    return corr_funcs



