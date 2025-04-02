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

    message_array_length = int(message_length / time_interval)  # Number of indexes for 'word'
    # Creating variable for area
    max_area = 0
    start_index=-1
    # Going through all possible starts
    for i in range(0, len(time_axis) - message_array_length, 1000):
        area = calc_integral(time_axis, amp_axis, hidden_func,i,i+message_array_length)
        if area >= max_area:
            max_area = area
            start_index = i
            # Debugging
            print("max = "+str(max_area)+", index = "+ str(start_index))
        if i%100 == 0:
            print("i = "+str(i))
            ########
    return start_index
