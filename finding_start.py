##########
# This file will help us find the beginning of the bit sending
# by searching for a decided beforehand function
# This file will get the recording as two arrays
# time and amplitude and the code function and will find when the correlation is greatest
# Code will also get the time of the message and bar to stop searching at.
# Imports
from finding_bits import *
###########
def find_start(message_length : int, time_axis : list, amp_axis : list, hidden_func, accuracy : int = 10000, start_index: int = 0, end_index : int =0) -> int:
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

    if end_index == 0:
        end_index = len(time_axis) - message_array_length

    max_area = 0
    # Going through all possible starts
    for i in range(start_index, end_index, accuracy):
        area = calc_integral(time_axis, amp_axis, hidden_func, i ,i+message_array_length)
        if area >= max_area:
            max_area = area
            start_index = i

    return start_index

def rec_find_start(message_length : int, time_axis : list, amp_axis : list, hidden_func, accuracy : int = 10000, start_index: int = 0, end_index : int =0)-> int:
    '''
            This function will find start of message
        :param message_length: Length in time of secret 'word'
        :param time_axis: Axis of time in wave
        :param amp_axis: Axis of amplitude in wave
        :param hidden_func: Function to look for
        :param accuracy: how accurate we want our search to be
        :return: Index in which we think the message started
        '''
    if accuracy <= 10:
        return (start_index + end_index) // 2

    index = find_start(message_length, time_axis, amp_axis, hidden_func, accuracy, start_index, end_index)
    return rec_find_start(message_length, time_axis, amp_axis, hidden_func, accuracy//10, index - accuracy, index + accuracy)
