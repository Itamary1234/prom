##########
# This file will help us find the beginning of the bit sending
# by searching for a decided beforehand function
# This file will get the recording as two arrays
# time and amplitude and the code function and will find when the correlation is greatest
# Code will also get the time of the message and bar to stop searching at.
# Imports
from finding_bits import *
###########
def find_start(time_axis: list, amp_axis: list, accuracy: int = 10000,
               start_index: int = 0, end_index: int = 0) -> int:
    '''
        This function will find start of message
    :param time_axis: Axis of time in wave
    :param amp_axis: Axis of amplitude in wave
    :param accuracy: Step size for searching
    :param start_index: Starting index for the search
    :param end_index: Ending index for the search (default is the length of time_axis minus message length)
    :return: Index in which we think the message started
    '''

    time_interval = time_axis[1] - time_axis[0]  # Time between each measurement

    message_array_length = int(T_WORD / time_interval)  # Number of indexes for 'word'
    # Creating variable for area

    if end_index == 0:
        end_index = len(time_axis) - message_array_length  # Set default end_index if not provided

    max_area = 0
    # Going through all possible starts in steps of 'accuracy'
    for i in range(start_index, end_index, accuracy):
        area = numpy_calc_integral(time_axis, amp_axis, start_func, i, i + message_array_length)
        if area >= max_area:  # Update if a larger area is found
            max_area = area
            start_index = i

    return start_index


def rec_find_start(time_axis: list, amp_axis: list,accuracy: int = 10000,
                   start_index: int = 0, end_index: int = 0) -> int:
    '''
        This function recursively refines the search for the start of the message
    :param time_axis: Axis of time in wave
    :param amp_axis: Axis of amplitude in wave
    :param accuracy: Initial step size for searching, which decreases recursively
    :param start_index: Starting index for the search
    :param end_index: Ending index for the search
    :return: Index in which we think the message started with improved accuracy
    '''

    if accuracy <= 10:  # Base case: Stop refining when accuracy reaches 10
        return (start_index + end_index) // 2  # Return midpoint for final estimate

    # Find best index at current accuracy level
    index = find_start(time_axis, amp_axis, accuracy, start_index, end_index)

    # Recursively refine search with smaller step size
    return rec_find_start(time_axis, amp_axis, accuracy // 10, index - accuracy,
                          index + accuracy)
