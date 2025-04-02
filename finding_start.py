##########
# This file will help us find the beginning of the bit sending
# by searching for a decided beforehand function
# This file will get the recording as two arrays
# time and amplitude and the code function and will find when the correlation is greatest
# Code will also get the time of the message and bar to stop searching at.
# Imports
from finding_bits import *
###########
def find_start(message_length : int, time_axis : list, amp_axis : list, hidden_func) -> int:
    '''
        This function will find start of message
    :param message_length: Length in time of secret 'word'
    :param time_axis: Axis of time in wave
    :param amp_axis: Axis of amplitude in wave
    :param hidden_func: Function to look for
    :return: Index in which we think the message started
    '''
    time_interval = time_axis[1] - time_axis[0]  # Time between each measurement

    message_array_length = int(round(message_length / time_interval))  # Number of indexes for 'word'
    # Creating variable for area
    max_area = 0
    # Going through all possible starts
    for i in range(len(time_axis) - message_array_length):
        # Creating potential arrays
        potential_time_array = time_axis[i:i+message_array_length]
        potential_amp_array = amp_axis[i:i+message_array_length]
        # Calculating integral
        area = calc_integral(potential_time_array, potential_amp_array, hidden_func)
        if area >= max_area:
            max_area = area
            start_index = i
    return start_index
